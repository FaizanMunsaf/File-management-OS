import tkinter
import tkinter.ttk
import os
import tkinter.messagebox as tsmg
import tkinter.simpledialog as inpmsg
from tkinter import filedialog as fd
from pathlib import Path


def create_widgets_in_first_frame():
    # Create the label for the frame
    first_window_label = tkinter.ttk.Label(first_frame, text='Folder Management', font="Arial 20 bold")
    first_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=tkinter.N)

    # Create the button for the frame
    first_window_folder_button = tkinter.Button(first_frame, text="Move on for folder management --> ",
                                                command=call_second_frame_on_top)
    first_window_folder_button.grid(column=0, row=1, pady=10, sticky=tkinter.N)

    first_window_label1 = tkinter.ttk.Label(first_frame, text='File Management', font="Arial 20 bold")
    first_window_label1.grid(column=0, row=2, pady=10, padx=10, sticky=tkinter.N)

    first_window_file_button = tkinter.Button(first_frame, text="Move on for folder management --> ",
                                              command=call_third_frame_on_top)
    first_window_file_button.grid(column=0, row=3, pady=10, sticky=tkinter.N)

    first_window_lable2 = tkinter.ttk.Label(first_frame, text="Folder priority", font="Arial 20 bold ")
    first_window_lable2.grid(column=0, row=4, pady=10, padx=10, sticky=tkinter.N)

    first_window_priority_button = tkinter.Button(first_frame, text="Move on for folder management --> ",
                                                  command=call_fourth_frame_on_top)
    first_window_priority_button.grid(column=0, row=5, pady=10, sticky=tkinter.N)

    first_window_quit_button = tkinter.Button(first_frame, text="Quit ", command=quit_program)
    first_window_quit_button.grid(column=0, row=6, padx=20, pady=10, sticky=tkinter.W)


def create_widgets_in_second_frame():
    # Create the label for the frame
    second_window_label = tkinter.ttk.Label(second_frame, text='Folder Management', font="Arial 20 bold")
    second_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=tkinter.N)

    # Create the button for the frame
    second_window_next_button = tkinter.Button(second_frame, text="Creation", command=create_folder)
    second_window_next_button.grid(column=0, row=1, pady=10, sticky=tkinter.N)

    second_window_next_button = tkinter.Button(second_frame, text="Deletion", command=Delete_folder)
    second_window_next_button.grid(column=0, row=2, pady=10, sticky=tkinter.N)

    second_window_next_button = tkinter.Button(second_frame, text="Updation", command=Rename_folder)
    second_window_next_button.grid(column=0, row=3, pady=10, sticky=tkinter.N)

    second_window_back_button = tkinter.Button(second_frame, text="Back", command=call_first_frame_on_top)
    second_window_back_button.grid(column=0, row=4, pady=10, sticky=tkinter.W)

    second_window_quit_button = tkinter.Button(second_frame, text="Quit", command=quit_program)
    second_window_quit_button.grid(column=0, row=4, pady=10, sticky=tkinter.E)


def create_widgets_in_third_frame():
    # Create the label for the frame
    third_window_label = tkinter.ttk.Label(third_frame, text='File Management', font="Arial 20 bold")
    third_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=tkinter.N)

    # Create the button for the frame
    third_window_next_button = tkinter.Button(third_frame, text="Creation", command=create_file)
    third_window_next_button.grid(column=0, row=1, pady=10, sticky=tkinter.N)

    third_window_next_button = tkinter.Button(third_frame, text="Deletion", command=Delete_file)
    third_window_next_button.grid(column=0, row=2, pady=10, sticky=tkinter.N)

    third_window_next_button = tkinter.Button(third_frame, text="Updation", command=Rename_file)
    third_window_next_button.grid(column=0, row=3, pady=10, sticky=tkinter.N)

    third_window_back_button = tkinter.Button(third_frame, text="Back", command=call_first_frame_on_top)
    third_window_back_button.grid(column=0, row=4, pady=10, sticky=tkinter.W)

    third_window_quit_button = tkinter.Button(third_frame, text="Quit", command=quit_program)
    third_window_quit_button.grid(column=0, row=4, pady=10, sticky=tkinter.E)


def create_widgets_in_fourth_frame():
    # Create the label for the frame
    third_window_label = tkinter.ttk.Label(fourth_frame, text='File Priority Updation', font="Arial 20 bold")
    third_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=tkinter.N)

    # Create the Button for the frame
    fourth_window_next_button = tkinter.Button(fourth_frame, text="Update priority", command=priority_algo)
    fourth_window_next_button.grid(column=0, row=1, pady=10, sticky=tkinter.N)

    third_window_quit_button = tkinter.Button(fourth_frame, text="Quit", command=quit_program)
    third_window_quit_button.grid(column=0, row=4, pady=10, sticky=tkinter.E)

    third_window_back_button = tkinter.Button(fourth_frame, text="Back", command=call_first_frame_on_top)
    third_window_back_button.grid(column=0, row=4, pady=10, sticky=tkinter.W)


def call_first_frame_on_top():
    # This function can be called only from the second window.
    # Hide the second window and show the first window.
    second_frame.grid_forget()
    third_frame.grid_forget()
    fourth_frame.grid_forget()
    first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


def call_second_frame_on_top():
    # This function can be called from the first and third windows.
    # Hide the first and third windows and show the second window.
    first_frame.grid_forget()
    second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


def call_third_frame_on_top():
    # This function can only be called from the second window.
    # Hide the second window and show the third window.
    first_frame.grid_forget()
    third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


def call_fourth_frame_on_top():
    first_frame.grid_forget()
    fourth_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


