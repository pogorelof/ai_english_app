from openai import OpenAI
from dotenv import load_dotenv
import os
import json


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    api_key=OPENAI_API_KEY
)

def check_translate_ai(word, user_translate):
    text_for_ai = f'{word}-{user_translate}'
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": "Определите правильность перевода английского слова на русский и предоставьте объяснения и советы. Укажите верный перевод слова. \n\n# Steps\n\n1. Получите английское слово и его перевод на русском через тире.\n2. Определите, является ли представленный перевод правильным.\n3. Если перевод неправильный, объясните причину ошибки и дайте рекомендации.\n4. В любом случае укажите правильный перевод слова.\n\n# Output Format\n\nФорматируйте ответ в виде JSON:\n- `result`: (true/false) указывает, является ли перевод правильным.\n- `explanation`: объясняет причину ошибки и дает советы, обязательно дает совет по изучению языка.\n- `translate`: правильный перевод английского слова на русский.\n\n# Examples\n\n# Notes\n\n- Обратите внимание на часто встречающиеся ошибки, такие как неверное написание или ложные друзья в языке.\n- Каждый выход должен включать правильный перевод, даже если первоначальный перевод верный."
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": text_for_ai
            }
        ]
        }
    ],
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={
        "type": "json_object"
    }
    )
    
    data = response.choices[0].message.content
    return json.loads(data)