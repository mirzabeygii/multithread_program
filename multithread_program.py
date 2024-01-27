import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import time
import webbrowser
import pygame
import os

class multithreadProgram:
    def __init__(self, root):
        self.root = root
        self.root.title("Multitrade Program")
        self.root.geometry("400x250")
        self.create_clock()
        self.create_buttons()

    def create_buttons(self):
        play_music_btn = ttk.Button(self.root, text="Play Music", command=self.play_music)
        play_music_btn.pack(pady=10)
        open_drawing_btn = ttk.Button(self.root, text="Drawing", command=self.open_drawing_window)
        open_drawing_btn.pack(pady=10)
        select_photo_btn = ttk.Button(self.root, text="Show Photo", command=self.select_photo)
        select_photo_btn.pack(pady=10)
        
    def create_clock(self):
        self.clock_label = ttk.Label(self.root, font=('Arial', 40))
        self.clock_label.pack()
        self.update_time()

    def update_time(self):
        current_time = time.strftime('%H:%M:%S') 
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_time)

    def play_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if file_path:
            self.display_music_info(file_path)
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()

    def display_music_info(self, file_path):
        music_window = tk.Toplevel(self.root)
        music_window.title("Now Playing")
        music_name = ttk.Label(music_window, text=" Music: " + file_path.split("/")[-1])
        music_name.pack()
        music_window.protocol("WM_DELETE_WINDOW", self.stop_music)

    def stop_music(self):
        pygame.mixer.music.stop()
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Toplevel) and "Now Playing" in widget.title():
                widget.destroy()

    def open_drawing_window(self):
        webbrowser.open_new_tab("https://sketch.io/sketchpad/")

    def select_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.display_photo(file_path)

    def display_photo(self, file_path):
        photo_window = tk.Toplevel(self.root)
        photo_window.title("Photo")
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(photo_window, image=photo)
        label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        label.pack()


root = tk.Tk()
app = multithreadProgram(root)
root.mainloop()
