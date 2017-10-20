from tkinter import *
import datetime

class Sostav_Produktov:
    
    def __init__ (self, f):
        self.__f = f
        self.__l = self.__f.readlines()
    
    def __str__ (self):  #������ ��� �����
        return self.__f.name    
    
    def Fill_New_File (self, nf): #�������� ����� ����
        self.__nf = nf
        print('{:<20}'.format('�������:'),'{:<20}'.format('�����:'),'{:<20}'.format('����:'),'{:<20}'.format('��������:'),'{:<20}'.format('�������:'),'\n', file = self.__nf)
        for x in self.__l:
            x = x.split()
            print('{:<20}'.format(x[0]),'{:<20}'.format(x[1]), '{:<20}'.format(x[2]), '{:<20}'.format(x[3]),'{:<20}'.format(x[4]), file = self.__nf)

    def Maximum_Caloricity(self):  #���������� ������������
        li = []
        for x in self.__l:
            x = x.split()
            li = li + [x[4]]
        return max(li)
    
    def average (self): #������� ������������ ������
        li = []
        sum = 0
        for x in self.__l:
            x = x.split()
            li = li + [x[4]]
        for x in li:
            sum = sum + int(x)
        return sum/len(li)

    def The_Greasy (self): #����� ������ �����
        maks = 0
        maksn = ''
        for x in self.__l:
            x = x.split()
            if int(x[2]) > maks:
                maks = int(x[2])
                maksn = x[0]
        return maksn


def button1():  #������ ���������� �����
    ff.Fill_New_File(nf)  
    nf.close()
    f.close()

def button3():  #������ ������������ ������������
    E1.delete(0, END)
    E1.insert(1,str(ff.Maximum_Caloricity()))
    
def button4(): #������ ������� ������������
    E2.delete(0, END)
    E2.insert(1,str(ff.average()))
    
def button5(): #����� ������ �����
    E3.delete(0, END)
    E3.insert(1,str(ff.The_Greasy()))
    

def button6(): #clear
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)

class Mine(object): #��� �� ��������

        def __init__(self):
            self._x = None

        def get_x(self):
            return self._x

        def set_x(self, value):
            self._x = value

        def del_x(self):
            self._x = 'No more'

        x = property(get_x, set_x, del_x, '��� �������� x.')


    
f = open('������_������.txt')  #������� ����
mine = Mine()
mine.x = datetime.datetime.now() #��� �������� ���������� ����������� ���� � �����
nf = open('�����_����_������_������.txt', 'w')  #������� ����� ����
ff = Sostav_Produktov(f)
print(ff)

root = Tk()

L1 = Label(text = '�������� �������:')
L1.grid(row = 0, column = 0)

L2 = Label(text = '����:')
L2.grid(row = 0, column = 1)

L3 = Label(text = mine.x)
L3.grid(row = 0, column = 2)


E1 = Entry(root)
E1.grid(row = 4, column = 3)
E2 = Entry(root)
E2.grid(row = 3, column = 3)
E3 = Entry(root)
E3.grid(row = 2, column = 3)

but1 = Button(root, text = '������� ����� ����', command = button1).grid(row = 1, column = 0, sticky = W)
but2 = Button(root, text = '������� ����', command = root.quit).grid(row = 5, column = 2, sticky = W)
but3 = Button(root, text = '���������� ������������:', command = button3).grid(row = 4, column = 0, sticky = W)
but4 = Button(root, text = '������� ������������:', command = button4).grid(row = 3, column = 0, sticky = W)
but5 = Button(root, text = '����� ������ �������:', command = button5).grid(row = 2, column = 0, sticky = W)
but6 = Button(root, text = '��������', command = button6).grid(row = 5, column = 1, sticky = W)


root.mainloop()
root.destroy()