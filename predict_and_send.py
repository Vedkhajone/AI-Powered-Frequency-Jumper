import pandas as pd
import serial
import time
import joblib
import wifi_scanner  # Your WiFi scan logic here

# Load model
model = joblib.load('model/wifi_model.pkl')

# Setup serial
ser = serial.Serial('COM6', 9600)  # Use your COM port

# Scan WiFi
wifi_data = wifi_scanner.scan_wifi()  # Get list of dicts

# Create DataFrame
df = pd.DataFrame(wifi_data)

# Add Congestion
channel_counts = df['Channel'].value_counts().to_dict()
df['Congestion'] = df['Channel'].map(channel_counts)

# Prediction
X = df[['RSSI', 'Channel', 'Congestion']]
predictions = model.predict(X)

# Choose best
df['Prediction'] = predictions
best = df[df['Prediction'] == 1].sort_values(by='RSSI', ascending=False).head(1)

if not best.empty:
    ssid_to_use = best.iloc[0]['SSID']
    print("🟢 GOOD network:", ssid_to_use)
    ser.write(f"JUMP:{ssid_to_use}\n".encode())
else:
    print("🔴 No good network found.")
    ser.write(b"STAY\n")
