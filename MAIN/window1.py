from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
import tkinter.font as tkFont

import statistics
from dataparser import DataParser
from widgets import StandardButton
from widgets import switch_frame
from widgets import WindowConfig
from window2 import Window2

class Window1:

    def __init__ (self, master, root):
        self.master = master
        self.root = root
        
         # Zenith's logo render
        self.zenith_label_render = PhotoImage(file='../IMAGES/zenith-faixa.png')

        # Define text fontstyle
        fontStyle = tkFont.Font(
                        family="Helvetica", 
                        size=10, 
                        weight="bold")
    
        content = Frame (master, width=450, height=650, background="black")

        # frame = ttk.Frame(content, relief="sunken", width=800, height=600)

        # Variables
        self.tokenSeparator  = StringVar(value=";")
        self.logFilename     = StringVar()
        self.cuttedFilename  = StringVar(value="<log file>")
        self.parserString    = StringVar()
        self.fieldString     = StringVar()
        self.fields_list     = StringVar()
        self.fields_list.set(('a:integer', 'b:float', 'c:str'))
        
        # Component Creation
        ZenithLabel     = Label(self.master, image= self.zenith_label_render, highlightthickness=0, borderwidth=0)

        titleBrowse     = LabelFrame     (content, bg= "Black", fg= "White", font=fontStyle, width= 340, text="1. Selecione o arquivo")
        lblBrowse       = ttk.Label      (titleBrowse, textvariable=self.cuttedFilename, background="black", foreground="white")
        btnBrowse       = StandardButton (frame= titleBrowse, text="Browse", command=self.browseLog)

        titleField      = LabelFrame     (content, bg= "Black", fg= "White", font=fontStyle, text="2. Organize a ordem dos tipos de dados")
        txtAddField     = ttk.Entry      (titleField, textvariable=self.fieldString, width=50)
        btnAddField     = StandardButton (frame=titleField, text="Add", command=self.addField)

        self.lbxFields  = Listbox        (titleField, selectmode="SINGLE", listvariable=self.fields_list, width=50)
        btnMovDnField   = StandardButton (frame=titleField, text="Move Down", command=self.moveDn)
        btnMovUpField   = StandardButton (frame=titleField, text="Move Up",   command=self.moveUp)
        btnRemField     = StandardButton (frame=titleField, text="Remover",   command=self.removeField)
        btnEdtField     = StandardButton (frame=titleField, text="Editar",    command=self.editField)

        titleSeparator  = LabelFrame     (content, bg= "Black", fg= "White", font=fontStyle, text="3. Selecione o token de separação")
        txtSeparator    = ttk.Entry      (titleSeparator, textvariable=self.tokenSeparator, width=50)
        btnParse        = StandardButton (frame=titleSeparator, text="Parse", command=self.parse)
        btnCancel       = StandardButton (frame=content, text="Sair", command=self.root.destroy)

        # Place the two differents Frames
        ZenithLabel.pack    (side= TOP)
        content.pack        (side= TOP, fill=Y)

        # Place components in content's grid
        titleBrowse.grid    (column=0, row=0, columnspan=2, padx=10, pady=10)
        lblBrowse.grid      (column=0, row=0, padx=19, pady=20)
        btnBrowse.grid      (column=1, row=0, padx=20, pady=20)

        titleField.grid     (column=0, row=1, columnspan=2, padx=10, pady=10)
        txtAddField.grid    (column=0, row=0, padx=10, pady=10)
        btnAddField.grid    (column=1, row=0, padx=20, pady=10)
        self.lbxFields.grid (column=0, row=1, rowspan=4, pady=10)
        btnMovUpField.grid  (column=1, row=1, padx=20, pady=5)
        btnMovDnField.grid  (column=1, row=2, padx=20, pady=5)
        btnEdtField.grid    (column=1, row=3, padx=20, pady=5)
        btnRemField.grid    (column=1, row=4, padx=20, pady=5)

        titleSeparator.grid (column=0, row=2, columnspan=2, padx=10, pady=10)
        txtSeparator.grid   (column=0, row=0, padx=10, pady=10)
        btnParse.grid       (column=1, row=0, padx=20, pady=10)
        btnCancel.grid      (column=0, row=3, padx=20, pady=10, sticky=E)

    def browseLog(self, *args):
        filename = filedialog.askopenfilename()
        if not filename == "":
            self.logFilename.set(filename)
            self.cuttedFilename.set(filename[0:44]+'...')

    def addField(self):
        value = self.fieldString.get()
        self.lbxFields.insert(0, value)

    def editField(self):
        index = int(self.lbxFields.curselection()[0])
        newStr = simpledialog.askstring(title="Edit", prompt="New Value:")
        self.lbxFields.insert(index, newStr)
        self.lbxFields.delete(index+1)
        
    def removeField(self):
        idx = self.lbxFields.curselection()
        self.lbxFields.delete(idx)

    def moveUp(self):
        idx = self.lbxFields.curselection()[0]
        if idx == 0:
            return None
        above = idx-1
        abv_txt = self.lbxFields.get(above)
        self.lbxFields.delete(above)
        self.lbxFields.insert(idx, abv_txt)

    def moveDn(self):
        idx = self.lbxFields.curselection()[0]
        if idx == self.lbxFields.size()-1:
            return None
        txt = self.lbxFields.get(idx)
        self.lbxFields.delete(idx)
        self.lbxFields.insert(idx+1, txt)

    def dictFromListBox(self, strTupleFields):
        fields = strTupleFields.get()[1:-1].split(',') # removes parantheses
        if fields[1] == '':
            fields = fields[:-1] # removes empty item when size is 1
        output = dict()
        for field in fields:
            field = field.strip().strip('\'') # removes spaces and single quotes
            # print("field:", field)
            name = field.split(':')[0]
            datatype = field.split(':')[1]
            output[name] = datatype
        return output

    def parse(self):
        struct = self.dictFromListBox(self.fields_list)
        struct["separator"] = self.tokenSeparator.get()
        parser = DataParser(struct)
        with open(self.logFilename.get(), 'r') as logfile:
            testline = logfile.readline()
            print(testline, struct)
            data = parser.parse_line(testline)
            if data == None:
                print("Could not match line structure to the log's [first] line")
                return None
        all_data = parser.parse_file(self.logFilename.get())
        self.generateStatistics(all_data)
        
    def generateStatistics(self, all_data):
        while(True):
            strPlots = simpledialog.askstring(title="Graph", prompt="Graphs: (empty to stop)",)
            if strPlots == '':
                self.window1_to_window2()
                break
            plots = strPlots.split(',')
            print("/nplotting: ", plots)
            g = statistics.generate_data_x_data(all_data[plots[0]], all_data[plots[1]], plots[0], plots[1])
        print("end", g)

    def window1_to_window2(self):
        window2Frame = Frame (self.root, bg="Black")
        switch_frame (self.master, window2Frame)
        window2 = Window2(window2Frame, self.root)
