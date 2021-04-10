import html

class Question:

    def __init__(self, text, answer):
        self.text = html.unescape(text)
        self.answer = answer