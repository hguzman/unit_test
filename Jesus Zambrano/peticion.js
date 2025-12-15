fetch('https://jsonplaceholder.typicode.com/users')
    .then(response => response.json())
    .then(users => 
        users.forEach(user => {
            const nombre = document.createElement('h2');
            nombre.innerHTML = user.name;
            document.body.appendChild(nombre); 
        })
    )
