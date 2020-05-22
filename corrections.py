import pandas as pd
import numpy as np
from colorama import Fore,Style
pd.set_option('max_row',500)
import sys
from os.path import expanduser

home = expanduser("~")

try:
    sys.argv[1]
except:
    raise  ValueError(Fore.RED+"Please inform the page"+Style.RESET_ALL)

try:
    sys.argv[2]
except:
    raise  ValueError(Fore.RED+"Please inform the folder"+Style.RESET_ALL)


page =sys.argv[1]
folder =sys.argv[2]

file_name=home+'/'+folder+'/'+'page_{0}/page_{0}_final.csv'.format(page)

df=pd.read_csv(file_name)

print("Here is the list of columns:")

for index,value in enumerate(list(df.columns)):
    print(Fore.YELLOW+str(index)+": "+value)

    print(Style.RESET_ALL)
col_index=int(input("What column do you want to change? "))
col=df.columns[col_index]

if sum(df[col].isna())==0:
    print(Fore.RED + "WARNING: this column is complete")
    print(Style.RESET_ALL)
    
row=df.index[0]
while row<=np.max(df.index):
    print('This is the current value in position ({},{}):\n'.format(row,col)+
                Fore.YELLOW+'{}'.format(df.at[row,col]))
    print(Style.RESET_ALL)
    change=input("Do you want to change? (Enter to skip) ")
    
    if change=='':
        row+=1
    elif change.lower()=='yes':
        new_value=input("Please, give me the new value: ")
        df.at[row,col]=new_value
        print(Fore.GREEN+"Saving changes ...")
        print(Style.RESET_ALL)
        df.to_csv(file_name, index=False)
        row+=1
    elif change.lower()=='no':
        cont=input("Do you want to continue? ")
        if cont.lower()=='yes':
            row+=1
        else:
            break
if row>np.max(df.index):
    print(Fore.MAGENTA+"This column has finish. Bye!")
    print(Style.RESET_ALL)
else:
    print(Fore.MAGENTA+"Bye!")
    print(Style.RESET_ALL)
