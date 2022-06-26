from requests import get
import bs4, os

# function to get the dictionary properly edited
def gettones() -> dict:
    """gets the tone indicators and their meaning from the masterlist

    Returns:
        dict: a dictionary with the tones as keys and their meanings as values
    """

    table = bs4.BeautifulSoup(
        get("https://toneindicators.carrd.co/#masterlist").text, "html.parser"
    ).find_all("td")

    inds = dict()
    for i in range(0, len(table) - 1, 2):
        item = table[i].get_text()
        item1 = table[i + 1].get_text()

        if len(item.split(" or ")) > 1:
            for poss in item.split(" or "):
                inds[poss] = item1
        else:
            inds[item] = item1

    inds["/nbh"] = "@ nobody here"

    return inds


# get the token
def gettoken() -> str:
    """gets the token from a .txt file

    Returns:
        str: the bot's token
    """

    token = ""
    with open(os.path.dirname(__file__) + "\\token.txt", "r") as t:
        token = t.readline()

    return token


# get question string
def getquestion(tones: dict) -> str:
    """gets the bot use explanation as well as all the tones and their meanings

    Args:
        tones (dict): the tones from gettones()

    Returns:
        str: the message to send to the user that requested it
    """

    line = f"""I'll explain how I work...

Simply use a tone indicator, like ``/srs``, anywhere in your message (as long as it's separated from other words with a space), and I'll send a message in the same channel saying what it means.

Currently, these are the tone indicators I recognize:

"""
    tmp_l = "\n".join(f"``{key:4}`` -> ``{value}``" for key, value in tones.items())
    line += tmp_l
    line += "\nUse ``./tone`` if you don't want me to explain it! /srs"

    return line


# get what
def whattone(content: str, tones: dict) -> str:
    """gets the tone indicator for a certain tone

    Args:
        content (str): the message in which the command was used
        tones (dict): the tones from gettones()

    Returns:
        str: a short string telling the user what tone indicator to use, or an error message
    """

    line = ""
    par = content.split(" ")

    if par == [content] or par[1] not in tones.values():
        tmp_l = ["That is an invalid use of ``t?what``, try ``t?what sarcastic``."]
    else:
        tmp_l = [
            f"The tone indicator for **{par[1]}** is ``{key}``."
            for key, value in tones.items()
            if par[1] == value
        ]

    line += tmp_l[0]
    return line


# get mean ind
def meanind(content: str, tones: dict) -> str:
    """gets the tone for a certain tone indicator

    Args:
        content (str): the message in which the command was used
        tones (dict): the tones from gettones()

    Returns:
        str: a short string telling the user what tone the indicator means, or an error message
    """

    line = ""
    par = content.split(" ")

    if par == [content] or par[1] not in tones.keys():
        tmp_l = ["That is an invalid use of ``t?mean``, try ``t?mean /s``."]
    else:
        tmp_l = [
            f"The meaning of **{par[1]}** is ``{value}``."
            for key, value in tones.items()
            if par[1] == key
        ]

    line += tmp_l[0]
    return line


# parse and see tone used
def toneused(content: str, tones: dict) -> str:
    """returns what tones were used in a certain message

    Args:
        content (str): the message in which the command was used
        tones (dict): the tones from gettones()

    Returns:
        str: a string with all the tone indicators and their meaning
    """

    line = ", ".join(
        f"``{pars}``: {tones[pars]}"
        for pars in content.split(" ")
        if pars in tones.keys()
    )

    return line
