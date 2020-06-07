from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as tkFont

class Window2:
    def __init__ (self, master):

        self.zenith_logo_render = PhotoImage(file='IMAGES/LogoZ.png')
        self.zenith_label_render = PhotoImage(file='IMAGES/zenith-faixa.png')

        self.master = master
        self.master.geometry("765x575")
        self.master.title("Report Maker")
        self.master.iconphoto(False, self.zenith_logo_render)
        self.master.config(bg="black")

        fontStyle = tkFont.Font(
                        family="Helvetica", 
                        size=10, 
                        weight="bold")

        Conteiner1 = Frame(self.master)
        Conteiner (Conteiner1, self.master)
        ButtonFinish = Button(
                            self.master, 
                            text="Finish", 
                            bg="black", 
                            fg="white", 
                            width=7, 
                            padx=5, 
                            font=fontStyle,
                            command= self.PyLaTex_function)
        ZenithLabel = Label(
                            self.master, 
                            image= self.zenith_label_render, 
                            highlightthickness=0, 
                            borderwidth=0)

        ZenithLabel.grid(
                        row=0, 
                        column=0, 
                        columnspan=2, 
                        padx=0, 
                        pady=0)
        Conteiner1.grid(
                        row=1, 
                        column=0, 
                        columnspan=2, 
                        padx=20, 
                        pady=10)
        ButtonFinish.grid(
                        row=2, 
                        column=1, 
                        sticky=E, 
                        padx=20)
    def PyLaTex_function ():
        txt = TextArea.get('1.0', END)

class Conteiner:
    def __init__ (self, conteiner, master):

        TextArea = Text(
                        conteiner, 
                        width=88, 
                        height=25)
        ScrollBar = Scrollbar(
                        conteiner, 
                        orient=VERTICAL)

        ScrollBar.config(command=TextArea.yview)
        TextArea.config(yscrollcommand=ScrollBar.set)
        TextArea.insert(INSERT, "%insert a LaTex code")
        ScrolledText(master)

        ScrollBar.grid(
                    row=0, 
                    column=1,
                    ipady=176.45, 
                    sticky=W)
        TextArea.grid(
                    row=0, 
                    column=0, 
                    sticky=E)
        
root = Tk()
window2 = Window2(root)
root.mainloop()
