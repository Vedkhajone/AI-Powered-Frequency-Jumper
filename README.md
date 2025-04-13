# AI-Powered Frequency Jumper 🚀

An intelligent Wi-Fi optimizer using Machine Learning and ESP32 that predicts the best available wireless network and jumps frequency automatically for enhanced communication.

## 📌 Features
- Scans nearby Wi-Fi networks (SSID & RSSI)
- Trains an ML model to detect the best network condition
- Sends prediction to ESP32 to switch frequency
- Real-time optimization for dynamic wireless environments

## 🧠 Tech Stack
- Python, Scikit-learn, Pandas
- ESP32 (Arduino framework)
- Serial communication
- Machine Learning (Classification)

## 🗂️ Folder Structure
- `data/` – Sample Wi-Fi RSSI data (CSV)
- `model/` – Trained ML model (.pkl)
- `esp32_code/` – Code to run on ESP32 to switch frequency
- `scripts/` – Python scripts for scanning, training, predicting

## ⚙️ How to Run

1. **Train Model**
   ```bash
   python scripts/train_model.py
   
2. **Start Prediction & Communication**
   ```bash
   python scripts/predict_and_send.py
   
3.**Upload ESP32 Code**
   -Use Arduino IDE or PlatformIO
   -Flash esp32_code/jumper.ino

4. **Install Requirements(imp)**
   ```bash
   pip install -r requirements.txt
   
#**DEVELOPER**
   ##**Vedhanshu Khajone**
