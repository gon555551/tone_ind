from requests import get
import bs4

# function to get the dictionary properly edited
def tones():
    # get the table from https://toneindicators.carrd.co/#masterlist
    table = bs4.BeautifulSoup(get('https://toneindicators.carrd.co/#masterlist').text, 'html.parser').find_all('td')

    # generate a dictionary with the tones and their meaning
    inds = dict()
    for i in range(0, len(table)-1, 2):
        item = table[i].get_text()
        item1 = table[i+1].get_text()
        if len(item.split(' or ')) > 1:
            inds[item.split(' or ')[0]] = item1
            inds[item.split(' or ')[1]] = item1
        else:
            inds[item] = item1
    # make /nbh's meaning more compact
    inds['/nbh'] = '@ nobody here'

    return inds

# get the token
def token():
    token = ''
    with open('token.txt', 'r') as t:
        token = t.readline()
    
    return token
