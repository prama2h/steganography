import cv2
import os
import string
import tkinter as tk
from tkinter import ttk, filedialog

def encode():
    global img, msg, password, d, c

    img = cv2.imread(file_path)
    msg = entry_msg.get()
    password = entry_password.get()

    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("Encryptedmsg.jpg", img)
    os.system("start Encryptedmsg.jpg")

    # Display console output
    console_output.set("Successfully encoded. Encryptedmsg.jpg created.")
    print("Successfully encoded. Encryptedmsg.jpg created.")

def decode():
    global img, msg, password, d, c

    message = ""
    n = 0
    m = 0
    z = 0

    pas = entry_passcode.get()

    if password == pas:
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        console_output.set(f"Decryption message: {message}")
        print(f"Decryption message: {message}")
    else:
        console_output.set("Not a valid key")
        print("Not a valid key")

def select_image():
    global img, file_path
    file_path = filedialog.askopenfilename()

    if file_path:  # Check if a file was selected
        img = cv2.imread(file_path)

        if img is not None:  # Check if image reading was successful
            console_output.set("Image selected successfully.")
            print("Image selected successfully.")
        else:
            console_output.set("Error: Unable to read the selected image.")
            print("Error: Unable to read the selected image.")
    else:
        console_output.set("Error: No image selected.")
        print("Error: No image selected.")

# Create the main window
root = tk.Tk()
root.title("Steganography Tool")

# Set ttk theme
style = ttk.Style()
style.theme_use("clam")  # You can change the theme ("clam", "alt", "default", "vista", etc.)

# Create and place widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_msg = ttk.Label(frame, text="Enter Secret Message:")
label_msg.grid(row=0, column=0, pady=5, padx=5, sticky=tk.W)

entry_msg = ttk.Entry(frame)
entry_msg.grid(row=0, column=1, pady=5, padx=5, sticky=tk.W)

label_password = ttk.Label(frame, text="Enter Password:")
label_password.grid(row=1, column=0, pady=5, padx=5, sticky=tk.W)

entry_password = ttk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)

btn_encode = ttk.Button(frame, text="Encode", command=encode)
btn_encode.grid(row=2, column=0, pady=10, padx=5, sticky=tk.W)

btn_select_image = ttk.Button(frame, text="Select Image", command=select_image)
btn_select_image.grid(row=2, column=1, pady=10, padx=5, sticky=tk.W)

label_passcode = ttk.Label(frame, text="Enter Passcode for Decryption:")
label_passcode.grid(row=3, column=0, pady=5, padx=5, sticky=tk.W)

entry_passcode = ttk.Entry(frame, show="*")
entry_passcode.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)

btn_decode = ttk.Button(frame, text="Decode", command=decode)
btn_decode.grid(row=4, column=0, pady=10, padx=5, sticky=tk.W)

# Console output label
console_output = tk.StringVar()
label_console = ttk.Label(frame, textvariable=console_output, wraplength=300)
label_console.grid(row=5, column=0, columnspan=2, pady=10, padx=5, sticky=tk.W)

# Run the main loop
root.mainloop()
