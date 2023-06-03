# projects
My Analog Clock

import math
import time
import tkinter as tk

class AnalogClock(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        tk.Canvas.__init__(self, master, **kwargs)
        self.width = int(self['width'])
        self.height = int(self['height'])
        self.size = min(self.width, self.height) // 2
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        self.draw_face()
        self.draw_hands()

    def draw_face(self):
        for i in range(60):
            angle = math.pi / 30 * i
            inner_ratio = 0.9 if i % 5 else 0.8
            x1 = self.center_x + self.size * math.sin(angle) * inner_ratio
            y1 = self.center_y - self.size * math.cos(angle) * inner_ratio
            x2 = self.center_x + self.size * math.sin(angle)
            y2 = self.center_y - self.size * math.cos(angle)
            self.create_line(x1, y1, x2, y2, fill="black")

    def draw_hands(self):
        self.hour_hand = self.create_line(0, 0, 0, 0, width=3, fill="black")
        self.minute_hand = self.create_line(0, 0, 0, 0, width=2, fill="black")
        self.second_hand = self.create_line(0, 0, 0, 0, width=1, fill="red")
        self.update_hands()

    def update_hands(self):
        current_time = time.localtime()
        hour = current_time.tm_hour % 12
        minute = current_time.tm_min
        second = current_time.tm_sec
        hour_angle = math.pi / 6 * hour + math.pi / 360 * minute
        minute_angle = math.pi / 30 * minute
        second_angle = math.pi / 30 * second
        hour_x = self.center_x + self.size * 0.5 * math.sin(hour_angle)
        hour_y = self.center_y - self.size * 0.5 * math.cos(hour_angle)
        minute_x = self.center_x + self.size * 0.8 * math.sin(minute_angle)
        minute_y = self.center_y - self.size * 0.8 * math.cos(minute_angle)
        second_x = self.center_x + self.size * 0.9 * math.sin(second_angle)
        second_y = self.center_y - self.size * 0.9 * math.cos(second_angle)
        self.coords(self.hour_hand, self.center_x, self.center_y, hour_x, hour_y)
        self.coords(self.minute_hand, self.center_x, self.center_y, minute_x, minute_y)
        self.coords(self.second_hand, self.center_x, self.center_y, second_x, second_y)
        self.after(1000, self.update_hands)

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root, width=300, height=300)
    clock.pack()
    root.mainloop()
