const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const stad = document.querySelector('#stad').value;
  fetch(`get_weather/${stad}`).then(response => response.text()).then(console.log);
});


fetch(`get_weather/den haag`).then(response => response.text()).then(console.log);