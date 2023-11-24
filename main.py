from openai import OpenAI

from pytube import YouTube

# api setup
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key = OPENAI_API_KEY)

# function
def summarizer(file_name):
    audio_file = open("audio_video/" + file_name , "rb")

    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format = 'text',
    )
    # checks if transcription is a string
    # if isinstance(transcription, str):
    #     print('transcription is a string')

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt= "Detailed summary of the text given in bullet form: " + transcription,
        max_tokens= 256
    )

    # prints the summary 
    # print(response.choices[0].text)

    tidy_file_name = file_name[:-4]

    f = open('summaries/' + tidy_file_name + '_summarized', "w")
    f.write(response.choices[0].text)
    f.close()        
    
def main():
    print("enter the name of your audio file: ")
    file_name = input()
    summarizer(file_name)
    exit()

main()









