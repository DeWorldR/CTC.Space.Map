import tkinter as tk
import pygame
import buttonweb as bw
from PIL import ImageTk, Image

def close_gui(button_to_close):
    button_to_close.destroy()

# button ตัวเลือกต่างๆ

def button_a1a():
    a1a = tk.Toplevel()
    a1a.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_a1a = tk.Label(a1a, image=background_photo)
    label_background_a1a.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_a1a.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/a1a.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(a1a, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=5)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/a1b.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(a1a, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=415)

    text_3 = Image.open('D:/งาน/project/GUIS/Image/Qrcode/img1.png')
    text_3 = text_3.resize((350, 350))
    tk_image = ImageTk.PhotoImage(text_3)
    label = tk.Label(a1a, image=tk_image)
    label.image = tk_image
    label.place(x=880, y=640)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonmap.png')
    button_1 = button_1.resize((600, 200))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(a1a, image=tk_image, command= bw.a1a)
    label.image = tk_image
    label.place(x=1280, y=790)

    button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_2 = button_2.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_2)
    label = tk.Button(a1a, image=tk_image, command=lambda: close_gui(a1a))
    label.image = tk_image
    label.place(x=1, y=890)

    image_A1a = Image.open('D:/งาน/project/GUIS/Image/imageM/a1.jpg')
    image_A1a = image_A1a.resize((750, 600))
    tk_image = ImageTk.PhotoImage(image_A1a)
    label = tk.Label(a1a, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=1, y=1)

    image_A2a = Image.open('D:/งาน/project/GUIS/Image/imageM/a2.jpg')
    image_A2a = image_A2a.resize((475, 300))
    tk_image = ImageTk.PhotoImage(image_A2a)
    label = tk.Label(a1a, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=1)

    image_A3a = Image.open('D:/งาน/project/GUIS/Image/imageM/a3.jpg')
    image_A3a = image_A3a.resize((475, 290))
    tk_image = ImageTk.PhotoImage(image_A3a)
    label = tk.Label(a1a, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=310)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button5.mp3')
    pygame.mixer.music.play()

    a1a.after(300000, lambda: close_gui(a1a))
    


def button_a1b():
    a1b = tk.Toplevel()
    a1b.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_a1b = tk.Label(a1b, image=background_photo)
    label_background_a1b.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_a1b.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/a2a.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(a1b, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=5)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/a2b.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(a1b, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=415)

    text_3 = Image.open('D:/งาน/project/GUIS/Image/Qrcode/img2.png')
    text_3 = text_3.resize((350, 350))
    tk_image = ImageTk.PhotoImage(text_3)
    label = tk.Label(a1b, image=tk_image)
    label.image = tk_image
    label.place(x=880, y=640)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonmap.png')
    button_1 = button_1.resize((600, 200))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(a1b, image=tk_image, command= bw.a1b)
    label.image = tk_image
    label.place(x=1280, y=790)

    button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_2 = button_2.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_2)
    label = tk.Button(a1b, image=tk_image, command=lambda: close_gui(a1b))
    label.image = tk_image
    label.place(x=1, y=890)
    

    image_A1b = Image.open('D:/งาน/project/GUIS/Image/imageM/b1.jpg')
    image_A1b = image_A1b.resize((750, 600))
    tk_image = ImageTk.PhotoImage(image_A1b)
    label = tk.Label(a1b, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=1, y=1)

    image_A2b = Image.open('D:/งาน/project/GUIS/Image/imageM/b2.jpg')
    image_A2b = image_A2b.resize((475, 300))
    tk_image = ImageTk.PhotoImage(image_A2b)
    label = tk.Label(a1b, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=1)

    image_A3b = Image.open('D:/งาน/project/GUIS/Image/imageM/b3.jpg')
    image_A3b = image_A3b.resize((475, 290))
    tk_image = ImageTk.PhotoImage(image_A3b)
    label = tk.Label(a1b, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=310)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button6.mp3')
    pygame.mixer.music.play()

    a1b.after(300000, lambda: close_gui(a1b))

