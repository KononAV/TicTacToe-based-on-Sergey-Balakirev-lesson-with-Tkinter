from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter.ttk import Style
from tkinter.messagebox import showinfo, showerror, askyesno

import random


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = ' '
    HUMAN_X = 'x'
    COMPUTER_O = 'o'

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self.win = 0
        self.sparing = False

    def __getitem__(self, item):
        self.check_index(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.check_index(key)
        self.pole[key[0]][key[1]].value = value
        self.win_update()

    @classmethod
    def check_index(cls, indx):
        if 0 > indx[0] > 3 or 0 > indx[1] > 3:
            raise IndexError('plohoi index')

    def init(self):
        for i in self.pole:
            for j in i:
                j.value = self.FREE_CELL
        self.win = 0

    def show(self):
        for i in self.pole:
            for j in i:
                print(j.value, end=' ')
            print()
        print('--------------')

    def human_go(self, coords):
        if not self:
            return

        while True:

            if self[coords[0], coords[1]] == self.FREE_CELL:
                self[coords[0], coords[1]] = self.HUMAN_X
                break

    def computer_go(self, coords=None):
        if not self:
            return
        while True:
            if not self.sparing:
                a = random.randint(0, 2)
                b = random.randint(0, 2)

                if self[a, b] != self.FREE_CELL:
                    continue
                self[a, b] = self.COMPUTER_O
                self.coor = [a, b]

                break
            else:
                if self[coords[0], coords[1]] == self.FREE_CELL:
                    self[coords[0], coords[1]] = self.COMPUTER_O
                    break

    def win_update(self):

        for i in self.pole:
            if all(x.value == self.HUMAN_X for x in i):
                self.win = 1
                return
            if all(x.value == self.COMPUTER_O for x in i):
                self.win = 2
                return

        for i in range(3):
            if all(x.value == self.HUMAN_X for x in (row[i] for row in self.pole)):
                self.win = 1
                return
            if all(x.value == self.COMPUTER_O for x in (row[i] for row in self.pole)):
                self.win = 2
                return

            if all(self.pole[i][i].value == self.HUMAN_X for i in range(3)) or \
                    all(self.pole[i][-1 - i].value == self.HUMAN_X for i in range(3)):
                self.win = 1
                return
            if all(self.pole[i][i].value == self.COMPUTER_O for i in range(3)) or \
                    all(self.pole[i][-1 - i].value == self.COMPUTER_O for i in range(3)):
                self.win = 2
                return

            if all(x.value != self.FREE_CELL for row in self.pole for x in row):
                self.win = 3

    @property
    def is_human_win(self):
        return self.win == 1

    @property
    def is_computer_win(self):
        return self.win == 2

    @property
    def is_draw(self):
        return self.win == 3

    def __bool__(self):
        return self.win == 0 and self.win not in (1, 2, 3, 4)


class Window:
    def __init__(self):
        self.i = 1

        self.first_window()

    def first_window(self):
        self.root = Tk()
        self.root.title('Tic')
        self.root.geometry('200x200')
        self.root.resizable(False, False)

        self.label = None
        self.game = TicTacToe()
        self.game.init()
        self.first_label = ttk.Label(self.root, text='v.0.0.1')
        self.first_label.place(relx=0.97, rely=0.9,anchor = NE)

        self.lable_cybe = ttk.Label(self.root, text=
        '''Start cybersport
         train''')
        self.lable_cybe.pack(anchor=S)
        self.button1 = ttk.Button(self.root, text='sparing mode', command=self.sparing)
        self.button1.place(relx=0.302, rely=0.2)
        self.button2 = ttk.Button(self.root, text='single mode', command=self.single)
        self.button2.place(relx=0.32, rely=0.4)
        self.button3 = ttk.Button(self.root, text='TicTacToe rules', command=self.rules)
        self.button3.place(relx=0.282, rely=0.7)

    def rules(self):

        self.rules_label = ttk.Label(text=
                                     '''   TicTacToe rules
  Players take turns putting their 
  marks in empty squares. The 
  first player to get 3 of her 
  marks in a row is the winner. 
  When all 9 squares are full, the
  game is over. If no player has 
  3 marks in a row, the game ends in
  a tie.


  ''')
        self.rules_label.place(x=0)
        self.but = Button(self.root, bg='white smoke', text='<-', width=6, command=self.destroing_rules)

        self.but.place(x=140, y=170)

    def destroing_rules(self):
        self.rules_label.destroy()
        self.but.destroy()

    def window(self):
        self.lable_cybe.destroy()
        self.main_menu = Menu()
        self.game.init()
        self.destroing()
        self.buttons()
        self.root.config(menu=self.main_menu)
        self.first_label.place(relx=0.97, rely=0.89,anchor = NE)

    def destroing(self):
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()

    def reset(self):
        if self.label:
            self.label.destroy()
        self.game.init()
        self.buttons()

    def star_menu(self):
        if self.label:
            self.label.destroy()
        self.window()

        self.main_menu.destroy()
        main_menu = Menu()
        main_menu.add_cascade(label='reset', command=self.reset)

        if self.game.sparing:
            main_menu.add_cascade(label='single mode', command=self.single)
            self.root.config(menu=main_menu)
        else:
            main_menu.add_cascade(label='sparing mode', command=self.sparing)
        self.root.config(menu=main_menu)



    def sparing(self):
        self.game.sparing = True
        self.star_menu()

    def single(self):
        self.game.sparing = False
        self.star_menu()


    def buttons(self):
        bton0 = ttk.Button(self.root, text=self.game.pole[0][0].value, width=5,
                           command=lambda: (self.click([0, 0], bton0)))
        bton0.place(x=30)
        bton1 = ttk.Button(self.root, text=self.game.pole[0][1].value, width=5,
                           command=lambda: (self.click([0, 1], bton1)))
        bton1.place(x=80)
        bton2 = ttk.Button(self.root, text=self.game.pole[0][2].value, width=5,
                           command=lambda: (self.click([0, 2], bton2)))
        bton2.place(x=130)

        bton3 = ttk.Button(self.root, text=self.game.pole[1][0].value, width=5,
                           command=lambda: (self.click([1, 0], bton3)))
        bton3.place(x=30, y=30)
        bton4 = ttk.Button(self.root, text=self.game.pole[1][1].value, width=5,
                           command=lambda: (self.click([1, 1], bton4)))
        bton4.place(x=80, y=30)
        bton5 = ttk.Button(self.root, text=self.game.pole[1][2].value, width=5,
                           command=lambda: (self.click([1, 2], bton5)))
        bton5.place(x=130, y=30)

        bton6 = ttk.Button(self.root, text=self.game.pole[2][0].value, width=5,
                           command=lambda: (self.click([2, 0], bton6)))
        bton6.place(x=30, y=60)
        bton7 = ttk.Button(self.root, text=self.game.pole[2][1].value, width=5,
                           command=lambda: (self.click([2, 1], bton7)))
        bton7.place(x=80, y=60)
        bton8 = ttk.Button(self.root, text=self.game.pole[2][2].value, width=5,
                           command=lambda: (self.click([2, 2], bton8)))
        bton8.place(x=130, y=60)

    def click(self, args, b):
        #print(self.game.show())  #consol version

        if self.game.pole[args[0]][args[1]].value == self.game.FREE_CELL:

            if not self.game.sparing:
                self.game.human_go(args)
                self.game.computer_go()
            else:
                if self.i % 2 != 0:
                    self.i += 1
                    self.game.human_go(args)
                else:
                    self.i += 1
                    self.game.computer_go(args)
            self.buttons()
            if self.game.win != 0:
                self.win_show()
        else:
            showerror(':)', 'zantato')
            return

    def win_show(self):
        self.label = ttk.Label(self.root, text='''>>>Click reset if you want
         to reset
>>>Choose game mode to
         change''')
        self.label.place(relx=0, rely=0.6)
        if self.game.is_human_win and self.game.sparing:
            showinfo('hooray!', "Победили х")
        elif self.game.is_human_win:
            showinfo('hooray!', "Поздравляем! Вы победили!")
        elif self.game.is_computer_win and self.game.sparing:
            showinfo('hooray!', 'Победили нулики')
        elif self.game.is_computer_win:
            showinfo('hooray!', "Вы проиграли!")
        else:
            showinfo('ugh', "Ничья.")

    def start(self):
        self.root.mainloop()


play = Window()
play.start()
