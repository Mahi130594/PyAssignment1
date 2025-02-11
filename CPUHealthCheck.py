import psutil
import time

threshold = 1
INTERVAL = 1 #in seconds
print("Monitoring CPU usage")
try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=INTERVAL)
        if cpu_usage > threshold:
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
except KeyboardInterrupt:
    print("interrupted by the user")