def button_a1c():
    a1c = tk.Toplevel()
    a1c.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_a1c = tk.Label(a1c, image=background_photo)
    label_background_a1c.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_a1c.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/a3a.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(a1c, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=5)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/a3b.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(a1c, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=415)

    text_3 = Image.open('D:/งาน/project/GUIS/Image/Qrcode/img3.png')
    text_3 = text_3.resize((350, 350))
    tk_image = ImageTk.PhotoImage(text_3)
    label = tk.Label(a1c, image=tk_image)
    label.image = tk_image
    label.place(x=880, y=640)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonmap.png')
    button_1 = button_1.resize((600, 200))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(a1c, image=tk_image, command= bw.a1c)
    label.image = tk_image
    label.place(x=1280, y=790)

    button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_2 = button_2.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_2)
    label = tk.Button(a1c, image=tk_image, command=lambda: close_gui(a1c))
    label.image = tk_image
    label.place(x=1, y=890)

    label_A1c = tk.Label(a1c, text="อาคารปฎิบัติการช่างไฟฟ้า")
    label_A1c.place(x=0, y=0)

    image_A1c = Image.open('D:/งาน/project/GUIS/Image/imageM/c1.jpg')
    image_A1c = image_A1c.resize((750, 600))
    tk_image = ImageTk.PhotoImage(image_A1c)
    label = tk.Label(a1c, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=1, y=1)

    image_A2c = Image.open('D:/งาน/project/GUIS/Image/imageM/c2.jpg')
    image_A2c = image_A2c.resize((475, 300))
    tk_image = ImageTk.PhotoImage(image_A2c)
    label = tk.Label(a1c, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=1)

    image_A3c = Image.open('D:/งาน/project/GUIS/Image/imageM/c3.jpg')
    image_A3c = image_A3c.resize((475, 290))
    tk_image = ImageTk.PhotoImage(image_A3c)
    label = tk.Label(a1c, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=310)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button7.mp3')
    pygame.mixer.music.play()

    a1c.after(300000, lambda: close_gui(a1c))

def button_a1d():
    a1d = tk.Toplevel()
    a1d.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_a1d = tk.Label(a1d, image=background_photo)
    label_background_a1d.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_a1d.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/a4a.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(a1d, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=5)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/a4b.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(a1d, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=415)

    text_3 = Image.open('D:/งาน/project/GUIS/Image/Qrcode/img4.png')
    text_3 = text_3.resize((350, 350))
    tk_image = ImageTk.PhotoImage(text_3)
    label = tk.Label(a1d, image=tk_image)
    label.image = tk_image
    label.place(x=880, y=640)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonmap.png')
    button_1 = button_1.resize((600, 200))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(a1d, image=tk_image, command= bw.a1d)
    label.image = tk_image
    label.place(x=1280, y=790)

    button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_2 = button_2.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_2)
    label = tk.Button(a1d, image=tk_image, command=lambda: close_gui(a1d))
    label.image = tk_image
    label.place(x=1, y=890)

    label_A1d = tk.Label(a1d, text="อาคารปฎิบัติการช่างก่อสร้าง")
    label_A1d.place(x=0, y=0)

    image_A1d = Image.open('D:/งาน/project/GUIS/Image/imageM/d1.jpg')
    image_A1d = image_A1d.resize((750, 600))
    tk_image = ImageTk.PhotoImage(image_A1d)
    label = tk.Label(a1d, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=1, y=1)

    image_A2d = Image.open('D:/งาน/project/GUIS/Image/imageM/d2.jpg')
    image_A2d = image_A2d.resize((475, 300))
    tk_image = ImageTk.PhotoImage(image_A2d)
    label = tk.Label(a1d, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=1)

    image_A3d = Image.open('D:/งาน/project/GUIS/Image/imageM/d3.jpg')
    image_A3d = image_A3d.resize((475, 290))
    tk_image = ImageTk.PhotoImage(image_A3d)
    label = tk.Label(a1d, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=310)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button8.mp3')
    pygame.mixer.music.play()

    a1d.after(300000, lambda: close_gui(a1d))

