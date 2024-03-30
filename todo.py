import tkinter as tk

class ToDoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("300x400")

        self.task_list = []

        self.task_entry = tk.Entry(self.master)
        self.task_entry.pack()

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_frame = tk.Frame(self.master)
        self.task_frame.pack()

    def add_task(self):
        task = self.task_entry.get()
        self.task_entry.delete(0, tk.END)

        if task:
            self.task_list.append(task)
            self.update_task_list()

    def update_task_list(self):
        # clear the task frame
        for child in self.task_frame.winfo_children():
            child.destroy()

        # add the tasks to the frame
        for task in self.task_list:
            task_frame = tk.Frame(self.task_frame)
            task_frame.pack(fill=tk.X)

            task_check = tk.Checkbutton(task_frame)
            task_check.pack(side=tk.LEFT)

            task_label = tk.Label(task_frame, text=task)
            task_label.pack(side=tk.LEFT)

            task_button = tk.Button(task_frame, text="Delete", command=lambda t=task: self.delete_task(t))
            task_button.pack(side=tk.RIGHT)

    def delete_task(self, task):
        self.task_list.remove(task)
        self.update_task_list()

root = tk.Tk()
to_do_list = ToDoList(root)
root.mainloop()
