import pygame
import tkinter
import customtkinter 
import math

customtkinter.set_appearance_mode("dark")

window = customtkinter.CTk()
window.geometry("750x750")

equation_label = customtkinter.StringVar()
equation_text = ""

# Funkce:
def press_button(symbol):
    global equation_text
    
    equation_text = equation_text + str(symbol)
    equation_label.set(equation_text)
    
def equals():
    global equation_text
    
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
        
    except ZeroDivisionError:
        equation_text = ""
        equation_label.set("Chyba, dělení nulou nelze !")
    
    except SyntaxError:
        equation_label.set("Chyba v syntaxi")
        equation_text = ""
        
def clear():
    global equation_text
    
    equation_text = ""
    equation_label.set("")

def square_root(number):
    return math.sqrt(number)

def factorial(number):
    return math.factorial(number)

def log(number):
    return math.log10(number)

def sin(number):
    return round(math.sin(math.radians(number)), 3)

def cos(number):
    return round(math.cos(math.radians(number)), 3)

def tg(number):
    return round(math.tan(math.radians(number)), 3)

def cotg(number):
    return 1/(round(math.tan(math.radians(number)), 3))

# Nadefinované konstanty:
EULER_NUMBER = math.e
PI = math.pi

label = customtkinter.CTkLabel(master=window, width = 100, height=18, text="Calculator", font=("Arial", 35))
label.pack(pady = (25, 0))

frame = customtkinter.CTkFrame(master=window, width=650, height=650, corner_radius=50, border_color="#000000", border_width=3)
frame.pack(padx = 20, pady = 20)

label_eq = customtkinter.CTkLabel(master=frame, textvariable = equation_label, width=600, height=60, font=("Arial", 30), fg_color="#fff", corner_radius=50, text_color="#000000", anchor="center")
label_eq.grid(padx = 25, pady = (25, 0))

frame2 = customtkinter.CTkFrame(master=frame, width=600, height=600, corner_radius=50)
frame2.grid(padx = 40, pady = 25)

# Row = 0
btn_1 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="log", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color = "#0000FF", command=lambda: press_button("log("))
btn_1.grid(row = 0, column = 0, padx = (40, 5), pady = (10, 5))

btn_2 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="e", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button(EULER_NUMBER))
btn_2.grid(row = 0, column = 1, padx = 5, pady = (10, 5))

btn_3 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="π", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button(PI))
btn_3.grid(row = 0, column = 2, padx = 5, pady = (10, 5))

btn_4 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="(", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button("("))
btn_4.grid(row = 0, column = 3, padx = 5, pady = (10, 5))

btn_5 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text=")", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button(")"))
btn_5.grid(row = 0, column = 4, padx = (5, 40), pady = (10, 5))

# Row = 1
btn_6 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="!", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button("factorial("))
btn_6.grid(row = 1, column = 0, padx = (40, 5), pady = 5)

btn_7 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="√", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button("square_root("))
btn_7.grid(row = 1, column = 1, padx = 5, pady = 5)

btn_8 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="x ^ y", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button("**"))
btn_8.grid(row = 1, column = 2, padx = 5, pady = 5)

btn_9 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="1 / x", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button("** -1"))
btn_9.grid(row = 1, column = 3, padx = 5, pady = 5)

btn_10 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="C", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=clear)
btn_10.grid(row = 1, column = 4, padx = (5, 40), pady = 5)

# Row = 2
btn_11 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="sin", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button("sin("))
btn_11.grid(row = 2, column = 0, padx = (40, 5), pady = 5)

btn_12 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text=1, font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#fff", text_color="#0000FF", command=lambda: press_button(1))
btn_12.grid(row = 2, column = 1, padx = 5, pady = 5)

btn_13 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text=2, font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#fff", text_color="#0000FF", command=lambda: press_button(2))
btn_13.grid(row = 2, column = 2, padx = 5, pady = 5)

btn_14 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text=3, font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#fff", text_color="#0000FF", command=lambda: press_button(3))
btn_14.grid(row = 2, column = 3, padx = 5, pady = 5)

btn_15 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="+", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button("+"))
btn_15.grid(row = 2, column = 4, padx = (5, 40), pady = 5)

# Row = 3
btn_16 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="cos", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button("cos("))
btn_16.grid(row = 3, column = 0, padx = (40, 5), pady = 5)

btn_17 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text=4, font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#fff", text_color="#0000FF", command=lambda: press_button(4))
btn_17.grid(row = 3, column = 1, padx = 5, pady = 5)

