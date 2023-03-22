"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import constants as c




def request_voice(sentence=None, output_type=None, name=None, language=None, client=None):
    try:
        if output_type == "mp3":
            response = client.synthesize_speech(Text=sentence["text"], OutputFormat=output_type, VoiceId=name, Engine="neural", LanguageCode=c.POLLY_LANG_SET[language])
        elif output_type == "json":
            response = client.synthesize_speech(Text=sentence["text"], OutputFormat=output_type, VoiceId=name, Engine="neural", LanguageCode=c.POLLY_LANG_SET[language], SpeechMarkTypes=["word"])
    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)
    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
           output = os.path.join(os.getcwd() + f"/biblioglot_package/audio/{sentence['index']}.{output_type}")
           try:
                if output_type == "mp3":
                    with open(output, "wb") as file:
                        file.write(stream.read())
                elif output_type == "json":
                    with open(output, "wb") as file:
                        file.write(stream.read())
                    with open(output, "r") as json_file:
                        content = json_file.read()
                    fixed_content = "[" + ",".join(content.strip().split("\n")) + "]"
                    with open(output, "w") as fixed_file:
                        fixed_file.write(fixed_content)
           except IOError as error:

              print(error)
              sys.exit(-1)
    else:
        print("Could not stream audio")
        sys.exit(-1)

def get_audio(json_data="", language="", name=""):
    session = Session(profile_name="default")
    polly = session.client("polly")
    for sentence in json_data:
        request_voice(sentence=sentence, name=name, output_type="mp3",language=language, client=polly)
        request_voice(sentence=sentence, name=name, output_type="json", language=language, client=polly)