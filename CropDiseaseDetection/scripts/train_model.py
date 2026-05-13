"""
CNN Model Training Script - Crop Disease Detection
----------------------------------------------------
Trains a custom CNN on the PlantVillage dataset.
Compatible with both local execution and Google Colab.

Usage (Local):
    python scripts/train_model.py

Usage (Google Colab):
    1. Upload this file to Colab or copy into a cell
    2. Mount Google Drive
    3. Set COLAB_MODE = True
    4. Run the script

Output:
    models/crop_disease_model.h5    - Trained model
    models/class_names.json         - Class name mapping
    reports/accuracy_plot.png       - Accuracy graph
    reports/loss_plot.png           - Loss graph
    reports/training_report.txt     - Training summary
"""

import os
import sys
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt

# Fix encoding for Windows terminals
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# -----------------------------------------------
# Colab Detection & Setup
# -----------------------------------------------
try:
    import google.colab
    COLAB_MODE = True
    print("[COLAB] Running on Google Colab")
except ImportError:
    COLAB_MODE = False
    print("[LOCAL] Running locally")

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, Flatten, Dense,
    Dropout, BatchNormalization, GlobalAveragePooling2D
)
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import (
    EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
)
from sklearn.metrics import classification_report, confusion_matrix

print(f"TensorFlow version: {tf.__version__}")
print(f"GPU Available: {len(tf.config.list_physical_devices('GPU')) > 0}")
if len(tf.config.list_physical_devices('GPU')) > 0:
    print(f"GPU Device: {tf.config.list_physical_devices('GPU')}")


# -----------------------------------------------
# Configuration
# -----------------------------------------------
class Config:
    """Training configuration."""

    # Paths (auto-configured for Colab or local)
    if COLAB_MODE:
        # Mount Google Drive in Colab
        from google.colab import drive
        drive.mount('/content/drive')
        BASE_DIR = "/content/drive/MyDrive/CropDiseaseDetection"
    else:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    TRAIN_DIR = os.path.join(BASE_DIR, "data", "train")
    VAL_DIR = os.path.join(BASE_DIR, "data", "validation")
    TEST_DIR = os.path.join(BASE_DIR, "data", "test")
    MODEL_DIR = os.path.join(BASE_DIR, "models")
    REPORT_DIR = os.path.join(BASE_DIR, "reports")

    # Model parameters
    IMG_SIZE = 128
    IMG_SHAPE = (128, 128, 3)
    BATCH_SIZE = 32
    EPOCHS = 30           # Max epochs (early stopping will stop earlier)
    LEARNING_RATE = 0.001

    # Output files
    MODEL_PATH = os.path.join(MODEL_DIR, "crop_disease_model.h5")
    CLASS_NAMES_PATH = os.path.join(MODEL_DIR, "class_names.json")


# Create output directories
os.makedirs(Config.MODEL_DIR, exist_ok=True)
os.makedirs(Config.REPORT_DIR, exist_ok=True)


# -----------------------------------------------
# Step 1: Data Loading & Augmentation
# -----------------------------------------------
def create_data_generators():
    """Create training and validation data generators with augmentation."""

    print("\n[*] Loading dataset...")
    print(f"   Train dir:      {Config.TRAIN_DIR}")
    print(f"   Validation dir: {Config.VAL_DIR}")
    print(f"   Test dir:       {Config.TEST_DIR}")

    # Training data with augmentation
    train_datagen = ImageDataGenerator(
        rescale=1.0 / 255,
        rotation_range=25,
        width_shift_range=0.2,
        height_shift_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        vertical_flip=False,
        brightness_range=[0.8, 1.2],
        fill_mode='nearest'
    )

    # Validation & Test data - only rescaling
    val_test_datagen = ImageDataGenerator(rescale=1.0 / 255)

    train_generator = train_datagen.flow_from_directory(
        Config.TRAIN_DIR,
        target_size=(Config.IMG_SIZE, Config.IMG_SIZE),
        batch_size=Config.BATCH_SIZE,
        class_mode='categorical',
        shuffle=True
    )

    val_generator = val_test_datagen.flow_from_directory(
        Config.VAL_DIR,
        target_size=(Config.IMG_SIZE, Config.IMG_SIZE),
        batch_size=Config.BATCH_SIZE,
        class_mode='categorical',
        shuffle=False
    )

    test_generator = val_test_datagen.flow_from_directory(
        Config.TEST_DIR,
        target_size=(Config.IMG_SIZE, Config.IMG_SIZE),
        batch_size=Config.BATCH_SIZE,
        class_mode='categorical',
        shuffle=False
    )

    num_classes = len(train_generator.class_indices)

    print(f"\n   [OK] Training samples:   {train_generator.samples}")
    print(f"   [OK] Validation samples: {val_generator.samples}")
    print(f"   [OK] Test samples:       {test_generator.samples}")
    print(f"   [OK] Number of classes:  {num_classes}")
    print(f"   [OK] Class names:        {list(train_generator.class_indices.keys())[:5]}...")

    return train_generator, val_generator, test_generator, num_classes


