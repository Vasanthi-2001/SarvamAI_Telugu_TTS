from flask import Flask, render_template, request
import requests
import base64

app = Flask(__name__)

API_KEY = "sk_pk9i680c_6yX1RJx6WQuoufVkycG90zap"
URL = "https://api.sarvam.ai/text-to-speech"

# Telugu voices
VOICES = ["anushka", "abhilash", "manisha", "vidya", "arya", "karun", "hitesh"]

@app.route("/", methods=["GET", "POST"])
def index():
    audio_data = None
    text_input = ""  # to preserve user input
    speaker_selected = VOICES[0]  # default selected voice

    if request.method == "POST":
        speaker_selected = request.form.get("voice")
        text_input = request.form.get("text")

        payload = {
            "text": text_input,
            "target_language_code": "te-IN",
            "speaker": speaker_selected,
            "model": "bulbul:v2"
        }

        headers = {
            "Content-Type": "application/json",
            "api-subscription-key": API_KEY
        }

        response = requests.post(URL, json=payload, headers=headers)
        if response.status_code == 200:
            res_json = response.json()
            audio_b64 = res_json["audios"][0]
            audio_data = audio_b64  # base64 string to embed
        else:
            return f"Error: {response.text}"

    return render_template(
        "index.html",
        voices=VOICES,
        audio_data=audio_data,
        text_input=text_input,
        speaker_selected=speaker_selected
    )

if __name__ == "__main__":
    app.run(debug=True)
