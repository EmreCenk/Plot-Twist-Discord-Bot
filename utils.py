
from typing import Tuple

def get_last_word(text: str) -> (str, int):
    """
    Gets the last word of any given sentence.
    :param text: text to look at
    :return: A boolean k where k[0] is the last word, and k[1] is the index of the first character
    of the word
    """
    text = text.split(" ")
    total_travelled = 0
    for i in range(len(text) - 1, -1, -1):
        total_travelled -= len(text[i])
        if len(text[i]) > 1:
            return text[i], total_travelled

def valid_message(text: str) -> Tuple[bool, str]:
    """
    :param text: a message sent in a server
    :return: a tuple k where k[0] is a boolean to determine if the message is valid and
    k[1] is the noun of the word. If k[0] is false, then k[1] is an empty string.
    """
    text = text.lower().replace(".", " ")
    if "is" not in text or "?" == text[-1]:
        # trivial case, if "is" isn't even in the message, we can't respond with "or is it?"
        return (False, "")

    last_word = get_last_word(text)
    text = text[: last_word[1] - 1]


    return (True, "")
if __name__ == '__main__':
    ex = "Everything is great."
    print(
        valid_message(ex)
    )