'''
This module defines translator functions
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# loading keys
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    '''
    Translates from English to French
    '''
    if english_text is None:
        return ''
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text
#print(englishToFrench(None))

def frenchToEnglish(french_text):
    '''
    Translates from French to English
    '''
    if french_text is None:
        return ''
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
