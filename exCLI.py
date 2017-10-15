# coding=utf-8

def action1():
    print('call f1')

def action3():
    print('call f3')

listMenu = ['Please select Item ID','1: Item1','2: Item2','3: Item3']


def action2():
    print('call f2')


dictAction={1:action1, 2: action2, 3:action3}

for item in listMenu:
    print(item)
else:
    intID = int(input('input number:'))
    dictAction[intID]()