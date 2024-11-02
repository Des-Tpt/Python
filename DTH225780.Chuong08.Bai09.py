
import tkinter as tk

window = tk.Tk()
window.title("Tính toán BMI")
window.geometry("400x250")
window.configure(bg="yellow")

label_height = tk.Label(window, text="Nhập chiều cao (m):",bg="yellow").place(x=0,y=0)

entry_height = tk.Entry(window)
entry_height.pack()

label_weight = tk.Label(window, text="Nhập cân nặng (kg):",bg="yellow").place(x=0,y=20)

entry_weight = tk.Entry(window)
entry_weight.pack()

button_calculate = tk.Button(window, text="Tính BMI",bg="skyblue")
button_calculate.pack()

label_bmi = tk.Label(window, text="BMI của bạn:",bg="yellow").place(x=0,y=60)

result_bmi = tk.Button(window, text="X")
result_bmi.pack()

label_status = tk.Label(window, text="Tình trạng của bạn:",bg="yellow").place(x=0,y=90)

result_status = tk.Button(window, text="Hơi Béo")
result_status.pack()

label_risk = tk.Label(window, text="Nguy cơ phát triển bệnh:",bg="yellow").place(x=0,y=110)

result_risk = tk.Button(window, text="Hơi hơi cao")
result_risk.pack()

button_quit = tk.Button(window, text="Thoát", command=window.quit,bg="skyblue")
button_quit.pack()

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        bmi = weight / (height ** 2)
        result_bmi.config(text=f"{bmi:.2f}")

        if bmi < 18.5:
            result_status.config(text="Gầy")
            result_risk.config(text="Thấp")
        elif 18.5 <= bmi < 25:
            result_status.config(text="Bình thường")
            result_risk.config(text="Thấp")
        elif 25 <= bmi < 30:
            result_status.config(text="Thừa cân")
            result_risk.config(text="Trung bình")
        else:
            result_status.config(text="Béo phì")
            result_risk.config(text="Cao")
    except ValueError:
        result_bmi.config(text="Vui lòng nhập số!")
        result_status.config(text="")
        result_risk.config(text="")

button_calculate.config(command=calculate_bmi)

window.mainloop()


