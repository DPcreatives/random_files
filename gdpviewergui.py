import tkinter as tk

class GDPviewer(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
      
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames={}
        DIFFFRAMES=(StartPage,DevPage)
        for F in DIFFFRAMES:
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")

            

        self.show_frame(StartPage)


    def show_frame(self,count):
        frame=self.frames[count]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        label=tk.Label(self,text="Welcome Page")
        label.pack()
        button=tk.Button(self,text="DevPage",command=lambda :controller.show_frame(DevPage))
        button.pack()
class DevPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)


        label=tk.Label(self,text="developer of this page is Divyanshu Parihar")
        label.pack()

app=GDPviewer()
app.mainloop()