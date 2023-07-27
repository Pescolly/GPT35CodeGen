import tkinter as tk
from tkinter import filedialog
import subprocess
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Video Player") # Set the title of the application window
        self.geometry("600x600") # Set the size of the application window
        self.configure(bg="black") # Set the background color of the application window to black
        
        self.button = tk.Button(self, text="yo yo yo", command=self.load_file) # Create a button with the text "yo yo yo" and associate the load_file method with its command
        self.button.pack() # Display the button on the application window

        self.movie_resolution_label = tk.Label(self, bg="black", fg="white")  # Create a label to display the movie resolution
        self.movie_resolution_label.pack()  # Display the label on the application window

        self.movie_runtime_label = tk.Label(self, bg="black", fg="white")  # Create a label to display the movie runtime
        self.movie_runtime_label.pack()  # Display the label on the application window
        
        self.text_field_1 = tk.Entry(self) # Create the first editable text field
        self.text_field_1.pack() # Display the first text field on the application window
        
        self.copy_button = tk.Button(self, text="Copy", command=self.copy_text) # Create a button with the text "Copy" and associate the copy_text method with its command
        self.copy_button.pack() # Display the copy button on the application window
        
        self.text_field_2 = tk.Entry(self) # Create the second editable text field
        self.text_field_2.pack() # Display the second text field on the application window
        
        self.drawing_region = tk.Canvas(self, width=200, height=200, bg="light grey") # Create a canvas for drawing
        self.drawing_region.pack() # Display the drawing region on the application window

    def load_file(self):
        try:
            filename = filedialog.askopenfilename(filetypes=(("MOV files", "*.mov"), ("All files", "*.*")))  # Use the filedialog module to open a file dialog and select a .mov file
            if filename:
                self.play_movie(filename)  # Call the play_movie method with the selected filename
        except Exception as e:
            raise(e)  # Raise any exception or error occurred during loading the file

    def play_movie(self, filename):
        try:
            if not os.path.isfile(filename):
                raise FileNotFoundError("No such file or directory: {}".format(filename))  # Raise FileNotFoundError if the selected file doesn't exist
			# Use subprocess to play the .mov file in a 1920x1080 window
            subprocess.Popen(["ffplay", "-autoexit", "-x", "1920", "-y", "1080", filename])
        except Exception as e:
            raise(e)  # Raise any exception or error occurred during playing the movie

    def copy_text(self):
        try:
            text = self.text_field_1.get() # Get the text from the first text field
            self.text_field_2.delete(0, tk.END) # Clear the second text field
            self.text_field_2.insert(0, text) # Set the text in the second text field
        except Exception as e:
            raise(e) # Raise any exception or error occurred during copying the text

app = Application()  # Create an instance of the Application class
app.mainloop()  # Run the main event loop
# This application uses the tkinter library to create a video player with a GUI.
# The application window has a black background and a size of 600x600 pixels.
# It includes a button labeled "yo yo yo" to load a .mov file.
# When the button is clicked, a file dialog is opened to select a .mov file.
# The selected file is then played using the ffplay command in a 1920x1080 window.
# The application also displays the resolution and runtime of the currently playing movie file.
# Below the movie information, there are two editable text fields and a copy button.
# Clicking the copy button moves the text from the first text field to the second.
# Finally, there is a 200x200 light grey canvas for drawing.
# The application handles errors and exceptions by raising them to the main event loop.