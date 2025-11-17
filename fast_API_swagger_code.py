# I have developed sarvam fast API with the swagger 
#added parameters in POST method


from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,StreamingResponse
import requests
import base64
import io
import uuid

app = FastAPI()

templates = Jinja2Templates(directory="templates")

API_KEY = "sk_pk9i680c_6yX1RJx6WQuoufVkycG90zap"
URL = "https://api.sarvam.ai/text-to-speech"

VOICES = ["anushka", "abhilash", "manisha", "vidya", "arya", "karun", "hitesh"]


# -----------------------------------
# ✅ Your original UI route (GET)
# -----------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "voices": VOICES,
            "audio_data": None,
            "text_input": "",
            "speaker_selected": VOICES[0]
        }
    )

 
@app.post("/api/tts")
async def api_tts(voice: str, text: str):
    payload = {
        "text": text,
        "target_language_code": "te-IN",
        "speaker": voice,
        "model": "bulbul:v2"
    }

    headers = {
        "Content-Type": "application/json",
        "api-subscription-key": API_KEY
    }

    response = requests.post(URL, json=payload, headers=headers)

    if response.status_code != 200:
        return {"error": response.text}

    audio_b64 = response.json()["audios"][0]
    audio_bytes = base64.b64decode(audio_b64)

    file_name = f"{voice}_{uuid.uuid4().hex}.mp3"

    return StreamingResponse(
        io.BytesIO(audio_bytes),
        media_type="audio/mpeg",
        headers={"Content-Disposition": f"attachment; filename={file_name}"}
    )


