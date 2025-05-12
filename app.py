from flask import Flask, request, render_template
import paho.mqtt.client as mqtt
import ssl

app = Flask(__name__)

# MQTT Config
MQTT_BROKER = 'broker.emqx.io'
MQTT_PORT = 8084  # WebSocket seguro
MQTT_TOPIC = 'test/pizzabot'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    try:
        mensaje = "Hola desde Flask con WebSocket TLS"
        mqtt_client = mqtt.Client(transport="websockets")

        # Activar TLS para WebSockets seguros (puerto 8084)
        mqtt_client.tls_set(cert_reqs=ssl.CERT_NONE)
        mqtt_client.tls_insecure_set(True)

        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
        mqtt_client.loop_start()
        mqtt_client.publish(MQTT_TOPIC, mensaje)
        mqtt_client.loop_stop()

        return 'Mensaje enviado correctamente'
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
