// URL del broker y topic de lectura
const BROKER_URL    = 'wss://broker.emqx.io:8084/mqtt';
const TOPIC_DATOS   = 'recibir/datos';

// Conéctate al broker por WebSocket
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

  // Suponemos que el payload es algo como "pizzas_hechas: 5" o simplemente "5"
  let payload = message.toString().trim();
  let valor;
  if (payload.includes(':')) {
    valor = payload.split(':')[1].trim();
  } else {
    valor = payload;
  }

  // Actualiza el span en la página
  const span = document.getElementById('pizzas_hechas');
  if (span) {
    span.textContent = valor;
  }
});
