import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

# Create MQTT client instance
client = mqtt.Client()

# Define the callback for receiving messages
client.on_message = on_message

# Connect to the MQTT broker
client.connect("broker.emqx.io", 1883, 60)

# Subscribe to the topic
client.subscribe("gateway/ip")

# Start listening for messages
client.loop_forever()
