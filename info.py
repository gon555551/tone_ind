from requests import get
import bs4

# function to get the dictionary properly edited
def gettones():
    
    # get the table from https://toneindicators.carrd.co/#masterlist
    table = bs4.BeautifulSoup(get('https://toneindicators.carrd.co/#masterlist').text, 'html.parser').find_all('td')

    # generate a dictionary with the tones and their meaning
    inds = dict()
    for i in range(0, len(table)-1, 2):
        item = table[i].get_text()
        item1 = table[i+1].get_text()
        
        # check if multiple possible indicators
        if len(item.split(' or ')) > 1:
            for poss in item.split(' or '):
                inds[poss] = item1
        else:
            inds[item] = item1
            
    # make /nbh's meaning more compact
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
    line = f'''Your message started with ``/?``,  so I'll explain how I work...

Simply use a tone indicator, like ``/srs``, anywhere in your message (as long as it's separated from other words with a space), and I'll send a message in the same channel saying what it means.

Currently, these are the tone indicators I recognize:

'''
    for key, value in tones.items():
        line += f'``{key:4}`` -> ``{value}``\n'
        
    line += '\nUse ``./tone`` if you don\'t want me to explain it! /srs'
    
    return line
