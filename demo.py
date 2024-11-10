from encodings import search_function
from pdb import run
import customtkinter
from customtkinter import *
from CTkListbox import CTkListbox
import webbrowser
import API
import infopage
set_appearance_mode("light")
data2=''
data4=''
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Spotilist")
        self.geometry("4000x4000")
        self.grid_columnconfigure((0, 1), weight=1)

#searchbar
        self.title = customtkinter.CTkLabel(self, text="Search songs, artist, or bands", fg_color="grey",font=("helvetica",18))
        self.title.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.Entry= customtkinter.CTkEntry(self,font=("helvetica",14),width=250)
        self.Entry.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        self.list= CTkListbox(self, width=5000)
        self.list.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")
        
            
        
        def searchfunction(e):
            global data2
            global data4

            typed= self.Entry.get()
            if typed=='':
                self.list.delete(0,END)
            else:
                lst = API.search(typed)
                data2 = map(API.getArtistName,lst[:3])
                data4 = map(API.getSongName,lst[3:])
            update()
        def pullup(e):
            infobox=CTkToplevel()
            infobox.title("Info")
            infobox.geometry("800x800")
        def update():
            global data2
            global data4
            
            self.list.delete(0,7)
            for x in data2:
                self.list.insert(END,"Artist: " + x)
            for x in data4:
                self.list.insert(END,"Song: " + x)
        self.Entry.bind("<KeyRelease>",searchfunction)
        self.list.bind("<<ListboxSelect>>",pullup)
                                          

        self.button = customtkinter.CTkButton(self, text="Clear Restuls", command=self.button_callback)
        self.button.grid(row=400, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

    def button_callback(self):
        self.list.delete(0,END)
        self.Entry.delete(0,END)

app = App()
app.mainloop()