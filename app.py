from flask import Flask, request, render_template
import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT Config
MQTT_BROKER = 'broker.hivemq.com'  # puedes cambiarlo a otro
MQTT_PORT = 1883
MQTT_TOPIC = 'test/pizzabot'
MQTT_USERNAME = 'AutoPizza'  # pon lo que tú quieras
MQTT_PASSWORD = '8523'

# Cliente MQTT
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
mqtt_client.loop_start()

@app.route('/')
def index():
    return render_template('index.html')  # asegúrate de tener el HTML en /templates

@app.route('/pedido', methods=['POST'])
def pedido():
    data = request.get_json()
    usuario = data.get('usuario', 'anónimo')
    pizza = data.get('pizza', 'desconocida')
    mensaje = f"{usuario} ha pedido: {pizza}"
    mqtt_client.publish(MQTT_TOPIC, mensaje)
    return 'Pedido enviado'

if __name__ == '__main__':
    app.run(debug=True)
