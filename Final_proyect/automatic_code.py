from tkinter import *
from pyswip import Prolog

prolog = Prolog()
prolog.consult('/Users/santosa/Documents/GitHub/Automatic-Code-Generation-in-Prolog/Final_proyect/prolog_autocode.pl')

def generate_code(language, specs):
    code = list(prolog.query(f"generate_code('{language}', {specs}, Code)"))
    return code[0]['Code'] if code else "Error: Failed to generate code."

def generate_code_button_clicked():
    language = language_var.get()
    specs = specs_entry.get()
    generated_code = generate_code(language, specs)
    code_text.delete(1.0, END)
    code_text.insert(END, generated_code)

# Crear la interfaz gráfica
root = Tk()
root.title("Code Generation Interface")

language_var = StringVar()
Label(root, text="Language (cpp/rust):").pack()
Entry(root, textvariable=language_var).pack()

Label(root, text="Specifications:").pack()
specs_entry = Entry(root)
specs_entry.pack()

generate_button = Button(root, text="Generate Code", command=generate_code_button_clicked)
generate_button.pack()

code_text = Text(root, height=10, width=50)
code_text.pack()

root.mainloop()