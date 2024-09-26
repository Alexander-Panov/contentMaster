import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

def word_statistics(text: str) -> int:
    return len(text.split())


def symbol_statistics(text: str) -> int:
    return len(text)


def keywords_statistics(text: str, lang="english") -> dict[str: int]:
    nltk.download('punkt_tab')
    nltk.download("stopwords")

    """ Возвращает словарь наиболее встречающихся ключевых слов с их частотой использования """
    # Создание объекта TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Tokenize the new text using NLTK
    words = word_tokenize(text)

    # Remove stopwords using NLTK
    new_filtered_words = [word for word in words if word.lower() not in stopwords.words(lang)]

    # Join the filtered words to form a clean text
    new_clean_text = ' '.join(new_filtered_words)

    # Применение TF-IDF к текстовым данным
    tfidf_matrix = tfidf_vectorizer.fit_transform([new_clean_text])

    # Получение списка ключевых слов и их значения TF-IDF для первого документа
    feature_names = tfidf_vectorizer.get_feature_names_out()

    tfidf_scores = tfidf_matrix.toarray()[0] / tfidf_matrix.max()


    # Сортировка слов по значениям TF-IDF
    sorted_keywords = [word for score, word in sorted(zip(tfidf_scores, feature_names), reverse=True) if score > 0.15][:5]

    return {word: new_clean_text.count(word) for word in sorted_keywords}


def clear_markdown(text: str) -> str:
    """ Очищает текст от Markdown разметки"""
    from io import StringIO

    from markdown import Markdown

    def unmark_element(element, stream=None):
        if stream is None:
            stream = StringIO()
        if element.text:
            stream.write(element.text)
        for sub in element:
            unmark_element(sub, stream)
        if element.tail:
            stream.write(element.tail)
        return stream.getvalue()

    # patching Markdown
    Markdown.output_formats["plain"] = unmark_element
    __md = Markdown(output_format="plain")
    __md.stripTopLevelTags = False

    return __md.convert(text)