def button_a1e():
    a1e = tk.Toplevel()
    a1e.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_a1e = tk.Label(a1e, image=background_photo)
    label_background_a1e.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_a1e.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/a5a.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(a1e, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=5)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/a5b.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(a1e, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=415)

    text_3 = Image.open('D:/งาน/project/GUIS/Image/Qrcode/img5.png')
    text_3 = text_3.resize((350, 350))
    tk_image = ImageTk.PhotoImage(text_3)
    label = tk.Label(a1e, image=tk_image)
    label.image = tk_image
    label.place(x=880, y=640)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonmap.png')
    button_1 = button_1.resize((600, 200))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(a1e, image=tk_image, command= bw.a1e)
    label.image = tk_image
    label.place(x=1280, y=790)

    button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_2 = button_2.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_2)
    label = tk.Button(a1e, image=tk_image, command=lambda: close_gui(a1e))
    label.image = tk_image
    label.place(x=1, y=890)

    image_A1e = Image.open('D:/งาน/project/GUIS/Image/imageM/e1.jpg')
    image_A1e = image_A1e.resize((750, 600))
    tk_image = ImageTk.PhotoImage(image_A1e)
    label = tk.Label(a1e, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=1, y=1)

    image_A2e = Image.open('D:/งาน/project/GUIS/Image/imageM/e2.jpg')
    image_A2e = image_A2e.resize((475, 300))
    tk_image = ImageTk.PhotoImage(image_A2e)
    label = tk.Label(a1e, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=1)

    image_A3e = Image.open('D:/งาน/project/GUIS/Image/imageM/e3.jpg')
    image_A3e = image_A3e.resize((475, 290))
    tk_image = ImageTk.PhotoImage(image_A3e)
    label = tk.Label(a1e, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=310)


    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button9.mp3')
    pygame.mixer.music.play()

    a1e.after(300000, lambda: close_gui(a1e))

def button_a1f():
    a1f = tk.Toplevel()
    a1f.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_a1f = tk.Label(a1f, image=background_photo)
    label_background_a1f.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_a1f.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/a6a.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(a1f, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=5)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/a6b.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(a1f, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=415)

    text_3 = Image.open('D:/งาน/project/GUIS/Image/Qrcode/img6.png')
    text_3 = text_3.resize((350, 350))
    tk_image = ImageTk.PhotoImage(text_3)
    label = tk.Label(a1f, image=tk_image)
    label.image = tk_image
    label.place(x=880, y=640)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonmap.png')
    button_1 = button_1.resize((600, 200))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(a1f, image=tk_image, command= bw.a1f)
    label.image = tk_image
    label.place(x=1280, y=790)

    button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_2 = button_2.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_2)
    label = tk.Button(a1f, image=tk_image, command=lambda: close_gui(a1f))
    label.image = tk_image
    label.place(x=1, y=890)

    image_A1f = Image.open('D:/งาน/project/GUIS/Image/imageM/f1.jpg')
    image_A1f = image_A1f.resize((750, 600))
    tk_image = ImageTk.PhotoImage(image_A1f)
    label = tk.Label(a1f, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=1, y=1)

    image_A2f = Image.open('D:/งาน/project/GUIS/Image/imageM/f2.jpg')
    image_A2f = image_A2f.resize((475, 300))
    tk_image = ImageTk.PhotoImage(image_A2f)
    label = tk.Label(a1f, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=1)

    image_A3f = Image.open('D:/งาน/project/GUIS/Image/imageM/f3.jpg')
    image_A3f = image_A3f.resize((475, 290))
    tk_image = ImageTk.PhotoImage(image_A3f)
    label = tk.Label(a1f, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=310)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button10.mp3')
    pygame.mixer.music.play()

    a1f.after(300000, lambda: close_gui(a1f))

