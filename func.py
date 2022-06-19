from requests import get
import bs4

# function to get the dictionary properly edited
def gettones():
    table = bs4.BeautifulSoup(get('https://toneindicators.carrd.co/#masterlist').text, 'html.parser').find_all('td')

    inds = dict()
    for i in range(0, len(table)-1, 2):
        item = table[i].get_text()
        item1 = table[i+1].get_text()
        
        if len(item.split(' or ')) > 1:
            for poss in item.split(' or '):
                inds[poss] = item1
        else:
            inds[item] = item1
            
    inds['/nbh'] = '@ nobody here'

    return inds

# get the token
def gettoken():
    token = ''
    with open('token.txt', 'r') as t:
        token = t.readline()
    
    return token

# get question string
def getquestion(tones: dict) -> str:
    line = f'''I'll explain how I work...

Simply use a tone indicator, like ``/srs``, anywhere in your message (as long as it's separated from other words with a space), and I'll send a message in the same channel saying what it means.
I'll only read the first one you use though!

Currently, these are the tone indicators I recognize:

'''
    for key, value in tones.items():
        line += f'``{key:4}`` -> ``{value}``\n'
        
    line += '\nUse ``./tone`` if you don\'t want me to explain it! /srs'
    
    return line

# get what
def whattone(content: str, tones: dict) -> str:
    line = ''
    par = content.split(' ')
    
    if par == [content] or par[1] not in tones.values():
        line += 'That is an invalid use of ``t?what``, try ``t?what sarcastic``.'
    else:
        for key, value in tones.items():
            if value == par[1]:
                line += f'The tone indicator for **{par[1]}** is ``{key}``.'
                break
    
    return line

# get mean ind
def meanind(content: str, tones: dict) -> str:
    line = ''
    par = content.split(' ')
    
    if par == [content] or par[1] not in tones.keys():
        line += 'That is an invalid use of ``t?mean``, try ``t?mean /s``.'
    else:
        for key, value in tones.items():
            if key == par[1]:
                line += f'The meaning of ``{par[1]}`` is **{value}**.'
                break
    
    return line

# parse and see tone used
def toneused(content: str, tones: dict) -> str:
    line = ''
    
    for tone in tones.keys():
            if tone in content.split(' '):
                line = f'``{tones[tone]}``'
                break
    return line
    