btn_18 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text=5, font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#fff", text_color="#0000FF", command=lambda: press_button(5))
btn_18.grid(row = 3, column = 2, padx = 5, pady = 5)

btn_19 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text=6, font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#fff", text_color="#0000FF", command=lambda: press_button(6))
btn_19.grid(row = 3, column = 3, padx = 5, pady = 5)

btn_20 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="-", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button("-"))
btn_20.grid(row = 3, column = 4, padx = (5, 40), pady = 5)

# Row = 4
btn_21 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="tg", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button("tg("))
btn_21.grid(row = 4, column = 0, padx = (40, 5), pady = 5)

btn_22 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text=7, font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#fff", text_color="#0000FF", command=lambda: press_button(7))
btn_22.grid(row = 4, column = 1, padx = 5, pady = 5)

btn_23 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text=8, font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#fff", text_color="#0000FF", command=lambda: press_button(8))
btn_23.grid(row = 4, column = 2, padx = 5, pady = 5)

btn_24 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text=9, font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#fff", text_color="#0000FF", command=lambda: press_button(9))
btn_24.grid(row = 4, column = 3, padx = 5, pady = 5)

btn_25 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="*", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button("*"))
btn_25.grid(row = 4, column = 4, padx = (5, 40), pady = 5)

# Row = 5
btn_26 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="cotg", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button("cotg("))
btn_26.grid(row = 5, column = 0, padx = (40, 5), pady = (5, 10))

btn_27 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text=".", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#fff", text_color="#0000FF", command=lambda: press_button("."))
btn_27.grid(row = 5, column = 1, padx = 5, pady = (5, 10))

btn_28 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text=0, font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#fff", text_color="#0000FF", command=lambda: press_button(0))
btn_28.grid(row = 5, column = 2, padx = 5, pady = (5, 10))

btn_29 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="=", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#fff", text_color="#0000FF", command=lambda: equals())
btn_29.grid(row = 5, column = 3, padx = 5, pady = (5, 10))

btn_30 = customtkinter.CTkButton(master=frame2, width=100, corner_radius=20, height=60, text="/", font = ("Arial", 20), border_color="#000000", border_width=3, fg_color="#0000FF", command=lambda: press_button("/"))
btn_30.grid(row = 5, column = 4, padx = (5, 40), pady = (5, 10))

# Nastavení změny barvy textu a pozadí při najetí myši:

