document.getElementById('clearBtn').addEventListener('click', function() {
    document.getElementById('loginForm').reset();
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const formData = new FormData(this);
    formData.append('requestType', 'insert');
    fetch('', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
        },
        body: formData,
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not ok.');
        }
    })
    .then(data => {
        if (data.redirect_url) {
            window.location.href = data.redirect_url;
        } else {
            console.log(data);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.getElementById('updateData').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const formData = new FormData(this);
    
    fetch('', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
        },
        body: formData,
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not ok.');
        }
    })
    .then(data => {
        if (data.redirect_url) {
            window.location.href = data.redirect_url;
        } else {
            console.log(data);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});