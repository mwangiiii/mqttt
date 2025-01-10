# IoT Gateway IP Address Publisher

This project simulates an application that uses MQTT to publish the dynamic IP address of a gateway to a subscriber. It is intended for scenarios where the static IP of a LoRa gateway is lost due to network changes, and users need to remotely retrieve the current IP.

---

## 📜 **Project Description**

The application connects to an MQTT broker and:
1. Reads the current dynamic IP address of the system.
2. Publishes the IP address to a specific MQTT topic (`gateway/ip`).
3. Allows subscribers to retrieve the IP in real-time by subscribing to the same topic.

This project is simulated on a standard computer in place of a Raspberry Pi and uses tools like Python and MQTT.

---

## 🎯 **Features**

- Connects to a public MQTT broker (`broker.emqx.io`).
- Automatically retries connection every 5 seconds if the broker is unavailable.
- Reads the system's dynamic IP address assigned via WiFi.
- Publishes the IP address to a topic (`gateway/ip`).
- Allows subscribers to receive the IP by listening to the same topic.

---

## 🛠️ **Tools & Technologies**

### **Software**
- Python
- Paho-MQTT library for Python
- MQTT Explorer for testing subscriptions
- Git for version control

### **Hardware (Optional for Simulation)**
- Raspberry Pi (simulated in this project as a PC)
---

## 🚀 **Setup & Usage**

### 1. **Clone the Repository**
```bash
git clone <repository-url>
cd iot_internship
```

### 2. Install Dependencies
Ensure Python is installed. Install the required library:
```bash
pip install paho-mqtt
```

### 3. Run the Publisher
start the publisher. 
```bash
python mqtt_ip_publisher.py
```
### 4. Run the Subscriber
In another terminal, run the subscriber to verify the IP:
```bash
python mqtt_ip_subscriber.py
```
### 5. Test with MQTT Explorer (Optional)
1. Connect to the broker (broker.emqx.io, Port 1883).
2. Subscribe to the topic: gateway/ip.
3. Verify the IP address is published in real-time.

---

## 📝 Scripts Overview
1. mqtt_ip_publisher.py
-    Connects to the MQTT broker.
-    Retrieves the system's dynamic IP address using socket.
-    Publishes the IP to the gateway/ip topic every 10 seconds.
2. mqtt_ip_subscriber.py
-    Connects to the MQTT broker.
-    Subscribes to the gateway/ip topic.
-    Prints the received IP address.
## 🌐 MQTT Broker Details
Host: broker.emqx.io
Port: 1883
Topic: gateway/ip
---

## 🤝 Contributing

1.Fork the repository.

2. Create a feature branch:
```bash
git checkout -b feature-name
```
3. Commit your changes:
```bash
git commit -m "Add feature"
```
4. Push to the branch:
```bash
git push origin feature-name
```
5. Open a pull request.

