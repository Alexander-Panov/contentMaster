import asyncio

from openai import AsyncOpenAI

client = AsyncOpenAI()
MODEL = "gpt-4o-mini"


async def generate_blog_topics(niche, keywords, word_count):
    # Define the prompt to guide ChatGPT in generating a list of trending blog topics
    system = f"You are an expert content strategist."

    prompt = f"""
    Your task is to generate a list of trending and current blog topics.

    **Niche**: {niche}
    **Keywords**: {', '.join(keywords)}
    **Desired Length**: {word_count} words

    Guidelines:
    1. Analyze the given niche and keywords to understand the target audience and popular interests.
    2. Generate a list of 10 to 15 blog topics that are trending and relevant to the niche.
    3. Ensure each topic is unique, specific, and has potential for high engagement.
    4. Avoid general topics; instead, focus on niche-specific and innovative ideas that stand out.
    5. Format the output as a list of raw topics, each one starts on a new line.

    Provide the list of blog topics below:
    """

    # Generate the blog topics using ChatGPT API
    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
        top_p=0.9,
        frequency_penalty=0.5,
        presence_penalty=0.3
    )

    # Extract the generated text
    topics_text = response.choices[0].message.content.strip()

    # Return the list of blog topics
    return topics_text.split('\n')


async def generate_blog(niche, topic, keywords, word_count):
    """

    :param niche: тематика
    :param topic: название
    :param keywords: ключевые слова
    :param word_count: длина блога
    :return:
    """
    # Define the prompt to guide ChatGPT in generating a blog post
    system = f"You are an expert {niche} blog writer."
    prompt = f"""    
    Your task is to write a detailed blog post.
    
    **Niche**: {niche}
    **Topic**: {topic}
    **Keywords**: {', '.join(keywords)}
    **Desired Length**: {word_count} words

    Guidelines:
    1. Start with an engaging introduction that introduces the topic and hooks the reader.
    2. Develop the content by expanding on the main points related to the keywords.
    3. Use subheadings, bullet points, or numbered lists where appropriate to enhance readability.
    4. Conclude with a summary and a call to action or thought-provoking question.
    5. Ensure the content is well-structured, coherent, and formatted in Markdown.

    Begin writing below:
    #{topic}
    """

    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        top_p=0.9,
        frequency_penalty=0.5,
        presence_penalty=0.3
    )

    # Extract the generated text
    blog_text = response.choices[0].message.content.strip()

    return blog_text


async def main():
    # Example usage
    niche = "Tech"
    keywords = ["AI", "blockchain", "cybersecurity", "machine learning", "IoT"]
    word_count = 150

    blog_topics = await generate_blog_topics(niche, keywords, word_count)
    print(blog_topics)

    # Example usage
    niche = "Health"
    topic = "The Benefits of a Plant-Based Diet"
    keywords = ["health", "nutrition", "sustainability", "plant-based proteins", "recipes"]
    word_count = 800

    blog_post = await generate_blog(niche, topic, keywords, word_count)
    print(blog_post)


if __name__ == '__main__':
    asyncio.run(main())
