from typing import Dict, Any
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
import openai

app = FastAPI()

openai.api_key = "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"

class RequestModel(BaseModel):
    language: str
    sentence: str

class ResponseModel(BaseModel):
    output: str

@app.post("/translate")
async def translate_text(request: RequestModel) -> RequestModel:
    language = request.language
    sentence = request.sentence
    message = "Explain each word from the text as the same original language " + language + " of this text: " + sentence
    print(message)
    x = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    final = x.choices[0].message.content.strip()
    return {"output": final}
