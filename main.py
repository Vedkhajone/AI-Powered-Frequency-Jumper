import subprocess
import time

print("📡 Starting AI Frequency Jumper...")

# Step 1: Collect Wi-Fi Data via Serial
print("📶 Reading Wi-Fi data from ESP32...")
subprocess.run(["python", "read_wifi_serial.py"])

# Step 2: Train the model
print("🧠 Training model on collected data...")
subprocess.run(["python", "train_model.py"])

# Step 3: Predict best Wi-Fi & send to ESP32
print("📡 Predicting best Wi-Fi and sending to ESP32...")
subprocess.run(["python", "predict_and_send.py"])

print("✅ Process Complete.")
