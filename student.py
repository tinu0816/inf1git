from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.__name =name
        self.__modules = []
        self.__grades={}

    def add_module(self,title):
        self.__modules.append(title)
        self.__grades[title]=title.get_grade()

    def get_list_modules(self):
        for el in self.__modules:
            print(el)


    def get_grades(self):
        for el in self.__grades:
            print(str(el) + ': '+str(self.__grades[el]))


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
