function updateFileName(inputId) {
    const fileInput = document.getElementById(`id_${inputId}`);
    const fileNameSpan = document.getElementById(`${inputId}-name`);
    if (fileInput.files.length > 0) {
        fileNameSpan.textContent = fileInput.files[0].name;
    } else {
        fileNameSpan.textContent = 'No file chosen';
    }
}