from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global  file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file= None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)
        f= open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            # save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            file.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")

    else:
        # save the existing file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        file.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad", "Notepad created by Shubham Choudhary")
def wrap():
    pass
def font():
    pass
def zoom():
    pass
def status():
    pass

if __name__ == '__main__':

    # Basic Tkinter setup

        root= Tk()

        root.title("Untitled - Notepad")
        root.wm_iconbitmap("icon.ico")

        root.geometry("644x788")


    # Add TextArea

        TextArea= Text(root, font= "lucida 13")
        file= None
        TextArea.pack(expand=TRUE, fill=BOTH)

    # Lets Create a menu bar

        m= Menu(root)
    # file menu starts
        FileMenu= Menu(m, tearoff=0)
    # To open the file

        FileMenu.add_command(label = "New", command=newFile)
    # To open already existing file

        FileMenu.add_command(label= "Open", command=openFile)
    # To save the current file

        FileMenu.add_command(label= "Save", command=saveFile)
        FileMenu.add_separator()
        FileMenu.add_command(label="Exit", command=quitApp)
        m.add_cascade(label="File", menu=FileMenu)

    # File menu ends


    #Edit Menu Starts

        EditMenu= Menu(m, tearoff=0)
    #To give a feature of cut

        EditMenu.add_command(label="Cut", command=cut)
    # To give a feature of copy
        EditMenu.add_command(label="Copy", command=copy)
    # To give a feature of paste
        EditMenu.add_command(label="Paste", command=paste)

        m.add_cascade(label="Edit", menu=EditMenu)

    #Edit Menu Ends

    # Help menu Starts

        HelpMenu = Menu(m, tearoff=0)
        HelpMenu.add_command(label="About Notepad", command=about)
        m.add_cascade(label="Help", menu=HelpMenu)
    # Help menu Ends

    # Format Menu Starts

        FormatMenu = Menu(m, tearoff=0)
        FormatMenu.add_command(label="Word Wrap", command= wrap)
        FormatMenu.add_command(label="Font", command=font)
        m.add_cascade(label="Format", menu=FormatMenu)

        root.config(menu=m)
    # View Menu Starts

        ViewMenu = Menu(m, tearoff=0)
        ViewMenu.add_command(label="Zoom", command=zoom)
        ViewMenu.add_command(label="Status Bar", command=status)
        m.add_cascade(label="View", menu=ViewMenu)

        root.config(menu=m)

    # Adding Scrollbar

        Scroll = Scrollbar(TextArea)
        Scroll.pack(side=RIGHT, fill=Y)
        Scroll.config(command = TextArea.yview)
        TextArea.config(yscrollcommand=Scroll.set)


        root.mainloop()

