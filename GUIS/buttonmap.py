import tkinter as tk
from PIL import ImageTk, Image

# button ตัวเลือกต่างๆ

def button_a1a():
    a1a = tk.Toplevel()
    label_A1a = tk.Label(a1a, text="อาคารแผนกวิชาสามัญสัมพันธ์")
    label_A1a.grid(row=0, column=0)

    image_A1a = Image.open('D:/งาน/project/GUIS/Image/1a.png')
    image_A1a = image_A1a.resize((300, 200))
    tk_image = ImageTk.PhotoImage(image_A1a)
    label = tk.Label(a1a, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.grid(row=1, column=0)

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


