from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
from ttkthemes import ThemedStyle
from tabula import read_pdf
from tkinter.font import Font
import pandas as pd
import numpy as np
import os
from os.path import expanduser
from wand.image import Image as Img
from PIL import Image
import pytesseract
from PyPDF2 import PdfFileWriter, PdfFileReader

home = expanduser("~")

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def method_one(): 
    global path_file
    file = askopenfile(mode ='r') 
    if file is not None:
        try:
            page_number=user_page.get()
            dfs = read_pdf(file.name, pages=int(page_number), pandas_options={'header':None})
            folder=home+'/'+user_folder.get()+'/page_'+page_number
            os.makedirs(folder, exist_ok=True) #overwrite caso a pasta já exista
            path_file=folder+'/'+'page_{}.csv'.format(page_number)
            dfs[0].to_csv(path_file, index=False)
            message_open = tk.Tk()
            message_open.geometry("500x100+650+450")
            message_open.title('Message')
            style = ThemedStyle(message_open)
            style.set_theme("arc")
            msg=tk.Frame(message_open)
            msg.pack()
            content=ttk.Label(msg, text="Done!", font=("Helvetica", "50"))
            content.pack()
        except:
            message_open = tk.Tk()
            message_open.geometry("500x100+650+450")
            message_open.title('Message')
            style = ThemedStyle(message_open)
            style.set_theme("arc")
            msg=tk.Frame(message_open)
            msg.pack()
            content=ttk.Label(msg, text="The tabulation fails. \nPlease, check the log file", font=("Helvetica", "16"))
            content.pack()

def method_two(): 
    global path_file
    file = askopenfile(mode ='r') 
    if file is not None:
        try:
            page_number=user_page.get()
            dfs = read_pdf(file.name, pages=int(page_number), pandas_options={'header':None}, guess=False)
            folder=home+'/'+user_folder.get()+'/page_'+page_number
            os.makedirs(folder, exist_ok=True) #overwrite caso a pasta já exista
            path_file=folder+'/'+'page_{}.csv'.format(page_number)
            dfs[0].to_csv(path_file, index=False)
            message_open = tk.Tk()
            message_open.geometry("500x100+650+450")
            message_open.title('Message')
            style = ThemedStyle(message_open)
            style.set_theme("arc")
            msg=tk.Frame(message_open)
            msg.pack()
            content=ttk.Label(msg, text="Done!", font=("Helvetica", "50"))
            content.pack()
        except:
            message_open = tk.Tk()
            message_open.geometry("500x100+650+450")
            message_open.title('Message')
            style = ThemedStyle(message_open)
            style.set_theme("arc")
            msg=tk.Frame(message_open)
            msg.pack()
            content=ttk.Label(msg, text="The tabulation fails. \nPlease, check the log file", font=("Helvetica", "16"))
            content.pack()


def method_three():
    global path_file
    file = askopenfile(mode ='r') 
    if file is not None:
        try:
        #cria arquivos das páginas
            document=file.name
            page_number=user_page.get()
            folder=home+'/'+user_folder.get()+'/page_'+page_number
            os.makedirs(folder, exist_ok=True) #overwrite caso a pasta já exista
            inputpdf = PdfFileReader(open(document, "rb"))
            for i in range(1,inputpdf.numPages+1):
                output = PdfFileWriter()
                output.addPage(inputpdf.getPage(i-1))
                pdf_file=folder+'/'+"document-page%s.pdf" % i
                with open(pdf_file, "wb") as outputStream:
                    output.write(outputStream)
            #transforma página em imagem, lê como string e salva em csv
            page_file=folder+'/'+"document-page%s.pdf" % page_number
            with Img(filename=page_file, resolution=400) as img:
                img.compression_quality = 99
                img_file=page_file.replace('pdf','jpg')
                img.save(filename=img_file)
            im = Image.open(img_file)
            text = pytesseract.image_to_string(im, lang = 'eng')
            #salva csv file
            text=text.replace(' ',',')
            csv_file=folder+'/'+'page_{}.csv'.format(page_number)
            h = open(csv_file,'w')
            h.write(text)
            h.close()
            #drop pdf files
            os.system('rm '+folder+'/*pdf')
            os.system('rm '+folder+'/*jpg')
            message_open = tk.Tk()
            message_open.geometry("500x100+650+450")
            message_open.title('Message')
            style = ThemedStyle(message_open)
            style.set_theme("arc")
            msg=tk.Frame(message_open)
            msg.pack()
            content=ttk.Label(msg, text="Done!", font=("Helvetica", "50"))
            content.pack()
        except:
            message_open = tk.Tk()
            message_open.geometry("500x100+650+450")
            message_open.title('Message')
            style = ThemedStyle(message_open)
            style.set_theme("arc")
            msg=tk.Frame(message_open)
            msg.pack()
            content=ttk.Label(msg, text="The tabulation fails. \nPlease, check the log file", font=("Helvetica", "16"))
            content.pack()