# -----------------------------------------------
# Step 2: Build CNN Model
# -----------------------------------------------
def build_cnn_model(num_classes):
    """Build the CNN architecture for crop disease classification."""

    print(f"\n[*] Building CNN model ({num_classes} classes)...")

    model = Sequential([
        # Block 1: 32 filters
        Conv2D(32, (3, 3), activation='relu', padding='same',
               input_shape=Config.IMG_SHAPE),
        BatchNormalization(),
        Conv2D(32, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),

        # Block 2: 64 filters
        Conv2D(64, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        Conv2D(64, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),

        # Block 3: 128 filters
        Conv2D(128, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        Conv2D(128, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),

        # Block 4: 256 filters
        Conv2D(256, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),

        # Classification head
        GlobalAveragePooling2D(),
        Dense(512, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(256, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=Config.LEARNING_RATE),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    model.summary()
    return model


# -----------------------------------------------
# Step 3: Train Model
# -----------------------------------------------
def train_model(model, train_gen, val_gen):
    """Train the CNN model with callbacks."""

    print(f"\n[*] Starting training...")
    print(f"   Epochs:     {Config.EPOCHS} (max)")
    print(f"   Batch size: {Config.BATCH_SIZE}")
    print(f"   Image size: {Config.IMG_SIZE}x{Config.IMG_SIZE}")

    callbacks = [
        # Stop training when validation loss stops improving
        EarlyStopping(
            monitor='val_loss',
            patience=7,
            restore_best_weights=True,
            verbose=1
        ),
        # Save best model
        ModelCheckpoint(
            Config.MODEL_PATH,
            monitor='val_accuracy',
            save_best_only=True,
            verbose=1
        ),
        # Reduce learning rate when plateauing
        ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=3,
            min_lr=1e-7,
            verbose=1
        )
    ]

    history = model.fit(
        train_gen,
        epochs=Config.EPOCHS,
        validation_data=val_gen,
        callbacks=callbacks,
        verbose=1
    )

    return history


# -----------------------------------------------
# Step 4: Evaluate & Generate Reports
# -----------------------------------------------
def evaluate_model(model, test_gen, history, class_names):
    """Evaluate model and generate reports."""

    print(f"\n[*] Evaluating model on test set...")

    # Test set evaluation
    test_loss, test_accuracy = model.evaluate(test_gen, verbose=1)
    print(f"\n   [OK] Test Accuracy: {test_accuracy * 100:.2f}%")
    print(f"   [OK] Test Loss:     {test_loss:.4f}")

    # Classification report
    test_gen.reset()
    y_pred = model.predict(test_gen, verbose=1)
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_true = test_gen.classes

    report = classification_report(
        y_true, y_pred_classes,
        target_names=class_names,
        output_dict=True
    )
    report_text = classification_report(
        y_true, y_pred_classes,
        target_names=class_names
    )
    print(f"\n[*] Classification Report:\n{report_text}")

    # -- Plot: Accuracy --
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(history.history['accuracy'], label='Training Accuracy',
            linewidth=2, color='#4CAF50')
    ax.plot(history.history['val_accuracy'], label='Validation Accuracy',
            linewidth=2, color='#2196F3')
    ax.set_title('Model Accuracy Over Epochs', fontsize=16, fontweight='bold')
    ax.set_xlabel('Epoch', fontsize=12)
    ax.set_ylabel('Accuracy', fontsize=12)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0, 1])
    plt.tight_layout()
    accuracy_path = os.path.join(Config.REPORT_DIR, "accuracy_plot.png")
    plt.savefig(accuracy_path, dpi=150)
    plt.close()
    print(f"   [SAVED] Accuracy plot: {accuracy_path}")

    # -- Plot: Loss --
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(history.history['loss'], label='Training Loss',
            linewidth=2, color='#F44336')
    ax.plot(history.history['val_loss'], label='Validation Loss',
            linewidth=2, color='#FF9800')
    ax.set_title('Model Loss Over Epochs', fontsize=16, fontweight='bold')
    ax.set_xlabel('Epoch', fontsize=12)
    ax.set_ylabel('Loss', fontsize=12)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    loss_path = os.path.join(Config.REPORT_DIR, "loss_plot.png")
    plt.savefig(loss_path, dpi=150)
    plt.close()
    print(f"   [SAVED] Loss plot: {loss_path}")

    # -- Training Report --
    report_path = os.path.join(Config.REPORT_DIR, "training_report.txt")
    with open(report_path, "w") as f:
        f.write("=" * 60 + "\n")
        f.write("  Crop Disease Detection - Training Report\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"TensorFlow Version: {tf.__version__}\n")
        f.write(f"GPU Used: {len(tf.config.list_physical_devices('GPU')) > 0}\n\n")
        f.write(f"Image Size:    {Config.IMG_SIZE}x{Config.IMG_SIZE}\n")
        f.write(f"Batch Size:    {Config.BATCH_SIZE}\n")
        f.write(f"Max Epochs:    {Config.EPOCHS}\n")
        f.write(f"Actual Epochs: {len(history.history['accuracy'])}\n\n")
        f.write(f"Test Accuracy: {test_accuracy * 100:.2f}%\n")
        f.write(f"Test Loss:     {test_loss:.4f}\n\n")
        f.write("Classification Report:\n")
        f.write("-" * 60 + "\n")
        f.write(report_text + "\n")

    print(f"   [SAVED] Training report: {report_path}")

    return test_accuracy, test_loss


def save_class_names(class_indices):
    """Save class name mapping as JSON."""
    # Invert: index -> class name
    class_names = {str(v): k for k, v in class_indices.items()}
    with open(Config.CLASS_NAMES_PATH, "w") as f:
        json.dump(class_names, f, indent=2)
    print(f"   [SAVED] Class names: {Config.CLASS_NAMES_PATH}")
    return [class_indices_to_sorted_names(class_indices)]


def class_indices_to_sorted_names(class_indices):
    """Convert class_indices dict to a sorted list of names."""
    return [name for name, _ in sorted(class_indices.items(), key=lambda x: x[1])]


# -----------------------------------------------
# Main
# -----------------------------------------------
def main():
    """Full training pipeline."""

    print("\n" + "=" * 60)
    print("  Crop Disease Detection - CNN Training Pipeline")
    print("=" * 60)

    # Validate directories
    if not os.path.exists(Config.TRAIN_DIR):
        print(f"\n[ERROR] Training data not found at: {Config.TRAIN_DIR}")
        print(f"   Please run 'python scripts/prepare_data.py' first.")
        if COLAB_MODE:
            print(f"\n   For Colab:")
            print(f"   1. Upload your dataset to Google Drive at:")
            print(f"      MyDrive/CropDiseaseDetection/data/")
            print(f"   2. Or run prepare_data.py in Colab first.")
        sys.exit(1)

    # Step 1: Load data
    train_gen, val_gen, test_gen, num_classes = create_data_generators()

    # Save class names
    save_class_names(train_gen.class_indices)
    class_names = class_indices_to_sorted_names(train_gen.class_indices)

    # Step 2: Build model
    model = build_cnn_model(num_classes)

    # Step 3: Train
    history = train_model(model, train_gen, val_gen)

    # Step 4: Evaluate
    test_accuracy, test_loss = evaluate_model(model, test_gen, history, class_names)

    # Final summary
    print("\n" + "=" * 60)
    print("  [DONE] Training Complete!")
    print("=" * 60)
    print(f"  Model saved:    {Config.MODEL_PATH}")
    print(f"  Test accuracy:  {test_accuracy * 100:.2f}%")
    print(f"  Reports saved:  {Config.REPORT_DIR}")
    print("=" * 60)

    if COLAB_MODE:
        print("\n  Download your model from Google Drive:")
        print(f"     {Config.MODEL_PATH}")
        print(f"     {Config.CLASS_NAMES_PATH}")


if __name__ == "__main__":
    main()
