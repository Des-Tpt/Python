import tkinter as tk

def chuyen_nam():
    nam_duong = int(entry_nam_duong.get())

    nam_am = chuyen_doi_nam(nam_duong)

    label_nam_am.config(text=f"Năm âm: {nam_am}")

def chuyen_doi_nam(nam):
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị"]
    return f"{can[(nam-4)%10]} {chi[(nam-4)%12]}"

window = tk.Tk()
window.config(bg="#FFFF00")
window.geometry("400x100")

label_nam_duong = tk.Label(window, text="Nhập năm dương:",bg="#FFFF00").place(x=0,y=0)
entry_nam_duong = tk.Entry(window)
button_chuyen = tk.Button(window, text="Chuyển", command=chuyen_nam,bg="skyblue")
label_nam_am = tk.Label(window, text="Năm âm:",bg="#FFFF00")

entry_nam_duong.pack()
button_chuyen.pack()
label_nam_am.pack()

window.mainloop()
