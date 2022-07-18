'''
PATCH NOTES ДЛЯ БУДУЩЕГО
-сделать распределение теории по кнопкам (не одним текстом)
'''
from tkinter import *
import random
knowledge={"m":"""
Матрицей размера n×m называется прямоугольная таблица специального вида, состоящая из n строк и m столбцов, заполненная числами.
Количество строк и столбцов задают размеры матрицы.
Матрица - это таблица данных, которая берется в круглые/квадратные скобки либо в вертикальные линии:

A = |4   1   7|
       |-1  0   2| 
       |3   -15 5|

Главной диагональю матрицы называется диагональ, проведённая из левого верхнего угла матрицы в правый нижний угол.

Побочной диагональю матрицы называется диагональ, проведённая из левого нижнего угла матрицы в правый верхний угол.


ОПЕРАЦИИ

вынесение/внесение минуса в матрицу:
необходимо всего лишь домножить каждый элемент матрицы на -1

умножение матрицы на число:
необходимо домножить каждый элемент матрицы на данное число

транспонирование матрицы:
матрица "поворачивается" относительно главной диагонали. Другими словами, строки матрицы становятся столбцами с теми же номерами. Пример:

A=
|1 0|
|2 3|

A`=
|1 2|
|0 3|

сумма, разность, умножение матриц
cкладывать и вычитать можно матрицы одного размера, в результате получается матрица того же размера.
Сложение матриц (сумма матриц) A + B есть операция вычисления матрицы C, все элементы которой равны
попарной сумме всех соответствующих элементов матриц A и B, то есть каждый элемент матрицы C равен:
c[i][j]=a[i][j]+b[i][j]
Вычитание матриц (разность матриц) A - B есть операция вычисления матрицы C, все элементы которой равны
попарной разности всех соответствующих элементов матриц A и B, то есть каждый элемент матрицы C равен
c[i][j]=a[i][j]+b[i][j]
Умножение производится аналогично.
Пример:
A=
|4 2|
|9 0|
B=
|3 1|
|3 4|
A+B=
|4+3 2+1| = |7 3|
|9+3 0+4|   |12 4|

определитель
Для матрицы 2×2 значение определителя равно разности произведений элементов главной и побочной диагоналей
Пример:
A=
|5  7|
|-4 1|
Определитель равен 5*1-7*(-4)=5+28=33
Для матрицы 3×3 значение определителя вычисляется правилом ТРЕУГОЛЬНИКА: оно равно сумме произведений элементов главной диагонали и произведений элементов лежащих на треугольниках
с гранью параллельной главной диагонали, от которой вычитается произведение элементов побочной диагонали и произведение элементов лежащих на
треугольниках с гранью параллельной побочной диагонали.
Пример:
A=
|5  7  1|
|-4 1  0|
|2  0  3|
Определитель равен 5·1·3 + 7·0·2 + 1·(-4)·0 - 1·1·2 - 5·0·0 - 7·(-4)·3 = 15 + 0 + 0 - 2 - 0 + 84 = 97

Использование матриц в математике довольно обширно: с их помощью решают системы уравнений, выполняют афинные преобразования и решают различные задачи. 
"""
}
questions={"0":"для внесения/вынесения минуса из матрицы каждый элемент необходимо домножить на... \n введите число",
           "1":"как называется правило, с помощью которого вычисляется определитель матрицы 3х3 \n введите слово в ИМЕНИТЕЛЬНОМ падеже",
           "2":"для матрицы 2×2 значение определителя равно разности произведений элементов главной и ... диагоналей \n введите слово В ТОМ ПАДЕЖЕ, В КОТОРОМ ОНО ДОЛЖНО СТОЯТЬ В ПРЕДЛОЖЕНИИ",
           "3":"матрицей называется прямоугольная таблица специального вида, состоящая из n строк и m столбцов, заполненная ... \n введите слово в ИМЕНИТЕЛЬНОМ падеже",
           "4":"cкладывать и вычитать можно матрицы одного ... \n введите слово В ТОМ ПАДЕЖЕ, В КОТОРОМ ОНО ДОЛЖНО СТОЯТЬ В ПРЕДЛОЖЕНИИ",
           "5":"cложение матриц (сумма матриц) A + B есть операция вычисления матрицы C, все элементы которой равны попарной ... всех соответствующих элементов матриц A и B \n введите слово в ИМЕНИТЕЛЬНОМ падеже",
           "6":"в процессе транспонирования матрицы она поворачивается относительно ... диагонали \n введите слово В ТОМ ПАДЕЖЕ, В КОТОРОМ ОНО ДОЛЖНО СТОЯТЬ В ПРЕДЛОЖЕНИИ",
           "7":"... диагональю матрицы называется диагональ, проведённая из левого верхнего угла матрицы в правый нижний угол. \n введите слово в ИМЕНИТЕЛЬНОМ падеже",
           "8":"при умножении матрицы на число необходимо домножить каждый ... матрицы на данное число \n введите слово в ИМЕНИТЕЛЬНОМ падеже",
           "9":"cкладывать и вычитать можно матрицы ... размера \n введите слово В ТОМ ПАДЕЖЕ, В КОТОРОМ ОНО ДОЛЖНО СТОЯТЬ В ПРЕДЛОЖЕНИИ",
           "10":"в процессе транспонирования ... матрицы становятся столбцами с теми же номерами \n введите слово в ИМЕНИТЕЛЬНОМ падеже"
           }
