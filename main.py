from tkinter import *

def check_bmi():
    mass = float(input_mass.get())
    height = float(input_height.get())
    bmi = round(mass/(height**2),1)
    if bmi < 18.4:
        result.config(text='Низкая масса тела: ' + str(bmi))
    elif bmi >= 18.4 and bmi <= 25:
        result.config(text='Ваш вес в норме: ' + str(bmi))
    else:
        result.config(text='Высокая масса тела: ' + str(bmi))

window = Tk()
window.title("Индекс массы тела")
window.minsize(width=300, height=100)
window.config(padx=30,pady=30)

result = Label(text="_____", font=("Arial", 15, "bold"))
result.grid(column=1, row=0)

mass = Label(text="Масса:", font=("Arial", 10, "bold"))
mass.grid(column=0, row=1)

height = Label(text="Рост:", font=("Arial", 10, "bold"))
height.grid(column=0, row=2)

button = Button(text="Узнать результат", command=check_bmi)
button.grid(column=1, row=3)

input_mass = Entry(width=10,)
input_mass.grid(column=1, row=1)

input_height = Entry(width=10)
input_height.grid(column=1, row=2)

window.mainloop()