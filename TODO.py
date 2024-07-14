import tkinter
import tkinter.messagebox

window = tkinter.Tk()

window.title("TO-DO LIST")


def task_adding():
    todo = task_add.get()
    if todo != "":
        todo_box.insert(tkinter.END, todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning !!!",message="please enter task here...!!")

def task_removing():
    try:
        index_todo = todo_box.curselection()
        todo_box.delete(index_todo[0])
    except:
        tkinter.messagebox.showwarning(title="Attention !!!",message="To Delete Task, You Must Select a Task...!!")
l2 = tkinter.Label(window, text="TO DO LIST",font=("Arial", 18, "bold"))
l2.place(x=650, y=100)

list_frame = tkinter.Frame(window)
list_frame.place(x=520,y=230)

L1 = tkinter.Label(window, text="Enter Task :")
L1.place(x=522,y=190)
task_add = tkinter.Entry(window, width=55)
task_add.place(x=600,y=190)

todo_box = tkinter.Listbox(list_frame, height=15, width=70)
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

todo_box.config(yscrollcommand=scroller.set)
# scroller.config(command=list_frame.yview)



add_btn = tkinter.Button(window, text="ADD TASK", background="skyblue", command=task_adding)
add_btn.place(x=650,y=500)

delete_btn = tkinter.Button(window, text="DELETE TASK", background="skyblue", command=task_removing)
delete_btn.place(x=750, y=500)

window.mainloop()
