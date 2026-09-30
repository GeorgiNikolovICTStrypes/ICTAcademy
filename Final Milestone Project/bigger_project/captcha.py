class Captcha:
    def generate(self):
        raise NotImplementedError
    def get_prompt(self):
        raise NotImplementedError
    def check(self):
        raise NotImplementedError
    def display(self, parent):
        raise NotImplementedError
    def get_answer(self):
        raise NotImplementedError