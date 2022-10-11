from distutils.cmd import Command
import tkinter

root = tkinter.Tk()
root.title("BMI Calculator")

# Create function(s)
def calculate_bmi():
    kg = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round(kg / (height ** 2), 2)
    label_result['text'] = f"BMI: {bmi}"

    if bmi >= 18.5 and bmi <=24.9:
        label_body['text']=f"You are normal"
    elif bmi < 18.5:
        label_body['text']=f"You are underweight"
    elif bmi >=25 and bmi <=29.9:
        label_body['text']=f"You are Overweight"
    elif bmi >=30:
        label_body['text']=f"You are Obese"

# Create GUI
label_kg = tkinter.Label(root, text="Weight in kg: ")
label_kg.grid(column=0, row=0)

entry_kg = tkinter.Entry(root)
entry_kg.grid(column=1, row=0)

label_height = tkinter.Label(root, text="Height in cm: ")
label_height.grid(column=0, row=1)

entry_height = tkinter.Entry(root)
entry_height.grid(column=1, row=1)

button_calculate = tkinter.Button(root, text="Calculate", command=calculate_bmi)
button_calculate.grid(column=0, row=2)

label_result = tkinter.Label(root, text="BMI: ")
label_result.grid(column=1, row=2)

label_body = tkinter.Label(root, text="Body type: ")
label_body.grid(column=1, row=3)

root.mainloop()
