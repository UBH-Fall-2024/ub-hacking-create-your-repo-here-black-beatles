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

#searchbar
        self.title = customtkinter.CTkLabel(self, text="Search songs, artist, or bands", fg_color="grey",font=("helvetica",18))
        self.title.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.Entry= customtkinter.CTkEntry(self,font=("helvetica",14))
        self.Entry.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        self.list= CTkListbox(self, width=50)
        self.list.grid(row=2, column=0, padx=20, pady=(0, 20), , sticky="w")
        def searchfunction(e):
            global data2
            global data4

            typed= self.Entry.get()
            data1=API.getArtistID(typed)
            data2=API.getArtistName(data1)
            data3=API.getSongID(typed)
            data4=API.getSongName(data3)
            print(data2)
            print(data4)
            self.list.insert(END,data2)
            self.list.insert(END,data4)
            
        self.Entry.bind("<KeyRelease>",searchfunction)
       
            
                                           

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=400, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        self.button1 = customtkinter.CTkButton(self, text="Like", command=self.liked)
        self.button1.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="w")

        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="Dislike")
        self.checkbox_2.grid(row=3, column=1, padx=20, pady=(0, 20), sticky="w")
    count1=0

    def liked(self):
        self.count1=self.count1+1
        print(str(self.count1))
    def button_callback(self):
        webbrowser.open("https://ublearns.buffalo.edu/d2l/login?sessionExpired=1&target=%2fd2l%2fle%2fcontent%2f212089%2fviewContent%2f4234407%2fView")
        print("button pressed")
    

app = App()
app.mainloop()