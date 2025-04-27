import random
import string
import tkinter as tk

# Function to generate a random password
def generate_password(length=12):
    # Allowed symbols for the password
    allowed_symbols = "!@#$%^&*"
    # Combine letters, digits, and allowed symbols
    all_characters = string.ascii_letters + string.digits + allowed_symbols
    # Generate password by selecting random characters from all_characters
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

# Function to handle button click or pressing Enter
def on_generate_button_click(event=None):
    try:
        # Get password length from the input
        password_length = int(entry_length.get())  
        # Generate a random password based on the input length
        generated_password = generate_password(password_length)
        
        # Check if a pop-up already exists, if yes, close it before creating a new one
        if hasattr(on_generate_button_click, "popup"):
            on_generate_button_click.popup.destroy()

        # Create a custom pop-up to display the generated password
        on_generate_button_click.popup = tk.Toplevel(root)
        on_generate_button_click.popup.title("Generated Password")
        
        # Set size and background color for the pop-up
        on_generate_button_click.popup.geometry("400x250")
        on_generate_button_click.popup.config(bg="#222222")  # Dark background
    
        # Create a label inside the pop-up
        label = tk.Label(on_generate_button_click.popup, text="This is Your Generated Password!", font=("Helvetica", 14, "bold"), fg="#ecf0f1", bg="#222222")
        label.pack(pady=15)
        
        # Display the password in an Entry widget so it can be copied
        password_entry = tk.Entry(on_generate_button_click.popup, font=("Helvetica", 12), width=35, justify="center", bd=2, relief="solid")
        password_entry.insert(tk.END, generated_password)  # Insert the generated password
        password_entry.pack(pady=10)
        
        # Focus the cursor on the Entry widget to facilitate copying
        password_entry.focus()
        password_entry.select_range(0, tk.END)  # Select all text for easy copying
        
        # Lock the Entry so it cannot be edited
        password_entry.config(state="disabled")  # Disable keyboard input

        # Function to copy the password to the clipboard
        def copy_to_clipboard():
            root.clipboard_clear()  # Clear the clipboard
            root.clipboard_append(generated_password)  # Copy password to clipboard
            root.update()  # Update clipboard
            # Display a success message after copying
            label_copy_status.config(text="Copied!", fg="#ffffff", font=("Arial", 12, "bold"))

        # Button to copy the password to clipboard
        button_copy = tk.Button(on_generate_button_click.popup, text="Copy Password", command=copy_to_clipboard, font=("Helvetica", 12), bg="#FEBA17", fg="black", bd=0, relief="flat", width=15)
        button_copy.pack(side="left", padx=10, pady=10)  # Position the button to the left

        # Button to close the pop-up
        button_close = tk.Button(on_generate_button_click.popup, text="Close", command=on_generate_button_click.popup.destroy, font=("Arial", 12, "bold"), bg="#e74c3c", fg="black", bd=0, relief="flat", width=15)
        button_close.pack(side="right", padx=10, pady=10)  # Position the button to the right
        
        # Label to display the copy status message (e.g., "Copied!")
        label_copy_status = tk.Label(on_generate_button_click.popup, text="", font=("Helvetica", 10), fg="red", bg="#222222")
        label_copy_status.pack(pady=10)
        
    except ValueError:
        # Show an error message if the input is not a valid integer
        tk.messagebox.showerror("Input Error", "Please enter a valid password length!")

# Create the main window for the application
root = tk.Tk()
root.title("Random Password Generator")

# Set the size and background color for the main window
root.geometry("400x300")
root.config(bg="#222222")

# Create a label and an entry field for inputting the password length
label_length = tk.Label(root, text="Enter The Password Length!", font=("Georgia", 12, "bold"), fg="white", bg="#222222")
label_length.pack(pady=15)

entry_length = tk.Entry(root, font=("Helvetica", 12), width=25)
entry_length.pack(pady=10)

# Bind the Enter key to call the on_generate_button_click function
entry_length.bind("<Return>", on_generate_button_click)

# Create a button to generate the password
button_generate = tk.Button(root, text="Generate Password", command=on_generate_button_click, font=("Helvetica", 12), bg="#ffffff", fg="black", bd=0, relief="flat", width=20)
button_generate.pack(pady=20)

# Run the Tkinter application
root.mainloop()