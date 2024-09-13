// static/js/generate_content.js


document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('generateForm');
    const generateButton = document.getElementById('generateButton');
    const errorMessage = document.getElementById('errorMessage');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const loadingText = document.getElementById('loadingText');

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        generateButton.disabled = true;
        loadingIndicator.classList.remove('d-none');
        loadingText.textContent = 'Генерация контента...';
        errorMessage.classList.add('d-none');

        fetch(form.action, {
            method: 'POST',
            body: new FormData(form),
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = data.redirect_url;
                } else {
                    throw new Error(data.error);
                }
            })
            .catch(error => {
                errorMessage.textContent = `Ошибка: ${error.message}`;
                errorMessage.classList.remove('d-none');
            })
            .finally(() => {
                generateButton.disabled = false;
                loadingIndicator.classList.add('d-none');
            });
    });
});