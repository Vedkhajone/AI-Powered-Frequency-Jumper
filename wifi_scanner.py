import subprocess
import re

def scan_wifi():
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'networks', 'mode=bssid'], shell=True).decode('utf-8', errors='ignore')
    networks = result.split('\n')
    wifi_list = []

    ssid, rssi, channel = None, None, None

    for line in networks:
        line = line.strip()
        if line.startswith("SSID"):
            ssid = line.split(":", 1)[1].strip()
        elif "Signal" in line:
            rssi = int(line.split(":")[1].strip().replace('%', ''))
        elif "Channel" in line:
            channel = int(line.split(":")[1].strip())
            if ssid and rssi and channel:
                wifi_list.append({'SSID': ssid, 'RSSI': rssi, 'Channel': channel})
                ssid, rssi, channel = None, None, None

    return wifi_list
