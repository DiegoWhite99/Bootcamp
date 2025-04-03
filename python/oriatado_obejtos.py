class Student:
    def __init__(self, document, name, lastname, age): # Initializes the Student object with document, name, lastname, and age attributes
        self.__document = document
        self.__name = name
        self.__lastname = lastname
        self.__age = age
    def get_document(self):
        return self.__document
    def get_name(self):
        return self.__name
    def get_lastname(self):
        return self.__lastname
    def get_age(self):
        return self.__age
    