def button_a1g():
    a1g = tk.Toplevel()
    a1g.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_a1g = tk.Label(a1g, image=background_photo)
    label_background_a1g.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_a1g.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/a7a.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(a1g, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=5)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/a7b.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(a1g, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=415)

    text_3 = Image.open('D:/งาน/project/GUIS/Image/Qrcode/img7.png')
    text_3 = text_3.resize((350, 350))
    tk_image = ImageTk.PhotoImage(text_3)
    label = tk.Label(a1g, image=tk_image)
    label.image = tk_image
    label.place(x=880, y=640)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonmap.png')
    button_1 = button_1.resize((600, 200))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(a1g, image=tk_image, command= bw.a1g)
    label.image = tk_image
    label.place(x=1280, y=790)

    button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_2 = button_2.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_2)
    label = tk.Button(a1g, image=tk_image, command=lambda: close_gui(a1g))
    label.image = tk_image
    label.place(x=1, y=890)

    image_A1g = Image.open('D:/งาน/project/GUIS/Image/imageM/g1.jpg')
    image_A1g = image_A1g.resize((750, 600))
    tk_image = ImageTk.PhotoImage(image_A1g)
    label = tk.Label(a1g, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=1, y=1)

    image_A2g = Image.open('D:/งาน/project/GUIS/Image/imageM/g2.jpg')
    image_A2g = image_A2g.resize((475, 300))
    tk_image = ImageTk.PhotoImage(image_A2g)
    label = tk.Label(a1g, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=1)

    image_A3g = Image.open('D:/งาน/project/GUIS/Image/imageM/f3.jpg')
    image_A3g = image_A3g.resize((475, 290))
    tk_image = ImageTk.PhotoImage(image_A3g)
    label = tk.Label(a1g, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=310)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button11.mp3')
    pygame.mixer.music.play()

    a1g.after(300000, lambda: close_gui(a1g))

def button_a1h():
    a1h = tk.Toplevel()
    a1h.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_a1h = tk.Label(a1h, image=background_photo)
    label_background_a1h.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_a1h.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/a8a.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(a1h, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=5)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/a8b.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(a1h, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=415)

    text_3 = Image.open('D:/งาน/project/GUIS/Image/Qrcode/img8.png')
    text_3 = text_3.resize((350, 350))
    tk_image = ImageTk.PhotoImage(text_3)
    label = tk.Label(a1h, image=tk_image)
    label.image = tk_image
    label.place(x=880, y=640)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonmap.png')
    button_1 = button_1.resize((600, 200))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(a1h, image=tk_image, command= bw.a1h)
    label.image = tk_image
    label.place(x=1280, y=790)

    button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_2 = button_2.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_2)
    label = tk.Button(a1h, image=tk_image, command=lambda: close_gui(a1h))
    label.image = tk_image
    label.place(x=1, y=890)

    image_A1h = Image.open('D:/งาน/project/GUIS/Image/imageM/h1.jpg')
    image_A1h = image_A1h.resize((750, 600))
    tk_image = ImageTk.PhotoImage(image_A1h)
    label = tk.Label(a1h, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=1, y=1)

    image_A2h = Image.open('D:/งาน/project/GUIS/Image/imageM/h2.jpg')
    image_A2h = image_A2h.resize((475, 300))
    tk_image = ImageTk.PhotoImage(image_A2h)
    label = tk.Label(a1h, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=1)

    image_A3h = Image.open('D:/งาน/project/GUIS/Image/imageM/h3.jpg')
    image_A3h = image_A3h.resize((475, 290))
    tk_image = ImageTk.PhotoImage(image_A3h)
    label = tk.Label(a1h, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=310)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button12.mp3')
    pygame.mixer.music.play()

    a1h.after(300000, lambda: close_gui(a1h))

