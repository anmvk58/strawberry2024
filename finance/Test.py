from abc import ABC, abstractmethod

class CheckString:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if len(value) == 0:
            raise ValueError(f'{self.name} must be at least 1 character')
        instance.__dict__[self.name] = value

class Person:
    first_name = CheckString()
    last_name = CheckString()

    def __str__(self):
        return f'{self.last_name} - {self.first_name}'

if __name__ == '__main__':
    peson1 = Person()
    peson1.last_name = 'A'
    peson1.first_name = ''
    print(peson1)