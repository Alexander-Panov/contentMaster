document.addEventListener('DOMContentLoaded', function () {

    //blog analytic
    const blog = document.getElementById('blogContent');
    const blogContent = blog.innerText;
    const analyticsModal = document.getElementById('analyticsModal');
    const analyticsContent = document.getElementById('analyticsContent');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const errorMessage = document.getElementById('errorMessage');
    let analyticsLoaded = false;

    analyticsModal.addEventListener('show.bs.modal', function (event) {
        showAnalyticsContent()
        if (!analyticsLoaded) {
            loadAnalytics();
        } else {
            showAnalyticsContent();
        }
    });

    // copy button
    const copyButton = document.getElementById('copyButton');

    copyButton.addEventListener('click', function () {
        // Создаем временный элемент textarea
        const tempTextArea = document.createElement('textarea');
        tempTextArea.value = blogContent;
        document.body.appendChild(tempTextArea);

        // Выбираем текст
        tempTextArea.select();
        tempTextArea.setSelectionRange(0, 99999); // Для мобильных устройств

        // Копируем текст
        document.execCommand('copy');

        // Удаляем временный элемент
        document.body.removeChild(tempTextArea);

        // Изменяем иконку и текст кнопки для обратной связи
        copyButton.innerHTML = '<i class="bi bi-check"></i>';
        copyButton.classList.add('btn-success');
        copyButton.classList.remove('btn-outline-secondary');

        // Возвращаем исходный вид кнопки через 2 секунды
        setTimeout(() => {
            copyButton.innerHTML = '<i class="bi bi-clipboard"></i>';
            copyButton.classList.remove('btn-success');
            copyButton.classList.add('btn-outline-secondary');
        }, 2000);
    });

    function loadAnalytics() {
        loadingIndicator.style.display = 'block';
        analyticsContent.style.display = 'none';
        errorMessage.innerHTML = ''

        // Отправляем запрос на сервер для получения аналитики
        fetch(blog.dataset.blogAnalyticAction)
            .then(response => response.json())
            .then(data => {
                document.getElementById('wordCount').textContent = data.word_count + ' ' + getWordForm(data.word_count, ['слово', 'слова', 'слов']);
                document.getElementById('symbolCount').textContent = data.symbol_count + ' ' + getWordForm(data.symbol_count, ['символ', 'символа', 'символов']);

                const keywordsList = document.getElementById('keywordsList');
                keywordsList.innerHTML = '';
                Object.entries(data.keywords).forEach(([keyword, frequency]) => {
                    const li = document.createElement('li');
                    li.textContent = `${keyword}: ${frequency} ${getWordForm(frequency, ['раз', 'раза', 'раз'])}`;
                    keywordsList.appendChild(li);
                });
                analyticsLoaded = true;
                showAnalyticsContent()
            })
            .catch(error => {
                loadingIndicator.style.display = 'none';
                console.error('Error:', error);
                errorMessage.innerHTML = '<p class="text-danger">Ошибка при загрузке аналитики. Пожалуйста, попробуйте позже.</p>';
            })
    }

    function showAnalyticsContent() {
        loadingIndicator.style.display = 'none';
        analyticsContent.style.display = 'block';
    }

    function getWordForm(number, forms) {
        const cases = [2, 0, 1, 1, 1, 2];
        return forms[(number % 100 > 4 && number % 100 < 20) ? 2 : cases[(number % 10 < 5) ? number % 10 : 5]];
    }
});