import tkinter as tk
from tkinter import filedialog
from subprocess import Popen, PIPE
import basicLexical  # Import the module where the logic is defined


def Lex(input_field, output_field):
    # Get the input from the first text field
    input_text = input_field.get("1.0", tk.END).strip()

    # Split input into lines and process each line separately
    lines = input_text.split('\n')

    output_field.config(state=tk.NORMAL)
    output_field.delete(1.0, tk.END)

    for line in lines:
        # Process the expression using the logic from basic.py
        tokens, error = basicLexical.run('<stdin>', line.strip())

        # Display the result or error in the second text field
        if error:
            output_field.insert(tk.END, error.as_string() + '\n')
        else:
            output_field.insert(tk.END, str(tokens) + '\n')

    output_field.config(state=tk.DISABLED)

def execute_syntaxique(input_field, output_field):
    # Get the input from the first text field
    input_text = input_field.get("1.0", tk.END).strip()

    # Execute the syntaxique.py script and capture the output
    process = Popen(['python', 'syntaxique.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)
    stdout, stderr = process.communicate(input=input_text)

    # Display the output in the second text field
    output_field.config(state=tk.NORMAL)
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, stdout)
    output_field.config(state=tk.DISABLED)

def sem(input_field, output_field):
    # Get the input from the first text field
    input_text = input_field.get("1.0", tk.END).strip()

    # Execute the syntaxique.py script and capture the output
    process = Popen(['python', 'sem.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)
    stdout, stderr = process.communicate(input=input_text)

    # Display the output in the second text field
    output_field.config(state=tk.NORMAL)
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, stdout)
    output_field.config(state=tk.DISABLED)

def upload_file(input_field):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.snk")])
    if file_path:
        with open(file_path, 'r') as file:
            file_content = file.read()
            input_field.delete(1.0, tk.END)
            input_field.insert(tk.END, file_content)

# Create the main window
window = tk.Tk()
window.title("Projet TP COMP")

# Create a button to execute the shell
execute_button = tk.Button(window, text="Lexical", command=lambda: Lex(input_field, output_field))
execute_button.grid(row=0, column=0, pady=10, padx=10)

# Create a button to execute syntaxique.py
syntaxique_button = tk.Button(window, text="Syntaxique", command=lambda: execute_syntaxique(input_field, output_field))
syntaxique_button.grid(row=0, column=1, pady=10, padx=10)

# Create a button to execute sem.py
sem_button = tk.Button(window, text="Semantique", command=lambda: sem(input_field, output_field))
sem_button.grid(row=0, column=2, pady=10, padx=10)

# Create a button to upload a file
upload_button = tk.Button(window, text="Upload File", command=lambda: upload_file(input_field))
upload_button.grid(row=0, column=3, pady=10, padx=10)

# Create a text field for input
input_field = tk.Text(window, height=30, width=50)
input_field.grid(row=1, column=0, pady=5, padx=10)

# Create a text field for output
output_field = tk.Text(window, height=30, width=120, state=tk.DISABLED)
output_field.grid(row=1, column=1, columnspan=3, pady=5, padx=10)

# Add green colored borders to text fields
input_field.config(
    highlightbackground="green",
    highlightcolor="green",
    highlightthickness=2,  # Adjust the thickness as needed
)
output_field.config(
    highlightbackground="green",
    highlightcolor="green",
    highlightthickness=2,  # Adjust the thickness as needed
)


# Start the GUI event loop
window.mainloop()
