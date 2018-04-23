import tkinter as tk

root = tk.Tk()

l1 = tk.Frame(root, background="red", width=100, height=50)
l2 = tk.Frame(root, background="orange", width=100, height=50)
l3 = tk.Frame(root, background="green", width=100, height=50)
l4 = tk.Frame(root, background="blue", width=100, height=50)

root.columnconfigure(2, weight=1)
l1.grid(row=1, column=1, columnspan=2, sticky="ew")
l2.grid(row=1, column=3, sticky="ew")
l3.grid(row=2, column=1, sticky="ew")
l4.grid(row=2, column=3, sticky="ew")

root.mainloop()
