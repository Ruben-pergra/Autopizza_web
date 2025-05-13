from flask import Flask, request, render_template
import paho.mqtt.client as mqtt
import ssl

app = Flask(_name_)

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

        # Define on_connect callback
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Conectado correctamente")
                client.publish(MQTT_TOPIC, mensaje)
            else:
                print(f"Falló la conexión: {rc}")

        mqtt_client.on_connect = on_connect

        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
        mqtt_client.loop_start()

        # Esperar brevemente para dar tiempo al publish (simple workaround)
        import time
        time.sleep(2)
        mqtt_client.loop_stop()

        return 'Mensaje enviado correctamente'
    except Exception as e:
        return f"Error: {str(e)}", 500

if _name_ == '_main_':
    app.run(debug=True)
