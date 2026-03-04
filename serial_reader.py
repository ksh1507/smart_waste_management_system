import serial
import json
import time

# Open serial port (update COM port if needed)
ser = serial.Serial('COM6', 9600, timeout=2)

# JSON data structure
data = {
    "mainDistance": None,
    "objectDetected": None,
    "moisture": None,
    "type": None,
    "angle": None,
    "fillWet": None,
    "fillDry": None,
    "levelWet": None,
    "levelDry": None,
    "timestamp": "N/A"
}

while True:
    try:
        line = ser.readline().decode().strip()
        if not line or "=" not in line:
            continue

        parts = line.split("&")
        for part in parts:
            if "=" in part:
                key, value = part.split("=")
                key = key.strip()
                value = value.strip()
                if key in data:
                    if key in ["type"]:
                        data[key] = value
                    else:
                        data[key] = int(value)

        data["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")

        with open("data.json", "w") as f:
            json.dump(data, f, indent=2)

        print("🔄 Data updated:", data)

    except Exception as e:
        print("❌ Error:", e)
        # Fallback: mark all values as "NO DATA" except timestamp
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        fallback_data = {k: "NO DATA" if k != "timestamp" else now for k in data}
        with open("data.json", "w") as f:
            json.dump(fallback_data, f, indent=2)
        time.sleep(1)
