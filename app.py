from flask import Flask, request, render_template
import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT Config
MQTT_BROKER = 'broker.hivemq.com'
MQTT_PORT = 8884
MQTT_TOPIC = 'test/pizzabot'

# Configurar cliente MQTT
mqtt_client = mqtt.Client()

try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
    mqtt_client.loop_start()
    print("✅ Conectado al broker MQTT")
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
        print("Mensaje MQTT enviado:", mensaje)
        return 'OK'
    except Exception as e:
        print("Error al enviar mensaje MQTT:", e)
        return 'ERROR', 500

if __name__ == '__main__':
    app.run()
