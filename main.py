import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont


# functions ###############################################

def get_photo():
    global photo_file
    try:
        photo_file = tk.filedialog.askopenfilename()
        print(photo_file)
    except Exception as e:
        messagebox.showerror("Error!", f"{str(e)}. Error with directory selection! See log for more info!")


def get_logo():
    global logo_file
    try:
        logo_file = tk.filedialog.askopenfilename()
        print(logo_file)
    except Exception as e:
        messagebox.showerror("Error!", f"{str(e)}. Error with directory selection! See log for more info!")


def go():
    global photo_file
    global logo_file

    # Create an Image Object from an Image
    im = Image.open(photo_file)

    width, height = im.size

    margin = int(t_margin.get())
    x = width - margin
    y = height - margin
    copy_of_image = im.copy()

    if logo_file:
        im2 = Image.open(logo_file)
        im2.thumbnail((100,100))
        copy_of_image.paste(im2, (x, y))

    draw = ImageDraw.Draw(copy_of_image)
    text = t_text.get()

    if len(text) >= 1:

        font = ImageFont.load_default()

        # draw watermark in the bottom right corner
        global dark_text
        fill = "#fff"
        if dark_text.get():
            fill = "#000"
        draw.text((x, y), text, font=font, fill=fill)
        copy_of_image.show()

    # Save copy image
    copy_of_image.save(photo_file + ".done.jpeg")


# Global Variables ######################################################

photo_file = ""
logo_file = ""
water_mark_text = ""

# GUI ####################################################################
window = tk.Tk()
window.title("Add Watermark to Photo")
window.config(padx=10, pady=10)

l_label = tk.Label(text="Watermark Text")
l_label.grid(row=0, column=0)

t_text = tk.Entry()
t_text.grid(row=0, column=1)

l_label = tk.Label(text="Margin (Integer)")
l_label.grid(row=0, column=2)

t_margin = tk.Entry()
t_margin.grid(row=0, column=3)

b_photo = tk.Button(text="Select Photo", command=get_photo)
b_photo.grid(row=1, column=0)

b_logo = tk.Button(text="Select logo", command=get_logo)
b_logo.grid(row=1, column=1)

dark_text = tk.BooleanVar()
c_dark = tk.Checkbutton(text="Dark Text", variable=dark_text)
c_dark.grid(row=1, column=2)

b_go = tk.Button(text="Go!", command=go)
b_go.grid(row=1, column=3)


app_image = tk.PhotoImage(file="applogo.png")

my_canvas = tk.Canvas(width=500, height=500, highlightthickness=0)
my_canvas.create_image(250, 250, image=app_image)
my_canvas.grid(row=3, column=0, columnspan=8, padx=10, pady=10)

window.mainloop()
