from tkinter import*

root=Tk()
root.geometry("600x600")
root.title("Cardiac diseases")

q1radbtnvar=StringVar(value="0")
q1label = Label(root, text="Do you experience shortage of breath in daily activities?")
q1label.pack()
q1radbtny = Radiobutton(root, text="Yes", variable=q1radbtnvar, value="yes")
q1radbtnn = Radiobutton(root, text="No", variable=q1radbtnvar, value="no")
q1radbtnn.pack()
q1radbtny.pack()

q2radbtnvar=StringVar(value="0")
q2label = Label(root, text="Do you have swelling in feet (shoes may feel tight)?")
q2label.pack()
q2radbtny = Radiobutton(root, text="Yes", variable=q2radbtnvar, value="yes")
q2radbtnn = Radiobutton(root, text="No", variable=q2radbtnvar, value="no")
q2radbtnn.pack()
q2radbtny.pack()

q3radbtnvar=StringVar(value="0")
q3label = Label(root, text="Do you feel confusion and loss of memory?")
q3label.pack()
q3radbtny = Radiobutton(root, text="Yes", variable=q3radbtnvar, value="yes")
q3radbtnn = Radiobutton(root, text="No", variable=q3radbtnvar, value="no")
q3radbtnn.pack()
q3radbtny.pack()

q4radbtnvar=StringVar(value="0")
q4label = Label(root, text="Do you experience coughing/wheezing that produces blood tinged mucus(nozee)?")
q4label.pack()
q4radbtny = Radiobutton(root, text="Yes", variable=q4radbtnvar, value="yes")
q4radbtnn = Radiobutton(root, text="No", variable=q4radbtnvar, value="no")
q4radbtnn.pack()
q4radbtny.pack()

q5radbtnvar=StringVar(value="0")
q5label = Label(root, text="Do you experience shortness of breath while resting?")
q5label.pack()
q5radbtny = Radiobutton(root, text="Yes", variable=q5radbtnvar, value="yes")
q5radbtnn = Radiobutton(root, text="No", variable=q5radbtnvar, value="no")
q5radbtnn.pack()
q5radbtny.pack()

def heart() :
    score = 0
    
    if q1radbtnvar.get()== "yes":
        score = score + 20
        print(score)
        
    if q2radbtnvar.get()== "yes":
        score = score + 20
        print(score)
    
    if q3radbtnvar.get()== "yes":
        score = score + 20
        print(score)
        
    if q4radbtnvar.get()== "yes":
        score = score + 20
        print(score)
        
    if q5radbtnvar.get()== "yes":
        score = score + 20
        print(score)
        
    if score <= 20:
        messagebox.showinfo("Update", "You don't need to see a doctor")
        
    elif score > 20 and score <= 40:
        messagebox.showinfo("Update", "You may need to see a doctor")
        
    else:
        messagebox.showinfo("Update", "You need to see a doctor")
        
btn = Button(root, text="Do i need to see a doctor",command=heart)
btn.pack()
root.mainloop()