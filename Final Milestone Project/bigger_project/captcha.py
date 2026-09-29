class Captcha:
    def generate(self):
        raise NotImplementedError
    def get_prompt(self):
        raise NotImplementedError
    def check(self):
        raise NotImplementedError