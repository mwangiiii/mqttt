import paho.mqtt.client as mqtt
import socket
import time

BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "gateway/ip"
RETRY_DELAY = 5

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to the MQTT broker.")
    else:
        print(f"Failed to connect, return code {rc}")

def get_ip_address():
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
        return ip_address
    except Exception as e:
        print(f"Error retrieving IP address: {e}")
        return None

# Create an MQTT client instance
client = mqtt.Client()

# Assign the on_connect callback function
client.on_connect = on_connect

# Attempt to connect to the broker
while True:
    try:
        client.connect(BROKER, PORT, 60)
        break
    except Exception as e:
        print(f"Connection failed: {e}. Retrying in {RETRY_DELAY} seconds...")
        time.sleep(RETRY_DELAY)

# Start the MQTT client loop
client.loop_start()

# Fetch the dynamic IP address
ip_address = get_ip_address()

# Publish the IP address to the MQTT topic
if ip_address:
    client.publish(TOPIC, ip_address)
    print(f"IP Address published to topic '{TOPIC}': {ip_address}")
else:
    print("No IP address to publish.")