answers={"0":"-1", "1":"треугольник", "2":'побочной', "3":"число", "4":"размера", "5":"сумма", "6":"главной", "7":"главная", "8":"элемент", "9":"одного", "10":"строка"}
def theory():
    theormenu=Tk()
    Label(theormenu, text=" ").grid(row=0, column=0)
    Label(theormenu, text='Выберите, что вы хотите сделать', font='Calibri 25', fg='green').grid(row=1, column=0)
    Button(theormenu, text='Ознакомиться с теорией', command=new, height=2, width=20).grid(row=2, column=0, sticky=W)
    Button(theormenu, text='Тест на знание теории', command=test, height=2, width=20).grid(row=2, column=0, sticky=E)
def new():
    new=Tk()
    frame_for_text = Frame(new)#место для текста
    frame_for_text.pack()
    answer_info_text = Text(frame_for_text, width=80, height=10, wrap=WORD) #текст с информацией
    answer_info_text.insert(INSERT, knowledge["m"])
    answer_info_text.configure(font=("Times New Roman", 14))
    answer_info_text.pack(pady=10, side=LEFT)
    scroll = Scrollbar(frame_for_text, command=answer_info_text.yview) #скролл для текста
    scroll.pack(side=RIGHT, fill=Y)
    answer_info_text.config(yscrollcommand=scroll.set)
    
    new.mainloop()
def test():
    test=Tk()
    Label(test, text=" ").grid(row=0, column=0)
    Label(test, text='Вам будет предложено 5 вопросов', font='Calibri 15', fg='green').grid(row=1, column=0, sticky=NS)
    Label(test, text='Вводите ваш ответ в специальное поле', font='Calibri 10', fg='blue').grid(row=2, column=0, sticky=NS)
    Button(test, text='Начать!', command=starttest, height=2, width=20).grid(row=3, column=0, sticky=NS)
