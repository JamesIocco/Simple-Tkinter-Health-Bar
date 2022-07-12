# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:40:34 2022

@author: JamesIocco
"""
import tkinter as tk
window = tk.Tk()



def heal():
    value = int(hp["text"])
    hp["text"] = f"{value + 1}"
    
    
    
def damage():
    value = int(hp["text"])
    hp["text"] = f"{value - 1}"
    


window.rowconfigure(0,minsize=250, weight=1)
window.columnconfigure([0, 1, 2], minsize=250, weight=1)



btn_damage = tk.Button(master=window, text="-1 Health", command=damage)
btn_damage.grid(row=0, column=0, sticky="nsew")



hp = tk.Label(master=window, text="0")
hp.grid(row=0, column=1)



btn_heal = tk.Button(master=window, text="+1 Health", command=heal)
btn_heal.grid(row=0, column=2, sticky="nsew")



window.mainloop()
