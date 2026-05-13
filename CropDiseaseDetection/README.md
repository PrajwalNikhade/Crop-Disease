# 🌿 AI-Based Crop Disease Detection Using Deep Learning (CNN)

An intelligent system that detects crop diseases from leaf images using Convolutional Neural Networks (CNN), built with TensorFlow/Keras and deployed via Streamlit.

## ✨ Features

- 🔬 **Disease Detection** — Identifies 38 types of crop diseases across 14 crops
- 📊 **Confidence Score** — Shows how sure the AI is about its prediction
- 💊 **Treatment Guide** — Provides recommended treatments and prevention tips
- 📚 **Disease Library** — Browse all detectable diseases with information
- 🎨 **Premium UI** — Beautiful dark-themed interface designed for non-technical users

## 🌾 Supported Crops

Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Bell Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.x |
| Deep Learning | TensorFlow / Keras |
| Image Processing | OpenCV |
| Visualization | Matplotlib |
| Web App | Streamlit |
| Dataset | PlantVillage (38 classes) |

## 📁 Project Structure

```
CropDiseaseDetection/
├── dataset/PlantVillage/    # Raw dataset (download from Kaggle)
├── data/                    # Prepared train/val/test splits
├── models/                  # Trained model & class mappings
├── scripts/
│   ├── prepare_data.py      # Dataset splitting script
│   └── train_model.py       # CNN training (local + Colab)
├── app/
│   ├── app.py               # Streamlit web application
│   ├── predict.py           # Prediction module
│   ├── disease_info.py      # Disease database (38 classes)
│   └── requirements.txt     # Dependencies
├── reports/                 # Training plots & reports
└── README.md
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r app/requirements.txt
```

### 2. Download Dataset

Download the PlantVillage dataset from Kaggle:
[https://www.kaggle.com/datasets/emmarex/plantdisease](https://www.kaggle.com/datasets/emmarex/plantdisease)

Extract it to `dataset/PlantVillage/` so the structure looks like:
```
dataset/PlantVillage/
├── Apple___Apple_scab/
├── Apple___Black_rot/
├── ...
└── Tomato___healthy/
```

### 3. Prepare Dataset

```bash
cd CropDiseaseDetection
python scripts/prepare_data.py
```

### 4. Train Model

**Local:**
```bash
python scripts/train_model.py
```

**Google Colab:**
1. Upload the `CropDiseaseDetection` folder to Google Drive
2. Open `scripts/train_model.py` in Colab
3. The script auto-detects Colab and mounts Google Drive
4. Run the script — it will save the model to Drive

### 5. Run Web App

```bash
streamlit run app/app.py
```

## 📊 Model Architecture

Custom CNN with 4 convolutional blocks:
- Conv2D (32) → BatchNorm → MaxPool → Dropout
- Conv2D (64) → BatchNorm → MaxPool → Dropout
- Conv2D (128) → BatchNorm → MaxPool → Dropout
- Conv2D (256) → BatchNorm → MaxPool → Dropout
- GlobalAveragePooling → Dense(512) → Dense(256) → Softmax(38)

**Image Size:** 128×128 pixels
**Optimizer:** Adam
**Loss:** Categorical Crossentropy

## 📈 Expected Accuracy

| Project Type | Target Accuracy |
|-------------|----------------|
| Mini Project | 80–85% |
| Major Project | 90–95% |

## ⚠️ Limitations

- Requires clear, well-lit leaf images
- Limited by the PlantVillage dataset coverage
- Requires internet/device to access the web app

## 🔮 Future Enhancements

- Transfer Learning (ResNet, MobileNet)
- Real-time webcam detection
- Mobile app integration
- Multi-language support (Hindi/Marathi)
- IoT sensor integration
- Drone-based monitoring

---

**Built with ❤️ using TensorFlow, Keras & Streamlit**
