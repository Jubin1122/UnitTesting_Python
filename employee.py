import requests

class Employee:
    """ Employee Class """

    raise_amt =  1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply