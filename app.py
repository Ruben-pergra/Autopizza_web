from flask import Flask, request
import paho.mqtt.publish as publish

app = Flask(__name__)

@app.route("/")
def index():
    return open("templates/index.html").read()

@app.route("/boton", methods=["POST"])
def boton():
    data = request.get_json()
    mensaje = data.get("mensaje", "")

    # Enviamos mensaje al broker MQTT público de HiveMQ
    publish.single(
        topic="test/pizzabot",              # puedes cambiar el topic
        payload=mensaje,
        hostname="broker.hivemq.com",
        port=1883
    )

    return "Mensaje enviado: " + mensaje
