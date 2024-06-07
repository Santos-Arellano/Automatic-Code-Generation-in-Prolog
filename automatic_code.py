from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pyswip import Prolog

# Inicializamos Prolog y consultamos el archivo Prolog
prolog = Prolog()
prolog.consult('prolog_autocode.pl')

def generate_code_button_clicked():
    # Obtenemos el lenguaje y las especificaciones ingresadas por el usuario
    language = language_var.get()
    specs = specs_text.get(1.0, END).strip()

    # Construimos la consulta a Prolog con el formato adecuado
    query = f"generate_code({language}, [{specs}], Code)."
    print("Query: ", query)
    try:
        # Realizamos la consulta a Prolog y obtenemos el código generado
        code = list(prolog.query(query))
        generated_code = code[0]['Code'] if code else "Error: Failed to generate code."
    except Exception as e:
        # Si hay un error, lo mostramos
        generated_code = f"Error: {e}"

    # Mostramos el código generado o el mensaje de error en la interfaz
    code_text.delete(1.0, END)
    code_text.insert(END, generated_code)

def copy_to_clipboard():
    # Copiamos el código generado al portapapeles
    generated_code = code_text.get(1.0, END).strip()
    if generated_code:
        root.clipboard_clear()
        root.clipboard_append(generated_code)
        root.update()  # Actualizamos el portapapeles con el nuevo contenido
        messagebox.showinfo("Copy to Clipboard", "Code copied to clipboard!")
    else:
        messagebox.showwarning("Copy to Clipboard", "No code to copy!")

def show_examples():
    # Creamos una nueva ventana para mostrar ejemplos de especificaciones
    examples_window = Toplevel(root)
    examples_window.title("Specification Examples")
    examples_window.geometry("400x300")

    # Definimos los ejemplos a mostrar
    examples = """
    1.- Assign: 
        assign(x, 10)
    2.- Loops:
        loop(i, 0, 5, [assign(sum, 'sum + i')])
        do_while('x < 5', [assign(x, 'x + 1')])
        while('x < 20', [assign(x, 'x + 1')])
    3.- Conditionals:
        if_else('x > 0', [assign(y, 'x - 1')], [assign(y, 'x + 1')])
    4.- Print:
        print('Hello, World!')
    5.- Nested syntax:
        loop(i, 0, 5, [if_else((i == 3), [print("Hello world")], [loop(i, 0, 5, [assign(sum, 'sum + i')])])])
    """

    # Agregamos los ejemplos a la ventana
    examples_label = Label(examples_window, text="Examples of Specifications:", font=('Helvetica', 12))
    examples_label.pack(pady=10)

    examples_text = Text(examples_window, height=10, width=50, wrap=WORD, font=('Helvetica', 12), relief=GROOVE, borderwidth=2)
    examples_text.insert(END, examples)
    examples_text.pack(pady=10)

    close_button = ttk.Button(examples_window, text="Close", command=examples_window.destroy)
    close_button.pack(pady=5)

# Creamos la interfaz gráfica
root = Tk()
root.title("Code Generation Interface")
root.geometry("500x500")

# Aplicamos estilos a la interfaz
style = ttk.Style()
style.theme_use('alt')  # Puedes cambiar esto a 'alt', 'clam', 'default', 'classic'

style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12, 'bold'), background='#4CA364', foreground='white')
style.configure('TEntry', font=('Helvetica', 12))
style.configure('TText', font=('Helvetica', 12))

# Creamos el marco principal de la interfaz
mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.pack(fill=BOTH, expand=True)

# Creamos los elementos de la interfaz (etiquetas, campos de texto, botones, etc.)
language_var = StringVar()
ttk.Label(mainframe, text="Language (cpp/rust):").pack(pady=5)
language_combobox = ttk.Combobox(mainframe, textvariable=language_var, values=["cpp", "rust"])
language_combobox.pack(fill=X, pady=5)

ttk.Label(mainframe, text="Specifications:").pack(pady=5)
specs_text = Text(mainframe, height=5, wrap=WORD, font=('Helvetica', 12), relief=GROOVE, borderwidth=2)
specs_text.pack(fill=X, pady=5)

generate_button = ttk.Button(mainframe, text="Generate Code", command=generate_code_button_clicked)
generate_button.pack(pady=5)

copy_button = ttk.Button(mainframe, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

examples_button = ttk.Button(mainframe, text="Show Examples", command=show_examples)
examples_button.pack(pady=5)

code_text = Text(mainframe, height=10, width=50, wrap=WORD, font=('Helvetica', 12), relief=GROOVE, borderwidth=2)
code_text.pack(pady=5)

# Iniciamos el bucle de eventos de la interfaz
root.mainloop()