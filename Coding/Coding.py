import tkinter as tk

root = tk.Tk()

label_flat = tk.Label(root, text="Flat Border", relief="flat")
label_flat.pack()

label_raised = tk.Label(root, text="Raised Border", relief="raised")
label_raised.pack()

label_sunken = tk.Label(root, text="Sunken Border", relief="sunken")
label_sunken.pack()

label_solid = tk.Label(root, text="Solid Border", relief="solid")
label_solid.pack()

label_ridge = tk.Label(root, text="Ridge Border", relief="ridge")
label_ridge.pack()

label_groove = tk.Label(root, text="Groove Border", relief="groove")
label_groove.pack()

root.mainloop()
