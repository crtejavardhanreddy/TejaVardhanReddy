import openai
from OpenAI_Keys import openAi_key

openai.api_key = openAi_key

def poem_on_samosa():
    prompt = 'Write a poem on Samosa'

response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {
            "role" : "User" ,
            "content": "Write a poem on samosa"
        }
    ]
)
print(response.choices[0]['message']['content'])


if __name__ == '__main__':
    poem_on_samosa()