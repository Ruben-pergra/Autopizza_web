from flask import Flask, request, render_template
import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT Config
MQTT_BROKER = 'broker.emqx.io'
MQTT_PORT = 8084
MQTT_TOPIC = 'test/pizzabot'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    mensaje = "Hola"
# Configurar cliente MQTT con WebSockets y TLS
    mqtt_client = mqtt.Client(transport="websockets")
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()
    print("✅ Conectado al broker MQTT con WebSockets")
    mqtt_client.publish(MQTT_TOPIC, mensaje)
    print("📨 Mensaje MQTT enviado:", mensaje)
    client.loop_stop()
    return 'OK'
    except Exception as e:
        print("❌ Error al enviar mensaje MQTT:", e)
        return 'ERROR', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
