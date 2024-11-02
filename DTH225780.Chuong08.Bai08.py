import tkinter as tk

window = tk.Tk()
window.title("Chuyển đổi nhiệt độ")
window.configure(bg="yellow")
window.geometry("400x100")

label_fahrenheit = tk.Label(window, text="Nhập độ F:",bg="yellow").place(x=0,y=0)

entry_fahrenheit = tk.Entry(window)
entry_fahrenheit.pack()

button_convert = tk.Button(window, text="Chuyển",bg="skyblue")
button_convert.pack()

label_celsius = tk.Label(window, text="Độ C:",bg="yellow").place(x=0,y=43)

result_label = tk.Label(window, text="Độ C ở đây",bg="yellow")
result_label.pack()

def convert_fahrenheit_to_celsius():
    fahrenheit = float(entry_fahrenheit.get())
    celsius = (fahrenheit - 32) * 5/9
    result_label.config(text=f"Độ C: {celsius:.2f}")

button_convert.config(command=convert_fahrenheit_to_celsius)

window.mainloop()

