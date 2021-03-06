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
from PIL import ImageTk, Image #to display image


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def open_file(): 
    global path_file
    file = askopenfile(mode ='r') 
    if file is not None:
        page_number=user_page.get()
        dfs = read_pdf(file.name, pages=int(page_number), pandas_options={'header':None})
        folder='page_'+page_number
        os.mkdir(folder)
        path_file=folder+'/'+'page_{}.csv'.format(page_number)
        dfs[0].to_csv(path_file, index=False)

# def show_image():
#     canvas = Canvas(root,  width=400, height=400)
#     canvas.grid(row=0,column=0, columnspan=2)
 
#     img = PhotoImage(file="osa_lightning.png")
#     canvas.create_image(10, 10, anchor=NW, image=img)

def open_excel():
    page_number=user_page.get()
    folder='page_'+page_number
    path_file=folder+'/'+'page_{}.csv'.format(page_number)
    os.system("start EXCEL.EXE {}".format(path_file))

def open_calc():
        page_number=user_page.get()
        folder='page_'+page_number
        path_file=folder+'/'+'page_{}.csv'.format(page_number)
        os.system("libreoffice {}".format(path_file))

def open_modfile():
    page_number=user_page.get()
    folder='page_'+page_number
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
    folder='page_'+page_number
    path_file=folder+'/'+'page_{}.csv'.format(page_number)
    #create a copy from manually modified file
    for col in df.iloc[:,1:].columns:
        df[col]=[to_number(k) for k in df[col]]

    new_name=path_file.replace('.csv','_final.csv')
    df.to_csv(new_name, index=False)



root = tk.Tk()
root.title('Transk Table 0.0.1')
photo = tk.PhotoImage(file = "../letter.png")
root.iconphoto(False, photo)
style = ThemedStyle(root)
style.set_theme("arc")

user_page=tk.StringVar()


#set default font
default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(size=15)
root.option_add("*Font", default_font)

#create myfont
my_font=Font(family="Helvetica", size=12)




#==================================================================
#==================================================================
#                           VIEW FRAME
#==================================================================
#==================================================================

frame_two=tk.Frame(root)
frame_two.grid(row=0, column=0, columnspan=2, sticky='NSEW')
# frame_two.pack(expand=True, fill='both')

xscrollbar = Scrollbar(frame_two, orient='horizontal')
xscrollbar.grid(row=1, column=0, sticky='EW')

yscrollbar = Scrollbar(frame_two)
yscrollbar.grid(row=0, column=1, sticky='NS')

canvas = Canvas(frame_two,  width=1600, height=700, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
canvas.grid(row=0,column=1, sticky='EW')

canvas.columnconfigure(0, weight=1)
canvas.columnconfigure(1, weight=1)



# canvas = Canvas(frame, bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
# canvas.grid(row=0, column=0, sticky=N+S+E+W)

img_file = "/home/lucas/projects/transk_table/maranhao.jpg"
img = ImageTk.PhotoImage(Image.open(img_file))
canvas.create_image(0,0,image=img, anchor="nw")
canvas.config(scrollregion=canvas.bbox(ALL))

xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)

#==================================================================
#==================================================================
#                           TERMINAL FRAME
#==================================================================
#==================================================================

termf = tk.Frame(root, height=200, width=1600)
termf.grid(row=1, column=0, sticky='NSEW')
# termf.pack(side='left', expand=True, fill='both')

termf.columnconfigure(0, weight=1)
termf.columnconfigure(1, weight=1)

wid = termf.winfo_id()
os.system('xterm -into %d -geometry 200x1600 -sb &' % wid)

#==================================================================
#==================================================================
#                           BUTTONS FRAME
#==================================================================
#==================================================================

frame_one=tk.Frame(root)
frame_one.grid(row=1, column=1, sticky='NSEW')
# frame_one.pack(side='left', expand=True, fill='both')

# frame_one.columnconfigure(0, weight=1)
# frame_one.columnconfigure(1, weight=1)

first_step=ttk.Label(frame_one, text="Type the page number: ", background='white')
first_step.grid(row=0, column=0)
first_step_entry=ttk.Entry(frame_one,width=15, textvariable=user_page)
first_step_entry.grid(row=1, column=0)
first_step_entry.focus()

buttton_feats={'open':['Open', lambda:open_file(), 2], 'excel':['Open Excel Sheet', lambda:open_excel(), 3],
'calc':['Open Calc Sheet', lambda:open_calc(), 4], 'clean':['Clean', lambda:combine_funcs(open_modfile, transform_cols), 5],
'quit':['Quit', root.destroy, 6]}

for key in buttton_feats.keys():
    open_btn = tk.Button(frame_one, text =buttton_feats[key][0], command = buttton_feats[key][1])
    open_btn.grid(row=buttton_feats[key][2],column=0, sticky='EW')
    open_btn.config(height=2, width=15)


#==================================================================
#==================================================================
#                           END
#==================================================================
#==================================================================

root.mainloop()

