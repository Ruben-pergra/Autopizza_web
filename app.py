from flask import Flask, request, render_template
import paho.mqtt.client as mqtt
import ssl
import time

app = Flask(__name__)

# Configuración MQTT
MQTT_BROKER = 'broker.emqx.io'
MQTT_PORT   = 8084       # WebSocket TLS
TOPIC_DATOS = 'test/pizzabot'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')
@app.route('/faq')
def faq():
    return render_template('faq.html')
@app.route('/eventos')
def eventos():
    return render_template('eventos.html')
@app.route('/galeria')
def galeria():
    return render_template('galeria.html')
@app.route('/tecnologia')
def tecnologia():
    return render_template('tecnologia.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    mensaje ="Pizza_bacon"
    # Publica un mensaje de pedido
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
    time.sleep(0.5)
    mqtt_client.loop_stop()
    return 'Pedido enviado'

if __name__ == '__main__':
    app.run(debug=True)
