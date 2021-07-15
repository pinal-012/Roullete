from tkinter import *
from tkinter import ttk  #for image
import random

root = Tk()
root.title("Welcome to Roullete!")
root.geometry("1150x1000")
root.configure(bg='light blue')

bonus_chips=5000

row1=[]
row2=[]
row3=[]

for i in range(3,37,3):
    row1.append(i)
for i in range(2,36,3):
    row2.append(i)
for i in range(1,35,3):
    row3.append(i)

red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

#------Begin: winning amount status
score_list=[]
def result():
    global bonus_chips
    odd=[i for i in range(1,37,2)]
    even=[i for i in range(2,37,2)]
    first_18=[i for i in range(1,19)]
    last_18=[i for i in range(19,37)]
    first_12=[i for i in range(1,13)]
    second_12=[i for i in range(13,25)]
    third_12=[i for i in range(25,37)]

    print(spin)
    print(dict1)
    for choice in dict1:
        #bet amount=price
        if choice=='EVEN':
            l2=[2*dict1[choice] if spin in even else 0]
            score_list.extend(l2)
        elif choice=='ODD':
            l2=[2*dict1[choice] if spin in odd else 0]
            score_list.extend(l2)
        elif choice=='RED':
            l2=[2*dict1[choice] if spin in red else 0]
            score_list.extend(l2)
        elif choice=='BLACK':
            l2=[2*dict1[choice] if spin in black else 0]
            score_list.extend(l2)
        elif choice=='1st 18':
            l2=[2*dict1[choice] if spin in first_18 else 0]
            score_list.extend(l2)
        elif choice=='18 to 36':
            l2=[2*dict1[choice] if spin in last_18 else 0]
            score_list.extend(l2)
        
        #bet amount=2*price
        elif choice=='1st 12':
            l2=[3*dict1[choice] if spin in first_12 else 0]
            score_list.extend(l2)
        elif choice=='2nd 12':
            l2=[3*dict1[choice] if spin in second_12 else 0]
            score_list.extend(l2)
        elif choice=='3rd 12':
            l2=[3*dict1[choice] if spin in third_12 else 0]
            score_list.extend(l2)
        elif choice=='R1 2 to 1':
            l2=[3*dict1[choice] if spin in row1 else 0]
            score_list.extend(l2)
        elif choice=='R2 2 to 1':
            l2=[3*dict1[choice] if spin in row2 else 0]
            score_list.extend(l2)
        elif choice=='R3 2 to 1':
            l2=[3*dict1[choice] if spin in row3 else 0]
            score_list.extend(l2)
        
        #bet amount=36*price
        elif choice in table or choice=='00':
            l2=[36*dict1[choice] if spin==choice else 0]
            score_list.extend(l2)
    print(score_list)
    score=sum(score_list)
    #bonus_chips=bonus_chips+score
    bonus_chips=bonus_chips+score
    bonus_chipsVar.set(bonus_chips)
    btn_playAgain.configure(state=NORMAL)
    print(bonus_chips)
#------End: winning amount status


#------Begin: spin roullete
spin=0
table=[]
def spin_roullete():
    global spin,table
    table=row1+row2+row3
    table.append('00')
    spin=random.choice(table)
    btn_spin.configure(text="Roullete Number {}".format(spin),font=('arial',13))
    btn_spin.configure(state=DISABLED)
    result()
#------End: spin roullete


#------Begin: Create dictionary of user selection and pop-up button
dict1={}
def select(x,obj):
    global bonus_chips
    chip=10
    if x not in dict1:
        dict1[x]=chip
        if x in list_table_end:
            prize=1
        elif x in row1 or x in row2 or x in row3 or x=='00':
            prize=35
        elif x in list_2to1 or x in list_12_group:
            prize=2

        popUp=f"{x}\n{dict1[x]}*{prize}\nBET:{dict1[x]}"
        obj.set(popUp)
        bonus_chips-=chip
        bonus_chipsVar.set(bonus_chips)

    else:
        dict1[x]+=chip
        if x in list_table_end:
            prize=1
        elif x in row1 or x in row2 or x in row3 or x=='00':
            prize=35
        elif x in list_2to1 or x in list_12_group:
            prize=2

        popUp=f"{x}\n{dict1[x]}*{prize}\nBET:{dict1[x]}"
        obj.set(popUp)
        bonus_chips-=chip
        bonus_chipsVar.set(bonus_chips)
    print(dict1)
#------End: Create dictionary of user selection and pop-up button   


# -----  begin :  btn display code
list_2to1=['R1 2 to 1','R2 2 to 1','R3 2 to 1']
list_12_group=['1st 12','2nd 12','3rd 12']
list_table_end=['1st 18','EVEN','RED','BLACK','ODD','18 to 36']

