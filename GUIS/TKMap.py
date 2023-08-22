import tkinter as tk
import webbrowser
import buttonweb as BW
import buttonmap as BM
import pygame
from tkinter import ttk
from PIL import Image, ImageTk

def Out_A4a():
    message_A4a = userInput.get()
    print(message_A4a)  

def button_frame(frame):
    notebook.select(frame)

def button_A1():
    button_frame(frame_A1)
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button1.mp3')
    pygame.mixer.music.play()

def button_A2():
    button_frame(frame_A2)
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button2.mp3')
    pygame.mixer.music.play()

def button_A3():
    button_frame(frame_A3)
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button3.mp3')
    pygame.mixer.music.play()

def button_A4():
    button_frame(frame_A4)
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('D:/งาน/project/GUIS/speak/button4.mp3')
    pygame.mixer.music.play()


# สร้าง GUI
root = tk.Tk()
userInput = tk.StringVar()
root.state('zoomed')

notebook = ttk.Notebook(root)

# Home
frame_home = ttk.Frame(notebook)

image_path = 'D:/งาน/project/GUIS/Image/Canva/Bg.png'
image = Image.open(image_path)
image = image.resize((1920, 1080))
background_photo = ImageTk.PhotoImage(image)
label_background_home = tk.Label(frame_home, image=background_photo)
label_background_home.image = background_photo  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
label_background_home.place(x=0, y=0)

Icon_path = 'D:/งาน/project/GUIS/Image/iconctc.png'
Icon = Image.open(Icon_path)
Icon = Icon.resize((600, 350))
Icon_photo = ImageTk.PhotoImage(Icon)
label_Icon_home = tk.Label(frame_home, image=Icon_photo, borderwidth=0)
label_Icon_home.Icon = Icon_photo
label_Icon_home.place(x=650, y= 150)

# อาคาร
frame_A1 = ttk.Frame(notebook)

image_A1 = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
image = Image.open(image_A1)
image = image.resize((1920, 1080))
background_A1 = ImageTk.PhotoImage(image)
label_background_A1 = tk.Label(frame_A1, image=background_A1)
label_background_A1.image = background_A1  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
label_background_A1.place(x=0, y=0)

image_button_A1a = 'D:/งาน/project/GUIS/Image/text/a1.png'
image = Image.open(image_button_A1a)
image = image.resize((570, 200))
button1_image = ImageTk.PhotoImage(image)
button_A1a = tk.Button(frame_A1, image=button1_image, command=BM.button_a1a)
button_A1a.image = button1_image
button_A1a.place(x=10, y=10, width=570, height=200)

image_button_A1b = 'D:/งาน/project/GUIS/Image/text/b1.png'
image = Image.open(image_button_A1b)
image = image.resize((570, 200))
button2_image = ImageTk.PhotoImage(image)
button_A1b = tk.Button(frame_A1, image=button2_image, command=BM.button_a1b)
button_A1b.image = button2_image
button_A1b.place(x=675, y=10, width=570, height=200)

image_button_A1c = 'D:/งาน/project/GUIS/Image/text/c1.png'
image = Image.open(image_button_A1c)
image = image.resize((570, 200))
button3_image = ImageTk.PhotoImage(image)
button_A1c = tk.Button(frame_A1, image=button3_image, command=BM.button_a1c)
button_A1c.image = button3_image
button_A1c.place(x=1340, y=10, width=570, height=200)

image_button_A1d = 'D:/งาน/project/GUIS/Image/text/d1.png'
image = Image.open(image_button_A1d)
image = image.resize((570, 200))
button4_image = ImageTk.PhotoImage(image)
button_A1d = tk.Button(frame_A1, image=button4_image, command=BM.button_a1d)
button_A1d.image = button4_image
button_A1d.place(x=10, y=290, width=570, height=200)

