class PriceControl:
    def __get__(self, instance, owner):
        return getattr(instance, self.var_name)

    def __set__(self, instance, value):
        if value < 0 or value > 100:
            raise ValueError('Price must be between 0 and 100.')
        return setattr(instance, self.var_name, value)

    def __set_name__(self, owner, name):
        self.var_name = "_" + name

class NameControl:
    def __get__(self, instance, owner):
        return getattr(instance, self.var_name)

    def __set__(self, instance, value):
        new_value = instance.__dict__[self.var_name]
        if new_value == '':
            return setattr(instance, self.var_name, value)
        elif new_value != value:
            if self.var_name == '_name':
                raise ValueError('Name can not be changed')
            elif self.var_name == '_author':
                raise ValueError('Author can not be changed')
        return setattr(instance, self.var_name, value)

    def __set_name__(self, owner, name):
        self.var_name = "_" + name

    #     global a
    #     a = value
    #     if a != value:
    #         if self.var_name == '_name':
    #             raise ValueError('Name can not be changed')
    #         elif self.var_name == '_author':
    #             raise ValueError('Author can not be changed')
    #     return setattr(instance, self.var_name, value)
    #
    # def __set_name__(self, owner, name):
    #     self.var_name = "_" + name

class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()
    def __init__(self, author, name, price):
        self._author = author
        self._name = name
        self.price = price

b = Book("William Faulkner", "The Sound and the Fury", 12)

b.author = " Roma Big Dick 2000"



