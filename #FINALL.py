#FINALL
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import time
import serial 
import time
import csv

try:
    arduino = serial.Serial('COM5', 9600, timeout=5) 
    time.sleep(2)  
except:
    messagebox.showerror("Arduino Error", "Failed to connect to Arduino. Check the COM port and connection.")
    arduino = None

start_time = None
is_timing = False
csv_file = 'study_sessions.csv'  

app = tk.Tk()
app.title("OCTO-TRACKER")
app.attributes('-fullscreen', True)
app.config(bg="black")  

def exit_fullscreen(event):
    app.attributes('-fullscreen', False)

app.bind('<Escape>', exit_fullscreen)

container = tk.Frame(app, bg="black")
container.pack(expand=True)

moods_data = []

def show_home_page():
    for widget in container.winfo_children():
        widget.destroy()

    title_label = tk.Label(container, text="OCTO-TRACKER", font=("Arial", 48), fg="white", bg="black")
    title_label.pack(pady=30)

    icon_label = tk.Label(container, bg="black")
    icon_label.pack(pady=20)

    warning_label = tk.Label(container, text="⚠️ Make sure the OCTO-TRACKER is connected to the laptop before you start the study session.",
                             bg="#444", fg="orange", font=("Arial", 14), padx=10, pady=10)
    warning_label.pack(pady=10, fill="x")

    study_button = tk.Button(container, text="STUDY", font=("Arial", 20), width=25, height=2, bg="gray", fg="black", command=show_study_input)
    study_button.pack(pady=10)

    dashboard_button = tk.Button(container, text="DASHBOARD", font=("Arial", 20), width=25, height=2, bg="gray", fg="black", command=show_dashboard)
    dashboard_button.pack(pady=10)

    assignment_button = tk.Button(container, text="ASSIGNMENT DEADLINES", font=("Arial", 20), width=25, height=2, bg="gray", fg="black", command=show_assignment_deadlines)
    assignment_button.pack(pady=10)

    exit_button = tk.Button(container, text="EXIT", command=app.destroy, bg="red", fg="white", font=("Arial", 16), width=25, height=2)
    exit_button.pack(pady=10)
    
    
