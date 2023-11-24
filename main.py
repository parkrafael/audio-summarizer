from openai import OpenAI

# API KEY SET 

OPENAI_API_KEY = "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"

client = OpenAI(
    api_key=OPENAI_API_KEY
)

audio_file = open("organic.mp3", "rb")

transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format = 'text',
)

# checks if transcription is a string
if isinstance(transcription, str):
    print('transcription is a string')

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt= "Summarize the text with proper indentation:" + transcription,
  max_tokens= 256
)

print(response.choices[0].text)

f = open("myfile.txt", "w")
f.write(response.choices[0].text)
f.close()