image_button_A1e = 'D:/งาน/project/GUIS/Image/text/e1.png'
image = Image.open(image_button_A1e)
image = image.resize((570, 200))
button5_image = ImageTk.PhotoImage(image)
button_A1e = tk.Button(frame_A1, image=button5_image, command=BM.button_a1e)
button_A1e.image = button5_image
button_A1e.place(x=675, y=290, width=570, height=200)

image_button_A1f = 'D:/งาน/project/GUIS/Image/text/f1.png'
image = Image.open(image_button_A1f)
image = image.resize((570, 200))
button6_image = ImageTk.PhotoImage(image)
button_A1f = tk.Button(frame_A1, image=button6_image, command=BM.button_a1f)
button_A1f.image = button6_image
button_A1f.place(x=1340, y=290, width=570, height=200)

image_button_A1g = 'D:/งาน/project/GUIS/Image/text/g1.png'
image = Image.open(image_button_A1g)
image = image.resize((570, 200))
button7_image = ImageTk.PhotoImage(image)
button_A1g = tk.Button(frame_A1, image=button7_image, command=BM.button_a1g)
button_A1g.image = button7_image
button_A1g.place(x=10, y=570, width=570, height=200)

image_button_A1h = 'D:/งาน/project/GUIS/Image/text/h1.png'
image = Image.open(image_button_A1h)
image = image.resize((570, 200))
button8_image = ImageTk.PhotoImage(image)
button_A1h = tk.Button(frame_A1, image=button8_image, command=BM.button_a1h)
button_A1h.image = button8_image
button_A1h.place(x=675, y=570, width=570, height=200)

image_button_A1i = 'D:/งาน/project/GUIS/Image/text/i1.png'
image = Image.open(image_button_A1i)
image = image.resize((570, 200))
button9_image = ImageTk.PhotoImage(image)
button_A1i = tk.Button(frame_A1, image=button9_image, command=BM.button_a1i)
button_A1i.image = button9_image
button_A1i.place(x=1340, y=570, width=570, height=200)

frame_A1.after(300000, lambda: button_frame(frame_home))

# อาคารสำนักงาน
frame_A2 = ttk.Frame(notebook)

image_A2 = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
image = Image.open(image_A2)
image = image.resize((1920, 1080))
background_A2 = ImageTk.PhotoImage(image)
label_background_A2 = tk.Label(frame_A2, image=background_A2)
label_background_A2.image = background_A2  # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
label_background_A2.place(x=0, y=0)

image_button_A2a = 'D:/งาน/project/GUIS/Image/text/2a.png'
image = Image.open(image_button_A2a)
image = image.resize((1900, 200))
button10_image = ImageTk.PhotoImage(image)
button_A2a = tk.Button(frame_A2, image=button10_image, command=BM.button_b1a)
button_A2a.image = button10_image
button_A2a.place(x=10, y=10, width=1900, height=200)

image_button_A2b = 'D:/งาน/project/GUIS/Image/text/2b.png'
image = Image.open(image_button_A2b)
image = image.resize((1900, 200))
button11_image = ImageTk.PhotoImage(image)
button_A2b = tk.Button(frame_A2, image=button11_image, command=BM.button_b1b)
button_A2b.image = button11_image
button_A2b.place(x=10, y=290, width=1900, height=200)

image_button_A2c = 'D:/งาน/project/GUIS/Image/text/2c.png'
image = Image.open(image_button_A2c)
image = image.resize((1900, 200))
button12_image = ImageTk.PhotoImage(image)
button_A2c = tk.Button(frame_A2, image=button12_image, command=BM.button_b1c)
button_A2c.image = button12_image
button_A2c.place(x=10, y=570, width=1900, height=200)

frame_A2.after(300000, lambda: button_frame(frame_home))

# คำถามที่พบบ่อย
frame_A3 = ttk.Frame(notebook)

image_A3 = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
image = Image.open(image_A3)
image = image.resize((1920, 1080))
background_A3 = ImageTk.PhotoImage(image)
label_background_A3 = tk.Label(frame_A3, image=background_A3)
label_background_A3.image = background_A3 # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
label_background_A3.place(x=0, y=0)

