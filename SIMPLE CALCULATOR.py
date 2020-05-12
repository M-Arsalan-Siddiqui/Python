from tkinter import *
root=Tk()
root.title(" Calculator" )
text_input =StringVar()
optr=""
text1=Entry(root,font=("arial",20,'bold'),justify='right',bd=20,bg='red',textvariable=text_input)
text1.grid(columnspan=4)

def bt_Click(number):
    global optr
    optr=optr+str(number)
    text_input.set(optr)
def bt_ClearText():
    global optr
    optr=""
    text_input.set('')
def bt_Answer():
    global optr
    final=str(eval(optr))
    text_input.set(final)
    optr=""
bt9=Button(root, text="9" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click(9))
bt8=Button(root, text="8" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click(8))
bt7=Button(root, text="7" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click(7))
bt6=Button(root, text="6" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click(6))
bt5=Button(root, text="5" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click(5))
bt4=Button(root, text="4" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click(4))
bt3=Button(root, text="3" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click(3))
bt2=Button(root, text="2" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click(2))
bt1=Button(root, text="1" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click(1))
bt0=Button(root, text="0" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click(0))
bt9.grid(row=1,column=2)
bt8.grid(row=1,column=1)
bt7.grid(row=1,column=0)
bt6.grid(row=2,column=2)
bt5.grid(row=2,column=1)
bt4.grid(row=2,column=0)
bt3.grid(row=3,column=2)
bt2.grid(row=3,column=1)
bt1.grid(row=3,column=0)
bt0.grid(row=4,column=0)
bt_Add=Button(root, text="+" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click('+'))
bt_sub=Button(root, text="-" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click('-'))
bt_Mul=Button(root, text="*" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click('*'))
bt_Div=Button(root, text="/" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=lambda:bt_Click('/'))
bt_equal=Button(root, text="=" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=bt_Answer)
bt_clear=Button(root, text="Clr" ,font=("arial",20,'bold'),padx=12,pady=12,fg="black",bg="red",command=bt_ClearText)
bt_Add.grid(row=1,column=3)
bt_sub.grid(row=2,column=3)
bt_Mul.grid(row=3,column=3)
bt_Div.grid(row=4,column=3)
bt_equal.grid(row=4,column=1)
bt_clear.grid(row=4,column=2)
root.mainloop()
