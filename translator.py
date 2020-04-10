import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from pandas.io.json import json_normalize
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
print("  ****** Welcome to  'Vamsi' Translator english to french and spansih *******\n\n\n")
      
choice=int(input("eenter your choice: \n1.AudioFile \n2.Speaklive\n3.enter text manually\n Enter a idex number above options :  "))
l=str(input("enter a languageshortcut: "))
if (choice == 1):
    
    url_s2t = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/1722eacb-4b3b-4918-bb09-f7622afdcb57"
    iam_apikey_s2t = "nf_XpCHUiwQQAVnO7l2GLmlVUzgRQFk3SI-cDYxBzw1A"
    authenticator = IAMAuthenticator(iam_apikey_s2t)
    s2t = SpeechToTextV1(authenticator=authenticator)
    s2t.set_service_url(url_s2t)
    filename='PolynomialRegressionandPipelines.mp3'
    with open(filename, mode="rb")  as wav:
        response = s2t.recognize(audio=wav, content_type='audio/mp3')
    response.result
    json_normalize(response.result['results'],"alternatives")
    response
    recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
    print(type(recognized_text))
    print(recognized_text)
# voice live input start
elif(choice == 2):
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")
    recognized_text=text
#voic live input end
elif (choice == 3):
    recognized_text=str(input("Enter a text to convert French or Spanish\n"))#text manually
#translator
url_lt='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/ebb9677b-6b06-4b91-8990-432553e659f0'
apikey_lt='p_NArNzxcsSNie7oOMud9sHg3tZ1RubejGKxluVkmK_5'
version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator


json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")


print("Enter 1.for spanish\n2.for french\n")
i=int(input("enter a response : "))
if(i==1):
    translation_response = language_translator.translate(text=recognized_text, model_id="en-es")
    translation_response

    translation=translation_response.get_result()
    translation
    sp=spanish_translation =translation['translations'][0]['translation']
    spanish_translation
    print("Spanish text is : ",sp,"\n\n")
else:
    French_translation=language_translator.translate(text=recognized_text , model_id="en-fr").get_result()
    re=French_translation['translations'][0]['translation']
    print("French text is : ",re)


'''translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()


translation_eng=translation_new['translations'][0]['translation']
translation_eng'''#conversion spanish to english
lan='''el    : Greek,
eo    : Esperanto,
en    : English,
af    : Afrikaans,
sw    : Swahili,
ca    : Catalan,
it    : Italian,
iw    : Hebrew,
sv    : Swedish,
cs    : Czech,
cy    : Welsh,
ar    : Arabic,
ur    : Urdu,
ga    : Irish,
eu    : Basque,
et    : Estonian,
az    : Azerbaijani,
id    : Indonesian,
es    : Spanish,
ru    : Russian,
gl    : Galician,
nl    : Dutch,
pt    : Portuguese,
la    : Latin,
tr    : Turkish,
tl    : Filipino,
lv    : Latvian,
lt    : Lithuanian,
th    : Thai,
vi    : Vietnamese,
gu    : Gujarati,
ro    : Romanian,
is    : Icelandic,
pl    : Polish,
ta    : Tamil,
yi    : Yiddish,
be    : Belarusian,
fr    : French,
bg    : Bulgarian,
uk    : Ukrainian,
hr    : Croatian,
bn    : Bengali,
sl    : Slovenian,
ht    : Haitian Creole,
da    : Danish,
fa    : Persian,
hi    : Hindi,
fi    : Finnish,
hu    : Hungarian,
ja    : Japanese,
ka    : Georgian,
te    : Telugu,
zh-TW : Chinese Traditional,
sq    : Albanian,
no    : Norwegian,
ko    : Korean,
kn    : Kannada,
mk    : Macedonian,
zh-CN : Chinese Simplified,
sk    : Slovak,
mt    : Maltese,
de    : German,
ms    : Malay,
sr    : Serbian'''


