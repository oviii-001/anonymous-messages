

document.getElementById('messageForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const message = document.getElementById('messageInput').value;
    document.getElementById('messageDisplay').innerText = `Anonymous Message: ${message}`;
    document.getElementById('messageInput').value = '';
});

