import tkinter as tk
from tkinter import messagebox
# create a main application window

root=tk.Tk()
root.title("Greeting App")
root.geometry("300x200")  # set window size

# function to display the greeting
def greet():
    name = name_entry.get()
    if name:
        messagebox.showinfo("Greeting", f"Hello,{name}!")
    else:
        messagebox.showwarning("Inpute Error", "Please enter your name")

# create a label        
name_label =  tk.Label(root,text="Please enter your name")
name_label.pack(pady=10)

# create a entry box for user input  
name_entry = tk.Entry(root)
name_entry.pack(pady=10)
   
    
# create the button that trigger the greet function
greet_button = tk.Button(root, text="Greet", command =greet)
greet_button.pack(pady=10) # pack the button into the window 

# start the Tkinter even loop
root.mainloop()