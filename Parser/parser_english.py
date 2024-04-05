import spacy

class EnglishParser:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def parse_sentence(self, sentence):
        doc = self.nlp(sentence)
        parsed_data = []

        for token in doc:
            parsed_data.append({'text': token.text, 'pos': token.pos_})

        return parsed_data

english_parser = EnglishParser()
parsed_result = english_parser.parse_sentence("This is a sample sentence.")
print(parsed_result)
