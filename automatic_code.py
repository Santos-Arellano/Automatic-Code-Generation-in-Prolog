from tkinter import *
from pyswip import Prolog

prolog = Prolog()
prolog.consult('prolog_autocode.pl')

def generate_code_button_clicked():
    language = language_var.get()
    specs = specs_entry.get()

    # Construct query string with proper formatting
    query = f"generate_code({language}, [{specs}], Code)."
    print("Queryyy: ", query)
    try:
        # Query Prolog and retrieve code
        code = list(prolog.query(query))
        generated_code = code[0]['Code'] if code else "Error: Failed to generate code."
    except Exception as e:
        generated_code = f"Error: {e}"

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