from tkinter import *
from math import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
matplotlib.use('TkAgg')

root =Tk()
root.title("Решение квадратного уравнения")
root.geometry("800x800")


def text_to_lbl(event):
    global d,x1,x2,x,a,b,c,roundedx_1,rounded_x2,x_list
    x_list = []
    a=float(a_arg_entry.get())
    a_arg_entry.delete(0, END) #Очистка поля ввода
    b=float(b_arg_entry.get())
    b_arg_entry.delete(0, END) #Очистка поля ввода
    c=float(c_arg_entry.get())
    c_arg_entry.delete(0, END) #Очистка поля ввода
    d=(b**2)-4*a*c
    discriminant["text"] = d
    if d>0:
        x.grid_remove() 
        x_1 = (-b + sqrt(d)) / (2 * a) 
        x_2 = (-b - sqrt(d)) / (2 * a) 
        rounded_x1=round(x_1,3) 
        rounded_x2=round(x_2,3) 
        x_list.append(rounded_x1)
        x_list.append(rounded_x2)
        x1["text"] = f"X1: {rounded_x1}" 
        x2["text"] = f"X2: {rounded_x2}" 
        x1.grid() 
        x2.grid() 
    elif d==0:
        x1.grid_remove()
        x2.grid_remove() 
        x1 = x2 = (-b / 2*a) 
        rounded_x1 = round(x1, 3)
        rounded_x2 = round(x2, 3)
        x_list.append(rounded_x1)
        x_list.append(rounded_x2)
        x["text"] = f"x: {x1}" 
        x.grid() 
    else:
        x.grid_remove() 
        x1.grid_remove() 
        x2.grid_remove() 
        lblimage.grid_remove()
        dd="Корень вычеслить невозможно!"
        x["text"] = dd 
        x.grid() 


def create_graphic(event):
        global y,picture, labelimage
        y0=0,0
        points=x_list[0],x_list[1]
        print(points)
        freq = 100
        xi = np.linspace(x_list[0], x_list[1], freq)
        if x_list[1]>x_list[0]:
            y = [-((a * t ** 2) + (b * t) + c) for t in xi]
            plt.scatter(points, y0, color='red')
        else:
            plt.scatter(points, y0, color='red')
            y = [((a * t ** 2) + (b * t) + c) for t in xi]
        if x_list[1]==x_list[0]:
            if a>0:
                xii = np.linspace(x_list[0], -x_list[1], freq)
                yy=[t**2 for t in xii]
                plt.scatter(points, y0, color='red')
                plt.plot(xii+x_list[0],yy)
            else:
                xii = np.linspace(x_list[0], -x_list[1], freq)
                yy = [-t ** 2 for t in xii]
                plt.scatter(points, y0, color='red')
                plt.plot(xii + x_list[0], yy)
        plt.plot(xi, y)
        plt.tick_params(axis='both', labelsize=14)
        plt.grid(True)
        ax = plt.gca()
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        plt.savefig('graph.png')
        image = Image.open("graph.png")
        picture = ImageTk.PhotoImage(image)
        labelimage = Label(root, image=picture)
        labelimage.image =picture
        labelimage.grid(row=9, rowspan=5, column=0, columnspan=10)



dformula = Label(root, text="уравнение = a*x^2+b*x+c=0", font = "Arial 20")
formula = Label(root, text ="формула дискриминанта - D=b^2-4*a*c", font="Arial 15")
txta=Label(root,text="a:",font="Arial 20")
txtb=Label(root,text="b:",font="Arial 20")
txtc=Label(root,text="c:",font="Arial 20")
result=Label(root, text="Дискременант равен: ",font="Arial 15")
discriminant = Label(root, text="", font = "Arial 25")
x=Label(root,text="",font="Arial 15")
x1=Label(root, text="",font="Arial 15")
x2=Label(root, text="",font="Arial 15")


btn_calculate = Button(root, text="вычислить", font="Arial 15")
btn_graphics = Button(root, text="Показать график", font="Arial 15")

a_arg_entry = Entry(root, bg="white")
b_arg_entry = Entry(root, bg="white")
c_arg_entry = Entry(root, bg="white")

dformula.grid(row=0,column=2,sticky="e")
formula.grid(row=1,column=2)
txta.grid(row=2,column=0)
txtb.grid(row=3,column=0)
txtc.grid(row=4,column=0)
result.grid(row=7,column=1)
x1.grid(row=8,column=1,columnspan=5)
x2.grid(row=9,column=1,columnspan=5)
x.grid(row =8,column=1)

a_arg_entry.grid(row=2,column=1,rowspan=1)
b_arg_entry.grid(row=3,column=1,rowspan=1)
c_arg_entry.grid(row=4,column=1,rowspan=1)


btn_calculate.bind("<Button-1>",text_to_lbl)
btn_calculate.grid(row=5,column=1,columnspan=1)
btn_graphics.bind("<Button-1>",create_graphic)
btn_graphics.grid(row=6,column=1,columnspan=1)

root.mainloop()