from sarvamai import SarvamAI

client = SarvamAI(api_subscription_key="sk_np68mb2c_xyG6KPnPCa2iYcXD7zdq1j47")

response = client.text_to_speech.convert(
    text="నమస్తే ఇది తెలుగు టెస్ట్.",
    target_language_code="te-IN",
)

print(type(response))
print(dir(response))
