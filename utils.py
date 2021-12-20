
from typing import Tuple

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

    text = text.split(" ")
    last_word = ""
    for i in range(len(text) - 1, -1, -1):
        if len(text[i]) > 1 and text[i] != "is":
            last_word = text[i]
            break

    return (True, last_word)
if __name__ == '__main__':
    ex = "Everything is great."
    print(
        valid_message(ex)
    )