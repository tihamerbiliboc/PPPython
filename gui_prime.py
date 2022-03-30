import tkinter as tk
import prime_generator as pg
import asyncio
import threading


def _asyncio_thread(async_loop):
    async_loop.run_until_complete(generate_primes())


def do_tasks(async_loop):
    """ Button-Event-Handler starting the asyncio part. """
    threading.Thread(target=_asyncio_thread, args=(async_loop,)).start()

async def generate_primes():

    tasks = pg.generate_primes_multiprocessing(1,10000)
    completed, pending = await asyncio.wait(tasks)
    results = [task.result() for task in completed]
    print('\n'.join(results))


def main(async_loop):

    window = tk.Tk()
    window.title("Prime Generator")
    window.geometry('600x400+50+50')
    set_range_label = tk.Label(window, text="Set Prime Range").pack()
    min_prime_label = tk.Label(window, text="Minimum").pack()
    min_prime_entry = tk.Entry(window)
    min_prime_entry.pack()
    max_prime_label = tk.Label(window, text="Maximum").pack()
    max_prime_entry = tk.Entry(window)
    max_prime_entry.pack()
    frame = tk.LabelFrame(window, text="Result")
    scroll = tk.Scrollbar(frame)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    primesText = tk.Text(frame, width=35, height=10, wrap=tk.WORD, yscrollcommand=scroll.set)
    generate_button = tk.Button(window, text="Generate Prime Numbers", command=lambda: do_tasks(async_loop)).pack()
    frame.pack()
    primesText.pack(side=tk.BOTTOM)

    window.mainloop()
