#sarvam console based application
# It is a console based application 
#It generates output in the vscode terminal



import requests
import base64
API_KEY = "YOUR_API_KEY_HERE"   # <-- Put your key here
url = "https://api.sarvam.ai/text-to-speech"
# Allowed bulbul:v2 Telugu voices
voices = [
    "anushka",
    "abhilash",
    "manisha",
    "vidya",
    "arya",
    "karun",
    "hitesh"
]

print("\n=== Sarvam Telugu TTS ===")
print("Select a voice:")
for i, v in enumerate(voices, start=1):
    print(f"{i}. {v}")

choice = int(input("\nEnter choice (1-7): "))
speaker = voices[choice - 1]

# Enter text from user
text = input("\nEnter the Telugu text to speak:\n> ")

payload = {
    "text": text,
    "target_language_code": "te-IN",
    "speaker": speaker,
    "model": "bulbul:v2"     # IMPORTANT for Telugu
}

headers = {
    "Content-Type": "application/json",
    "api-subscription-key": API_KEY
}

print("\nGenerating speech ...")

response = requests.post(url, json=payload, headers=headers)
print("STATUS:", response.status_code)

if response.status_code == 200:
    res_json = response.json()
    audio_b64 = res_json["audios"][0]      # base64
    audio_bytes = base64.b64decode(audio_b64)

    output_file = f"output_{speaker}.wav"
    with open(output_file, "wb") as f:
        f.write(audio_bytes)

    print(f"\n✔ Audio saved as **{output_file}**")
else:
    print("\n❌ Error:")
    print(response.text)
