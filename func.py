from requests import get
import bs4, os, dotenv


class EventHandler:
    tones: dict
    token: str
    question: str

    def __init__(self) -> None:
        self.tones = self.gettones()
        self.token = self.gettoken()
        self.question = self.getquestion()

    # function to get the dictionary properly edited
    def gettones(self) -> dict:
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
    def gettoken(self) -> str:
        """gets the token from a .txt file

        Returns:
            str: the bot's token
        """
        dotenv.load_dotenv()
        return os.environ["TOKEN"]

    # get question string
    def getquestion(self) -> str:
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
        tmp_l = "\n".join(
            f"``{key:4}`` -> ``{value}``" for key, value in self.tones.items()
        )
        line += tmp_l
        line += "\nUse ``./tone`` if you don't want me to explain it! /srs"

        return line

    # get what
    def whattone(self, content: str) -> str:
        """gets the tone indicator for a certain tone

        Args:
            content (str): the message in which the command was used
            tones (dict): the tones from gettones()

        Returns:
            str: a short string telling the user what tone indicator to use, or an error message
        """

        line = ""
        par = content.split(" ")

        if par == [content] or par[1] not in self.tones.values():
            tmp_l = ["That is an invalid use of ``t?what``, try ``t?what sarcastic``."]
        else:
            tmp_l = [
                f"The tone indicator for **{par[1]}** is ``{key}``."
                for key, value in self.tones.items()
                if par[1] == value
            ]

        line += tmp_l[0]
        return line

    # get mean ind
    def meanind(self, content: str) -> str:
        """gets the tone for a certain tone indicator

        Args:
            content (str): the message in which the command was used
            tones (dict): the tones from gettones()

        Returns:
            str: a short string telling the user what tone the indicator means, or an error message
        """

        line = ""
        par = content.split(" ")

        if par == [content] or par[1] not in self.tones.keys():
            tmp_l = ["That is an invalid use of ``t?mean``, try ``t?mean /s``."]
        else:
            tmp_l = [
                f"The meaning of **{par[1]}** is ``{value}``."
                for key, value in self.tones.items()
                if par[1] == key
            ]

        line += tmp_l[0]
        return line

    # parse and see tone used
    def toneused(self, content: str) -> str:
        """returns what tones were used in a certain message

        Args:
            content (str): the message in which the command was used
            tones (dict): the tones from gettones()

        Returns:
            str: a string with all the tone indicators and their meaning
        """

        line = ", ".join(
            f"``{pars}``: {self.tones[pars]}"
            for pars in content.split(" ")
            if pars in self.tones.keys()
        )

        return line
