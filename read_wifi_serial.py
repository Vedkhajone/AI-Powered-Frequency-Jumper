import serial
import csv
from datetime import datetime

# Set your port (check in Arduino IDE or Device Manager)
SERIAL_PORT = 'COM6'  # Change to '/dev/ttyUSB0' or similar on Linux/Mac
BAUD_RATE = 115200
CSV_FILE = 'data/wifi_data.csv'

# Start serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
print(f"[INFO] Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")

# Open CSV and write headers
with open('data/wifi_data.csv', 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Timestamp', 'SSID', 'RSSI', 'Channel'])

    try:
        while True:
            line = ser.readline().decode().strip()

            if line == "---":
                print("------ NEW SCAN ------")
                continue

            parts = line.split(',')
            if len(parts) == 3:
                ssid, rssi, channel = parts
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                writer.writerow([timestamp, ssid, rssi, channel])
                print(f"Saved: {ssid}, {rssi}, {channel}")

    except KeyboardInterrupt:
        print("\n[INFO] Stopped by user. CSV saved.")
        ser.close()
