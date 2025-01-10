const app = Vue.createApp({
    data() {
        return {
            ipAddress: null,
            errorMessage: null,
        };
    },
    methods: {
        fetchIP() {
            const mqttClient = mqtt.connect('wss://broker.emqx.io:1883/mqtt'); // WebSocket connection to MQTT broker
            const topic = "gateway/ip";

            mqttClient.on('connect', () => {
                this.errorMessage = null;
                mqttClient.subscribe(topic, (err) => {
                    if (err) {
                        this.errorMessage = "Failed to subscribe to topic.";
                    }
                });
            });

            mqttClient.on('message', (receivedTopic, message) => {
                if (receivedTopic === topic) {
                    this.ipAddress = message.toString();
                    mqttClient.end(); // Disconnect after receiving the message
                }
            });

            mqttClient.on('error', () => {
                this.errorMessage = "Failed to connect to MQTT broker.";
            });
        },
    },
});

app.mount('#app');