def create_folder():
    directory = inpmsg.askstring("Input", "Enter your Folder name", parent=second_frame)
    parent_dir = "C:\\Users\\Faizan Munsaf\\OneDrive\\Desktop\\Os project\\"

    mode = 0o666

    path = os.path.join(parent_dir, directory)

    os.mkdir(path, mode)

    tsmg.showinfo("Folder Creation process", "Folder create  success fully")


def Delete_folder():
    path = fd.askdirectory()

    os.rmdir(path)

    tsmg.showerror("Folder Deletion process", "Folder Deletion  success fully")


def Rename_folder():
    try:
        location = "C:\\Users\\Faizan Munsaf\\OneDrive\\Desktop\\Os project\\"
        old_name = fd.askdirectory()
        old_1 = Path(old_name).stem
        old = os.path.join(location, old_1)
        new_name = inpmsg.askstring("Input", "Enter your Rename Folder name", parent=second_frame)
        new = os.path.join(location, new_name)

        os.renames(old, new)
        tsmg.showwarning("Folder Rename process", "Folder Rename  success fully")
    except:
        tsmg.showerror("Folder Processing", "There is an Folder error")


def create_file():
    try:
        select_path = fd.askdirectory()
        file = inpmsg.askstring("Input", "Enter your Creation File name", parent=third_frame)
        f = open(os.path.join(select_path, file), "w")
        f.close()
        tsmg.showinfo("File Creation process", "File create  success fully")
    except:
        tsmg.showerror("file processing", "There is an error")


def Delete_file():
    try:
        path = fd.askopenfilename()
        if os.path.exists(path):
            os.remove(path)
        else:
            tsmg.showerror("File error", "File Doesn't exist")

        tsmg.showerror("File Deletion process", "File Deletion  success fully")
    except:
        tsmg.showerror("File Deletion process", "There is an error")


def Rename_file():
    try:
        location = "C:\\Users\\Faizan Munsaf\\OneDrive\\Desktop\\Os project\\"
        tsmg.showwarning("Folder process", "Please choose your folder")
        old_name = fd.askdirectory()
        old_1 = Path(old_name).stem
        old_1_1 = os.path.join(location, old_1)
        tsmg.showwarning("File process", "Please choose your file")
        old_file = fd.askopenfilename()
        old_file_1 = Path(old_file).name
        old = os.path.join(old_1_1, old_file_1)
        new_name = inpmsg.askstring("Input", "Enter your Rename Folder name", parent=second_frame)
        new = os.path.join(old_1_1, new_name)
        os.renames(old, new)

        tsmg.showwarning("File rename process", "File update  success fully")
    except:
        tsmg.showerror("File processing", "FIle renaming error")


def priority_algo():
    try:
        location = "C:\\Users\\Faizan Munsaf\\OneDrive\\Desktop\\Os project\\"
        path1 = fd.askdirectory()
        path = fd.askdirectory()
        count1 = count = 0
        inc = 0
        for f1 in os.listdir(path1):
            if os.path.isfile(os.path.join(path1, f1)):
                count1 += 1

        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                count += 1
        print(f"{Path(path).stem} : {count} "
              f"\n{Path(path1).stem} : {count1}")
        if count >= count1:
            old_name = Path(path).stem
            old = os.path.join(location, old_name)
            inc += 1
            new_name = str(inc)
            new = os.path.join(location, new_name)

            os.renames(old, new)

            old_name1 = Path(path1).stem
            old1 = os.path.join(location, old_name1)
            inc += 1
            new_name1 = str(inc)
            new1 = os.path.join(location, new_name1)

            os.renames(old1, new1)
            tsmg.showwarning("Folder Rename process", "Folder Rename  success fully \n Now it's priority is High")

        else:
            old_name1 = Path(path1).stem
            old1 = os.path.join(location, old_name1)
            inc += 1
            new_name1 = str(inc)
            new1 = os.path.join(location, new_name1)

            os.renames(old1, new1)

            old_name = Path(path).stem
            old = os.path.join(location, old_name)
            inc += 1
            new_name = str(inc)
            new = os.path.join(location, new_name)

            os.renames(old, new)
            tsmg.showwarning("Folder Rename process", "Folder Rename  success fully \n Now Folder priority is change")
    except:
        tsmg.showerror("Folder Rename process", "There is any where else")


def quit_program():
    root_window.destroy()


###############################
# Main program starts here :) #
###############################

# Create the root GUI window.
root_window = tkinter.Tk()

root_window.geometry("625x665")
root_window.title(" Project Code")

# Define window size
window_width = 200
window_heigth = 100

# Create frames inside the root window to hold other GUI elements. All frames must be created in the main program,
# otherwise they are not accessible in functions.
first_frame = tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
first_frame['borderwidth'] = 150
first_frame['relief'] = 'sunken'
first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E, tkinter.S))

second_frame = tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
second_frame['borderwidth'] = 150
second_frame['relief'] = 'sunken'
second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E, tkinter.S))

third_frame = tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
third_frame['borderwidth'] = 150
third_frame['relief'] = 'sunken'
third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

fourth_frame = tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
fourth_frame['borderwidth'] = 150
fourth_frame['relief'] = 'sunken'
fourth_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# Create all widgets to all frames
create_widgets_in_fourth_frame()
create_widgets_in_third_frame()
create_widgets_in_second_frame()
create_widgets_in_first_frame()

# Hide all frames in reverse order, but leave first frame visible (unhidden).
fourth_frame.grid_forget()
third_frame.grid_forget()
second_frame.grid_forget()

# Start tkinter event - loop
root_window.mainloop()
