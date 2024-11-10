import customtkinter
from customtkinter import *
from CTkListbox import CTkListbox
import webbrowser
import API
import tkinter
import demo
set_appearance_mode("light")
data2=''
data4=''
class infopage(customtkinter.CTk):
    def __init__(root):
        super().__init__()

        root.title("info")
        root.geometry("4000x4000")
        root.grid_columnconfigure((0, 1), weight=1)
        root.title = customtkinter.CTkLabel(root, text="Search songs, artist, or bands", fg_color="grey",font=("helvetica",18))