from tkinter import *

# class Gui:
#     def __init__(self, root):
#         frames = []
#         for i in range(5):
#             frames.append(Frame(root, borderwidth=0))
#             Label(frames[i], text=f'borderwidth = {i}').pack(side="left")
#             frames[i].pack()
#             inner_frame = []
#             for j,relief in enumerate((RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID)):
#                 inner_frame.append(Frame(frames[i], borderwidth=i, relief= relief))
#                 Label(inner_frame[j], text=relief, width=10).pack(side="left")
#                 inner_frame[j].pack(side="left", padx=7 - i, pady = 5 + i)
# root = Tk()
# gui = Gui(root)


root = Tk()
var = IntVar()
for text, value in (('item1', 1), ('item2', 2), ('item3', 3)):
    Radiobutton(root, text=text, value=value, variable=var, indicatoron=0).pack(anchor="w", \
        fill="x", padx=18, ipadx=40)
var.set(3)
root.mainloop()