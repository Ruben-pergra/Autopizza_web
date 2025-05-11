from flask import Flask, request, render_template
import paho.mqtt.publish as publish

app = Flask(__name__)

# MQTT Config
MQTT_BROKER = 'broker.hivemq.com'
MQTT_PORT = 1883
MQTT_TOPIC = 'test/pizzabot'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pedido', methods=['POST'])
def pedido():
    data = request.get_json()
    usuario = data.get('usuario', 'anónimo')
    pizza = data.get('pizza', 'desconocida')
    mensaje = f"[DEBUG] {usuario} ha pedido: {pizza}"

    try:
        publish.single(MQTT_TOPIC, mensaje, hostname=MQTT_BROKER, port=MQTT_PORT)
        print("Mensaje MQTT enviado:", mensaje)
        return 'Pedido enviado correctamente'
    except Exception as e:
        print("Error al enviar mensaje MQTT:", e)
        return 'Error al enviar pedido', 500

if __name__ == '__main__':
    app.run(debug=True)