def open_excel():
    page_number=user_page.get()
    folder=home+'/'+user_folder.get()+'/page_'+page_number
    path_file=folder+'/'+'page_{}.csv'.format(page_number)
    os.system("start EXCEL.EXE {}".format(path_file))

def open_calc():
        page_number=user_page.get()
        folder=home+'/'+user_folder.get()+'/page_'+page_number
        path_file=folder+'/'+'page_{}.csv'.format(page_number)
        os.system("libreoffice {}".format(path_file))

def open_modfile():
    page_number=user_page.get()
    folder=home+'/'+user_folder.get()+'/page_'+page_number
    path_file=folder+'/'+'page_{}.csv'.format(page_number)
    #create a copy from manually modified file
    new_name=path_file.replace('.csv','_final.csv')
    os.system("cp {} {}".format(path_file,new_name))
    global df
    df = pd.read_csv(new_name)


def to_number(x):
    if isinstance(x,str):
        x_clean = x.replace(' ','').replace('.','')
        if x_clean.isdigit():
            return int(x_clean)
        else:
            return np.nan
    else:
        return x

def transform_cols():    
    page_number=user_page.get()
    folder=home+'/'+user_folder.get()+'/page_'+page_number
    path_file=folder+'/'+'page_{}.csv'.format(page_number)
    #create a copy from manually modified file
    for col in df.iloc[:,1:].columns:
        df[col]=[to_number(k) for k in df[col]]

    new_name=path_file.replace('.csv','_final.csv')
    df.to_csv(new_name, index=False)



root = tk.Tk()
root.geometry('+250+150')
root.title('Transk Table 0.0.1')
photo = tk.PhotoImage(file = "letter.png")
root.iconphoto(False, photo)
style = ThemedStyle(root)
style.set_theme("arc")

#define as variáveis a serem inseridas pelo usuário
user_page=tk.StringVar() 
user_folder=tk.StringVar()


#set default font
default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(size=15)
root.option_add("*Font", default_font)

#create myfont
my_font=Font(family="Helvetica", size=12)
my_font2=Font(family="Helvetica", size=50)



#==================================================================
#==================================================================
#                           VIEW FRAME
#==================================================================
#==================================================================

# frame_one=tk.Frame(root)
# frame_one.grid(row=0, column=0, sticky="EW")

#==================================================================
#==================================================================
#                           FILE FRAME
#==================================================================
#==================================================================

frame_one=tk.Frame(root)
frame_one.grid(row=0, column=0, sticky="EW")

first_step=ttk.Label(frame_one, text="Type the page number: ", background='white')
first_step.grid(row=0, column=0)
first_step_entry=ttk.Entry(frame_one,width=15, textvariable=user_page)
first_step_entry.grid(row=0, column=1)
first_step_entry.focus()

second_step=ttk.Label(frame_one, text="Type the working directory: ", background='white')
second_step.grid(row=1, column=0)
second_step_entry=ttk.Entry(frame_one,width=15, textvariable=user_folder)
second_step_entry.grid(row=1, column=1)
second_step_entry.focus()

#READ
read_btn1 = ttk.Button(frame_one, text ='Method 1', command = lambda:method_one()) 
read_btn1.grid(row=2, column=0, sticky='EW')

read_btn2 = ttk.Button(frame_one, text ='Method 2', command = lambda:method_two()) 
read_btn2.grid(row=2, column=1, sticky='EW')

read_btn2 = ttk.Button(frame_one, text ='Method 3', command = lambda:method_three()) 
read_btn2.grid(row=2, column=2, sticky='EW')

#OPEN EXCEL
excel_btn = ttk.Button(frame_one, text ='Open Excel Sheet', command = lambda:open_excel()) 
excel_btn.grid(row=3, column=0,)

#OPEN CALC
calc_btn = ttk.Button(frame_one, text ='Open Calc Sheet', command = lambda:open_calc()) 
calc_btn.grid(row=3, column=1)

#CLEAN
clean_btn = ttk.Button(frame_one, text ='Clean', command = combine_funcs(open_modfile, transform_cols)) 
clean_btn.grid(row=4, column=0, columnspan=2, sticky='EW')

#QUIT
clean_btn = ttk.Button(frame_one, text ='Quit', command = root.destroy) 
clean_btn.grid(row=5, column=0, columnspan=2, sticky='EW')

#==================================================================
#==================================================================
#                           TERMINAL FRAME
#==================================================================
#==================================================================

termf = tk.Frame(root, height=800, width=1400)
termf.grid(row=1, sticky='EW')
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 800x1400 -sb &' % wid)

#==================================================================
#==================================================================
#                           END
#==================================================================
#==================================================================

root.mainloop()