def button_a1i():
    a1i = tk.Toplevel()
    a1i.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_a1i = tk.Label(a1i, image=background_photo)
    label_background_a1i.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_a1i.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/a9a.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(a1i, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=5)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/a9b.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(a1i, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=415)

    text_3 = Image.open('D:/งาน/project/GUIS/Image/Qrcode/img9.png')
    text_3 = text_3.resize((350, 350))
    tk_image = ImageTk.PhotoImage(text_3)
    label = tk.Label(a1i, image=tk_image)
    label.image = tk_image
    label.place(x=880, y=640)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonmap.png')
    button_1 = button_1.resize((600, 200))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(a1i, image=tk_image, command= bw.a1i)
    label.image = tk_image
    label.place(x=1280, y=790)

    button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_2 = button_2.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_2)
    label = tk.Button(a1i, image=tk_image, command=lambda: close_gui(a1i))
    label.image = tk_image
    label.place(x=1, y=890)

    image_A1i = Image.open('D:/งาน/project/GUIS/Image/imageM/i1.jpg')
    image_A1i = image_A1i.resize((750, 600))
    tk_image = ImageTk.PhotoImage(image_A1i)
    label = tk.Label(a1i, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=1, y=1)

    image_A2i = Image.open('D:/งาน/project/GUIS/Image/imageM/i2.jpg')
    image_A2i = image_A2i.resize((475, 300))
    tk_image = ImageTk.PhotoImage(image_A2i)
    label = tk.Label(a1i, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=1)

    image_A3i = Image.open('D:/งาน/project/GUIS/Image/imageM/i3.jpg')
    image_A3i = image_A3i.resize((475, 290))
    tk_image = ImageTk.PhotoImage(image_A3i)
    label = tk.Label(a1i, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=310)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button13.mp3')
    pygame.mixer.music.play()

    a1i.after(300000, lambda: close_gui(a1i))

#อาคารสำนักงาน

def button_b1a():
    b1a = tk.Toplevel()
    b1a.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_b1a = tk.Label(b1a, image=background_photo)
    label_background_b1a.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_b1a.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/b1a.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(b1a, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=5)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/b2a.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(b1a, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=415)

    text_3 = Image.open('D:/งาน/project/GUIS/Image/Qrcode/img10.png')
    text_3 = text_3.resize((350, 350))
    tk_image = ImageTk.PhotoImage(text_3)
    label = tk.Label(b1a, image=tk_image)
    label.image = tk_image
    label.place(x=880, y=640)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonmap.png')
    button_1 = button_1.resize((600, 200))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(b1a, image=tk_image, command= bw.a)
    label.image = tk_image
    label.place(x=1280, y=790)

    button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_2 = button_2.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_2)
    label = tk.Button(b1a, image=tk_image, command=lambda: close_gui(b1a))
    label.image = tk_image
    label.place(x=1, y=890)

    image_B1a = Image.open('D:/งาน/project/GUIS/Image/imageM/1a.jpg')
    image_B1a = image_B1a.resize((750, 600))
    tk_image = ImageTk.PhotoImage(image_B1a)
    label = tk.Label(b1a, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=1, y=1)

    image_B2a = Image.open('D:/งาน/project/GUIS/Image/imageM/2a.jpg')
    image_B2a = image_B2a.resize((475, 300))
    tk_image = ImageTk.PhotoImage(image_B2a)
    label = tk.Label(b1a, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=1)

    image_B3a = Image.open('D:/งาน/project/GUIS/Image/imageM/3a.jpg')
    image_B3a = image_B3a.resize((475, 290))
    tk_image = ImageTk.PhotoImage(image_B3a)
    label = tk.Label(b1a, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=310)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button14.mp3')
    pygame.mixer.music.play()

    b1a.after(300000, lambda: close_gui(b1a))

def button_b1b():
    b1b = tk.Toplevel()
    b1b.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_b1b = tk.Label(b1b, image=background_photo)
    label_background_b1b.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_b1b.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/b1b.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(b1b, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=5)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/b2b.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(b1b, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=415)

    text_3 = Image.open('D:/งาน/project/GUIS/Image/Qrcode/img11.png')
    text_3 = text_3.resize((350, 350))
    tk_image = ImageTk.PhotoImage(text_3)
    label = tk.Label(b1b, image=tk_image)
    label.image = tk_image
    label.place(x=880, y=640)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonmap.png')
    button_1 = button_1.resize((600, 200))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(b1b, image=tk_image, command= bw.b)
    label.image = tk_image
    label.place(x=1280, y=790)

    button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_2 = button_2.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_2)
    label = tk.Button(b1b, image=tk_image, command=lambda: close_gui(b1b))
    label.image = tk_image
    label.place(x=1, y=890)

    image_B1b = Image.open('D:/งาน/project/GUIS/Image/imageM/1b.jpg')
    image_B1b = image_B1b.resize((750, 600))
    tk_image = ImageTk.PhotoImage(image_B1b)
    label = tk.Label(b1b, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=1, y=1)

    image_B2b = Image.open('D:/งาน/project/GUIS/Image/imageM/2b.jpg')
    image_B2b = image_B2b.resize((475, 300))
    tk_image = ImageTk.PhotoImage(image_B2b)
    label = tk.Label(b1b, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=1)

    image_B3b = Image.open('D:/งาน/project/GUIS/Image/imageM/3b.jpg')
    image_B3b = image_B3b.resize((475, 290))
    tk_image = ImageTk.PhotoImage(image_B3b)
    label = tk.Label(b1b, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=310)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button15.mp3')
    pygame.mixer.music.play()

    b1b.after(300000, lambda: close_gui(b1b))

