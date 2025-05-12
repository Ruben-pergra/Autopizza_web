from flask import Flask, request, render_template, jsonify
import paho.mqtt.client as mqtt
import ssl
import threading
import json

app = Flask(__name__)

# MQTT Config
MQTT_BROKER = 'broker.emqx.io'
MQTT_PORT = 8084
MQTT_TOPIC = 'test/pizzabot'

# Estado para mensaje recibido
mensaje_recibido = {"msg": ""}

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker MQTT")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Error de conexión MQTT: {rc}")

def on_message(client, userdata, msg):
    global mensaje_recibido
    try:
        payload = json.loads(msg.payload.decode())
        if "msg" in payload and payload["msg"] == "leer":
            print("Mensaje 'leer' recibido")
            mensaje_recibido["msg"] = "leer"
    except Exception as e:
        print("Error al procesar mensaje:", e)

# Inicializar cliente MQTT en un hilo aparte
def mqtt_background_loop():
    client = mqtt.Client(transport="websockets")
    client.tls_set(cert_reqs=ssl.CERT_NONE)
    client.tls_insecure_set(True)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()

mqtt_thread = threading.Thread(target=mqtt_background_loop)
mqtt_thread.daemon = True
mqtt_thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estado')
def estado():
    # Devolver estado y resetear si ya se leyó
    if mensaje_recibido["msg"] == "leer":
        mensaje_recibido["msg"] = ""
        return jsonify({"nuevo": True})
    return jsonify({"nuevo": False})

@app.route('/enviar', methods=['POST'])
def enviar():
    try:
        mensaje = "Hola desde Flask con WebSocket TLS"
        mqtt_client = mqtt.Client(transport="websockets")
        mqtt_client.tls_set(cert_reqs=ssl.CERT_NONE)
        mqtt_client.tls_insecure_set(True)

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                client.publish(MQTT_TOPIC, mensaje)

        mqtt_client.on_connect = on_connect
        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
        mqtt_client.loop_start()
        import time
        time.sleep(2)
        mqtt_client.loop_stop()

        return 'Mensaje enviado correctamente'
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
