import tkinter as tk
from tkinter import *

class main():
    def __init__(self):
        self.root = Tk()
        self.root.title("BodyMassIndex")
        self.root.resizable(False, False)
        self.root.geometry("320x210")
        self.BmiTitle=Label(self.root, font=("Courier",20), text="Body Mass Index")
        self.BmiTitle.pack(anchor="n")
        self.r=IntVar()
        self.manBut=Radiobutton(self.root,text="Male", variable=self.r,value=1,font=("Courier",12)).place(x=60,y=30)
        self.WomanBut = Radiobutton(self.root, text="Female", font=("Courier",12), variable=self.r, value=2).place(x=180,y=30)
        heightlab = Label(self.root,font=("Courier",12), text="Height(cm):" )
        heightlab.place(x=35,y=60)
        vcmd = self.root.register(self.correct)
        self.heightInp = Entry(self.root,width=12,font=("Courier",12), validate="key",validatecommand=(vcmd,'%P'))
        self.heightInp.place(x=150, y=60)
        weightlab = Label(self.root,font=("Courier",12), text="Weight(kg):")
        weightlab.place(x=35,y=90)
        self.weightInp = Entry(self.root,width=12,font=("Courier",12), validate="key",validatecommand=(vcmd,'%P'))
        self.weightInp.place(x=150,y=90)
        calculateBut = Button(self.root,font=("Courier",12), text="Calculate")
        calculateBut.bind("<Button>", self.calculate)
        calculateBut.place(x=100,y=120)
        calculateBut.after(10,self.FirstTimeBool)
        self.root.mainloop()
    def FirstTimeBool(self):
        self.FirstTime = "True"
    def correct(self,inp):
        if inp.isdigit():
            return True
        elif inp == "":
            return True
        else:
            return False
    def calculate(self, *args) :
        if self.FirstTime=="False":
            self.label.destroy()
        else:
            resultLab = Label(self.root,font=("Courier",12), text="Your result:")
            resultLab.place(x=30, y=170)
        weight = int(self.weightInp.get())
        height = int(self.heightInp.get()) * 0.01
        self.label = Label(self.root,font=("Courier",10), text=round(weight / height ** 2))
        self.label.place(x=150,y=172)
        self.result()
    def result(self):
        print(self.FirstTime)
        if self.FirstTime=="False":
            self.reslabel.destroy()
        else:
            self.FirstTime="False"
        if self.r.get()==1:
            if 25 >= self.label.cget("text")>=20 :
                self.reslabel=Label(self.root,font=("Courier",10),text="(Healthy)")
                self.reslabel.place(x=168,y=171)
            elif self.label.cget("text")<=19:
                self.reslabel = Label(self.root,font=("Courier",10), text="(Underweight)")
                self.reslabel.place(x=168,y=171)
            elif 30 >= self.label.cget("text")>=26 :
                self.reslabel = Label(self.root,font=("Courier",10), text="(Overweight)")
                self.reslabel.place(x=168,y=171)
            elif 40 >= self.label.cget("text")>=31 :
                self.reslabel = Label(self.root,font=("Courier",10), text="(Obese)")
                self.reslabel.place(x=168,y=171)
            elif self.label.cget("text")>40 :
                self.reslabel = Label(self.root,font=("Courier",10), text="(Extremely obese)")
                self.reslabel.place(x=168,y=171)
        elif self.r.get()==2:
            if self.label.cget("text")<=18 :
                self.reslabel = Label(self.root,font=("Courier",10), text="(Underweight)")
                self.reslabel.place(x=168,y=171)
            elif 24 >= self.label.cget("text")>=19 :
                self.reslabel = Label(self.root,font=("Courier",10), text="(Healthy)")
                self.reslabel.place(x=168,y=171)
            elif 30 >= self.label.cget("text")>=25 :
                self.reslabel = Label(self.root,font=("Courier",10), text="(Overweight)")
                self.reslabel.place(x=168,y=171)
            elif 40 >= self.label.cget("text")>=31 :
                self.reslabel = Label(self.root,font=("Courier",10), text="(Obese)")
                self.reslabel.place(x=168,y=171)
            elif self.label.cget("text")>40 :
                self.reslabel = Label(self.root,font=("Courier",10), text="(Extremely obese)")
                self.reslabel.place(x=168,y=171)
if __name__=="__main__":
    main=main()
