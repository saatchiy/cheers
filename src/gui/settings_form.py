from tkinter import *
from tkinter import messagebox
import sys
from mpmath import mpf, nstr
from exceptions.validation_exception import ValidationException

class SettingsForm:

    def __init__(self):
        
        self.__init_setting_form()

    def __init_setting_form(self):
        self.__setting_form = Tk()
        self.__setting_form.title("Settings")
        self.__setting_form.minsize(450, 300)
        self.__setting_form.maxsize(450, 300)
        self.__create_widgets()

    def __create_widgets(self):
        """Creates controls of the main form."""
        pass
