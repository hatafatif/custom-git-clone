import tkinter
import customtkinter
import os

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    text = entry.get()
    os.system(f'git clone {text}')

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

entry = customtkinter.CTkEntry(master=app, placeholder_text="CTkEntry")
entry.pack(padx=20, pady=10)

app.mainloop()