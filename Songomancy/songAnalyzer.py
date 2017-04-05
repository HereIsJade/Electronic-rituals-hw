# -*- coding: utf-8 -*-
import json
from watson_developer_cloud import ToneAnalyzerV3
import requests
from bs4 import BeautifulSoup


tone_analyzer = ToneAnalyzerV3(
   username='3a90c2e4-ecc8-4ba3-b94b-fcc6ec238486',
   password='gGdiDcP1APki',
   version='2017-04-04')

emotion_texts=['A man in a passion, rides a mad horse.',
'From the deepest desires often come the deadliest hate.',
'Fear is a distorting mirror in which anything can appear as a caricature of itself, stretched to terrible proportions; once inflamed, the imagination pursues the craziest and most unlikely possibilities. What is most absurd suddenly seems the most probable.',
"Find a place inside where there's joy, and the joy will burn out the pain.",
'Pain is temporary. It may last a minute, or an hour, or a day, or a year, but eventually it will subside and something else will take its place. If I quit, however, it lasts forever.'
]

# emotion_texts={
#     "Anger":'A man in a passion, rides a mad horse.',
#     "Disgust":'From the deepest desires often come the deadliest hate.',
#     "Fear":'Fear is a distorting mirror in which anything can appear as a caricature of itself, stretched to terrible proportions; once inflamed, the imagination pursues the craziest and most unlikely possibilities. What is most absurd suddenly seems the most probable.',
#     "Joy":"Find a place inside where there's joy, and the joy will burn out the pain.",
#     "Sadness":'Pain is temporary. It may last a minute, or an hour, or a day, or a year, but eventually it will subside and something else will take its place. If I quit, however, it lasts forever.'
# }

# http://www.metrolyrics.com/disorder-lyrics-joy-division.html
# http://www.metrolyrics.com/eating-hooks-lyrics-moderat.html
def getLyrics(artist,song):
    lyrics=''
    artist=artist.replace(' ','-').lower()
    song=song.replace(' ','-').lower()
    print artist,song
    url="http://www.metrolyrics.com/"+song+"-lyrics-"+artist+".html"
    # url="http://www.metrolyrics.com/eating-hooks-lyrics-moderat.html"
    print url
    html=requests.get(url).text
    soup=BeautifulSoup(html,'html.parser')
    for num in range (0,len(soup.select('.verse'))):
        verses=soup.select('.verse')[num].text
        lyrics += verses
    return lyrics

def getAdvice(artist,song):
    advice=''
    with open('try.json', 'w') as outfile:
        json.dump(tone_analyzer.tone(text=getLyrics(artist,song)), outfile, indent=2)

    with open('try.json') as data_file:
        data = json.load(data_file)
        emotion_tone=data["document_tone"]["tone_categories"][0]["tones"]
        language_tone=data["document_tone"]["tone_categories"][1]["tones"]
        social_tone=data["document_tone"]["tone_categories"][2]["tones"]

    for num in range (0,5):
        if emotion_tone[num]["score"]>0.5:
            advice+=emotion_texts[num]+'\n'
    return advice