sheet=[]
def starttest():
    def check():
        global sheet      
        if str(ans1.get())==answers[str(sheet[0])]:
            Label(starttest, text="Правильно!", font='Calibri 15', fg='green').grid(row=1, column=0, sticky=E)
        else:
            Label(starttest, text="Неправильно! Правильный ответ: "+answers[str(sheet[0])], font='Calibri 15', fg='red').grid(row=1, column=0, sticky=E)
        if str(ans2.get())==answers[str(sheet[1])]:
            Label(starttest, text="Правильно!", font='Calibri 15', fg='green').grid(row=3, column=0, sticky=E)
        else:
            Label(starttest, text="Неправильно! Правильный ответ: "+answers[str(sheet[1])], font='Calibri 15', fg='red').grid(row=3, column=0, sticky=E)
        if str(ans3.get())==answers[str(sheet[2])]:
            Label(starttest, text="Правильно!", font='Calibri 15', fg='green').grid(row=5, column=0, sticky=E)
        else:
            Label(starttest, text="Неправильно! Правильный ответ: "+answers[str(sheet[2])], font='Calibri 15', fg='red').grid(row=5, column=0, sticky=E)
        if str(ans4.get())==answers[str(sheet[3])]:
            Label(starttest, text="Правильно!", font='Calibri 15', fg='green').grid(row=7, column=0, sticky=E)
        else:
            Label(starttest, text="Неправильно! Правильный ответ: "+answers[str(sheet[3])], font='Calibri 15', fg='red').grid(row=7, column=0, sticky=E)
        if str(ans5.get())==answers[str(sheet[4])]:
            Label(starttest, text="Правильно!", font='Calibri 15', fg='green').grid(row=9, column=0, sticky=E)
        else:
            Label(starttest, text="Неправильно! Правильный ответ: "+answers[str(sheet[4])], font='Calibri 15', fg='red').grid(row=9, column=0, sticky=E)     
    starttest=Tk()
   # starttest.geometry('x600')
    count=0
    was=[]
    for i in range(5):
        n=random.randint(0, 4)
        while True:
            if n in was:
                n=random.randint(0, 4)
            else:
                was.append(n)
                break
        Label(starttest, text=questions[str(n)], font='Calibri 15', fg='blue').grid(row=2*i, column=0, sticky=NS)
        global sheet
        sheet.append(n)
    Button(starttest, text="Готово!", command=check, height=2, width=20).grid(row=11, column=0, sticky=NS)    
    ans1=Entry(starttest, width=20)
    ans1.grid(row=1, column=0, sticky=NS)    
    ans2=Entry(starttest, width=20)
    ans2.grid(row=3, column=0, sticky=NS)   
    ans3=Entry(starttest, width=20)
    ans3.grid(row=5, column=0, sticky=NS)   
    ans4=Entry(starttest, width=20)
    ans4.grid(row=7, column=0, sticky=NS)
    ans5=Entry(starttest, width=20)
    ans5.grid(row=9, column=0, sticky=NS)
    starttest.mainloop()    
