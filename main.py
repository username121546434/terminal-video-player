import time
import cv2 as cv
import tkinter as tk
from tkinter import filedialog
import os
from PIL.Image import fromarray
from draw_frame import draw_frame
from scale import resize

os.system('cls' if os.name == 'nt' else 'clear')

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

cap = cv.VideoCapture(file_path)
frame_n = 0
frame_count = cap.get(cv.CAP_PROP_FRAME_COUNT)
target_frame_time = 1 / 61

while True:
    flag, frame = cap.read()
    frame_n += 1
    
    if flag:
        frame_start = time.perf_counter()
        img = fromarray(frame)
        resize(img)
        if frame_n > 1 and img.size != last_size:
            os.system('cls' if os.name == 'nt' else 'clear')
        last_size = img.size
        frame = draw_frame(img)
        frame_time = time.perf_counter() - frame_start
        if frame_time < target_frame_time:
            time.sleep(target_frame_time - frame_time)
        fps = (1 / (time.perf_counter() - frame_start))
        print(
            f'\033[0;0HFrame {frame_n}/{frame_count}, {img.width}x{img.height}, {len(frame)} chars, {fps:.1f}fps',
            frame, sep='\n', end='', flush=True
        )
    else:
        break
