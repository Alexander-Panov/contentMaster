document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('generateForm');
    const suggestTopicsBtn = document.getElementById('suggestTopicsBtn');
    const suggestedTopics = document.getElementById('suggestedTopics');
    const topicsList = document.getElementById('topicsList');
    const nicheInput = document.getElementById('id_niche');
    const topicInput = document.getElementById('id_topic');
    const keywordsInput = document.getElementById('id_keywords');
    const wordCountInput = document.getElementById('id_word_count');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const loadingText = document.getElementById('loadingText');

    suggestTopicsBtn.addEventListener('click', function () {
        // Проверка на заполненность всех полей
        if (!keywordsInput.value || !wordCountInput.value || !nicheInput.value) {
            alert('Пожалуйста, заполните все поля перед генерацией тем.');
            return;
        }

        const niche = nicheInput.value;
        const keywords = keywordsInput.value;
        const word_count = wordCountInput.value;

        suggestTopicsBtn.disabled = true;
        loadingIndicator.classList.remove('d-none');
        loadingText.textContent = 'Генерация тем...';

        fetch(form.dataset.suggestTopicsAction, {
            method: 'POST',
            body: new FormData(form),
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    topicsList.innerHTML = '';
                    data.topics.forEach(topic => {
                        const button = document.createElement('button');
                        button.textContent = topic;
                        button.classList.add('btn', 'btn-outline-secondary', 'btn-sm', 'mb-2');
                        button.addEventListener('click', function (e) {
                            e.preventDefault();
                            topicInput.value = topic;
                        });
                        topicsList.appendChild(button);
                    });
                    suggestedTopics.classList.remove('d-none');
                } else {
                    console.error('Error generating topics:', data.error);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            })
            .finally(() => {
                suggestTopicsBtn.disabled = false;
                loadingIndicator.classList.add('d-none');
            });
    });
});