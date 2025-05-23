// URL del broker y topic de lectura
const BROKER_URL  = 'wss://broker.emqx.io:8084/mqtt';
const TOPIC_DATOS = 'recibir/datos';

// Conectamos al broker por WebSocket seguro
const client = mqtt.connect(BROKER_URL, {
  reconnectPeriod: 1000
});

client.on('connect', () => {
  console.log('→ Conectado al broker MQTT');
  client.subscribe(TOPIC_DATOS, err => {
    if (err) {
      console.error('Error suscribiendo a', TOPIC_DATOS, err);
    } else {
      console.log('→ Suscrito a', TOPIC_DATOS);
    }
  });
});

client.on('message', (topic, message) => {
  if (topic !== TOPIC_DATOS) return;

  // Payload puede ser "pizzas_hechas: 5" o solo "5"
  let payload = message.toString().trim();
  let valor = payload.includes(':')
    ? payload.split(':')[1].trim()
    : payload;

  // Actualizar el contador en la página
  const span = document.getElementById('pizzas_hechas');
  if (span) span.textContent = valor;
});
