import random as ran
import time
from tkinter import Tk,Button as bn,DISABLED,messagebox as msg


def show_symbol(x,y):
    global fir
    global pX,pY
    global mov,pairs

    bts[x,y]['text'] = bs[x,y]
    bts[x,y].update_idletasks()

    if fir:
        pX = x
        pY = y
        fir = False
        mov += 1
    elif pX != x or pY != y:
        if bts[pX,pY]['text'] != bts[x,y]['text']:
            time.sleep(0.5)
            bts[pX,pY]['text'] = ''
            bts[x,y]['text'] = ''
        else:
            bts[pX,pY]['command'] = DISABLED
            bts[x,y]['command'] = DISABLED
            pairs += 1
            if pairs == len(bts)/2:
                msg.showinfo('Match','Number of moves:' + str(mov)\
                    ,command=close_win)
        fir = True
def close_win(self):
    root.destroy()
root = Tk()
root.title('Match')
root.resizable(False,False)
bts = {}
fir = True
pX = 0
pY = 0
mov = 0
pairs = 0
bs = {}
sym = [u'\u2702',u'\u2702',u'\u2705',u'\u2705',u'\u2708',u'\u2708',
u'\u2709',u'\u2709',u'\u270A',u'\u270A',u'\u270B',u'\u270B',
u'\u270C',u'\u270C',u'\u270F',u'\u270F',u'\u2712',u'\u2712',
u'\u2714',u'\u2714',u'\u2716',u'\u2716',u'\u2728',u'\u2728']
ran.shuffle(sym)

for x in range(6):
    for y in range(4):
        bt = bn(command=lambda x=x,y=y:show_symbol(x,y),\
            width=3,height=3)
        bt.grid(column=x,row=y)
        bts[x,y] = bt
        bs[x,y] = sym.pop()
root.mainloop()