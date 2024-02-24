from customtkinter import *
from tkinter import messagebox

window = CTk()
window.resizable()
window.title('TicTacToe')


def check_winner():
    winning_possibilities = [
        (b1, b2, b3), (b4, b5, b6), (b7, b8, b9),  # rows
        (b1, b4, b7), (b2, b5, b8), (b3, b6, b9),  # columns
        (b1, b5, b9), (b3, b5, b7)  # diagonals
    ]

    for possibility in winning_possibilities:
        if possibility[0].cget('text') == possibility[1].cget('text') == possibility[2].cget('text') != ' ':
            possibility[0].configure(fg_color='white')
            possibility[1].configure(fg_color='white')
            possibility[2].configure(fg_color='white')
            for btn in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
                btn.configure(state=DISABLED, text=' ')
            return True
    return False


current_player = 'X'
count = 0

def click_button(button):
    global current_player, count
    if button.cget('text') == ' ':  # Check if the button is empty
        button.configure(text=current_player)
        current_player = 'O' if current_player == 'X' else 'X'
        count += 1
    else:
        messagebox.showerror(title='error',  message="This button is already taken!")
    
    if check_winner():
        btn_status.configure(text= f'Player {'O' if current_player == 'X' else 'X'} wins! \n Play again')
        btn_status.grid(columnspan=5, row=5)
        for btn in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
            btn.configure(state=DISABLED)

    elif count == 9:
        btn_status.configure(text= f'Draw! \n Play again')
        btn_status.grid(columnspan=5, row=5)
        for btn in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
            btn.configure(state=DISABLED, text=' ')


def play_again():
    global current_player, count
    for btn in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        btn['text'] = ' '
        btn.configure(state=NORMAL)
        btn.configure(fg_color='grey')
    
    current_player = 'X'
    count = 0
    btn_status.configure(text='')
    btn_status.grid_forget()


# title
CTkLabel(window, text='TicTacToe', font=('ds-digital', 32,'bold')).grid(column=2, row=1, pady=10)

# buttons
b1 = CTkButton(window, text=" ", font=('ds-digital', 32,'bold'), height=100,width=100, command= lambda:click_button(b1),bg_color='black', fg_color='grey')
b1.grid(row=2, column=1, padx=10, pady=10)
b2 = CTkButton(window, text=' ', font=('ds-digital', 32,'bold'), height=100,width=100, command= lambda:click_button(b2),bg_color='black', fg_color='grey')
b2.grid(row=2, column=2, padx=10, pady=10)
b3 = CTkButton(window, text=' ', font=('ds-digital', 32,'bold'), height=100,width=100, command= lambda:click_button(b3),bg_color='black', fg_color='grey')
b3.grid(row=2, column=3, padx=10, pady=10)

b4 = CTkButton(window, text=' ', font=('ds-digital', 32,'bold'), height=100,width=100, command= lambda:click_button(b4),bg_color='black', fg_color='grey')
b4.grid(row=3, column=1, padx=10, pady=10)
b5 = CTkButton(window, text=' ', font=('ds-digital', 32,'bold'), height=100,width=100, command= lambda:click_button(b5),bg_color='black', fg_color='grey')
b5.grid(row=3, column=2, padx=10, pady=10)
b6 = CTkButton(window, text=' ', font=('ds-digital', 32,'bold'), height=100,width=100, command= lambda:click_button(b6),bg_color='black', fg_color='grey')
b6.grid(row=3, column=3, padx=10, pady=10)

b7 = CTkButton(window, text=' ', font=('ds-digital', 32,'bold'), height=100,width=100, command= lambda:click_button(b7),bg_color='black', fg_color='grey')
b7.grid(row=4, column=1, padx=10, pady=10)
b8 = CTkButton(window, text=' ', font=('ds-digital', 32,'bold'), height=100,width=100, command= lambda:click_button(b8),bg_color='black', fg_color='grey')
b8.grid(row=4, column=2, padx=10, pady=10)
b9 = CTkButton(window, text=' ', font=('ds-digital', 32,'bold'), height=100,width=100, command= lambda:click_button(b9),bg_color='black', fg_color='grey')
b9.grid(row=4, column=3, padx=10, pady=10)

btn_status = CTkButton(window, font=('ds-digital', 26,'bold') , command=play_again)

window.mainloop()