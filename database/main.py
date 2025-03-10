from tkinter import Tk, Label, Button, Entry, StringVar
def register_command():
    with open("user_info.txt", "a") as f:
        f.write(f"{username_value.get()}:{password_value.get()},")
root = Tk()
username_value = StringVar()
Label(root, text="Username").grid(row=0, column=0)
username_entry = Entry(root, textvariable=username_value)
username_entry.grid(row=0, column=1)

password_value = StringVar()
Label(root, text="password").grid(row=1, column=0)
password_entry = Entry(root, textvariable=password_value)
password_entry.grid(row=1, column=1)

register_button = Button(root, text="register", command=register_command)
register_button.grid(row=2, column=0, columnspan=2)
root.mainloop()