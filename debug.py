import paho.mqtt.publish as publish

try:
    publish.single(
        topic="test/pizzabot",
        payload="debugueando",
        hostname="broker.hivemq.com",
        port=1883,
        client_id="debug-client"
    )
    print("Mensaje enviado correctamente")
except Exception as e:
    print("Error al enviar mensaje MQTT:", e)
