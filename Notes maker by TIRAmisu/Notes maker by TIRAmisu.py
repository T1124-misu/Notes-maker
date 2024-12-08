from customtkinter import *
from tkinter import messagebox
import time
import os

class app:
    def __init__(self):
        #====================== WINDOW GEOMETRY 
        self.root = CTk() 
        self.root.title("Schedule management app") 
        self.root.geometry("1280x720") 
        #======================
        
        #====================== NON-FRAME
        self.ppp = CTkLabel(
            self.root,
            text="",
            font=("times new roman", 30)
        ).pack(padx=5, pady=5)
        self.title = CTkLabel(
            self.root,
            text="Schedule creator and loader",
            font=("times new roman", 30)
        ).pack(padx=5, pady=5)
        self.frame1 = CTkScrollableFrame(
            self.root,
            fg_color="#fff100",
            border_color="#fff100",
            border_width=3,
            width=300,
            height=550,
            scrollbar_button_color="#fff100",
            scrollbar_button_hover_color="#fff100"
        )
        self.frame1.place(x=50,y=100)
        self.frame2 = CTkFrame(
            self.root,
            fg_color="#133e87",
            border_color="#133e87",
            border_width=3,
            width=800,
            height=10
        )
        self.frame2.place(x=400,y=100)
        self.frame3 = CTkFrame(
            self.root,
            fg_color="#ffffff",
            border_color="#ffffff",
            border_width=3,
            width=8000,
            height=350
        )
        self.frame3.place(x=400,y=200)
        self.cred = CTkLabel(
            self.root,
            text="© T.I.R.A.misu",
            font=("times new roman", 15)
        ).place(x=50,y=680)
        self.dayvalue = None
        #======================
        
        #====================== FRAME1 GROUP 
        self.selectday = CTkLabel(
            self.frame1,
            text="Select day",
            font=("times new roman", 20),
            text_color="#000000"
        ).pack(padx=5, pady=5)
        self.daybox = CTkComboBox(
            self.frame1,
            values=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            corner_radius=16,
            border_color="#121212",
            border_width=3,
            command=self.combo_box_value,
            fg_color="#121212"
        )
        self.daybox.pack(padx=5, pady=5)
        self.selectdate = CTkLabel(
            self.frame1,
            text="Input date",
            font=("times new roman", 20),
            text_color="#000000"
        ).pack(padx=5, pady=5)
        self.date = CTkEntry(
            self.frame1,
            placeholder_text="Date format must be in = dd-mm-yyyy",
            placeholder_text_color="grey",
            width=300,
            corner_radius=16,
            border_color="#121212",
            border_width=3,
            fg_color="#121212"
        )
        self.date.pack(padx=5, pady=5)
        self.addnote = CTkLabel(
            self.frame1,
            text="Add note",
            font=("times new roman", 20),
            text_color="#000000"
        ).pack(padx=5, pady=5)
        self.txtb = CTkTextbox(
            self.frame1,
            scrollbar_button_color="#121212",
            scrollbar_button_hover_color="#000000",
            corner_radius=16,
            width=300,
            height=300,
            border_color="#121212",
            border_width=3,
            fg_color="#121212"
        )
        self.txtb.pack(padx=5, pady=5)
        self.addbutton = CTkButton(
            self.frame1,
            text="Add note to archive",
            font=("times new roman", 15),
            corner_radius=16,
            border_color="#121212",
            border_width=3,
            fg_color="#121212",
            hover_color="#000000",
            command=self.add_note  # Link the button to the add_note method
        ).pack(padx=5, pady=5)
        #======================
        
        #====================== FRAME2 GROUP
        self.idk = CTkLabel(
            self.frame2,
            text="Open notes",
            font=("times new roman", 20),
            text_color="#ffffff"
        ).pack(anchor="w", padx=5, pady=5)
        self.opbar = CTkEntry(
            self.frame2,
            placeholder_text="Input the date you want to see (dd-mm-yyyy)",
            placeholder_text_color="grey",
            width=710,
            corner_radius=16,
            border_color="#121212",
            border_width=3,
            fg_color="#121212"
        )
        self.opbar.pack(side="left", padx=5, pady=5)
        self.opbtn = CTkButton(
            self.frame2,
            text="Open",
            font=("times new roman", 15),
            corner_radius=16,
            border_color="#121212",
            border_width=3,
            fg_color="#121212",
            hover_color="#000000",
            width=50,
            command=self.open_note  # Link the button to the open_note method
        )
        self.opbtn.pack(side="right", padx=5, pady=5)
        #======================
        
        #====================== FRAME3 GROUP
        self.note_display = CTkTextbox(
            self.frame3,
            height=460,
            width=780,
            corner_radius=16,
            border_color="#ffffff",
            border_width=3,
            fg_color="#ffffff",
            text_color="#121212",
            font=("times new roman",20),
            scrollbar_button_color="#ffffff",
            scrollbar_button_hover_color="#121212"
        )
        self.note_display.pack(padx=5, pady=5)
        #====================== FRAME3
        
        #====================== WINDOW LOOP
        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.on_closing
        )
        self.root.mainloop()
    def combo_box_value(self, value):
        self.dayvalue = value
    def add_note(self):
        if self.dayvalue is None:
            messagebox.showerror("Input Error", "Please select a day.")
            return
        day = self.dayvalue
        note = self.txtb.get("1.0", "end-1c")  
        date_input = self.date.get()  
        if not date_input:
            messagebox.showerror("Input Error", "Please enter a valid date.")
            return
        try:
            day, month, year = map(int, date_input.split('-'))
            time.strptime(date_input, "%d-%m-%Y")  
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in dd-mm-yyyy format.")
            return
        custom_path = "E:\\Note archives"  
        if not os.path.exists(custom_path):
            os.makedirs(custom_path)
        file_name = f"{custom_path}/{date_input}.txt"
        try:
            with open(file_name, "w") as file:
                file.write(f"Date: {date_input}\n")
                file.write(f"Day: {day}\n")
                file.write(f"Note: {note}\n")
            messagebox.showinfo("Success", f"Note added to {file_name}")
            self.clear_fields()  
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file: {e}")
    def clear_fields(self):
        self.date.delete(0, "end")
        self.txtb.delete("1.0", "end")
        self.daybox.set("")
    def open_note(self):
        date_input = self.opbar.get()
        if not date_input:
            messagebox.showerror("Input Error", "Please enter a valid date to open.")
            return
        try:
            day, month, year = map(int, date_input.split('-'))
            time.strptime(date_input, "%d-%m-%Y")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in dd-mm-yyyy format.")
            return
        custom_path = "E:\\Note archives"  
        file_name = f"{custom_path}/{date_input}.txt"
        if not os.path.exists(file_name):
            messagebox.showerror("File Not Found", f"No note found for {date_input}.")
            return
        try:
            with open(file_name, "r") as file:
                content = file.read()
                lines = content.split("\n")
                day_name = None
                for line in lines:
                    if line.startswith("Day:"):
                        day_name = line.split(":")[1].strip()
                if day_name:
                    content = content.replace(f"Day: {day_name}", f"Day: {day_name}")
                self.note_display.delete("1.0", "end")  
                self.note_display.insert("1.0", content) 
                self.note_display.update()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while opening the file: {e}")
    def on_closing(self):
        if messagebox.askyesno(title="=^._.^= Quit confirmation", message="Quit now ?????"):
            self.root.destroy()
            messagebox.showinfo("=^._.^= Thanks for using this program", "Have a nice day")
app()

