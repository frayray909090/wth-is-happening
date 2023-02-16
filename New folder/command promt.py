import tkinter as tk
import requests as request

password = "Siri"
password1 = "What"
password2 = "Mop"

question = "who made you?"

awnser = "espero_dev made me"

def load():
    if textbox.get("1.0", "end-1c") == password or textbox.get("1.0", "end-1c") == password1 or textbox.get("1.0", "end-1c") == password2:
        ll = tk.Label(root, text=textbox.get("1.0", "end-1c"), font=('Ubuntu', 18))
        ll.pack(padx=5, pady=5) 

def AI():
    if textbox.get("1.0", "end-1c") == question:
        ll = tk.Label(root, text=awnser, font=('Ubuntu', 18))
        ll.pack(padx=5, pady=5) 

root = tk.Tk()

root.geometry("500x500")
root.title("hello")

label = tk.Label(root, text="hello", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=1, font=('Arial', 16))
textbox.pack(padx=20)

button = tk.Button(root, text="load command", command=load)
button.pack()
button = tk.Button(root, text="AI chat", command=AI)
button.pack()

root.mainloop()