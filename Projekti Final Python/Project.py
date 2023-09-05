#Made by: Ardi Osmani
#Email : ao52311@ubt-uni.net

import tkinter as tk
import pandas as pd

window = tk.Tk()
window.geometry("930x530")
window.title("Semester Program")

path_label = tk.Label(text="Enter file path:")
path_label.pack()

path_entry = tk.Entry()
path_entry.pack()

year_label = tk.Label(text="Select year:")
year_label.pack()
year_var = tk.StringVar()
year_menu = tk.OptionMenu(window, year_var, "", "1", "2", "3", "4")
year_menu.pack()


code_label = tk.Label(text="Enter Department:")
code_label.pack()
code_entry = tk.Entry()
code_entry.pack()






def clear_program():

    year_var.set("")

    code_entry.delete(0, tk.END)

    courses_listbox.delete(0, tk.END)
    saved_courses_listbox.delete(0, tk.END)


    courses_listbox.insert(tk.END, "The Courses Display")
    saved_courses_listbox.insert(tk.END, "The Saved Courses Display")






def display_program():

    if not path_entry.get():
        saved_courses_listbox.delete(0, tk.END)
        saved_courses_listbox.insert(tk.END, "Error: Please enter a file path")
        saved_courses_listbox.itemconfigure(0, fg="red")
        return


    df = pd.read_csv(path_entry.get())

    if year_var.get() and code_entry.get():
        filtered_df = df[(df["Year"] == int(year_var.get())) & (df["Department"] == code_entry.get())]
    elif year_var.get():
        filtered_df = df[df["Year"] == int(year_var.get())]
    elif code_entry.get():
        filtered_df = df[df["Department"] == code_entry.get()]
    else:
        saved_courses_listbox.delete(0, tk.END)
        saved_courses_listbox.insert(tk.END, "Error: Please select a year or a department")
        saved_courses_listbox.itemconfigure(0, fg="red")
        return


    #courses_listbox.delete(0)

    courses_listbox.insert(0, "=============================================================================")

    for index, row in filtered_df.iterrows():
        courses_listbox.insert(0, f"{row['Course']} (Year {row['Year']}, {row['Department']}, {row['Time']})")





def save_program():
    num_saved_courses = 0

    selected_courses = courses_listbox.curselection()

    num_saved_courses += len(selected_courses)

    if num_saved_courses > 3:
        saved_courses_listbox.delete(0, tk.END)
        saved_courses_listbox.insert(tk.END, "Error: No more than 3 Courses")
        saved_courses_listbox.itemconfigure(0, fg="red")
        return


    courses = []
    times = []

    for index in selected_courses:
        courses.append(courses_listbox.get(index))
        time = courses_listbox.get(index).split(",")[-1].strip()
        times.append(time)

    if len(set(times)) < len(times):
        saved_courses_listbox.delete(0, tk.END)
        saved_courses_listbox.insert(tk.END, "Error: Cannot have duplicate times")
        saved_courses_listbox.itemconfigure(0, fg="red")
        return

    df = pd.DataFrame(courses)

    df.to_csv("timetable.csv", index=False, header=False)

    saved_courses_listbox.delete(0, tk.END)

    for course in courses:
        saved_courses_listbox.insert(tk.END, course)










display_button = tk.Button(text="Display", command=display_program)


clear_button = tk.Button(text="Clear", command=clear_program)

save_button = tk.Button(text="Save", command=save_program)


warning_label = tk.Label(text="")
warning_label.pack()

courses_listbox = tk.Listbox(window, height=10, width=40, font=("Helvetica", 14, "bold"), selectmode=tk.MULTIPLE)

courses_listbox.insert(tk.END, "The Courses Display")

saved_courses_listbox = tk.Listbox(window, height=10, width=40, font=("Helvetica", 14, "bold"))

saved_courses_listbox.insert(tk.END, "The Saved Courses Display")

button_frame = tk.Frame(window)

display_button.pack(pady=5)
clear_button.pack(pady=5)
save_button.pack(pady=5)
saved_courses_listbox.pack(side='left', padx=10)
courses_listbox.pack(side='left', padx=10)


button_frame.pack()

window.mainloop()
