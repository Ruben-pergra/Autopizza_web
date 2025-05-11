from flask import Flask, request, render_template
import paho.mqtt.publish as publish

app = Flask(__name__)

MQTT_BROKER = 'broker.hivemq.com'
MQTT_PORT = 1883
MQTT_TOPIC = 'test/pizzabot'

@app.route('/')
def index():
    return render_template('basic.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    try:
        publish.single(MQTT_TOPIC, "Hola", hostname=MQTT_BROKER, port=MQTT_PORT)
        print("Mensaje MQTT enviado: Hola")
        return 'OK'
    except Exception as e:
        print("Error al enviar mensaje MQTT:", e)
        return 'ERROR', 500

if __name__ == '__main__':
    app.run(debug=True)
