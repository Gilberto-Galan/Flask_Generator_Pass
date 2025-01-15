// Obtener elementos
const copyButton = document.getElementById('copyButton');
const passwordField = document.getElementById('passwordField');
const copyModal = new bootstrap.Modal(document.getElementById('copyModal'));

// Función para copiar al portapapeles
if (copyButton && passwordField) {
    copyButton.addEventListener('click', () => {
        // Seleccionar el texto del campo de contraseña
        passwordField.select();
        passwordField.setSelectionRange(0, 99999); // Para dispositivos móviles

        // Copiar el texto al portapapeles
        document.execCommand('copy');

        // Mostrar el modal de confirmación
        copyModal.show();
    });
}
