from flask import Flask, request, render_template
import paho.mqtt.client as mqtt
import ssl
import qrcode
import io
import base64

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

        mqtt_client.tls_set(cert_reqs=ssl.CERT_NONE)
        mqtt_client.tls_insecure_set(True)

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Conectado correctamente")
                client.publish(MQTT_TOPIC, mensaje)
            else:
                print(f"Falló la conexión: {rc}")

        mqtt_client.on_connect = on_connect
        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
        mqtt_client.loop_start()

        import time
        time.sleep(2)
        mqtt_client.loop_stop()

        # Generar QR
        qr = qrcode.make(mensaje)
        buffer = io.BytesIO()
        qr.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

        # Pasar la imagen codificada al HTML
        return render_template('qr.html', qr_image=img_str)

    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True))
