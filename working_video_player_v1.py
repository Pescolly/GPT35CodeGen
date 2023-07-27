#took 3 iterations

from tkinter import Tk, Button, filedialog, messagebox
import os
import subprocess

def play_movie():
    try:
        # Open a file dialog to select a .mov file
        file_path = filedialog.askopenfilename(filetypes=[("Movie files", "*.mov")])

        # Check if a file was selected
        if file_path:
            # Check if the file exists
            if os.path.exists(file_path):
                # Use subprocess to open the .mov file in a 1920x1080 window
                subprocess.run(["ffplay", "-x", "1920", "-y", "1080", file_path])
            else:
                # Show error message if the file does not exist
                messagebox.showerror("Error", "File does not exist.")
        else:
            # Show error message if no file was selected
            messagebox.showerror("Error", "No file selected.")
    except Exception as e:
        # Raise any Exceptions or Errors
        raise (e)


# Create the main window
window = Tk()
window.title("Movie Player")
window.geometry("600x600")

# Create a button to load a .mov file
button = Button(window, text="yo yo yo", command=play_movie)
button.pack()

# Start the tkinter event loop
window.mainloop()

"""
COMMENTS:

- This code uses the tkinter library to create a UI application in Python 3.9.
- The application allows the user to select and play a .mov file.
- The video is played using the ffplay command from the FFmpeg package.
- The UI consists of a button labeled "yo yo yo" which triggers the file selection process.
- The selected file is then checked for existence and played if it exists.
- Any Exceptions or Errors are raised and displayed to the user.
- The UI window has dimensions of 600x600 pixels.
- The video playback window is set to a resolution of 1920x1080 pixels.
"""