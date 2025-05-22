// Configuración del broker y topics
const BROKER_URL = 'wss://broker.emqx.io:8084/mqtt';
const TOPIC_DATOS       = 'recibir/datos';
const TOPIC_CONFIRMACION = 'mandar/qr';

// Conectamos al broker
const client = mqtt.connect(BROKER_URL, {
  reconnectPeriod: 1000
});

client.on('connect', () => {
  console.log('→ Conectado al broker MQTT');
  // Nos suscribimos a los topics que nos interesan
  client.subscribe([ TOPIC_DATOS, TOPIC_CONFIRMACION ], err => {
    if (!err) console.log('→ Suscrito a:', TOPIC_DATOS, TOPIC_CONFIRMACION);
  });
});

client.on('message', (topic, message) => {
  const msg = message.toString();
  console.log(`← [${topic}] ${msg}`);

  if (topic === TOPIC_DATOS) {
    // Actualizamos solo el contador de pizzas hechas
    // Suponemos que el payload es directamente el número o "pizzas_hechas: 12"
    let valor = msg;
    if (msg.includes(':')) {
      valor = msg.split(':')[1].trim();
    }
    document.getElementById('pizzas_hechas').textContent = valor;
  } else if (topic === TOPIC_CONFIRMACION) {
    // Lo mostramos en el log de mensajes
    const div = document.getElementById('mensajes');
    const p   = document.createElement('p');
    p.textContent = `[${new Date().toLocaleTimeString()}] ${msg}`;
    div.appendChild(p);
  }
});
