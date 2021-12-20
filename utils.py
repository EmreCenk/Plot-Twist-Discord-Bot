


def valid_message(text: str) -> bool:
    """
    :param text: a message sent in a server
    :return: whether the bot can respond with "or is it?"
    """
    if "is" not in text:
        # trivial case, if "is" isn't even in the message, we can't respond with "or is it?"
        return False

if __name__ == '__main__':
    ex = "Everything is great."
    print(
        valid_message(ex)
    )