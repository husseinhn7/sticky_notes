
from tkinter import *
from tkinter import filedialog
def add_note():
    def color(c):
        if c==1:
            text['bg']="#7afcff"
            text['fg']="black"
        elif c==2:
            text['bg']="light yellow"
            text['fg']="black"
        elif c==3:
            text['bg']="#353535"
            text['fg']="#DEDEDE"
        elif c==4:
            text['bg']="light green"
            text['fg']="black"
        elif c==7:
            try:
                f=filedialog.askopenfilename(title="open a file",filetypes= (("text files","*.txt"),("all files","*.*")))
                st=open(f,"r")
                text.insert(END,st.read())
                st.close()
            except:
                pass
        elif c==8:
            try:
                
                fd=filedialog.asksaveasfilename(title="save a file",defaultextension=".txt",filetypes= (("text file","*.txt"),("all files","*.*")))
                d=text.get("1.0", "end-1c")
                c=open(fd,"w")
                c.write(str(d))
                c.close()
            except:
                pass


    note=Tk()
    note.title("Stiky Notes")
    
    note.geometry("370x350")
    note.config(bg="#353535")
    note.attributes('-topmost',True)
    ft=Frame(note)
    ft.pack(anchor="nw")
    Button(ft,text="       ",font=("arial",10),bg="#7afcff",borderwidth=0,command= lambda:color(1),width=6,height=3).pack(side="left")
    Button(ft,text="       ",font=("arial",10),bg="light yellow",borderwidth=0,command= lambda:color(2),width=6,height=3).pack(side="left")
    Button(ft,text="       ",font=("arial",10),bg="#353535",borderwidth=0,command= lambda:color(3),width=6,height=3).pack(side="left")
    Button(ft,text="       ",font=("arial",10),bg="light green",borderwidth=0,command= lambda:color(4),width=6,height=3).pack(side="left")
    Button(ft,text="open\nnote",font=("arial",10),fg="#DEDEDE",bg="#353535",borderwidth=0,command= lambda:color(7),width=6,height=3).pack(side="left")
    Button(ft,text="create\nnote",font=("arial",10),fg="#DEDEDE",bg="#353535",borderwidth=0,command= add_note,width=6,height=3).pack(side="left")
    Button(ft,text="save\nnote",font=("arial",10),fg="#DEDEDE",bg="#353535",borderwidth=0,command=lambda:color(8),width=6,height=3).pack(side="left")

    text=Text(note,font=("arial",15),fg="#DEDEDE",bg="#353535",borderwidth=0)
    text.pack(expand=True, fill='both',anchor="nw")

    note.mainloop()

add_note()

