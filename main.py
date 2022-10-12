# import pyautogui
# while True:
#     a = pyautogui.confirm('তুমি কি আমাকে ভালোবাসো?', buttons= ['হ্যাঁ', 'না'])
#     if a == 'হ্যাঁ':
#         break
# pyautogui.hotkey('winleft', 'd')

#
#
# # a = 1
# # if False:
# #     a += 1
# # print(a)
# #
# #
#
#
#

# from pytube import YouTube
#
# link = YouTube('https://www.youtube.com/watch?v=7YcW25PHnAA')
#
# print(link.keywords)
# print(link.thumbnail_url)
# print(link.caption_tracks)
# print(link.captions)
# print(link)




chain = "................…...…………………................................................................................................................................................................................................................."
people = 3
dot = 0
for i in range(len(chain)+1):
     math = i * people
     dot += math
print(dot)



# from tkinter import *
# from tkinter.ttk import *
# from time import strftime
#
# root = Tk()
# root.title('Advance Clock')
#
# e = Entry(root)
# e.pack()
#
#
# def my_click():
#     my_label = Label(root, text=e.get())
#     my_label.pack()
#
#
# def time():
#     string = strftime('%I:%M:%S %p')
#     lbl.config(text=string)
#     lbl.after(1000, time)
#
#
# lbl = Label(root, font=('calibri', 40, 'bold'),
#             background='purple',
#             foreground='white')
#
# lbl.pack(anchor='center')
# time()
# my_button = Button(root, text="Enter Your Note", command=my_click)
# my_button.pack()
#
# mainloop()
#///////////////////////////////////////////////////////////////////////


from PIL import Image
import pyautogui
import os
import pyperclip


user = os.environ.get('USERNAME')

try:
    os.mkdir('ss')

except Exception:

    pass

path = "ss\\screenshot_1.png"
# path = f"C:\\Users\\{user}\\Desktop\\screenshot_1.png"

myScreenshot = pyautogui.screenshot()
myScreenshot.save(path)

im = Image.open(path)
im.show()

pyperclip.copy(path)
spam = pyperclip.paste()
print(spam)
