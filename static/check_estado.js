setInterval(() => {
  fetch('/estado')
    .then(response => response.json())
    .then(data => {
      if (data.nuevo) {
        alert("Mensaje 'leer' recibido por MQTT");
      }
    });
}, 2000);
