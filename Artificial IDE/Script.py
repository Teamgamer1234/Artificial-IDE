import tkinter as tk
import subprocess

def run_python_script():
    script_text = text_widget.get("1.0", "end-1c")
    try:
        result = subprocess.check_output(["python", "-c", script_text], stderr=subprocess.STDOUT, universal_newlines=True)
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
        output_text.config(state=tk.DISABLED)
    except subprocess.CalledProcessError as e:
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, e.output)
        output_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Artificial  IDE")

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(fill=tk.BOTH, expand=True)

run_button = tk.Button(root, text="Run", command=run_python_script)
run_button.pack()

output_text = tk.Text(root, state=tk.DISABLED, wrap=tk.WORD)
output_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
