import customtkinter
from customtkinter import *
import webbrowser
set_appearance_mode("light")
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
        self.list= customtkinter.CTkScrollableFrame(self, width=50)
        self.list.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")
                                           

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