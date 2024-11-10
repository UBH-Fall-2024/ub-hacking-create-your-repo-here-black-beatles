from encodings import search_function
import customtkinter
from customtkinter import *
from CTkListbox import CTkListbox
import webbrowser
import API
set_appearance_mode("light")
data2=''
data4=''
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Spotilist")
        self.geometry("400x400")
        self.grid_columnconfigure((0, 1), weight=1)