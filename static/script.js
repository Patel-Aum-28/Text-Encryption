function submitForm(event, operation) {
    event.preventDefault();
    var form = event.target;
    var formData = new FormData(form);
    
    fetch(form.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('output-text').value = data;
    })
    .catch(error => console.error('Error:', error));
}
