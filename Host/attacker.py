import requests
import random
import time

TARGET_IP = "192.168.59.36"  # Replace with Target Device's IP
TARGET_PORT = 5050  # Must match the Flask server port

# Simulated attack log generator
def send_attack():
    attack_types = ["Normal", "SQL Injection", "DDoS", "Malware", "Zero-Day"]
    while True:
        log = {
            "IP": f"192.168.1.{random.randint(1, 255)}",
            "Flow Duration": random.randint(100, 10000),  # Added required field
            "Total Fwd Packets": random.randint(1, 100),  # Added required field
            "Total Backward Packets": random.randint(1, 100),  # Added required field
            "Fwd Packet Length Mean": random.uniform(0.1, 1500.0),  # Added required field
            "CPU Usage": random.randint(1, 100),
            "Memory": random.randint(100, 8000),
            "Request Type": random.choice(attack_types)
        }
        print(f"Sending log: {log}")
        
        try:
            response = requests.post(f"http://{TARGET_IP}:{TARGET_PORT}/receive_log", json=log)
            print(f"Response: {response.status_code}, {response.text}")  # Debugging response
        except Exception as e:
            print(f"Error sending log: {e}")
        
        time.sleep(2)  # Send logs every 2 seconds

if __name__ == "__main__":
    send_attack()
