import pygame
import os
import tkinter as tk
from tkinter import filedialog, messagebox

pygame.mixer.init()

root = tk.Tk()
root.title("Python Music Player")

def play_music():
    try:
        selected_song = playlistbox.get(tk.ACTIVE)
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def stop_music():
    pygame.mixer.music.stop()

def add_songs_from_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        mp3_files = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]
        for song in mp3_files:
            song_path = os.path.join(folder_path, song)
            playlistbox.insert(tk.END, song_path)

def remove_from_playlist():
    selected_song = playlistbox.curselection()
    if selected_song:
        playlistbox.delete(selected_song)

playlistbox = tk.Listbox(root, selectmode=tk.SINGLE, activestyle=tk.NONE, height=10, width=60)
playlistbox.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

play_button = tk.Button(root, text="Play", command=play_music)
stop_button = tk.Button(root, text="Stop", command=stop_music)
add_button = tk.Button(root, text="Add Songs from Folder", command=add_songs_from_folder)
remove_button = tk.Button(root, text="Remove Song", command=remove_from_playlist)

play_button.grid(row=1, column=0, padx=20, pady=20)
stop_button.grid(row=1, column=1, padx=20, pady=20)
add_button.grid(row=2, column=0, padx=20)
remove_button.grid(row=2, column=1, padx=20)

root.mainloop()
