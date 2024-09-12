import asyncio

from openai import OpenAI, AsyncOpenAI

client = AsyncOpenAI()
MODEL = "gpt-4o-mini"


async def generate_blog(topic, keywords, word_count):
    # Define the prompt to guide ChatGPT in generating a blog post
    system = "You are an expert blog writer. "
    prompt = f"""    
    Your task is to write a detailed blog post.

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
    topic = "The Benefits of a Plant-Based Diet"
    keywords = ["health", "nutrition", "sustainability", "plant-based proteins", "recipes"]
    word_count = 800

    blog_post = await generate_blog(topic, keywords, word_count)
    print(blog_post)


if __name__ == '__main__':
    asyncio.run(main())
