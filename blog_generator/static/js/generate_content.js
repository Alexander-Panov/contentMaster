// static/js/generate_content.js


document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('generateForm');
    const generateButton = document.getElementById('generateButton');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const errorMessage = document.getElementById('errorMessage');

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        generateButton.disabled = true;
        loadingIndicator.classList.remove('d-none');
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