def button_b1c():
    b1c = tk.Toplevel()
    b1c.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_b1c = tk.Label(b1c, image=background_photo)
    label_background_b1c.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_b1c.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/b1c.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(b1c, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=5)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/b2c.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(b1c, image=tk_image)
    label.image = tk_image
    label.place(x=1280, y=415)

    text_3 = Image.open('D:/งาน/project/GUIS/Image/Qrcode/img12.png')
    text_3 = text_3.resize((350, 350))
    tk_image = ImageTk.PhotoImage(text_3)
    label = tk.Label(b1c, image=tk_image)
    label.image = tk_image
    label.place(x=880, y=640)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonmap.png')
    button_1 = button_1.resize((600, 200))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(b1c, image=tk_image, command= bw.a1c)
    label.image = tk_image
    label.place(x=1280, y=790)

    button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_2 = button_2.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_2)
    label = tk.Button(b1c, image=tk_image, command=lambda: close_gui(b1c))
    label.image = tk_image
    label.place(x=1, y=890)

    image_B1c = Image.open('D:/งาน/project/GUIS/Image/imageM/1c.jpg')
    image_B1c = image_B1c.resize((750, 600))
    tk_image = ImageTk.PhotoImage(image_B1c)
    label = tk.Label(b1c, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=1, y=1)

    image_B2c = Image.open('D:/งาน/project/GUIS/Image/imageM/2c.jpg')
    image_B2c = image_B2c.resize((475, 300))
    tk_image = ImageTk.PhotoImage(image_B2c)
    label = tk.Label(b1c, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=1)

    image_B3c = Image.open('D:/งาน/project/GUIS/Image/imageM/3c.jpg')
    image_B3c = image_B3c.resize((475, 290))
    tk_image = ImageTk.PhotoImage(image_B3c)
    label = tk.Label(b1c, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=760, y=310)

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button16.mp3')
    pygame.mixer.music.play()

    b1c.after(300000, lambda: close_gui(b1c))

#คำถาม

def button_A3b():
    A3b = tk.Toplevel()
    A3b.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_A3b = tk.Label(A3b, image=background_photo)
    label_background_A3b.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_A3b.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/1b.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(A3b, image=tk_image)
    label.image = tk_image
    label.place(x=670, y=20)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/M1.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(A3b, image=tk_image)
    label.image = tk_image
    label.place(x=1295, y=20)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_1 = button_1.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(A3b, image=tk_image, command=lambda: close_gui(A3b))
    label.image = tk_image
    label.place(x=20, y=890)

    image_button_A1a = 'D:/งาน/project/GUIS/Image/text/a1.png'
    image = Image.open(image_button_A1a)
    image = image.resize((600, 200))
    button1_image = ImageTk.PhotoImage(image)
    button_A1a = tk.Button(A3b, image=button1_image, command=button_a1a)
    button_A1a.image = button1_image
    button_A1a.place(x=1295, y=570)

    image_button_A1b = 'D:/งาน/project/GUIS/Image/text/b1.png'
    image = Image.open(image_button_A1b)
    image = image.resize((600, 200))
    button2_image = ImageTk.PhotoImage(image)
    button_A1b = tk.Button(A3b, image=button2_image, command=button_a1b)
    button_A1b.image = button2_image
    button_A1b.place(x=1295, y=790)

    image_1b = Image.open('D:/งาน/project/GUIS/Image/imageM/a1.jpg')
    image_1b = image_1b.resize((600, 400))
    tk_image = ImageTk.PhotoImage(image_1b)
    label = tk.Label(A3b, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=20, y=20)

    image_2b = Image.open('D:/งาน/project/GUIS/Image/imageM/b1.jpg')
    image_2b = image_2b.resize((600, 400))
    tk_image = ImageTk.PhotoImage(image_2b)
    label = tk.Label(A3b, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=670, y=470)

    A3b.after(300000, lambda: close_gui(A3b))

