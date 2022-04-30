import math
import random
from telnetlib import EC
from tkinter import *
from time import *
from time import sleep
from tkinter import *
import numpy

window = Tk()
window_width = 1060
window_height = 900
x_location = (window.winfo_screenwidth() - window_width) / 2
y_location = (window.winfo_screenheight() - window_height) / 2
window.geometry(f'{window_width}x{window_height}+{int(x_location)}+{int(y_location)}')
window.title("Sorting Algorithm")
window.config(background="#ffffff")
window.resizable(False, False)
canvas_height = 740
canvas_width = 1000
canvas = Canvas(window, height=canvas_height, width=canvas_width, bg="#6bbbff", bd=2)
canvas.place(x=30, y=130)

item_list = []
color_list = []

def draw(self):
    x = slider.get()
    item_list.clear()
    canvas.delete("all")
    if x > 40:
        gap_size = 1
        rotation = 90
        text_gap = 13
        font_size = 8
    else:
        rotation = 0
        text_gap = 10
        gap_size = 2
        font_size = 8

    gaps = (x + 1) * gap_size
    columns = x
    column_width = ((canvas_width - gaps) / x)
    for i in range(1, columns + 1):
        current = canvas_height - random.randint(20, 650)
        current_color_num = math.floor(current/7.3)
        string_color = "#ffffff"
        color_list.append(string_color)
        item_list.append(current)
        canvas.create_rectangle((gap_size * i) + (column_width * (i - 1) + 4), canvas_height,
                                (column_width * i) + (gap_size * i) + 4, canvas_height - item_list[i - 1],
                                outline="#6bbbff", fill="#ffffff",tags=i)
        canvas.create_text((gap_size * i) + (column_width * (i - 1) + 4) + column_width / 2 + 0.75,
                           canvas_height - item_list[i - 1] + text_gap, text=item_list[i - 1], angle=rotation,
                           font=('', font_size))


def reset():
        x = len(item_list)
        item_list.clear()
        canvas.delete("all")
        if x > 40:
            gap_size = 1
            rotation = 90
            text_gap = 13
            font_size = 8
        else:
            rotation = 0
            text_gap = 10
            gap_size = 2
            font_size = 8

        gaps = (x + 1) * gap_size
        columns = x
        column_width = ((canvas_width - gaps) / x)

        for i in range(1, columns + 1):
            curr = color_list[i]
            current = canvas_height - random.randint(10, 700)
            item_list.append(current)
            canvas.create_rectangle((gap_size * i) + (column_width * (i - 1) + 4), canvas_height,
                                    (column_width * i) + (gap_size * i) + 4, canvas_height - item_list[i - 1],
                                    outline="#6bbbff", fill=curr, tags=i)
            canvas.create_text((gap_size * i) + (column_width * (i - 1) + 4) + column_width / 2 + 0.75,
                               canvas_height - item_list[i - 1] + text_gap, text=item_list[i - 1], angle=rotation,
                               font=('', font_size))


