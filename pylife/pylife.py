import tkinter as tk
import time
import random


class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.pack()

        root.geometry("300x300")
        root.title("lifegame")

        self.canvas = tk.Canvas(root, bg="white", height=300, width=300)

        self.field = [[0] * 32 for i in range(32)]
        for i in range(0, 32):
            for j in range(0, 32):
                self.field[i][j] = 1 if random.random() >= 0.5 else 0

        self.canvas.pack()

    def draw(self):
        while True:
            self.canvas.delete("all")
            cell_size = 8
            for i in range(0, 32):
                for j in range(0, 32):
                    x1 = 22 + j * cell_size
                    x2 = x1 + cell_size
                    y1 = 22 + i * cell_size
                    y2 = y1 + cell_size
                    if self.field[i][j]:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill='red', outline='')
                    else:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='')
            self.nextStep()
            self.canvas.update()
            time.sleep(0.25)

    def nextStep(self):
        sum_field = [[0] * (32 + 2) for i in range(32 + 2)]
        next_field = [[0] * 32 for i in range(32)]
        for i in range(0, 32):
            for j in range(0, 32):
                for dy in range(0, 3):
                    for dx in range(0, 3):
                        if dx == 1 and dy == 1:
                            continue
                        sum_field[i + dy][j + dx] += self.field[i][j]

        for i in range(0, 32):
            for j in range(0, 32):
                if sum_field[i + 1][j + 1] <= 1:
                    next_field[i][j] = 0
                elif sum_field[i + 1][j + 1] == 2:
                    next_field[i][j] = self.field[i][j]
                elif sum_field[i + 1][j + 1] == 3:
                    next_field[i][j] = 1
                elif sum_field[i + 1][j + 1] >= 4:
                    next_field[i][j] = 0
        self.field = next_field


def main():
    main_win = tk.Tk()
    app = Application(root=main_win)
    app.after(250, app.draw)
    app.mainloop()


if __name__ == "__main__":
    main()
