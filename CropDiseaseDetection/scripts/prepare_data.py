"""
Dataset Preparation Script
--------------------------
Splits the PlantVillage dataset into train/validation/test sets.

Usage:
    python scripts/prepare_data.py

Expected folder structure:
    dataset/PlantVillage/
        ├── Apple___Apple_scab/
        ├── Apple___Black_rot/
        ├── ...
        └── Tomato___healthy/

Output:
    data/train/       (80%)
    data/validation/  (10%)
    data/test/        (10%)
"""

import os
import shutil
import random
from pathlib import Path

# ──────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────
DATASET_DIR = os.path.join("dataset", "PlantVillage")
OUTPUT_DIR = "data"
TRAIN_RATIO = 0.80
VAL_RATIO = 0.10
TEST_RATIO = 0.10
RANDOM_SEED = 42
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".JPG", ".JPEG", ".PNG"}


def is_image_file(filename):
    """Check if a file is an image based on extension."""
    return Path(filename).suffix in IMAGE_EXTENSIONS


def prepare_dataset():
    """Split dataset into train, validation, and test sets."""

    # Validate source directory
    if not os.path.exists(DATASET_DIR):
        print(f"❌ Error: Dataset directory not found at '{DATASET_DIR}'")
        print(f"   Please download the PlantVillage dataset and place it at:")
        print(f"   {os.path.abspath(DATASET_DIR)}")
        print(f"\n   Download from: https://www.kaggle.com/datasets/emmarex/plantdisease")
        return

    # Get all class directories
    classes = sorted([
        d for d in os.listdir(DATASET_DIR)
        if os.path.isdir(os.path.join(DATASET_DIR, d))
    ])

    if len(classes) == 0:
        print(f"❌ Error: No class folders found in '{DATASET_DIR}'")
        return

    print(f"{'='*60}")
    print(f"  PlantVillage Dataset Preparation")
    print(f"{'='*60}")
    print(f"  Source:     {os.path.abspath(DATASET_DIR)}")
    print(f"  Output:     {os.path.abspath(OUTPUT_DIR)}")
    print(f"  Classes:    {len(classes)}")
    print(f"  Split:      Train {TRAIN_RATIO*100:.0f}% | Val {VAL_RATIO*100:.0f}% | Test {TEST_RATIO*100:.0f}%")
    print(f"{'='*60}\n")

    # Create output directories
    for split in ["train", "validation", "test"]:
        for cls in classes:
            os.makedirs(os.path.join(OUTPUT_DIR, split, cls), exist_ok=True)

    # Split and copy data
    random.seed(RANDOM_SEED)
    total_stats = {"train": 0, "validation": 0, "test": 0}
    class_stats = []

    for cls in classes:
        cls_dir = os.path.join(DATASET_DIR, cls)
        images = [f for f in os.listdir(cls_dir) if is_image_file(f)]
        random.shuffle(images)

        n_total = len(images)
        n_train = int(n_total * TRAIN_RATIO)
        n_val = int(n_total * VAL_RATIO)

        splits = {
            "train": images[:n_train],
            "validation": images[n_train:n_train + n_val],
            "test": images[n_train + n_val:]
        }

        for split_name, split_images in splits.items():
            for img_name in split_images:
                src = os.path.join(cls_dir, img_name)
                dst = os.path.join(OUTPUT_DIR, split_name, cls, img_name)
                shutil.copy2(src, dst)
            total_stats[split_name] += len(split_images)

        class_stats.append({
            "class": cls,
            "total": n_total,
            "train": len(splits["train"]),
            "val": len(splits["validation"]),
            "test": len(splits["test"])
        })

        print(f"  ✅ {cls}: {n_total} images "
              f"(train={len(splits['train'])}, "
              f"val={len(splits['validation'])}, "
              f"test={len(splits['test'])})")

    # Print summary
    grand_total = sum(total_stats.values())
    print(f"\n{'='*60}")
    print(f"  Summary")
    print(f"{'='*60}")
    print(f"  Total images:      {grand_total}")
    print(f"  Training set:      {total_stats['train']} ({total_stats['train']/grand_total*100:.1f}%)")
    print(f"  Validation set:    {total_stats['validation']} ({total_stats['validation']/grand_total*100:.1f}%)")
    print(f"  Test set:          {total_stats['test']} ({total_stats['test']/grand_total*100:.1f}%)")
    print(f"  Number of classes: {len(classes)}")
    print(f"{'='*60}")
    print(f"\n  ✅ Dataset prepared successfully!")
    print(f"  📁 Output directory: {os.path.abspath(OUTPUT_DIR)}")

    # Save class names to a file for reference
    class_names_path = os.path.join("models", "class_names.txt")
    os.makedirs("models", exist_ok=True)
    with open(class_names_path, "w") as f:
        for cls in classes:
            f.write(cls + "\n")
    print(f"  📝 Class names saved to: {class_names_path}")


if __name__ == "__main__":
    prepare_dataset()
