import tkinter as tk

def calculate_love_score(name1, name2):
    combined_names = name1.lower() + name2.lower()
    love_score = 0
    
    # Count the occurrences of each letter in "true love"
    for letter in "true love":
        love_score += combined_names.count(letter)
    
    return love_score

def calculate_and_display():
    name1 = entry_name1.get()
    name2 = entry_name2.get()
    
    love_score = calculate_love_score(name1, name2)
    
    result_label.config(text=f"The love score between {name1.capitalize()} and {name2.capitalize()} is {love_score}.")

# Create the main window
window = tk.Tk()
window.title("Love Calculator")

# Create labels and entry fields
label_name1 = tk.Label(window, text="Enter first name:")
label_name1.grid(row=0, column=0, padx=5, pady=5)

entry_name1 = tk.Entry(window)
entry_name1.grid(row=0, column=1, padx=5, pady=5)

label_name2 = tk.Label(window, text="Enter second name:")
label_name2.grid(row=1, column=0, padx=5, pady=5)

entry_name2 = tk.Entry(window)
entry_name2.grid(row=1, column=1, padx=5, pady=5)

result_label = tk.Label(window, text="")
result_label.grid(row=2, columnspan=2, padx=5, pady=10)

calculate_button = tk.Button(window, text="Calculate", command=calculate_and_display)
calculate_button.grid(row=3, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
window.mainloop()
