from openai import OpenAI


def generate_text(prompt):
    response = client.chat.completions.create(
        model = "gpt-4",
        messages = [
            {'role':'system','content':'You are a knowledgeable instructor for elementary school students'},
            {'role':'user','content': prompt}
        ],
        temperature = 0,
        max_tokens= 200,
    )
    result = response.choices[0].message.content.strip()

    return result


# response = client.images.generate(
#     prompt = prompt,
#     n = 1,
#     size ="512x512"
# )
#
# print(response.data[0].url)