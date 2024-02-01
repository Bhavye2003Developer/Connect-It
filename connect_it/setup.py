import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

# print(ip)

os.system("pip install -r requirements.txt")
print("packages installed successfully...")
os.system(f"python manage.py runserver {ip}:8000")
