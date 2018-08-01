const signUp = () => {
  fetch('http://127.0.0.1:5000/api/v1/auth/signup', {
    method: 'POST',
    body: JSON.stringify({
      name: document.querySelector('input[name=name]').value,
      username: document.querySelector('input[name=username]').value,
      email: document.querySelector('input[name=email]').value,
      password: document.querySelector('input[name=password]').value
    }),
    headers: {
      'content-type': 'application/json'
    }
  })
    .then(response => {
      if (!response.ok) {
        document.querySelector('p#signup-message').innerHTML = 'Please Try Again!'
      }
      response.json()
    })
    .then(data => {
      if (data) {
        document.querySelector('p#signup-message').innerHTML = 'Success! Please Sign In'
      }
    })
}

const signIn = () => {
  
}