def button_A3c():
    A3c = tk.Toplevel()
    A3c.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_A3c = tk.Label(A3c, image=background_photo)
    label_background_A3c.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_A3c.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/1c.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(A3c, image=tk_image)
    label.image = tk_image
    label.place(x=670, y=20)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/M2.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(A3c, image=tk_image)
    label.image = tk_image
    label.place(x=1295, y=20)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_1 = button_1.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(A3c, image=tk_image, command=lambda: close_gui(A3c))
    label.image = tk_image
    label.place(x=20, y=890)

    button_2 = 'D:/งาน/project/GUIS/Image/text/2c.png'
    image = Image.open(button_2)
    image = image.resize((600, 200))
    button2_image = ImageTk.PhotoImage(image)
    button_A1a = tk.Button(A3c, image=button2_image, command=button_b1c)
    button_A1a.image = button2_image
    button_A1a.place(x=1295, y=570)

    button_3 = 'D:/งาน/project/GUIS/Image/text/2c.png'
    image = Image.open(button_3)
    image = image.resize((600, 200))
    button3_image = ImageTk.PhotoImage(image)
    button_A1b = tk.Button(A3c, image=button3_image, command=button_b1c)
    button_A1b.image = button3_image
    button_A1b.place(x=1295, y=790)

    image_1b = Image.open('D:/งาน/project/GUIS/Image/imageM/1c.jpg')
    image_1b = image_1b.resize((600, 400))
    tk_image = ImageTk.PhotoImage(image_1b)
    label = tk.Label(A3c, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=20, y=20)

    image_2b = Image.open('D:/งาน/project/GUIS/Image/imageM/3c.jpg')
    image_2b = image_2b.resize((600, 400))
    tk_image = ImageTk.PhotoImage(image_2b)
    label = tk.Label(A3c, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=670, y=470)

    A3c.after(300000, lambda: close_gui(A3c))



def button_A3d():
    A3d = tk.Toplevel()
    A3d.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_A3d = tk.Label(A3d, image=background_photo)
    label_background_A3d.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_A3d.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/1d.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(A3d, image=tk_image)
    label.image = tk_image
    label.place(x=670, y=20)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/M3.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(A3d, image=tk_image)
    label.image = tk_image
    label.place(x=1295, y=20)

    text_3 = Image.open('D:/งาน/project/GUIS/Image/Qrcode/img13.png')
    text_3 = text_3.resize((350, 350))
    tk_image = ImageTk.PhotoImage(text_3)
    label = tk.Label(A3d, image=tk_image)
    label.image = tk_image
    label.place(x=915, y=440)

    button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonmap.png')
    button_2 = button_2.resize((600, 200))
    tk_image = ImageTk.PhotoImage(button_2)
    label = tk.Button(A3d, image=tk_image, command= bw.r)
    label.image = tk_image
    label.place(x=1295, y=570)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_1 = button_1.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(A3d, image=tk_image, command=lambda: close_gui(A3d))
    label.image = tk_image
    label.place(x=20, y=890)

    image_1b = Image.open('D:/งาน/project/GUIS/Image/imageM/3.jpg')
    image_1b = image_1b.resize((600, 400))
    tk_image = ImageTk.PhotoImage(image_1b)
    label = tk.Label(A3d, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=20, y=20)

    A3d.after(300000, lambda: close_gui(A3d))