# 1) Početní operace + konstanty:
btn_1.bind("<Enter>", lambda event: btn_1.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_1.bind("<Leave>", lambda event: btn_1.configure(text_color="#fff", fg_color = "#0000FF"))

btn_2.bind("<Enter>", lambda event: btn_2.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_2.bind("<Leave>", lambda event: btn_2.configure(text_color="#fff", fg_color = "#0000FF"))

btn_3.bind("<Enter>", lambda event: btn_3.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_3.bind("<Leave>", lambda event: btn_3.configure(text_color="#fff", fg_color = "#0000FF"))

btn_4.bind("<Enter>", lambda event: btn_4.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_4.bind("<Leave>", lambda event: btn_4.configure(text_color="#fff", fg_color = "#0000FF"))

btn_5.bind("<Enter>", lambda event: btn_5.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_5.bind("<Leave>", lambda event: btn_5.configure(text_color="#fff", fg_color = "#0000FF"))

btn_6.bind("<Enter>", lambda event: btn_6.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_6.bind("<Leave>", lambda event: btn_6.configure(text_color="#fff", fg_color = "#0000FF"))

btn_7.bind("<Enter>", lambda event: btn_7.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_7.bind("<Leave>", lambda event: btn_7.configure(text_color="#fff", fg_color = "#0000FF"))

btn_8.bind("<Enter>", lambda event: btn_8.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_8.bind("<Leave>", lambda event: btn_8.configure(text_color="#fff", fg_color = "#0000FF"))

btn_9.bind("<Enter>", lambda event: btn_9.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_9.bind("<Leave>", lambda event: btn_9.configure(text_color="#fff", fg_color = "#0000FF"))

btn_10.bind("<Enter>", lambda event: btn_10.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_10.bind("<Leave>", lambda event: btn_10.configure(text_color="#fff", fg_color = "#0000FF"))

btn_11.bind("<Enter>", lambda event: btn_11.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_11.bind("<Leave>", lambda event: btn_11.configure(text_color="#fff", fg_color = "#0000FF"))

btn_15.bind("<Enter>", lambda event: btn_15.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_15.bind("<Leave>", lambda event: btn_15.configure(text_color="#fff", fg_color = "#0000FF"))

btn_16.bind("<Enter>", lambda event: btn_16.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_16.bind("<Leave>", lambda event: btn_16.configure(text_color="#fff", fg_color = "#0000FF"))

btn_20.bind("<Enter>", lambda event: btn_20.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_20.bind("<Leave>", lambda event: btn_20.configure(text_color="#fff", fg_color = "#0000FF"))

btn_21.bind("<Enter>", lambda event: btn_21.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_21.bind("<Leave>", lambda event: btn_21.configure(text_color="#fff", fg_color = "#0000FF"))

btn_25.bind("<Enter>", lambda event: btn_25.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_25.bind("<Leave>", lambda event: btn_25.configure(text_color="#fff", fg_color = "#0000FF"))

btn_26.bind("<Enter>", lambda event: btn_26.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_26.bind("<Leave>", lambda event: btn_26.configure(text_color="#fff", fg_color = "#0000FF"))

btn_30.bind("<Enter>", lambda event: btn_30.configure(text_color="#0000FF", fg_color = "#fff")) 
btn_30.bind("<Leave>", lambda event: btn_30.configure(text_color="#fff", fg_color = "#0000FF"))

# 2) Čísla, rovná se, desetinná tečka:
btn_12.bind("<Enter>", lambda event: btn_12.configure(text_color="#fff", fg_color = "#0000FF")) 
btn_12.bind("<Leave>", lambda event: btn_12.configure(text_color="#0000FF", fg_color = "#fff"))

btn_13.bind("<Enter>", lambda event: btn_13.configure(text_color="#fff", fg_color = "#0000FF")) 
btn_13.bind("<Leave>", lambda event: btn_13.configure(text_color="#0000FF", fg_color = "#fff"))

btn_14.bind("<Enter>", lambda event: btn_14.configure(text_color="#fff", fg_color = "#0000FF")) 
btn_14.bind("<Leave>", lambda event: btn_14.configure(text_color="#0000FF", fg_color = "#fff"))

btn_17.bind("<Enter>", lambda event: btn_17.configure(text_color="#fff", fg_color = "#0000FF")) 
btn_17.bind("<Leave>", lambda event: btn_17.configure(text_color="#0000FF", fg_color = "#fff"))

btn_18.bind("<Enter>", lambda event: btn_18.configure(text_color="#fff", fg_color = "#0000FF")) 
btn_18.bind("<Leave>", lambda event: btn_18.configure(text_color="#0000FF", fg_color = "#fff"))

btn_19.bind("<Enter>", lambda event: btn_19.configure(text_color="#fff", fg_color = "#0000FF")) 
btn_19.bind("<Leave>", lambda event: btn_19.configure(text_color="#0000FF", fg_color = "#fff"))

btn_22.bind("<Enter>", lambda event: btn_22.configure(text_color="#fff", fg_color = "#0000FF")) 
btn_22.bind("<Leave>", lambda event: btn_22.configure(text_color="#0000FF", fg_color = "#fff"))

btn_23.bind("<Enter>", lambda event: btn_23.configure(text_color="#fff", fg_color = "#0000FF")) 
btn_23.bind("<Leave>", lambda event: btn_23.configure(text_color="#0000FF", fg_color = "#fff"))

btn_24.bind("<Enter>", lambda event: btn_24.configure(text_color="#fff", fg_color = "#0000FF")) 
btn_24.bind("<Leave>", lambda event: btn_24.configure(text_color="#0000FF", fg_color = "#fff"))

btn_27.bind("<Enter>", lambda event: btn_27.configure(text_color="#fff", fg_color = "#0000FF")) 
btn_27.bind("<Leave>", lambda event: btn_27.configure(text_color="#0000FF", fg_color = "#fff"))

btn_28.bind("<Enter>", lambda event: btn_28.configure(text_color="#fff", fg_color = "#0000FF")) 
btn_28.bind("<Leave>", lambda event: btn_28.configure(text_color="#0000FF", fg_color = "#fff"))

btn_29.bind("<Enter>", lambda event: btn_29.configure(text_color="#fff", fg_color = "#0000FF")) 
btn_29.bind("<Leave>", lambda event: btn_29.configure(text_color="#0000FF", fg_color = "#fff"))

window.mainloop()