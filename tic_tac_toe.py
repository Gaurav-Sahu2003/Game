from tkinter import *
from tkinter import font as tkFont
root=Tk()
root.geometry("350x400")
root.title("Tic Tac Toe")
root.configure(bg="lightpink3")
t =1
count1=0
count2=0

def restart():
    b1.config(text="")
    b2.config(text="")
    b3.config(text="")
    b4.config(text="")
    b5.config(text="")
    b6.config(text="")
    b7.config(text="")
    b8.config(text="")
    b9.config(text="")
    fb.config(text="")
    global t
    t=1
    
def winner():
    a1=b1["text"]
    a2=b2["text"]
    a3=b3["text"]
    a4=b4["text"]
    a5=b5["text"]
    a6=b6["text"]
    a7=b7["text"]
    a8=b8["text"]
    a9=b9["text"]
    global count1
    global count2
    
    if (a1=="X" and a2=="X" and a3=="X") or (a4=="X" and a5=="X" and a6=="X") or (a7=="X" and a8=="X" and a9=="X") or (a1=="X" and a4=="X" and a7=="X") or (a2=="X" and a5=="X" and a8=="X") or (a3=="X" and a6=="X" and a9=="X") or (a1=="X" and a5=="X" and a9=="X")or (a3=="X" and a5=="X" and a7=="X"):
              
              count1 +=1
               
              pb1.config(text=count1)
              
              print("Player 1 is Winner")
              fb.config(text="Player 1 is Winner")
        
              root.after(2000,restart)
    if (a1=="O" and a2=="O" and a3=="O") or (a4=="O" and a5=="O" and a6=="O") or (a7=="O" and a8=="O" and a9=="O") or (a1=="O" and a4=="O" and a7=="O") or (a2=="O" and a5=="O" and a8=="O") or (a3=="O" and a6=="O" and a9=="O") or (a1=="O" and a5=="O" and a9=="O")or (a3=="O" and a5=="O" and a7=="O"):
              fb.config(text="Player 2 is Winner")
              count2 +=1
              
              
              print("Player 2  is Winner")
              pb2.config(text=count2) 
            
              root.after(2000,restart)
    if t==10:
        print("draw")
        fb.config(text="It is a Tie")
        root.after(1500,restart)
    

def show1():
  global t
  if len(b1["text"])==0: 
    if t%2 != 0:
        b1.config(text="X",fg="Black")
    else:
        b1.config(text="O",fg="White")
    t +=1
    winner() 
        
    

def show2():
    global t
    if len(b2["text"])==0:
        if t%2 != 0:
            b2.config(text="X",fg="Black")
        else:
            b2.config(text="O",fg="White")
        t +=1  
        winner()
        

def show3():
  global t
  if len(b3["text"])==0:  
    if t%2 != 0:
        b3.config(text="X",fg="Black")
    else:
        b3.config(text="O",fg="White")
    t +=1  
    winner()
    
    
def show4():
    global t
    if len(b4["text"])==0:
        if t%2 != 0:
            b4.config(text="X",fg="Black")
        else:
            b4.config(text="O",fg="White")
        t +=1
        winner()
         

def show5():
    global t
    if len(b5["text"])==0:
        if t%2 != 0:
            b5.config(text="X",fg="Black")
        else:
            b5.config(text="O",fg="White")
        t +=1  
        winner()
        
    
def show6():
    global t
    if len(b6["text"])==0:
        if t%2 != 0:
            b6.config(text="X",fg="Black")
        else:
            b6.config(text="O",fg="White")
        t +=1  
        winner()
        
    
def show7():
    global t
    if len(b7["text"])==0:
        if t%2 != 0:
            b7.config(text="X",fg="Black")
        else:
            b7.config(text="O",fg="White")
        t +=1  
        winner()
        
    
def show8():
    global t
    if len(b8["text"])==0:
        if t%2 != 0:
            b8.config(text="X",fg="Black")
        else:
            b8.config(text="O",fg="White")
        t +=1  
        winner()
        
    
    
def show9():
    global t
    if len(b9["text"])==0:
        if t%2 != 0:
            b9.config(text="X",fg="Black")
        else:
            b9.config(text="O",fg="White")
        t +=1
        winner()
        
helv38=tkFont.Font(family="Helvetica",size=10,weight=tkFont.BOLD)
l1=Label(text="Player 1",bg="white",borderwidth=3,relief="sunken",font=helv38,fg="mediumvioletred")
l2=Label(text="Player 2",bg="white",borderwidth=3,relief="sunken",font=helv38,fg="maroon4")

helv36=tkFont.Font(family="Helvetica",size=36,weight=tkFont.BOLD)
helv37=tkFont.Font(family="Helvetica",size=16,weight=tkFont.BOLD)
pb1=Button(text="",bg="thistle2")
pb2=Button(text="",bg="thistle2")



b1=Button(text="" , command=show1,bg="violetred4",border="10",font=helv36)
b2=Button(text="" , command=show2,bg="violetred4",border="10",font=helv36)
b3=Button(text="" , command=show3,bg="violetred4",border="10",font=helv36)
b4=Button(text="" , command=show4,bg="violetred4",border="10",font=helv36)
b5=Button(text="" , command=show5,bg="violetred4",border="10",font=helv36)
b6=Button(text="" , command=show6,bg="violetred4",border="10",font=helv36)
b7=Button(text="" , command=show7,bg="violetred4",border="10",font=helv36)
b8=Button(text="" , command=show8,bg="violetred4",border="10",font=helv36)
b9=Button(text="" , command=show9,bg="violetred4",border="10",font=helv36)

fb=Button(text="",bg="palevioletred3",font=helv37)

l1.place(x=50,y=10,width=60,height=25)
l2.place(x=190,y=10,width=60,height=25)

pb1.place(x=120,y=10,width=40,height=25)
pb2.place(x=260,y=10,width=40,height=25)

b1.place(x=50,y=50,width=80,height=80)
b2.place(x=130,y=50,width=80,height=80)
b3.place(x=210,y=50,width=80,height=80)
b4.place(x=50,y=130,width=80,height=80)
b5.place(x=130,y=130,width=80,height=80)
b6.place(x=210,y=130,width=80,height=80)
b7.place(x=50,y=210,width=80,height=80)
b8.place(x=130,y=210,width=80,height=80)
b9.place(x=210,y=210,width=80,height=80)

fb.place(x=50,y=350,width=239,height=40)

mainloop()