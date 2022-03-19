import tkinter as tk
import prime_generator as pg

window = tk.Tk()
window.title("Prime Generator")
window.geometry('600x400+50+50')
set_range_label = tk.Label(window,text="Set Prime Range").pack()
min_prime_label = tk.Label(window, text="Minimum").pack()
min_prime_entry = tk.Entry(window)
min_prime_entry.pack()
max_prime_label = tk.Label(window, text="Maximum").pack()
max_prime_entry = tk.Entry(window)
max_prime_entry.pack()
frame = tk.LabelFrame(window, text="Result")
scroll=tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
primesText = tk.Text(frame, width=35, height=10,wrap=tk.WORD,yscrollcommand=scroll.set)

def on_click_generate_primes():
    primesText.insert(tk.END,str(pg.generate_primes(int(min_prime_entry.get()),int(max_prime_entry.get()))))

generate_button = tk.Button(window, text="Generate Prime Numbers", command=on_click_generate_primes).pack()
frame.pack()
primesText.pack(side=tk.BOTTOM)


