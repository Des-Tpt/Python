from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import messagebox

def on_ok_click():
	user_oldpassword = user_oldpassword_entry.get()
	user_newpassword = user_newpassword_entry.get()
	confirm_password = user_again_entry.get()

	if user_newpassword != confirm_password:
		messagebox.showerror("Error", "New passwords do not match!")
	else:
		messagebox.showinfo("Success", "Password changed successfully!")

root = Tk()
root.geometry("450x300")
root.title("Enter new password")

user_oldpassword = Label(root, text="Old password:").place(x=40,y=60)
user_newpassword = Label(root, text="New password").place(x=40,y=100)
user_again       = Label(root, text=" Enter new password again").place(x=40,y=140)

user_oldpassword_entry = Entry(root, show='*')
user_oldpassword_entry.place(x=150,y=60)

user_newpassword_entry = Entry(root, show='*')
user_newpassword_entry.place(x=150,y=100)

user_again_entry = Entry(root, show='*')
user_again_entry.place(x=150,y=140)

bnt_ok = Button(root, text="     Ok      ",command=on_ok_click).place(x=100,y=180)
bnt_scancel = Button(root, text="Scancel",command=root.quit).place(x=200, y=180)
root.mainloop()