def selection_sort():
    item_list_length = len(item_list)

    if item_list_length > 40:
        gap_size = 1
        rotation = 90
        text_gap = 13
        font_size = 8
    else:
        rotation = 0
        text_gap = 10
        gap_size = 2
        font_size = 8
    gaps = (item_list_length + 1) * gap_size
    columns = item_list_length
    column_width = ((canvas_width - gaps) / item_list_length)
    item_list.append(numpy.amax(item_list))
    for i in range(0,item_list_length+1):
        curri = color_list[i]
        min = 1000
        min_location = 0
        for j in range(i,item_list_length+1):
            canvas.create_rectangle((gap_size * j) + (column_width * (j - 1) + 4), canvas_height,
                                    (column_width * j) + (gap_size * j) + 4, canvas_height - item_list[j - 1],
                                    outline="#6bbbff", fill="#ff6b6b")

            current = item_list[j]
            sleep(speed_slider.get())
            canvas.update()
            if min > current:
                min = current
                min_location = j
            canvas.create_rectangle((gap_size * j) + (column_width * (j - 1) + 4), canvas_height,
                                    (column_width * j) + (gap_size * j) + 4, canvas_height - item_list[j - 1],
                                    outline="#6bbbff", fill="#ffffff")
            canvas.create_text((gap_size * j) + (column_width * (j - 1) + 4) + column_width / 2 + 0.75,
                               canvas_height - item_list[j - 1] + text_gap, text=item_list[j - 1], angle=rotation,
                               font=('', font_size), fill="#000000")
        canvas.create_rectangle((gap_size * i) + (column_width * (i - 1) + 4), canvas_height,
                                (column_width * i) + (gap_size * i) + 4, 0,
                                outline="#6bbbff", fill="#6bbbff")
        canvas.create_rectangle((gap_size * i) + (column_width * (i - 1) + 4), canvas_height,
                                (column_width * i) + (gap_size * i) + 4, canvas_height - item_list[i - 1],
                                outline="#6bbbff", fill="#6bff7c")
        place_holder = item_list[i]
        item_list[i]=item_list[min_location]
        item_list[min_location]=place_holder
        canvas.create_text((gap_size * i) + (column_width * (i - 1) + 4) + column_width / 2 + 0.75,
                           canvas_height - item_list[i - 1] + text_gap, text=item_list[i - 1], angle=rotation,
                          font=('', font_size), fill="#990000")
        canvas.update()


def bubble_sort():
    item_list_length = len(item_list)
    if item_list_length > 40:
        gap_size = 1
        rotation = 90
        text_gap = 13
        font_size = 8
    else:
        rotation = 0
        text_gap = 10
        gap_size = 2
        font_size = 8
    gaps = (item_list_length + 1) * gap_size
    columns = item_list_length
    column_width = ((canvas_width - gaps) / item_list_length)
    correct=2
    item_list.append(numpy.amax(item_list))
    item_list.append(numpy.amax(item_list))
    while item_list_length>0:
        item_list_length-=1
        for i in range (0, item_list_length+2):
            canvas.create_rectangle((gap_size * i) + (column_width * (i - 1) + 4), canvas_height,
                                    (column_width * i) + (gap_size * i) + 4, canvas_height - item_list[i - 1],
                                    outline="#6bbbff", fill="#ff6b6b")
            canvas.update()
            correct+=1
            if item_list[i]>item_list[i+1]:
                place_holder = item_list[i+1]
                item_list[i+1]=item_list[i]
                item_list[i]=place_holder
                correct=0
            canvas.create_rectangle((gap_size * i) + (column_width * (i - 1) + 4), canvas_height,
                                    (column_width * i) + (gap_size * i) + 4, 0,
                                    outline="#6bbbff", fill="#6bbbff")
            canvas.create_rectangle((gap_size * i) + (column_width * (i - 1) + 4), canvas_height,
                                    (column_width * i) + (gap_size * i) + 4, canvas_height - item_list[i - 1],
                                    outline="#6bbbff", fill="#ffffff")
            canvas.create_text((gap_size * i) + (column_width * (i - 1) + 4) + column_width / 2 + 0.75,
                               canvas_height - item_list[i - 1] + text_gap, text=item_list[i - 1], angle=rotation,
                               font=('', font_size), fill="#000000")
            if i == item_list_length+1:
                canvas.create_rectangle((gap_size * i) + (column_width * (i - 1) + 4), canvas_height,
                                        (column_width * i) + (gap_size * i) + 4, canvas_height - item_list[i - 1],
                                        outline="#6bbbff", fill="#ffffff")
                canvas.create_text((gap_size * i) + (column_width * (i - 1) + 4) + column_width / 2 + 0.75,
                                   canvas_height - item_list[i - 1] + text_gap, text=item_list[i - 1], angle=rotation,
                                   font=('', font_size), fill="#000000")
            sleep(speed_slider.get())
            canvas.update()