image_button_A3a = 'D:/งาน/project/GUIS/Image/text/3a.png'
image = Image.open(image_button_A3a)
image = image.resize((570, 200))
button13_image = ImageTk.PhotoImage(image)
button_A3a = tk.Button(frame_A3, image=button13_image, command=BW.ctcweb)
button_A3a.image = button13_image
button_A3a.place(x=10, y=10)

image_button_A3b = 'D:/งาน/project/GUIS/Image/text/3b.png'
image = Image.open(image_button_A3b)
image = image.resize((570, 200))
button14_image = ImageTk.PhotoImage(image)
button_A3b = tk.Button(frame_A3, image=button14_image, command=BM.button_A3b)
button_A3a.image = button14_image
button_A3b.place(x=675, y=10)

image_button_A3c = 'D:/งาน/project/GUIS/Image/text/3c.png'
image = Image.open(image_button_A3c)
image = image.resize((570, 200))
button15_image = ImageTk.PhotoImage(image)
button_A3c = tk.Button(frame_A3, image=button15_image, command=BM.button_A3c)
button_A3c.image = button15_image
button_A3c.place(x=1340, y=10, width=570, height=200)

image_button_A3d = 'D:/งาน/project/GUIS/Image/text/3d.png'
image = Image.open(image_button_A3d)
image = image.resize((570, 200))
button16_image = ImageTk.PhotoImage(image)
button_A3d = tk.Button(frame_A3, image=button16_image, command=BM.button_A3d)
button_A3d.image = button16_image
button_A3d.place(x=10, y=290, width=570, height=200)

image_button_A3e = 'D:/งาน/project/GUIS/Image/text/3e.png'
image = Image.open(image_button_A3e)
image = image.resize((570, 200))
button17_image = ImageTk.PhotoImage(image)
button_A3e = tk.Button(frame_A3, image=button17_image, command=BM.button_A3e)
button_A3e.image = button17_image
button_A3e.place(x=675, y=290, width=570, height=200)

image_button_A3f = 'D:/งาน/project/GUIS/Image/text/3f.png'
image = Image.open(image_button_A3f)
image = image.resize((570, 200))
button18_image = ImageTk.PhotoImage(image)
button_A3f = tk.Button(frame_A3, image=button18_image, command=BM.button_A3f)
button_A3f.image = button18_image
button_A3f.place(x=1340, y=290, width=570, height=200)

image_button_A3g = 'D:/งาน/project/GUIS/Image/text/3g.png'
image = Image.open(image_button_A3g)
image = image.resize((570, 200))
button19_image = ImageTk.PhotoImage(image)
button_A3g = tk.Button(frame_A3, image=button19_image, command=BM.button_A3g)
button_A3g.image = button19_image
button_A3g.place(x=10, y=570, width=570, height=200)

image_button_A3h = 'D:/งาน/project/GUIS/Image/text/3h.png'
image = Image.open(image_button_A3h)
image = image.resize((570, 200))
button20_image = ImageTk.PhotoImage(image)
button_A3h = tk.Button(frame_A3, image=button20_image, command=BM.button_A3h)
button_A3h.image = button20_image
button_A3h.place(x=675, y=570, width=570, height=200)

image_button_A3i = 'D:/งาน/project/GUIS/Image/text/3h.png'
image = Image.open(image_button_A3i)
image = image.resize((570, 200))
button21_image = ImageTk.PhotoImage(image)
button_A3i = tk.Button(frame_A3, image=button21_image, command=BM.button_A3i)
button_A3i.image = button21_image
button_A3i.place(x=1340, y=570, width=570, height=200)

frame_A3.after(300000, lambda: button_frame(frame_home))

# ค้นหา
frame_A4 = ttk.Frame(notebook)
image_A4 = 'D:/งาน/project/GUIS/Image/Canva/Bga.png'
image = Image.open(image_A4)
image = image.resize((1920, 1080))
background_A4 = ImageTk.PhotoImage(image)
label_background_A4 = tk.Label(frame_A4, image=background_A4)
label_background_A4.image = background_A4 # เก็บอ้างอิงภาพเพื่อป้องกันการแสดงผลผิดพลาด
label_background_A4.place(x=0, y=0)

