const broker = 'wss://broker.emqx.io:8084/mqtt';
const topic = 'test/pizzabot';

const client = mqtt.connect(broker, {
  reconnectPeriod: 1000
});

client.on('connect', function () {
  console.log('Conectado al broker MQTT');
  client.subscribe(topic, function (err) {
    if (!err) {
      console.log('Suscrito al topic:', topic);
    }
  });
});

client.on('message', function (topic, message) {
  const mensaje = message.toString();
  console.log('Mensaje recibido:', mensaje);
  const mensajesDiv = document.getElementById('mensajes');
  const nuevo = document.createElement('p');
  nuevo.textContent = mensaje;
  mensajesDiv.appendChild(nuevo);
});
