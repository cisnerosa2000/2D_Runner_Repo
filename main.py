from Tkinter import *

root = Tk()

screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.attributes("-topmost",1)
root.geometry("%dx%d+0+0" % (screen_w, screen_h))
root.title("Tile")

canvas = Canvas()
canvas.config(bg="light blue")
canvas.config(width=screen_w,height=screen_h )






canvas.pack()
root.mainloop()