text_1 = Image.open('D:/งาน/project/GUIS/Image/text/fa4.png')
text_1 = text_1.resize((1500, 700))
tk_image = ImageTk.PhotoImage(text_1)
label = tk.Label(frame_A4, image=tk_image, borderwidth=0)
label.image = tk_image
label.place(x=250, y=150)

frame_A4.after(300000, lambda: button_frame(frame_home))

# แท็บ
notebook.add(frame_home, text='Home')
notebook.add(frame_A1, text='อาคารเรียน')
notebook.add(frame_A2, text='อาคารสำนักงาน')
notebook.add(frame_A3, text='คำถามที่พบบ่อย')
notebook.add(frame_A4, text='วิธีการใช้งาน')

# Frame

button1_image_path = 'D:/งาน/project/GUIS/Image/i1.png'
button1_image = Image.open(button1_image_path)
button1_image = button1_image.resize((500, 300))
button1_photo = ImageTk.PhotoImage(button1_image)
button1 = tk.Button(frame_home, image=button1_photo, text="อาคารเรียน", relief="groove", command=lambda: button_A1())
button1.image = button1_photo
button1.place(x=100, y=250)

button2_image_path = 'D:/งาน/project/GUIS/Image/i2.png'
button2_image = Image.open(button2_image_path)
button2_image = button2_image.resize((500, 300))
button2_photo = ImageTk.PhotoImage(button2_image)
button2 = tk.Button(frame_home, image=button2_photo, text="อาคารสำนักงาน", relief="groove", command=lambda: button_A2())
button2.image = button2_photo
button2.place(x=320, y=620)

button3_image_path = 'D:/งาน/project/GUIS/Image/i3.png'
button3_image = Image.open(button3_image_path)
button3_image = button3_image.resize((500, 300))
button3_photo = ImageTk.PhotoImage(button3_image)
button3 = tk.Button(frame_home, image=button3_photo, text="คำถามที่พบบ่อย", command=lambda: button_A3())
button3.image = button3_photo
button3.place(x=1320, y=250)

button4_image_path = 'D:/งาน/project/GUIS/Image/i4.png'
button4_image = Image.open(button4_image_path)
button4_image = button4_image.resize((500, 300))
button4_photo = ImageTk.PhotoImage(button4_image)
button4 = tk.Button(frame_home, image=button4_photo, text="ค้นหา", command=lambda: button_A4())
button4.image = button4_photo
button4.place(x=1150, y=620)

# ย้อนกลับ
button_1 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
button_1 = button_1.resize((400, 100))
tk_image = ImageTk.PhotoImage(button_1)
back_button1 = tk.Button(frame_A1, image=tk_image, command=lambda: button_frame(frame_home))
back_button1.image = tk_image
back_button1.place(x=760, y=850)

button_2 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
button_2 = button_2.resize((400, 100))
tk_image = ImageTk.PhotoImage(button_2)
back_button2 = tk.Button(frame_A2, image=tk_image, command=lambda: button_frame(frame_home))
back_button2.image = tk_image
back_button2.place(x=760, y=850, width=400, height=100)

button_3 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
button_3 = button_3.resize((400, 100))
tk_image = ImageTk.PhotoImage(button_3)
back_button3 = tk.Button(frame_A3, image=tk_image, command=lambda: button_frame(frame_home))
back_button3.image = tk_image
back_button3.place(x=760, y=850, width=400, height=100)

button_4 = Image.open('D:/งาน/project/GUIS/Image/text/buttonback.png')
button_4 = button_4.resize((400, 100))
tk_image = ImageTk.PhotoImage(button_4)
back_button4 = tk.Button(frame_A4, image=tk_image, command=lambda: button_frame(frame_home))
back_button4.image = tk_image
back_button4.place(x=20, y=890)

notebook.pack(expand=True, fill='both')

root.mainloop()
