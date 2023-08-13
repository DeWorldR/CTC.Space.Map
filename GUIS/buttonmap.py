import tkinter as tk
import pygame
from PIL import ImageTk, Image

def close_gui(button_to_close):
    button_to_close.destroy()

# button ตัวเลือกต่างๆ

def button_a1a():
    a1a = tk.Toplevel()
    a1a.state('zoomed')
    label_A1a = tk.Label(a1a, text="อาคารวิษณุพัฒนา")
    label_A1a.grid(row=0, column=0)

    image_A1a = Image.open('D:/งาน/project/GUIS/Image/1a.png')
    image_A1a = image_A1a.resize((300, 200))
    tk_image = ImageTk.PhotoImage(image_A1a)
    label = tk.Label(a1a, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.grid(row=1, column=0)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button5.mp3')
    pygame.mixer.music.play()

    a1a.after(300000, lambda: close_gui(a1a))


def button_a1b():
    a1b = tk.Toplevel()
    label_A1b = tk.Label(a1b, text="อาคารเรียน3")
    label_A1b.grid(row=0, column=0)

    image_A1b = Image.open('D:/งาน/project/GUIS/Image/1a.png')
    image_A1b = image_A1b.resize((300, 200))
    tk_image = ImageTk.PhotoImage(image_A1b)
    label = tk.Label(a1b, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.grid(row=1, column=0)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button6.mp3')
    pygame.mixer.music.play()

    a1b.after(300000, lambda: close_gui(a1b))

def button_a1c():
    a1c = tk.Toplevel()
    label_A1c = tk.Label(a1c, text="อาคารปฎิบัติการช่างไฟฟ้า")
    label_A1c.grid(row=0, column=0)

    image_A1c = Image.open('D:/งาน/project/GUIS/Image/1a.png')
    image_A1c = image_A1c.resize((300, 200))
    tk_image = ImageTk.PhotoImage(image_A1c)
    label = tk.Label(a1c, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.grid(row=1, column=0)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button7.mp3')
    pygame.mixer.music.play()

    a1c.after(300000, lambda: close_gui(a1c))

def button_a1d():
    a1d = tk.Toplevel()
    label_A1d = tk.Label(a1d, text="อาคารปฎิบัติการช่างก่อสร้าง")
    label_A1d.grid(row=0, column=0)

    image_A1d = Image.open('D:/งาน/project/GUIS/Image/1a.png')
    image_A1d = image_A1d.resize((300, 200))
    tk_image = ImageTk.PhotoImage(image_A1d)
    label = tk.Label(a1d, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.grid(row=1, column=0)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button8.mp3')
    pygame.mixer.music.play()

    a1d.after(300000, lambda: close_gui(a1d))

def button_a1e():
    a1e = tk.Toplevel()
    label_A1e = tk.Label(a1e, text="อาคารปฎิบัติการช่างกลโรงงาน")
    label_A1e.grid(row=0, column=0)

    image_A1e = Image.open('D:/งาน/project/GUIS/Image/1a.png')
    image_A1e = image_A1e.resize((300, 200))
    tk_image = ImageTk.PhotoImage(image_A1e)
    label = tk.Label(a1e, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.grid(row=1, column=0)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button9.mp3')
    pygame.mixer.music.play()

    a1e.after(300000, lambda: close_gui(a1e))

def button_a1f():
    a1f = tk.Toplevel()
    label_A1f = tk.Label(a1f, text="อาคารปฎิบัติการอิเล็กทรอนิกส์")
    label_A1f.grid(row=0, column=0)

    image_A1f = Image.open('D:/งาน/project/GUIS/Image/1a.png')
    image_A1f = image_A1f.resize((300, 200))
    tk_image = ImageTk.PhotoImage(image_A1f)
    label = tk.Label(a1f, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.grid(row=1, column=0)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button10.mp3')
    pygame.mixer.music.play()

    a1f.after(300000, lambda: close_gui(a1f))

def button_a1g():
    a1g = tk.Toplevel()
    label_A1g = tk.Label(a1g, text="อาคารปฎิบัติการช่างยนต์")
    label_A1g.grid(row=0, column=0)

    image_A1g = Image.open('D:/งาน/project/GUIS/Image/1a.png')
    image_A1g = image_A1g.resize((300, 200))
    tk_image = ImageTk.PhotoImage(image_A1g)
    label = tk.Label(a1g, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.grid(row=1, column=0)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button11.mp3')
    pygame.mixer.music.play()

    a1g.after(300000, lambda: close_gui(a1g))
def button_a1h():
    a1h = tk.Toplevel()
    label_A1h = tk.Label(a1h, text="อาคารปฎิบัติการเทคนิคพื้นฐาน")
    label_A1h.grid(row=0, column=0)

    image_A1h = Image.open('D:/งาน/project/GUIS/Image/1a.png')
    image_A1h = image_A1h.resize((300, 200))
    tk_image = ImageTk.PhotoImage(image_A1h)
    label = tk.Label(a1h, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.grid(row=1, column=0)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button12.mp3')
    pygame.mixer.music.play()

    a1h.after(300000, lambda: close_gui(a1h))

def button_a1i():
    a1i = tk.Toplevel()
    label_A1i = tk.Label(a1i, text="อาคารปฎิบัติการอเนกประสงค์")
    label_A1i.grid(row=0, column=0)

    image_A1i = Image.open('D:/งาน/project/GUIS/Image/1a.png')
    image_A1i = image_A1i.resize((300, 200))
    tk_image = ImageTk.PhotoImage(image_A1i)
    label = tk.Label(a1i, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.grid(row=1, column=0)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button13.mp3')
    pygame.mixer.music.play()

    a1i.after(300000, lambda: close_gui(a1i))


