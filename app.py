from flask import Flask, request, render_template
import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT Config
MQTT_BROKER = 'broker.hivemq.com'
MQTT_PORT = 1883
MQTT_TOPIC = 'test/pizzabot'

# Cliente MQTT sin usuario/contraseña
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
mqtt_client.loop_start()

@app.route('/')
def index():
    return render_template('index.html')  # Asegúrate de tener templates/index.html

@app.route('/pedido', methods=['POST'])
def pedido():
    data = request.get_json()
    usuario = data.get('usuario', 'anónimo')
    pizza = data.get('pizza', 'desconocida')
    mensaje = f"{usuario} ha pedido: {pizza}"
    publish.single("test/pizzabot", "debugueando", hostname="broker.hivemq.com", port=1883)
    mqtt_client.publish(MQTT_TOPIC, mensaje)
    return 'Pedido enviado correctamente'

if __name__ == '__main__':
    app.run(debug=True)
