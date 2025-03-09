from random import randint

class Helper:
    @staticmethod
    def generate_phone_number():
        return f"8{randint(1111111111, 9999999999)}"