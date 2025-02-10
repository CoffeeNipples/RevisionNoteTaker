#Note taking python script
import os
import tkinter as tk 
from PIL import Image,ImageDraw

counter = "COUNTFILE.txt"

def load_counter():
    if os.path.exists(counter):
        with open(counter,"r") as file:
            return int(file.read().strip())
    return 1

def save_counter(count):
    with open(counter,"w") as file:
        file.write(str(count))

def save_text():
    save = text.get("1.0", tk.END)
    print(save)
    return save

def save_on_close():
    """Save the text from Text widget to a file when closing GUI"""
    save = text.get("1.0",tk.END).strip()
    if save:
        with open("maths_revision.txt","a") as file:
            file.write("\n" + save + "\n")
    root.destroy()

class DrawingBox:
    def __init__(self,root):
        self.root = root
        self.root.title("Drawing Note")

        self.canvas = tk.Canvas(bg="white", width=500,height=500)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>",self.draw)

        self.last_x = None
        self.last_y = None

        self.save_button = tk.Button(self.root, text="Save Drawing", command= self.save)
        self.save_button.pack(padx=10)

        self.clear_button = tk.Button(self.root, text ="Clear Drawing", command = self.clear_canvas)
        self.clear_button.pack(padx=10)

    def draw(self,event):
        x,y = event.x, event.y

        self.canvas.create_oval(x,y,x+2,y+2, fill="black", width=10)

    def save(self):
        count = load_counter()
        filename = f"Drawing{count}.png"

        img = Image.new("RGB",(500,500),"white")
        draw = ImageDraw.Draw(img)

        for items in self.canvas.find_all():
            coords = self.canvas.coords(items)
            if len(coords) == 4:
                draw.line(coords, fill="black", width=2)

        img.save(filename)
        print(f"Drawing saved as {filename}")

        save_counter(count+1)

    def clear_canvas(self):
        self.canvas.delete("all")           #remove all drawn elements
        self.last_x,self.last_y = None,None #reset last position            

root = tk.Tk()
app = DrawingBox(root)
root.title("Revision Tool")

title = tk.Label(text = "Study Notes Taker")
title.pack()

text = tk.Text()
text.pack()

button = tk.Button(root, text = 'Save Text', command = save_text)
button.pack()



root.protocol("WM_DELETE_WINDOW", save_on_close)

root.mainloop()

