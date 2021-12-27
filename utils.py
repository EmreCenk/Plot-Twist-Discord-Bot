
from typing import Tuple
from spacy.lang.en import English
import spacy

class response:
    def __init__(self,
                 validity: bool,
                 is_alternative: str,
                 subject: str,
                 adjective: str,
                 ):
        self.validity = validity
        self.subject = subject
        self.adjective = adjective
        self.is_alternative = is_alternative
    def __repr__(self):
        return str((self.validity, self.is_alternative, self.subject, self.adjective))
class message_checker():
    def __init__(self):
        self.nlp = English()
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.add_pipe(self.nlp.create_pipe("sentencizer"))

    def get_last_sentence(self, text: str = "", doc = None) -> str:
        if doc is None:
            doc = self.nlp((text))
        return list(doc.sents)[-1].text

    def valid_message(self, text: str) -> response:
        """
        :param text: sentence to check validity for
        :return: response
        """
        doc = self.nlp((text))
        # last_sentence = self.get_last_sentence(doc = doc)
        # print(last_sentence)



        latest_is_index = None
        for i, token in enumerate(doc):
            if token.lemma_ == "be":
                latest_is_index = i
        if latest_is_index == None:
            return response(False, "", "", "")
        # print(doc[latest_is_index - 1].pos_, doc[latest_is_index - 1].text)
        if doc[latest_is_index - 1].pos_ not in ["NOUN", "PROPN", "PRON"]:
            return response(False, "", "", "")

        adjective = doc[latest_is_index + 1].text
        # print("alpha", doc[latest_is_index + 1].pos_ in ["ADJ", "PART"], doc[latest_is_index + 1].text, doc[latest_is_index + 1].lemma_)
        # if doc[latest_is_index + 1].lemma_ == "not":
        adjective = doc[latest_is_index + 1].text + " "
        for i in range(latest_is_index + 2, len(doc)):
            if doc[i].pos_ in ["NOUN", "ADJ", "DET", "VERB"]: adjective += doc[i].text + " "
            else: break

        # else:
        #     for chunk in doc.noun_chunks:
        #         if (doc[latest_is_index + 1] in chunk) or (doc[latest_is_index + 1].pos_ in ["ADJ", "PART"] and doc[latest_is_index + 2] in chunk):
        #             print("dodo", chunk.text)
        #             adjective = chunk.text
        #

        for chunk in doc.noun_chunks:
            # print("omicron", chunk)
            if doc[latest_is_index - 1] in chunk:
                # print("returning:", True, doc[latest_is_index].text, chunk.text, adjective)
                return response(True, doc[latest_is_index].text, chunk.text, adjective)

        # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
        # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
        #
        # for token in doc:
        #     print(token.lemma_, token.pos_)
        #
        # print("*********")
        # for entity in doc.ents:
        #     print(entity.text, entity.label_)
        # print(
        #
        # )
        return response(False, "", "", "")

    def negate(self, phrase):
        """
        Negates any given phrase. For instance:
        "great" -> "not great"
        "not great" -> "great"
        TODO: insert an antonym library here

        :param phrase: phrase
        :return:
        """
        doc = self.nlp((phrase))
        # print("theta", doc)
        if len(doc) == 0:
            # print("nodoc")
            negated = "not "
            for j in doc: negated += j.text + " "
            return negated
        if doc[0].lemma_ == "not":
            negated = ""
            doc = doc[1:] #removing 'not'
        else: negated = "not "
        for j in doc: negated += j.text + " "
        return negated

if __name__ == '__main__':
    checker = message_checker()
    tests = [
            "The world is great. Marvel is better than DC.",
             "We are great people!",
             "I am great.",
             "The alphabet is crucial in understanding the world.",
             "Your mother is not cool",  #phrases like this were used so much in the servers, that I have no choice but to add them as a test case.
             "Your desk is pretty cool.",

            #SAME TESTS WITH '
             "I'm not a good guy",
             "The world's great.",
             "Marvel's better than DC.",
             "We're great people!",
             "I'm great.",
             "The alphabet's crucial in understanding the world.",
             "Your mother's not cool", # phrases like this were used so much in the servers, that I have no choice but to add them as a test case.
             "Your desk's pretty cool.",

             "I'm not doing it",
             ]
    # print(f'Message from {message.author}: {message.content}')

    for e in tests:
        some_response = checker.valid_message(e)
        # some_response.
        if some_response.validity == False: continue
        some_response.subject = some_response.subject.replace("'m", "am").replace("'re", "are").replace("'s", "is")
        some_response.is_alternative = some_response.is_alternative.replace("'m", "am").replace("'re", "are").replace("'s", "is")
        some_response.adjective = some_response.adjective.replace("'m", "am").replace("'re", "are").replace("'s", "is")


        text_to_send = f"...{some_response.is_alternative} {some_response.subject} {some_response.adjective}?"
        text_to_send += f"\nThe truth was right in front of you the whole time..."
        text_to_send += f"\n{some_response.subject} {some_response.is_alternative} {checker.negate(some_response.adjective)}"
        text_to_send += "\nNote: plz give <@569431484486909964> some ideas for this not to suck"
        # print(
        print("\n\nmessage:")
        print(text_to_send)
        print()
        print("-"*100)
        print()