def insertion_sort():
    item_list_length = len(item_list)
    if item_list_length > 40:
        gap_size = 1
        rotation = 90
        text_gap = 13
        font_size = 8
    else:
        rotation = 0
        text_gap = 10
        gap_size = 2
        font_size = 8
    gaps = (item_list_length + 1) * gap_size
    columns = item_list_length
    column_width = ((canvas_width - gaps) / item_list_length)
    item_list.append(1)
    for i in range(1, item_list_length+1):
        if item_list[i]<item_list[i-1]:
            j=i
            while item_list[j]<item_list[j-1] and j>0:
                place_holder=item_list[j]
                canvas.create_rectangle((gap_size * j) + (column_width * (j - 1) + 4), canvas_height,
                                        (column_width * j) + (gap_size * j) + 4, 0,
                                        outline="#6bbbff", fill="#6bbbff")
                canvas.create_rectangle((gap_size * (j-1)) + (column_width * ((j-1) - 1) + 4), canvas_height,
                                        (column_width * (j-1)) + (gap_size * (j-1)) + 4, 0,
                                        outline="#6bbbff", fill="#6bbbff")
                item_list[j]=item_list[j-1]
                canvas.create_rectangle((gap_size * j) + (column_width * (j - 1) + 4), canvas_height,
                                        (column_width * j) + (gap_size * j) + 4, canvas_height - item_list[j - 1],
                                        outline="#6bbbff", fill="#ffffff")

                canvas.create_text((gap_size * j) + (column_width * (j - 1) + 4) + column_width / 2 + 0.75,
                                   canvas_height - item_list[j - 1] + text_gap, text=item_list[j - 1], angle=rotation,
                                   font=('', font_size), fill="#000000")

                item_list[j-1]=place_holder
                canvas.create_rectangle((gap_size * (j-1)) + (column_width * ((j-1) - 1) + 4), canvas_height,
                                        (column_width * (j-1)) + (gap_size * (j-1)) + 4, canvas_height - item_list[(j-1) - 1],
                                        outline="#6bbbff", fill="#6bff7c")
                canvas.update()
                sleep(speed_slider.get())
                canvas.create_rectangle((gap_size * (j - 1)) + (column_width * ((j - 1) - 1) + 4), canvas_height,
                                        (column_width * (j - 1)) + (gap_size * (j - 1)) + 4,
                                        canvas_height - item_list[(j - 1) - 1],
                                        outline="#6bbbff", fill="#ffffff")
                canvas.update()
                canvas.create_text((gap_size * (j-1)) + (column_width * ((j-1) - 1) + 4) + column_width / 2 + 0.75,
                                   canvas_height - item_list[(j-1) - 1] + text_gap, text=item_list[(j-1) - 1], angle=rotation,
                                   font=('', font_size), fill="#000000")
                j-=1
                canvas.update()
                sleep(speed_slider.get())
                canvas.update()



slider = Scale(window, from_=2, to=80, orient=HORIZONTAL, bg="#ffffff", bd=0, sliderlength=20, troughcolor="#000000",
               width=6, length=150, command=draw)
slider.place(x=300, y=40)
speed_slider = Scale(window, from_=0, to=0.1, orient=HORIZONTAL, bg="#ffffff", bd=0, sliderlength=20, troughcolor="#000000",
               width=6, length=150, resolution=0.005)
speed_slider.place(x=460, y=40)
speed_slider.set(0.01)

selection_sort_button = Button(window, text="Selection Sort", command=selection_sort, width=20, bg="#ffffff")
selection_sort_button.place(x=300, y=80)
reset_button = Button(window, text="reset", command=reset, width=20, bg="#ffffff")
reset_button.place(x=620, y= 40)
bubble_sort_button = Button(window,text="Bubble Sort", command= bubble_sort, width=20, bg="#ffffff")
bubble_sort_button.place(x=460, y=80)
insertion_sort_button = Button(window, text="Insertion Sort", command=insertion_sort, width=20, bg="#ffffff")
insertion_sort_button.place(x=620,y=80)

speed_label = Label(window, text="Set Speed", bg="#ffffff")
speed_label.place(x=510, y=15)
count_label = Label(window, text="Set Amount", bg="#ffffff")
count_label.place(x=345, y=15)
window.mainloop()