def show_study_input():
    for widget in container.winfo_children():
        widget.destroy()

    title_label = tk.Label(container, text="STUDY", font=("Arial", 36), fg="orange", bg="black")
    title_label.pack(pady=20)

    instructions_frame = tk.Frame(container, bg="gray", padx=10, pady=10, highlightbackground="orange", highlightthickness=2)
    instructions_frame.pack(pady=10)

    instructions_text = (
        "Make sure the **BREAK** side of the **OCTO-TRACKER** is facing up before starting the study session.\n\n"
        "Flip the **OCTO-TRACKER** to the appropriate side to choose the subject and start the study session.\n\n"
        "Flip the **OCTO-TRACKER** to the **BREAK** side to end the current session."
    )
    instruction_label = tk.Label(instructions_frame, text=instructions_text, fg="black", bg="gray", font=("Arial", 14), justify='left', wraplength=600)
    instruction_label.pack()

    timer_label = tk.Label(container, text="00:00", font=("Arial", 48), fg="orange", bg="black")
    timer_label.pack(pady=40)

    arduino_label = tk.Label(container, text="Arduino Data: --", font=("Arial", 18), fg="white", bg="black")
    arduino_label.pack(pady=10)

    def start_study_session():
        global start_time, is_timing, study_line     
        

        is_timing = False

        def update_timer_and_arduino():
            global is_timing, start_time, study_line, has_saved  

            if not hasattr(update_timer_and_arduino, "has_saved"):
             update_timer_and_arduino.has_saved = False  

            current_time = time.time()
 

            if is_timing and start_time is not None:
                elapsed_time = current_time - start_time  
                hours = int(elapsed_time // 3600)
                minutes = int((elapsed_time % 3600) // 60)
                seconds = int(elapsed_time % 60)

                timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

            if arduino and arduino.in_waiting > 0:
                arduino_data = arduino.readline().decode().strip()
                if arduino_data:
                    print(f"Received data: {arduino_data}")  
                    arduino_label.config(text=f"Arduino Data: {arduino_data}")

                    if arduino_data == "Challenge 1": 
                        if not is_timing:
                            study_line = "Challenge 1"
                            start_time = current_time 
                            is_timing = True                          
                            
                    if arduino_data == "DBW": 
                        if not is_timing:
                            study_line = "DBW"
                            start_time = current_time 
                            is_timing = True
                          
                    if arduino_data == "PBR": 
                         if not is_timing:
                             study_line = "PBR"
                             start_time = current_time 
                             is_timing = True                       

                    if arduino_data == "PPI": 
                         if not is_timing:
                             study_line = "PPI"
                             start_time = current_time 
                             is_timing = True
                            
                    if arduino_data == "SE": 
                         if not is_timing:
                             study_line = "SE"
                             start_time = current_time 
                             is_timing = True
                        
                            
                    if arduino_data == "DT": 
                         if not is_timing:
                             study_line = "DT"
                             start_time = current_time 
                             is_timing = True

                    if arduino_data == "Break":  
                        if is_timing and start_time is not None:
                            end_time = current_time
                            elapsed_time = end_time - start_time  
                            is_timing = False

                            mood = show_mood_tracker()
                            # salvev timpul într-un fișier CSV
                            with open(csv_file, 'a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow([study_line, task_completion,
                                                 mood,
                                                time.strftime("%Y-%m-%d", time.localtime(start_time)),
                                                time.strftime("%H:%M:%S", time.localtime(start_time)),
                                                time.strftime("%Y-%m-%d", time.localtime(end_time)),
                                                time.strftime("%H:%M:%S", time.localtime(end_time)), 
                                                elapsed_time / 60], )
                            return 

            
            app.after(100, update_timer_and_arduino)

      
        update_timer_and_arduino()


    start_study_session()

    back_button = tk.Button(container, text="Back", command=show_home_page, bg="gray", fg="black", font=("Arial", 16), width=25, height=2)
    back_button.pack(pady=10)

    start_button = tk.Button(
        container,
        text="Start Study Session",
        command=start_study_session,
        bg="gray",
        fg="black",
        font=("Arial", 16),
        width=25,
        height=2
    )
    start_button.pack(pady=10)

 
    ###
    # back_button = tk.Button(
    #     container,
    #     text="Back",
    #     command=show_home_page,
    #     bg="gray",
    #     fg="black",
    #     font=("Arial", 16),
    #     width=25,
    #     height=2
    # )
    # back_button.pack(pady=10)
    
def show_task_completion():
    task_window = tk.Toplevel(container)
    task_window.title("Task completion")

    task_window.geometry("300x150+{}+{}".format(int(app.winfo_screenwidth() / 2 - 200), int(app.winfo_screenheight() / 2 + 200)))

    task_label = tk.Label(task_window, text="Did you complete your task?", font=("Arial", 14))
    task_label.pack(pady=10)

    def save_task_completion(value):
        global task_completion
        task_completion = value  
        print("Task completion:", "Yes" if value == 1 else "No")
        task_window.destroy()  

        show_study_input() 

    yes_button = tk.Button(task_window, text="Yes", command=lambda: save_task_completion(1), font=("Arial", 12), bg="green", fg="white", width=10)
    no_button = tk.Button(task_window, text="No", command=lambda: save_task_completion(0), font=("Arial", 12), bg="red", fg="white", width=10)

    yes_button.pack(side="left", padx=20, pady=10)
    no_button.pack(side="right", padx=20, pady=10)

def show_back_button():
    """Display a 'Back' button in the main container to return to the Study page."""
    back_button = tk.Button(
        container,
        text="Back to study",
        command=show_study_input,
        bg="gray",
        fg="black",
        font=("Arial", 16),
        width=25,
        height=2
    )
    back_button.pack(pady=10)


def show_mood_tracker():
    for widget in container.winfo_children():
        widget.destroy()

    top_frame = tk.Frame(container, bg="black")
    top_frame.grid(row=0, column=0, pady=(50, 20), sticky="n")  

    mood_label = tk.Label(top_frame, text="MOOD TRACKER", font=("Arial", 36), fg="orange", bg="black")
    mood_label.pack(anchor="n", pady=(30, 5))

    subtitle_label = tk.Label(top_frame, text="How satisfied do you feel after your study session today?", font=("Arial", 16), fg="white", bg="black")
    subtitle_label.pack(anchor="n", pady=(25, 10))


    window = tk.Toplevel(container)
    window.title("Enter Mood")

    window.geometry("500x450+{}+{}".format(int(app.winfo_screenwidth() / 2 - 250), int(app.winfo_screenheight() / 2 - 175))) 
       
    instructions_text = (
        "Please select a number from 1 to 7 to indicate your satisfaction level:\n"
        "1. Exhausted - Completely brunt out by the session."
        "2. Frustrated - Upset due to difficulties encountered or lack of productivity.\n"
        "3. Disappointed - Unsatisfied with the progress, feeling like more could have been done.\n"
        "4. Neutral - The session was average with no strong feelings.\n"
        "5. Satisfied - Content with the effort and results, feeling productive.\n"
        "6. Confident - Satisfied with the progress  and confident in understanding.\n"
        "7. Energized - Feeling highly accomplished and motivated, ready for more."
       
    )
    instructions_label = tk.Label(window, text=instructions_text, font=("Arial", 12), justify="left", wraplength=450)
    instructions_label.pack(pady=10)

    entry_label = tk.Label(window, text="Enter your satisfaction level (1-7):", font=("Arial", 14))
    entry_label.pack(pady=10)
    def validate_input(value):
      return value == "" or (value.isdigit() and 1 <= int(value) <= 7)

    validate_cmd = window.register(validate_input)
    mood_entry = tk.Entry(window, validate="key", validatecommand=(validate_cmd, "%P"))
    mood_entry.pack(pady=10)

    def save_mood():
        global mood_data
        mood_data = mood_entry.get()
        print("Mood data saved:", mood_data)
        window.destroy()
        show_task_completion()  

    save_button = tk.Button(window, text="Save Mood", command=save_mood)
    save_button.pack(pady=10)

    back_button = tk.Button(window, text="Back", command=lambda: [window.destroy(), show_study_input()], bg="gray", fg="black", font=("Arial", 12), width=10)
    back_button.pack(pady=10)

    window.mainloop()
    return mood_data


    
def show_dashboard():
    for widget in container.winfo_children():
        widget.destroy()

    title_label = tk.Label(container, text="DASHBOARD", font=("Arial", 36), fg="orange", bg="black")
    title_label.pack(pady=30)

    placeholder_label = tk.Label(container, text="Dashboard details", font=("Arial", 16), fg="white", bg="black")
    placeholder_label.pack(pady=10)

    image_frame = tk.Frame(container, bg="black")
    image_frame.pack(pady=20)

    try:
        img1 = Image.open(r'C:/Users/Windows 11 ENG/Downloads/updated_visualization_with_fixed_duration_labels.jpg')

        img1 = img1.resize((1200, 700), Image.Resampling.LANCZOS)

        tk_img1 = ImageTk.PhotoImage(img1)

        img_label1 = tk.Label(image_frame, image=tk_img1, bg="black")
        img_label1.image = tk_img1  
        img_label1.pack()

    except Exception as e:
        error_label = tk.Label(image_frame, text=f"Error loading image: {str(e)}", font=("Arial", 14), fg="red", bg="black")
        error_label.pack()

    back_button = tk.Button(container, text="Back", command=show_home_page, bg="gray", fg="black", font=("Arial", 16), width=25, height=2)
    back_button.pack(pady=10)





import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
saved_assignments = []

def show_assignment_deadlines():
    for widget in container.winfo_children():
        widget.destroy()
    
    deadlines_label = tk.Label(container, text="ASSIGNMENT DEADLINES", font=("Arial", 36), fg="orange", bg="black")
    deadlines_label.pack(pady=20)

    table_frame = tk.Frame(container, bg="black")
    table_frame.pack(pady=10)

    tk.Label(table_frame, text="Course", font=("Arial", 16), fg="white", bg="black").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(table_frame, text="Assignment Description", font=("Arial", 16), fg="white", bg="black").grid(row=0, column=1, padx=10, pady=10)
    tk.Label(table_frame, text="Due Date", font=("Arial", 16), fg="white", bg="black").grid(row=0, column=2, padx=10, pady=10)
    tk.Label(table_frame, text="Status", font=("Arial", 16), fg="white", bg="black").grid(row=0, column=3, padx=10, pady=10)

    course_vars = []
    due_date_entries = []
    status_labels = []

    def update_status(due_date_entry, status_label):
        today = datetime.today()
        due_date_str = due_date_entry.get()
        try:
            due_date = datetime.strptime(due_date_str, "%d-%m-%Y")
            days_left = (due_date - today).days
            status_text = f"{days_left} days left" if days_left >= 0 else "Overdue"
            status_label.config(text=status_text)
        except ValueError:
            status_label.config(text="Invalid Date")

    def add_row(course_value="Select Course", due_date_value="", status_value="Not started"):
        row = len(course_vars) + 1

        course_var = tk.StringVar()
        course_var.set(course_value)  
        course_options = ['PBR1', 'DBW', 'Challenge1', 'PPI', 'DT']
        course_dropdown = tk.OptionMenu(table_frame, course_var, *course_options)
        course_dropdown.config(font=("Arial", 14), bg="gray", fg="black")
        course_dropdown.grid(row=row, column=0, padx=10, pady=10)
        course_vars.append(course_var)

        description_entry = tk.Entry(table_frame, font=("Arial", 14), width=20)
        description_entry.grid(row=row, column=1, padx=10, pady=10)

        due_date_entry = DateEntry(table_frame, font=("Arial", 14), width=15, bg="gray", fg="black", date_pattern="dd-MM-yyyy")
        if due_date_value:
            due_date_entry.set_date(due_date_value)  
        due_date_entry.grid(row=row, column=2, padx=10, pady=10) 
        due_date_entries.append(due_date_entry)

        status_label = tk.Label(table_frame, text=status_value, font=("Arial", 14), fg="gray", bg="black")
        status_label.grid(row=row, column=3, padx=10, pady=10)  
        status_labels.append(status_label)

        update_status(due_date_entry, status_label)

        due_date_entry.bind("<<DateEntrySelected>>", lambda e: update_status(due_date_entry, status_label))

    add_row_button = tk.Button(container, text="Add Assignment", font=("Arial", 16), bg="gray", fg="black", command=add_row)
    add_row_button.pack(pady=20)

    def save_assignments():
        global saved_assignments
        saved_assignments = []  
        for i in range(len(course_vars)):
            course = course_vars[i].get()
            due_date = due_date_entries[i].get()
            description = table_frame.grid_slaves(row=i+1, column=1)[0].get() 
            status = status_labels[i].cget("text")
            if course == "Select Course" or not due_date or not description:
                messagebox.showwarning("Incomplete Data", f"Please complete all fields for row {i + 1}")
                return
            saved_assignments.append((course, description, due_date, status)) 

        messagebox.showinfo("Saved", "Assignments saved successfully!")

    def load_saved_assignments():
        for assignment in saved_assignments:
            course_value, description_value, due_date_value, status_value = assignment
            add_row(course_value, due_date_value, status_value)
            description_entry = table_frame.grid_slaves(row=len(course_vars), column=1)[-1]  
            description_entry.insert(0, description_value)

    save_button = tk.Button(container, text="Save Assignments", font=("Arial", 16), bg="orange", fg="black", command=save_assignments)
    save_button.pack(pady=20)

    back_button = tk.Button(container, text="Back", command=show_home_page, bg="gray", fg="black", font=("Arial", 16), width=25, height=2)
    back_button.pack(pady=10)

    load_saved_assignments()





 
show_home_page()
app.mainloop()

