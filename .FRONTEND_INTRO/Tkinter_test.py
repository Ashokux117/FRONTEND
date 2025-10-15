import tkinter as tk
# create a main application window

root=tk.Tk()
root.title("siple Tkinter App")
root.geometry("200x100")  # set window size

# function to print "hello world"in the console 
def say_hello():
    print("Hello, World!")
    print("good bye")
    
# create the button that trigger the say_hello function
hello_button = tk.Button(root, text="click Me", command =say_hello)
hello_button.pack(pady=20) # pack the button into the window 

# start the Tkinter even loop
root.mainloop()