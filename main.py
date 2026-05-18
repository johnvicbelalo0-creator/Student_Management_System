import tkinter as tk

root = tk.Tk()
root.geometry('500x600')
root.title('Student Management System')

bg_color = '#273b7a'

login_student_icon = tk.PhotoImage(file='Img/login_student_img.png')
login_admin_icon = tk.PhotoImage(file='Img/admin_img.png')
add_student_icon = tk.PhotoImage(file='Img/add_student_img.png')

welcome_page_fm = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)

heading_lb = tk.Label(welcome_page_fm, text= 'Welcome To \nStudent Management System', bg=bg_color, fg='white', font=('Bold', 18))
heading_lb.place(x=0, y=0, width=400) 

# ---Student Login Button---
student_login_btn = tk.Button(welcome_page_fm, text='Login Student', bg=bg_color, fg='white', font=('Bold', 15), bd=0)
student_login_btn.place(x=120, y=125, width=200)

student_login_img = tk.Button(welcome_page_fm, image=login_student_icon, bd=0)
student_login_img.place(x=60, y=100)


# ---Admin Login Button---
admin_login_btn = tk.Button(welcome_page_fm, text='Login Admin', bg=bg_color, fg='white', font=('Bold', 15), bd=0)
admin_login_btn.place(x=120, y=225, width=200)

admin_login_img = tk.Button(welcome_page_fm, image=login_admin_icon, bd=0)
admin_login_img.place(x=60, y=200)

welcome_page_fm.pack(pady=30)
welcome_page_fm.pack_propagate(False)
welcome_page_fm.configure(width=400, height=420)


root.mainloop()
