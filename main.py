import customtkinter
import random
from PIL import Image

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")


class Adjustment(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        img1 = customtkinter.CTkImage(Image.open(r"C:\Users\admin\PycharmProjects\Color Picker App\random.png"))

        self.red_s = customtkinter.CTkSlider(self, from_=0, to=255, button_color="red", progress_color="red")
        self.green_s = customtkinter.CTkSlider(self, from_=0, to=255, button_color="green", progress_color="green")
        self.blue_s = customtkinter.CTkSlider(self, from_=0, to=255, button_color="blue", progress_color="blue")
        self.btn = customtkinter.CTkButton(self, text="Generate Color", command=self.rgb)
        self.show = customtkinter.CTkButton(self, text="", height=200, width=200, state='disabled')
        self.hex = customtkinter.CTkLabel(self, text="Click button to get color in HEX", width=200)
        self.rnd = customtkinter.CTkButton(self, text="Random Color", image=img1, command=self.rndrgb, width=25)

        self.show.grid(row=0, rowspan=4, column=0)
        self.hex.grid(row=4, column=0)
        self.rnd.grid(row=4, column=1)
        self.red_s.grid(row=0, column=1, pady=0)
        self.green_s.grid(row=1, column=1, pady=0)
        self.blue_s.grid(row=2, column=1, pady=0)
        self.btn.grid(row=3, column=1, pady=0)

        self.color = ""

    def rgb(self):
        red = int(self.red_s.get())
        green = int(self.green_s.get())
        blue = int(self.blue_s.get())

        self.color = "#{:02x}{:02x}{:02x}".format(red, green, blue)
        self.show.configure(fg_color=self.color)
        self.hex.configure(text=self.color)

    def rndrgb(self):
        red = int(random.randint(0, 255))
        green = int(random.randint(0, 255))
        blue = int(random.randint(0, 255))

        self.color = "#{:02x}{:02x}{:02x}".format(red, green, blue)

        self.red_s.set(red)
        self.green_s.set(green)
        self.blue_s.set(blue)

        self.show.configure(fg_color=self.color)
        self.hex.configure(text=self.color)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x230")
        self.resizable(False, False)
        self.title("Hex Color Picker")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.adjustment = Adjustment(master=self)
        self.adjustment.grid(row=0, column=1, padx=0, pady=0, sticky="")


app = App()
app.mainloop()
