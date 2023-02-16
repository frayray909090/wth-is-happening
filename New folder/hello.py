import tkinter as tk

def load():
    if textbox.get("1.0", "end-1c") == "password":
        loaded = tk.Toplevel()
        loaded.geometry("150x150")
        loaded.title("loaded")
        ll = tk.Label(loaded, text="loaded", font=('Ubuntu', 18))
        ll.pack(padx=20, pady=20)

    if textbox.get("1.0", "end-1c") == "error":
        loaded = tk.Toplevel()
        loaded.geometry("150x150")
        loaded.title("error")
        ll = tk.Label(loaded, text="error", font=('Ubuntu', 18))
        ll.pack(padx=20, pady=20)

    if textbox.get("1.0", "end-1c") == "warn":
        loaded = tk.Toplevel()
        loaded.geometry("150x150")
        loaded.title("warn")
        ll = tk.Label(loaded, text="warn", font=('Ubuntu', 18))
        ll.pack(padx=20, pady=20)

    if textbox.get("1.0", "end-1c") == "test":
        loaded = tk.Toplevel()
        loaded.geometry("150x150")
        loaded.title("test")
        ll = tk.Label(loaded, text="test", font=('Ubuntu', 18))
        ll.pack(padx=20, pady=20)    

root = tk.Tk()

root.geometry("500x500")
root.title("hello")

label = tk.Label(root, text="hello", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10)

button = tk.Button(root, text="click me", command=load)
button.pack()

root.mainloop()