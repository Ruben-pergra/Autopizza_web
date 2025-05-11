from flask import Flask, request, render_template
import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT Config
MQTT_BROKER = 'broker.emqx.io'
MQTT_PORT = 8084
MQTT_TOPIC = 'test/pizzabot'

# Configurar cliente MQTT con WebSockets y TLS
mqtt_client = mqtt.Client(transport="websockets")
mqtt_client.tls_set()

try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
    mqtt_client.loop_start()
    print("✅ Conectado al broker MQTT con WebSockets")
except Exception as e:
    print("❌ Error al conectar al broker MQTT:", e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    mensaje = "Hola"
    try:
        mqtt_client.publish(MQTT_TOPIC, mensaje)
        print("📨 Mensaje MQTT enviado:", mensaje)
        return 'OK'
    except Exception as e:
        print("❌ Error al enviar mensaje MQTT:", e)
        return 'ERROR', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
