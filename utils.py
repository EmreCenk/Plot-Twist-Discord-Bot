
from typing import Tuple
from spacy.lang.en import English
import spacy

class response:
    def __init__(self,
                 validity: bool,
                 noun: str,
                 adjective: str,
                 is_alternative: str):
        self.validity = validity
        self.noun = noun
        self.adjective = adjective
        self.is_alternative = is_alternative
    def __repr__(self):
        return str((self.validity, self.is_alternative, self.noun, self.adjective))
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
        # Process whole documents
        doc = self.nlp((text))
        last_sentence = self.get_last_sentence(doc = doc)
        print(last_sentence)



        latest_is_index = None
        for i, token in enumerate(doc):
            if token.lemma_ == "be":
                latest_is_index = i
        if latest_is_index == None:
            return response(False, "", "", "")
        print(doc[latest_is_index - 1].pos_, doc[latest_is_index - 1].text)
        if doc[latest_is_index - 1].pos_ not in ["NOUN", "PROPN", "PRON"]:
            return response(False, "", "", "")

        adjective = doc[latest_is_index + 1].text
        for chunk in doc.noun_chunks:
            if doc[latest_is_index + 1] in chunk:
                adjective = chunk.text

        for chunk in doc.noun_chunks:
            if doc[latest_is_index - 1] in chunk:
                return response(True, chunk.text, adjective, doc[latest_is_index].text)

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
        return response(True, "", "", "")

if __name__ == '__main__':
    checker = message_checker()
    tests = ["The world is great. Marvel is better than DC.",
             "We are great people!",
             "I am great.",
             "The alphabet is crucial in understanding the world."]
    for e in tests:
        # print(
        print(checker.valid_message(e))
        # )
        print()
        print("-"*100)
        print()