def buttonCode():

    #'00' button code
    zeroVar=StringVar()
    zeroVar.set('00')
    btn_00=Button(textvariable=zeroVar,height=16,width=5,bg='green',fg='white',font=('arial',9),command=lambda x='00',obj=zeroVar:select(x,obj))
    btn_00.grid(row=1, column=0,rowspan=3)

    #2 to 1 button code--->list_2to1=['R1 2 to 1','R2 2 to 1','R3 2 to 1']
    for i in list_2to1:
        twoToOneVar=StringVar()
        twoToOneVar.set(i)
        btn=Button(textvariable=twoToOneVar,height=6,width=6,bg='green',fg='white',font=('arial',7),command=lambda x=i,obj=twoToOneVar:select(x,obj))
        btn.grid(row=list_2to1.index(i)+1, column=13,ipady=3)

    #num 1 to 36 button code
    for i in row1:
        if i in red:
            topLineVar=StringVar()
            topLineVar.set(i)
            btn=Button(textvariable=topLineVar,height=3,width=7,bg='red',fg='white',font=('arial',15),command=lambda x=i,obj=topLineVar:select(x,obj))
            btn.grid(row=1, column=row1.index(i)+1)

        else:
            topLineVar=StringVar()
            topLineVar.set(i)
            btn=Button(textvariable=topLineVar,height=3,width=7,bg='black',fg='white',font=('arial',15),command=lambda x=i,obj=topLineVar:select(x,obj))
            btn.grid(row=1, column=row1.index(i)+1)
            
    for j in row2:
        if j in red:
            middleLineVar=StringVar()
            middleLineVar.set(j)
            btn=Button(textvariable=middleLineVar,height=3,width=7,bg='red',fg='white',font=('arial',15),command=lambda x=j,obj=middleLineVar:select(x,obj))
            btn.grid(row=2, column=row2.index(j)+1)
        else:
            middleLineVar=StringVar()
            middleLineVar.set(j)
            btn=Button(textvariable=middleLineVar,height=3,width=7,bg='black',fg='white',font=('arial',15),command=lambda x=j,obj=middleLineVar:select(x,obj))
            btn.grid(row=2, column=row2.index(j)+1)

    for k in row3:
        if k in red:
            lastLineVar=StringVar()
            lastLineVar.set(k)
            btn=Button(textvariable=lastLineVar,height=3,width=7,bg='red',fg='white',font=('arial',15),command=lambda x=k,obj=lastLineVar:select(x,obj))
            btn.grid(row=3, column=row3.index(k)+1)
        else:
            lastLineVar=StringVar()
            lastLineVar.set(k)
            btn=Button(textvariable=lastLineVar,height=3,width=7,bg='black',fg='white',font=('arial',15),command=lambda x=k,obj=lastLineVar:select(x,obj))
            btn.grid(row=3, column=row3.index(k)+1)

    # button 1st 12, 2nd 12, 3rd 12 --->list_12_group=['1st 12','2nd 12','3rd 12']
    group12Column=1
    for a in list_12_group:
        group12Var=StringVar()
        group12Var.set(a)
        btn=Button(textvariable=group12Var,height=2,width=31,bg='green',fg='white',font=('arial',15),command=lambda x=a,obj=group12Var:select(x,obj))
        btn.grid(row=4, column=group12Column,columnspan=4)
        group12Column+=4

    #button even,odd,red,black,1st 18,18 to 36---->list_table_end=['1st 18','EVEN','RED','BLACK','ODD','18 to 36']
    tableEndColumn=1
    for b in list_table_end:
        tableEndVar=StringVar()
        tableEndVar.set(b)
        if b=='RED':
            btn_1st_18=Button(textvariable=tableEndVar,height=2,width=15,bg='red',fg='white',font=('arial',15),command=lambda x=b,obj=tableEndVar:select(x,obj))
            btn_1st_18.grid(row=5, column=tableEndColumn,columnspan=2)
            tableEndColumn+=2
        elif b=='BLACK':
            btn_1st_18=Button(textvariable=tableEndVar,height=2,width=15,bg='black',fg='white',font=('arial',15),command=lambda x=b,obj=tableEndVar:select(x,obj))
            btn_1st_18.grid(row=5, column=tableEndColumn,columnspan=2)
            tableEndColumn+=2
        else:
            btn_1st_18=Button(textvariable=tableEndVar,height=2,width=15,bg='green',fg='white',font=('arial',15),command=lambda x=b,obj=tableEndVar:select(x,obj))
            btn_1st_18.grid(row=5, column=tableEndColumn,columnspan=2)
            tableEndColumn+=2

# -----  End :  btn display code 

#------Begin: PLay-Again/Reset code
def playAgain():
    btn_spin.configure(text='SPIN')
    dict1.clear()
    score_list.clear()
    btn_playAgain.configure(state=DISABLED)
    btn_spin.configure(state=NORMAL)
    buttonCode()                        #calling of button code function
#------End: PLay-Again/Reset code

#welcome Lable
welcome_label = Label(text='Welcome to Roullete!',height=1,width=60,fg='light blue',bg='black',font=('arial',20,'bold'))
welcome_label.grid(row=0,column=0,pady=10,columnspan=14)

#playAgain button
btn_playAgain=Button(text='Play Again',height=3,width=15,bg='black',fg='white',font=('arial',15),state=DISABLED,command=playAgain)
btn_playAgain.grid(row=6, column=11,columnspan=2,pady=60)

#Button spin
photo = PhotoImage(file = r"C:\Users\RUSHIRAJ\Desktop\tkinter\Games\Roullete\roulette.png") # Creating a photoimage object to use image 
photoimage = photo.subsample(5,5)      ## Resizing image to fit on button 
btn_spin=Button(text='SPIN',height=200,width=165,bg='black',fg='white',font=('arial',15),command=spin_roullete, image = photoimage,compound = BOTTOM)# here, image option is used to set image on button compound option is used to align image on bottom side of button 
btn_spin.grid(row=6, column=1,columnspan=2,pady=10)

#button player chips
btn_playerChips=Button(text='Player Chips',height=3,width=15,bg='black',fg='white',font=('arial',15))
btn_playerChips.grid(row=6, column=5,columnspan=2,pady=60)

#button chips display
bonus_chipsVar=StringVar()
bonus_chipsVar.set(bonus_chips)
btn_Chips=Button(textvariable=bonus_chipsVar,height=3,width=15,bg='black',fg='white',font=('arial',15))
btn_Chips.grid(row=6, column=7,columnspan=2,pady=60)


#First function calling
buttonCode()

mainloop()


