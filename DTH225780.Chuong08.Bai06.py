
from tkinter import Tk
from tkinter import Button
from tkinter import Label


root = Tk()
root.geometry("500x200")
root.title("frame 2")

bw0 = Label(root, text="borderwidth = 0").place(x=0,y=0)
bw1 = Label(root, text="borderwidth = 1").place(x=0,y=40)
bw2 = Label(root, text="borderwidth = 2").place(x=0,y=80)
bw3 = Label(root, text="borderwidth = 3").place(x=0,y=120)
bw4 = Label(root, text="borderwidth = 4").place(x=0,y=160)

raised = Label(root, text="raised").place(x=120,y=0)
sunken = Label(root, text="sunken").place(x=180,y=0)
flat = Label(root, text="flat").place(x=260,y=0)
ridge = Label(root, text="ridge").place(x=320,y=0)
groove = Label(root, text="groove").place(x=380,y=0)
solid = Label(root, text="solid").place(x=440,y=0)

Button(root, text="raised",command=root.quit).place(x=120, y=40)
Button(root, text="raised",command=root.quit).place(x=120, y=80)
Button(root, text="raised",command=root.quit).place(x=120, y=120)
Button(root, text="raised",command=root.quit).place(x=120, y=160)

Button(root, text="sunken",command=root.quit).place(x=180, y=40)
Button(root, text="sunken",command=root.quit).place(x=180, y=80)
Button(root, text="sunken",command=root.quit).place(x=180, y=120)
Button(root, text="sunken",command=root.quit).place(x=180, y=160)

Label(root, text="flat").place(x=260,y=40)
Label(root, text="flat").place(x=260,y=80)
Label(root, text="flat").place(x=260,y=120)
Label(root, text="flat").place(x=260,y=160)

Button(root, text="ridge",command=root.quit).place(x=320, y=40)
Button(root, text="ridge",command=root.quit).place(x=320, y=80)
Button(root, text="ridge",command=root.quit).place(x=320, y=120)
Button(root, text="ridge",command=root.quit).place(x=320, y=160)

Button(root, text="groove",command=root.quit).place(x=380, y=40)
Button(root, text="groove",command=root.quit).place(x=380, y=80)
Button(root, text="groove",command=root.quit).place(x=380, y=120)
Button(root, text="groove",command=root.quit).place(x=380, y=160)

Button(root, text="solid",command=root.quit).place(x=440, y=40)
Button(root, text="solid",command=root.quit).place(x=440, y=80)
Button(root, text="solid",command=root.quit).place(x=440, y=120)
Button(root, text="solid",command=root.quit).place(x=440, y=160)
root.mainloop()
