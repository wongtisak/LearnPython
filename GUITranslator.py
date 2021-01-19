# GUITranslator.py
from tkinter import * #จาก Libraly ชื่อ tkinter ให้ดึงความสามารถทั้งหมด

from tkinter import ttk #ttk is theme of tk
###---------- Google Translater-------
from googletrans import Translator
translator = Translator()

GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry('500x300')# กว้าง x สูง
GUI.title('โปรแกรมแปลภาษา by วงศ์ธิศักดิ์')
# -------- config--------
FONT = ('Angsana New',15)
#---------Label--------
L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',fon=FONT)
L.pack()
# -------Entry (ช่องกรอกข้อความ)--------
v_vocab = StringVar() #กล่องเก็บข้อความ

E1 = ttk.Entry(GUI,textvariable=v_vocab,font=FONT,width=40)
E1.pack(pady=20)



# -------Button (ปุ่มแปล)--------
#B1 = Button(GUI,text='Translate') #สร้างปุ่มขึ้นมา
#B1.pack() # show ปุ่มขึ้นมาวางจากบนลงล่าง
def Translate():
    vocab = v_vocab.get() #.get คือสั่งให้แสดงผลออกมา
    meaning = translator.translate(vocab,dest='th')
    print(vocab + ':' + meaning.text)
    v_result.set(vocab + ' : ' + meaning.text)

B1 = ttk.Button(GUI,text='Translate',command=Translate) #สร้างปุ่มขึ้นมา
B1.pack(ipadx=20,ipady=10) # show ปุ่มขึ้นมาวางจากบนลงล่าง
#---------Label--------
L = ttk.Label(GUI,text='คำแปล',fon=FONT)
L.pack()
#--------Result------
v_result = StringVar() #นี่คือกล่องสำหรับเก็บคำแปล
FONT2=('Angsana New', 20)
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT2, foreground='green')
R1.pack()


GUI.mainloop()#ทำให้โปรแกรม run ตลอดเวลาจนกว่าจะปิด (ต้องอยู่บรรทัดสุดท้ายเท่านั้น)
