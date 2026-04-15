from google import genai
from openai import OpenAI
from rich.markdown import Markdown
from starlette.responses import JSONResponse

google_api_key = 'AIzaSyCQJ8itl7YR-Ptb6ONqzrunM8TuFfFI1GY'
baseurl = "https://generativelanguage.googleapis.com/v1beta/openai/"
gemini = OpenAI(base_url=baseurl, api_key=google_api_key)
system_prompt= 'Bạn là trợ lý'
user_prompt= input(f'Nhập câu hỏi:....')

def GeminiCLient(api_key):
    model = 'gemini-2.5-flash-lite'
    response = gemini.chat.completions.create(
        model = model,
        messages=[
            {
                'role': 'system',
                'content': system_prompt
            },
            {
                'role': 'user',
                'content': user_prompt
            },

        ],
        response_format= {'type': 'json_object'}
    )
    result = response.choices[0].message.content

    return print(result)

if __name__ == '__main__':
    GeminiCLient(google_api_key)


