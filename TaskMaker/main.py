import tkinter as tk
from tkinter import messagebox
import pandas as pd

def add_task():
    task_title = title_entry.get()
    task_description = description_entry.get()
    
    if task_title and task_description:
        task_list.insert(tk.END, task_title)
        descriptions.append(task_description)
        title_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter both title and description.")

def display_description(event):
    selected_indices = task_list.curselection()
    description_listbox.delete(0, tk.END)
    
    for index in selected_indices:
        description_listbox.insert(tk.END, descriptions[index])

def mark_completed():
    selected_indices = task_list.curselection()
    for index in reversed(selected_indices):
        task_list.delete(index)
        descriptions.pop(index)
    description_listbox.delete(0, tk.END)


def save_tasks_to_excel():
    data = {"Titles": task_list.get(0, tk.END), "Descriptions": descriptions}
    df = pd.DataFrame(data)
    df.to_excel("tasks.xlsx", index=False)


def load_tasks_from_excel():
    try:
        df = pd.read_excel("tasks.xlsx")
        task_list.delete(0, tk.END)  
        descriptions.clear()  
        
        for _, row in df.iterrows():
            title = row["Titles"]
            description = row["Descriptions"]
            task_list.insert(tk.END, title)
            descriptions.append(description)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "Excel file 'tasks.xlsx' not found.")

root = tk.Tk()
root.title("Task Tracker")

title_label = tk.Label(root, text="Title:")
title_label.grid(row=0, column=0, sticky="w")

title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1, padx=5, pady=5)

description_label = tk.Label(root, text="Description:")
description_label.grid(row=1, column=0, sticky="w")

description_entry = tk.Entry(root)
description_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

task_list = tk.Listbox(root, width=30, height=10, selectmode=tk.MULTIPLE)
task_list.grid(row=0, column=2, rowspan=4, padx=10)

task_list.bind("<<ListboxSelect>>", display_description)

mark_completed_button = tk.Button(root, text="Mark Completed", command=mark_completed)
mark_completed_button.grid(row=4, column=2, padx=10, pady=5)

save_button = tk.Button(root, text="Save Tasks", command=save_tasks_to_excel)
save_button.grid(row=5, column=0, columnspan=2, pady=10)

load_button = tk.Button(root, text="Load Tasks", command=load_tasks_from_excel)
load_button.grid(row=6, column=0, columnspan=2, pady=10)

descriptions = []

description_listbox = tk.Listbox(root, width=50, height=10)
description_listbox.grid(row=0, column=3, rowspan=4, padx=10)

load_tasks_from_excel()

root.mainloop()
