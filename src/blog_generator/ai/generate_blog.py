import asyncio
import re

from asgiref.sync import sync_to_async
from openai import AsyncOpenAI

from blog_generator.models import Author

client = AsyncOpenAI(base_url="https://api.vsegpt.ru/v1")

def clear_numeration(theme: str) -> str:
    return re.sub(r'^\d+\.\s*', '', theme)


async def generate_blog_topics(niche, keywords, word_count, language_model, language, style):
    # Define the prompt to guide ChatGPT in generating a list of trending blog topics
    system = f"You are an expert content strategist."

    prompt = f"""
    Your task is to generate a list of trending and current blog topics.

    **Niche**: {niche}
    **Keywords**: {', '.join(keywords)}
    **Desired Length**: {word_count} words
    **Language**: {language}
    **Style**: {style}

    Guidelines:
    1. Analyze the given niche and keywords to understand the target audience and popular interests.
    2. Generate a list of 10 to 15 blog topics that are trending and relevant to the niche.
    3. Ensure each topic is unique, specific, and has potential for high engagement.
    4. Avoid general topics; instead, focus on niche-specific and innovative ideas that stand out.
    5. Format the output as plain text where each topic starts on a new line, and only a single line break (\\n) is used between topics.

    Generate the topics in {language} and write in a {style}.

    Provide the list of blog topics below, each one on a new line:
    """

    # Generate the blog topics using ChatGPT API
    response = await client.chat.completions.create(
        model=language_model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
        top_p=0.9,
        frequency_penalty=0.5,
        presence_penalty=0.3,
        extra_headers={"X-Title": "ContentMaster"}
    )

    # Extract the generated text
    topics_text = response.choices[0].message.content.strip()
    topics = topics_text.replace('\n\n', '\n').strip().split('\n')
    # Return the list of blog topics
    return [clear_numeration(topic.strip()).strip() for topic in topics]


async def generate_blog(niche, topic, keywords, word_count, author: Author, language_model, language, style):
    """
    :param niche: тематика
    :param topic: название
    :param keywords: ключевые слова
    :param word_count: длина блога
    :param author: информация об авторе (словарный запас, тональность, описание)
    :return:
    """
    # Define the prompt to guide ChatGPT in generating a blog post
    system = f"You are writing this blog post as {author.name}, who is an expert in {niche}. Your tone should be {author.tone}, and the blog should be written in {language} in a {style} style"

    # Include the author's bio, vocabulary, and specialization
    author_info = f"""
    Author bio: {author.bio}
    Vocabulary and phrases: {', '.join(author.phrases)}
    Specialization: {author.niche}
    """

    # Main prompt for blog generation
    prompt = f"""    
    Your task is to write a detailed blog post in the style of {author.name}.

    **Niche**: {niche}
    **Topic**: {topic}
    **Keywords**: {', '.join(keywords)}
    **Desired Length**: {word_count} words
    **Language**: {language}
    **Style**: {style}

    Guidelines:
    1. Write in a style and tone consistent with the author's typical writing (Tone: {author.tone}, Style: {style}).
    2. Incorporate the author's vocabulary and phrases where appropriate (Vocabulary: {', '.join(author.phrases)}).
    3. Start with an engaging introduction that introduces the topic and hooks the reader.
    4. Develop the content by expanding on the main points related to the keywords.
    5. Use subheadings, bullet points, or numbered lists where appropriate to enhance readability.
    6. Conclude with a summary and a call to action or thought-provoking question.
    7. Ensure the content is well-structured, coherent, and formatted in Markdown.

    Begin writing below:
    # {topic}
    """

    response = await client.chat.completions.create(
        model=language_model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": author_info},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        top_p=0.9,
        frequency_penalty=0.5,
        presence_penalty=0.3,
        extra_headers={"X-Title": "ContentMaster"}
    )

    # Extract the generated text
    blog_text = response.choices[0].message.content.replace(f"# {topic}", '').strip()

    return blog_text


async def main():
    # Example usage
    niche = "Tech"
    keywords = ["AI", "blockchain", "cybersecurity", "machine learning", "IoT"]
    word_count = 150

    # blog_topics = await generate_blog_topics(niche, keywords, word_count)
    # print(blog_topics)

    # Example usage
    niche = "Health"
    topic = "The Benefits of a Plant-Based Diet"
    keywords = ["health", "nutrition", "sustainability", "plant-based proteins", "recipes"]
    word_count = 800

    def get_author(author_id):
        # Сохраняем данные в сессии
        return Author.objects.get(id=author_id)

    author = await sync_to_async(get_author)(14)

    blog_post = await generate_blog(niche, topic, keywords, word_count, author)
    print(blog_post)


if __name__ == '__main__':
    asyncio.run(main())
