from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from pyswip import Prolog

# Initialize Prolog and consult the Prolog file
prolog = Prolog()
prolog.consult('prolog_autocode.pl')

def generate_code_button_clicked():
    language = language_var.get()
    specs = specs_examples[language]

    # Construct query string with proper formatting
    query = f"generate_code({language}, [{specs}], Code)."
    print("Query: ", query)
    try:
        # Query Prolog and retrieve code
        code = list(prolog.query(query))
        generated_code = code[0]['Code'] if code else "Error: Failed to generate code."
    except Exception as e:
        generated_code = f"Error: {e}"

    # Display the generated code or error message
    code_text.delete(1.0, END)
    code_text.insert(END, generated_code)

def copy_to_clipboard():
    # Copy the generated code to the clipboard
    generated_code = code_text.get(1.0, END).strip()
    if generated_code:
        root.clipboard_clear()
        root.clipboard_append(generated_code)
        root.update()  # Update the clipboard with the new content
        messagebox.showinfo("Copy to Clipboard", "Code copied to clipboard!")
    else:
        messagebox.showwarning("Copy to Clipboard", "No code to copy!")

# Create the GUI
root = ThemedTk(theme="radiance")  # Use a nzicer theme
root.title("Code Generation Interface")
root.geometry("500x400")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.pack(fill=BOTH, expand=True)

# Example specifications for each language
specs_examples = {
    'cpp': 'assign(x, 10), loop(i, 0, 5, [assign(sum, \'sum + i\')]), if_else(\'x > 0\', [assign(y, \'x - 1\')], [assign(y, \'x + 1\')])',
    'rust': 'assign(x, 10), loop(i, 0, 5, [assign(sum, \'sum + i\')]), if_else(\'x > 0\', [assign(y, \'x - 1\')], [assign(y, \'x + 1\')])'
}

language_var = StringVar()
ttk.Label(mainframe, text="Language:").pack(pady=5)
ttk.OptionMenu(mainframe, language_var, *specs_examples.keys()).pack(fill=X, pady=5)

generate_button = ttk.Button(mainframe, text="Generate Code", command=generate_code_button_clicked)
generate_button.pack(pady=5)

copy_button = ttk.Button(mainframe, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

code_text = Text(mainframe, height=10, width=50, wrap=WORD, font=('Helvetica', 12), relief=GROOVE, borderwidth=2)
code_text.pack(pady=5)

# Start the GUI event loop
root.mainloop()