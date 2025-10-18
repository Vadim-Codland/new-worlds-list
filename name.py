import requests
import q


def gpt(text):
    prompt = {
        "modelUri": f"gpt://{q.id_ya}/yandexgpt",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "4000"
        },
        "messages": [
            {
                'role':'system',
                'text': '''
ты очень переживаешь за чистоту природы рассказываешь про важность чистоты природы , можешь рассказать
о том как утилизировать вещества и предметы и сколько что будет разлогаться но только тогда когда тебя 
об этом просят и ты умеешь шутить'''
            },
            {
                "role": "user",
                "text": text
            }
        ]
    }
    
    
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {q.key_ya}"
    }
    
    response = requests.post(url, headers=headers, json=prompt)
    result = response.json().get('result')
    return result['alternatives'][0]['message']['text']
