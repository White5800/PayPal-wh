const form = document.getElementById('demoForm');

form.addEventListener('submit', (event) => {
  event.preventDefault(); 

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Envoi des données au serveur (remplace 'votre-serveur.com')
  fetch('http://votre-serveur.com/submit', { 
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ username, password })
  })
  .then(response => {
    // Gère la réponse du serveur
    console.log('Données envoyées :', response);
  })
  .catch(error => console.error('Erreur :', error));
});