def practice():
    def minus():
        def do():
            itog=Tk()
            Label(itog, text=str(-int(one.get())), font='Calibri 15').grid(row=0, column=0, sticky=E)
            Label(itog, text=str(-int(two.get())), font='Calibri 15').grid(row=0, column=1, sticky=E)
            Label(itog, text=str(-int(three.get())), font='Calibri 15').grid(row=0, column=2, sticky=E)
            Label(itog, text=str(-int(four.get())), font='Calibri 15').grid(row=1, column=0, sticky=E)
            Label(itog, text=str(-int(five.get())), font='Calibri 15').grid(row=1, column=1, sticky=E)
            Label(itog, text=str(-int(six.get())), font='Calibri 15').grid(row=1, column=2, sticky=E)
            Label(itog, text=str(-int(seven.get())), font='Calibri 15').grid(row=2, column=0, sticky=E)
            Label(itog, text=str(-int(eight.get())), font='Calibri 15').grid(row=2, column=1, sticky=E)
            Label(itog, text=str(-int(nine.get())), font='Calibri 15').grid(row=2, column=2, sticky=E)
            Label(itog, text='Как это получилось: мы просто домножили каждый элемент матрицы на -1', font='Calibri 15', fg='blue').grid(row=3, column=4, sticky=E)
            
        m=Tk()
        Label(m, text='Введите матрицу:').grid(row=0, column=0, sticky=NS)
        one=Entry(m, width=20)
        one.grid(row=1, column=0)
        two=Entry(m, width=20)
        two.grid(row=1, column=1)
        three=Entry(m, width=20)
        three.grid(row=1, column=2)
        four=Entry(m, width=20)
        four.grid(row=2, column=0)
        five=Entry(m, width=20)
        five.grid(row=2, column=1)
        six=Entry(m, width=20)
        six.grid(row=2, column=2)
        seven=Entry(m, width=20)
        seven.grid(row=3, column=0)
        eight=Entry(m, width=20)
        eight.grid(row=3, column=1)
        nine=Entry(m, width=20)
        nine.grid(row=3, column=2)
        Button(m, text='Рассчитать!', command=do).grid(row=4, column=1, sticky=NS)
        
    def mult():
        def do():
            ch=int(chislo.get())
            itog=Tk()
            Label(itog, text=str(int(one.get())*ch), font='Calibri 15').grid(row=0, column=0, sticky=E)
            
            Label(itog, text=str(int(two.get())*ch), font='Calibri 15').grid(row=0, column=1, sticky=E)
            Label(itog, text=str(int(three.get())*ch), font='Calibri 15').grid(row=0, column=2, sticky=E)
            Label(itog, text=str(int(four.get())*ch), font='Calibri 15').grid(row=1, column=0, sticky=E)
            Label(itog, text=str(int(five.get())*ch), font='Calibri 15').grid(row=1, column=1, sticky=E)
            Label(itog, text=str(int(six.get())*ch), font='Calibri 15').grid(row=1, column=2, sticky=E)
            Label(itog, text=str(int(seven.get())*ch), font='Calibri 15').grid(row=2, column=0, sticky=E)
            Label(itog, text=str(int(eight.get())*ch), font='Calibri 15').grid(row=2, column=1, sticky=E)
                  
            Label(itog, text=str(int(nine.get())*ch), font='Calibri 15').grid(row=2, column=2, sticky=E)
            qwer='Как это получилось: мы умножили каждый элемент матрицы на '+str(ch)
            Label(itog, text=qwer, font='Calibri 15', fg='blue').grid(row=3, column=4, sticky=E)      
            
        m=Tk()
        Label(m, text='Введите матрицу:').grid(row=0, column=0, sticky=NS)
        one=Entry(m, width=20)
        one.grid(row=1, column=0)
        two=Entry(m, width=20)
        two.grid(row=1, column=1)
        three=Entry(m, width=20)
        three.grid(row=1, column=2)
        four=Entry(m, width=20)
        four.grid(row=2, column=0)
        five=Entry(m, width=20)
        five.grid(row=2, column=1)
        six=Entry(m, width=20)
        six.grid(row=2, column=2)
        seven=Entry(m, width=20)
        seven.grid(row=3, column=0)
        eight=Entry(m, width=20)
        eight.grid(row=3, column=1)
        nine=Entry(m, width=20)
        nine.grid(row=3, column=2)
        chislo=Entry(m, width=20)
        Label(m, text='').grid(row=4, column=0)
        chislo.grid(row=5, column=1, sticky=NS)
        Label(m, text="введите число").grid(row=5, column=0)
        Button(m, text='Рассчитать!', command=do).grid(row=6, column=1, sticky=NS)
    def trans():
        def do():
            print(one.get(), four.get(), seven.get())
            print(two.get(), five.get(), eight.get())
            print(three.get(), six.get(), nine.get())
        m=Tk()
        one=Entry(m, width=20)
        one.grid(row=0, column=0)
        two=Entry(m, width=20)
        two.grid(row=0, column=1)
        three=Entry(m, width=20)
        three.grid(row=0, column=2)
        four=Entry(m, width=20)
        four.grid(row=1, column=0)
        five=Entry(m, width=20)
        five.grid(row=1, column=1)
        six=Entry(m, width=20)
        six.grid(row=1, column=2)
        seven=Entry(m, width=20)
        seven.grid(row=2, column=0)
        eight=Entry(m, width=20)
        eight.grid(row=2, column=1)
        nine=Entry(m, width=20)
        nine.grid(row=2, column=2)
        Button(m, text='Рассчитать!', command=do).grid(row=3, column=1, sticky=NS)
    def ariph():
        def do():
            print("Сложение матриц")
            print(int(one.get())+int(one1.get()), int(two.get())+int(two1.get()), int(three.get())+int(three1.get()))
            print(int(four.get())+int(four1.get()), int(five.get())+int(five1.get()), int(six.get())+int(six1.get()))
            print(int(seven.get())+int(seven1.get()), int(eight.get())+int(eight1.get()), int(nine.get())+int(nine1.get()))
            print("Как это получилось: мы сложили каждый элемент первой матрицы на элемент второй матрицы с таким же номером")
            print("Вычитание матриц")
            print(int(one.get())-int(one1.get()), int(two.get())-int(two1.get()), int(three.get())-int(three1.get()))
            print(int(four.get())-int(four1.get()), int(five.get())-int(five1.get()), int(six.get())-int(six1.get()))
            print(int(seven.get())-int(seven1.get()), int(eight.get())-int(eight1.get()), int(nine.get())-int(nine1.get()))
            print("Как это получилось: мы умножили каждый элемент первой матрицы на элемент второй матрицы с таким же номером")
            print("Умножение матриц")
            print(int(one.get())*int(one1.get()), int(two.get())*int(two1.get()), int(three.get())*int(three1.get()))
            print(int(four.get())*int(four1.get()), int(five.get())*int(five1.get()), int(six.get())*int(six1.get()))
            print(int(seven.get())*int(seven1.get()), int(eight.get())*int(eight1.get()), int(nine.get())*int(nine1.get()))
            print("Как это получилось: мы умножили каждый элемент первой матрицы на элемент второй матрицы с таким же номером")
        m=Tk()
        Label(m, text="Первая матрица:").grid(row=0, column=0)
        one=Entry(m, width=20)
        one.grid(row=1, column=0)
        two=Entry(m, width=20)
        two.grid(row=1, column=1)
        three=Entry(m, width=20)
        three.grid(row=1, column=2)
        four=Entry(m, width=20)
        four.grid(row=2, column=0)
        five=Entry(m, width=20)
        five.grid(row=2, column=1)
        six=Entry(m, width=20)
        six.grid(row=2, column=2)
        seven=Entry(m, width=20)
        seven.grid(row=3, column=0)
        eight=Entry(m, width=20)
        eight.grid(row=3, column=1)
        nine=Entry(m, width=20)
        nine.grid(row=3, column=2)
        Label(m, text="Вторая матрица:").grid(row=4, column=0)
        one1=Entry(m, width=20)
        one1.grid(row=5, column=0)
        two1=Entry(m, width=20)
        two1.grid(row=5, column=1)
        three1=Entry(m, width=20)
        three1.grid(row=5, column=2)
        four1=Entry(m, width=20)
        four1.grid(row=6, column=0)
        five1=Entry(m, width=20)
        five1.grid(row=6, column=1)
        six1=Entry(m, width=20)
        six1.grid(row=6, column=2)
        seven1=Entry(m, width=20)
        seven1.grid(row=7, column=0)
        eight1=Entry(m, width=20)
        eight1.grid(row=7, column=1)
        nine1=Entry(m, width=20)
        nine1.grid(row=7, column=2)
        Button(m, text='Рассчитать!', command=do).grid(row=8, column=1, sticky=NS)
    def minor():
        draw()
    def deter():
        def do():
            on=int(one.get())
            tw=int(two.get())
            th=int(three.get())
            fo=int(four.get())
            fi=int(five.get())
            si=int(six.get())
            se=int(seven.get())
            ei=int(eight.get())
            ni=int(nine.get())
            itog=Tk()
            Label(itog, text=str(on*fi*ni+fo*ei*th+tw*si*se-th*fi*se-on*si*ei-ni*tw*fo), font='Calibri 15', fg='red').grid(row=0, column=0, sticky=W)
            Label(itog, text='Как это получилось: a11*a22*a33+a21*a32*a13+a12*a23*a31-', font='Calibri 15').grid(row=1, column=0, sticky=W)
            Label(itog, text='-a13*a22*a31-a11*a23*a32-a33*a12*a21, a - элемент', font='Calibri 15').grid(row=2, column=0, sticky=W)
            Label(itog, text='матрицы, цифры после него - строка и столбец в матрице', font='Calibri 15').grid(row=3, column=0, sticky=W)

        m=Tk()
        Label(m, text='Введите матрицу:').grid(row=0, column=0, sticky=NS)
        one=Entry(m, width=20)
        one.grid(row=1, column=0)
        two=Entry(m, width=20)
        two.grid(row=1, column=1)
        three=Entry(m, width=20)
        three.grid(row=1, column=2)
        four=Entry(m, width=20)
        four.grid(row=2, column=0)
        five=Entry(m, width=20)
        five.grid(row=2, column=1)
        six=Entry(m, width=20)
        six.grid(row=2, column=2)
        seven=Entry(m, width=20)
        seven.grid(row=3, column=0)
        eight=Entry(m, width=20)
        eight.grid(row=3, column=1)
        nine=Entry(m, width=20)
        nine.grid(row=3, column=2)
        Button(m, text='Рассчитать!', command=do).grid(row=4, column=1, sticky=NS)
    pracmenu=Tk()
    Label(pracmenu, text=" ").grid(row=0, column=0)
    Label(pracmenu, text='Выберите, что вы хотите сделать', font='Calibri 25', fg='green').grid(row=1, column=0)
    Button(pracmenu, text='Вынесение/внесение минуса в матрицу', command=minus, height=2, width=40).grid(row=2, column=0, sticky=NS)
    Button(pracmenu, text='Умножение матрицы на число', command=mult, height=2, width=40).grid(row=3, column=0, sticky=NS)
    Button(pracmenu, text='Транспонирование матрицы', command=trans, height=2, width=40).grid(row=4, column=0, sticky=NS)
    Button(pracmenu, text='Сумма, разность, умножение матриц', command=ariph, height=2, width=40).grid(row=5, column=0, sticky=NS)
    Button(pracmenu, text='Алгебраич. дополнение и минор', command=minor, height=2, width=40).grid(row=6, column=0, sticky=NS)
    Button(pracmenu, text='Определитель матрицы', command=deter, height=2, width=40).grid(row=7, column=0, sticky=NS)
    #Label(pracmenu, text="Введите число строк и").grid(row=8, column=0, sticky=W)
    #Label(pracmenu, text="стобцов в матрице").grid(row=9, column=0, sticky=W)
    #height = Entry(pracmenu, width=20)
    #height.grid(row=8, column=0, sticky=NS)
    #width=Entry(pracmenu, width=20)
    #width.grid(row=8, column=0, sticky=E)
    
root=Tk()
root.title('Калькулятор матриц [v1.0] by StalSkyle')
root.resizable(width=False, height=False)
info0=Label(root, text=' ', font = 'Times 15').grid(row=0, column=0, sticky=W)
info1=Label(root, text='Приветствуем Вас в Калькуляторе матриц', font = 'Calibri 30', fg='red').grid(row=1, column=0, sticky=NS)
info2=Label(root, text='Выберите раздел, с которого хотите начать', font='Calibri 15', fg='blue').grid(row=2, column=0, sticky=NS)
info3=Label(root, text=' ', font='Times 20').grid(row=3, column=0)
Button(root, text='Теория', command=theory, height=2, width=20).grid(row=4, column=0, sticky=W)
Button(root, text='Практика', command=practice, height=2, width=20).grid(row=4, column=0, sticky=E)
