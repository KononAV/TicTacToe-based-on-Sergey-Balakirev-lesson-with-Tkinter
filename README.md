This TicTacToe game use Sergey Balakirev lesson (Python OOP course) as a base. I didnt delete abiliti to play in console with 
coords. Just comment Tkinter start part and add:

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")

Sparring part can be used too. Just activate self.sparing = True
