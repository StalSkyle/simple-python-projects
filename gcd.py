from tkinter import *
import math
root=Tk()
root.title('Нахождение НОД и НОК чисел')
nok1=0
nok2=0
helper=0
def about():
    def nod2():
        #ПОЛУЧЕНИЕ
        per=int(chi1.get())
        vtor=int(chi2.get())
        #ВЫЧИСЛЕНИЕ
        Label(a, text='НОД ='+str(math.gcd(per, vtor))).grid(row=3, column=2, sticky=NS)
        Label(a, text='НОК ='+str(per*vtor//math.gcd(per, vtor))).grid(row=4, column=2, sticky=NS)
        
    def nod3():
        #ПОЛУЧЕНИЕ
        per=int(chi1.get())
        vtor=int(chi2.get())
        tret=int(chi3.get())
        #ВЫЧИСЛЕНИЕ
        nok1=per*vtor//math.gcd(per, vtor)
        Label(a, text='НОД ='+str(math.gcd(per, vtor))).grid(row=3, column=3, sticky=NS)
        Label(a, text='НОК ='+str(per*vtor//math.gcd(per, vtor))).grid(row=4, column=3, sticky=NS)
        
    def nod4():
        #ПОЛУЧЕНИЕ
        per=int(chi1.get())
        vtor=int(chi2.get())
        tret=int(chi3.get())
        chet=int(chi4.get())
        #ВЫЧИСЛЕНИЕ
        nok1=per*vtor//math.gcd(per, vtor)
        helper=nok1*tret//math.gcd(nok1, tret)
        nok2=helper*chet//math.gcd(helper, chet)
        Label(a, text='НОД ='+str(math.gcd(per, vtor))).grid(row=3, column=4, sticky=NS)
        Label(a, text='НОК ='+str(per*vtor//math.gcd(per, vtor))).grid(row=4, column=4, sticky=NS)
    v=var.get()
      
    if v==0:
        a=Toplevel()#
        a.geometry('350x150+400+200')#
        #ОБЪЯВЛЕНИЕ
        info2=Label(a, text='Ввод данных')
        fir=Label(a, text='1-e')
        sec=Label(a, text='2-e')
        thi=Label(a, text='3-e')
        fort=Label(a, text='4-e')
        chi1=Entry(a, width=20)
        chi2=Entry(a, width=20)
        chi3=Entry(a, width=20)
        chi4=Entry(a, width=20)
        #РАЗМЕЩЕНИЕ
        info2.grid(row=0, column=2, sticky=N)
        fir.grid(row=1, column=0, sticky=N)
        chi1.grid(row=1, column=1, sticky=N)
        sec.grid(row=1, column=2, sticky=N)
        chi2.grid(row=1, column=3, sticky=N)
        Button(a, text='Рассчитать!', command=nod2).grid(row=2, column=2, sticky=N)
        
    if v==1:
        a=Toplevel()#
        a.geometry('450x150+400+200')#
        #ОБЪЯВЛЕНИЕ
        info2=Label(a, text='Ввод данных')
        fir=Label(a, text='1-e')
        sec=Label(a, text='2-e')
        thi=Label(a, text='3-e')
        fort=Label(a, text='4-e')
        chi1=Entry(a, width=20)
        chi2=Entry(a, width=20)
        chi3=Entry(a, width=20)
        chi4=Entry(a, width=20)
        #РАЗМЕЩЕНИЕ
        info2.grid(row=0, column=3, sticky=N)
        fir.grid(row=1, column=0, sticky=N)
        chi1.grid(row=1, column=1, sticky=N)
        sec.grid(row=1, column=2, sticky=N)
        chi2.grid(row=1, column=3, sticky=N)
        thi.grid(row=1, column=4, sticky=N)
        chi3.grid(row=1, column=5, sticky=N)
        Button(a, text='Рассчитать!', command=nod3).grid(row=2, column=3, sticky=N)
    if v==2:
        a=Toplevel()#
        a.geometry('650x150+400+200')#
        #ОБЪЯВЛЕНИЕ
        info2=Label(a, text='Ввод данных')
        fir=Label(a, text='1-e')
        sec=Label(a, text='2-e')
        thi=Label(a, text='3-e')
        fort=Label(a, text='4-e')
        chi1=Entry(a, width=20)
        chi2=Entry(a, width=20)
        chi3=Entry(a, width=20)
        chi4=Entry(a, width=20)
        #РАЗМЕЩЕНИЕ
        info2.grid(row=0, column=4, sticky=N)
        fir.grid(row=1, column=0, sticky=N)
        chi1.grid(row=1, column=1, sticky=N)
        sec.grid(row=1, column=2, sticky=N)
        chi2.grid(row=1, column=3, sticky=N)
        thi.grid(row=1, column=4, sticky=N)
        chi3.grid(row=1, column=5, sticky=N)
        fort.grid(row=1, column=6, sticky=N)
        chi4.grid(row=1, column=7, sticky=N)
        Button(a, text='Рассчитать!', command=nod4).grid(row=2, column=4, sticky=N)
#ГЛАВНОЕ ОКНО    
var=IntVar()
var.set(1)
info=Label(root, text='Калькулятор для нахождения НОД и НОК чисел').grid(row=0, column=1, sticky=W)
Radiobutton(root, text='2 числа', variable=var, value=0).grid(row=1, column=0, sticky=W)
Radiobutton(root, text='3 числа', variable=var, value=1).grid(row=1, column=1, sticky=N)
Radiobutton(root, text='4 числа', variable=var, value=2).grid(row=1, column=2, sticky=W)
Button(root, text='Ввести данные', command=about).grid(row=2, column=1, sticky=N)
root.mainloop()
