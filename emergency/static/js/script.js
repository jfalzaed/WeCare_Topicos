// Función para detectar si el usuario está en un dispositivo móvil
function isMobileDevice() {
    return /Mobi|Android/i.test(navigator.userAgent);
}

// Función para manejar las llamadas de emergencia
function handleEmergencyCall(number, service) {
    if (isMobileDevice()) {
        // Si es un dispositivo móvil, confirma antes de llamar directamente
        if (confirm(`Are you sure you want to call ${service}?`)) {
            window.location.href = `tel:${number}`;
        }
    } else {
        // Si es una computadora, muestra el número como una alerta
        alert(`On a computer, please call ${number} for ${service}.`);
    }
}