def button_A3e():
    A3e = tk.Toplevel()
    A3e.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_A3e = tk.Label(A3e, image=background_photo)
    label_background_A3e.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_A3e.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/1e.png')
    text_1 = text_1.resize((600, 400))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(A3e, image=tk_image)
    label.image = tk_image
    label.place(x=670, y=20)

    text_2 = Image.open('D:/งาน/project/GUIS/Image/text/M4.png')
    text_2 = text_2.resize((600, 500))
    tk_image = ImageTk.PhotoImage(text_2)
    label = tk.Label(A3e, image=tk_image)
    label.image = tk_image
    label.place(x=1295, y=20)

    button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
    button_1 = button_1.resize((400, 100))
    tk_image = ImageTk.PhotoImage(button_1)
    label = tk.Button(A3e, image=tk_image, command=lambda: close_gui(A3e))
    label.image = tk_image
    label.place(x=20, y=890)

    button_2 = 'D:/งาน/project/GUIS/Image/text/r1.png'
    image = Image.open(button_2)
    image = image.resize((600, 200))
    button2_image = ImageTk.PhotoImage(image)
    button_A1a = tk.Button(A3e, image=button2_image, command=bw.r1)
    button_A1a.image = button2_image
    button_A1a.place(x=1295, y=570)

    button_3 = 'D:/งาน/project/GUIS/Image/text/r2.png'
    image = Image.open(button_3)
    image = image.resize((600, 200))
    button3_image = ImageTk.PhotoImage(image)
    button_A1b = tk.Button(A3e, image=button3_image, command=bw.r2)
    button_A1b.image = button3_image
    button_A1b.place(x=1295, y=790)

    image_1b = Image.open('D:/งาน/project/GUIS/Image/imageM/r1.jpg')
    image_1b = image_1b.resize((600, 400))
    tk_image = ImageTk.PhotoImage(image_1b)
    label = tk.Label(A3e, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=20, y=20)

    image_2b = Image.open('D:/งาน/project/GUIS/Image/imageM/r2.jpg')
    image_2b = image_2b.resize((600, 400))
    tk_image = ImageTk.PhotoImage(image_2b)
    label = tk.Label(A3e, image=tk_image)
    label.image = tk_image  # ป้องกันการลบรูป
    label.place(x=670, y=470)

    A3e.after(300000, lambda: close_gui(A3e))

def button_A3f():
    A3f = tk.Toplevel()
    A3f.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_A3f = tk.Label(A3f, image=background_photo)
    label_background_A3f.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_A3f.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/text/1f.png')
    text_1 = text_1.resize((1500, 700))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(A3f, image=tk_image, borderwidth=0)
    label.image = tk_image
    label.place(x=250, y=150)

    A3f.after(300000, lambda: close_gui(A3f))

def button_A3g():
    A3g = tk.Toplevel()
    A3g.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_A3g = tk.Label(A3g, image=background_photo)
    label_background_A3g.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_A3g.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/note.png')
    text_1 = text_1.resize((1500, 700))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(A3g, image=tk_image, borderwidth=0)
    label.image = tk_image
    label.place(x=250, y=150)

    A3g.after(300000, lambda: close_gui(A3g))

def button_A3h():
    A3h = tk.Toplevel()
    A3h.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_A3h = tk.Label(A3h, image=background_photo)
    label_background_A3h.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_A3h.place(x=0, y=0)

    text_1 = Image.open('D:/งาน/project/GUIS/Image/note.png')
    text_1 = text_1.resize((1500, 700))
    tk_image = ImageTk.PhotoImage(text_1)
    label = tk.Label(A3h, image=tk_image, borderwidth=0)
    label.image = tk_image
    label.place(x=250, y=150)

    A3h.after(300000, lambda: close_gui(A3h))

def button_A3i():
    A3i = tk.Toplevel()
    A3i.state('zoomed')
    image_path = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    background_photo = ImageTk.PhotoImage(image)
    label_background_A3i = tk.Label(A3i, image=background_photo)
    label_background_A3i.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
    label_background_A3i.place(x=0, y=0)



