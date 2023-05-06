# 1
# from random import *
# meno = input('Ako sa voláš?')
# print('Ahoj '+meno+' rád Ťa spoznávam :)')
# roknarodenia = input(meno+', v ktorom roku si sa narodil?')
# meno2 = choice(('Alena', 'Barbora', 'Eva', 'Sofia'))
# vek = 2023 - int(roknarodenia) 
# print('Á spomínam si, v roku '+ str(roknarodenia) +' sa narodila aj '+meno2 +' a mate '+ str(vek) + ' rokov')

# 2
# from random import *
# meno = input('Ako sa voláš?')
# print('Ahoj '+meno+' rád Ťa spoznávam :)')
# roknarodenia = input(meno+', v ktorom roku si sa narodil?')
# meno2 = choice(('Alena', 'Barbora', 'Eva', 'Sofia'))
# roknarodenia = int(roknarodenia)
# vek = 2023 - roknarodenia
# vek = str(vek) 
# roknarodenia = str(roknarodenia)
# print('Á spomínam si, v roku '+roknarodenia+' sa narodila aj '+meno2 +'mate '+vek+ ' rokov')

# 3
# meno = input('Ako sa voláš?')
# vek = input(meno+', kolko mas rokov? ')
# z = 100 - int(vek)
# print('zostav ti', z, 'rokov')

# 4
# print('**********')
# print('*        *')
# print('* Andrea *')
# print('*        *')
# print('**********')

# 5
# jeden = 'andrea'
# dva = 'michal'
# spolu = ''
# for i in range(len(dva)):
#     spolu = spolu + (jeden[i] + dva[i])
# print(spolu)

# 6
# jeden = 'andrea'
# dva = 'michal'
# spolu = ''
# for i in range(len(dva)):
#    spolu = spolu + (jeden[i] + dva[i])
# print(spolu)
# jeden2= ''
# dva2 = ''
# for b in range(len(spolu)):
#     jeden2 = spolu[::2]
#     dva2 = spolu[1::2]
# print(jeden2)
# print(dva)

# 7
# jeden = 'diana'
# dva = 'ferdinand'
# spolu = ''
# for i in range(len(dva)):
#     if i < len(jeden):
#         spolu = spolu + (jeden[i] + dva[i])
#     else:
#         spolu = spolu + dva[i]
# print(spolu)

# 8
# v = input('napis vetu ' )
# if '?' in v:
#     print('opytovacia')
# elif '!' in v:
#     print('rozkazovacia')
# elif '.' in v:
#     print('oznamovacia')
# else:
#     print('neukoncil si vetu')

# 9
# import tkinter
# from random import *
# canvas = tkinter.Canvas(width=600,height = 300,bg ='white')
# canvas.pack()

# farba = ['green', 'blue', 'red', 'yellow']
# entry = tkinter.Entry()
# entry.pack()
# def z():
#     zadaj = entry.get()
#     x = 300 - (len(zadaj) * 5)
#     for i in range(len(zadaj)):
#         angle = randint(-360,360)
#         farby = choice(farba)
#         canvas.create_text(x,150,text=zadaj[i],fill=farby,font=30)
#         x+=20
# button = tkinter.Button(text= 'ok',command=z)
# button.pack()
# canvas.mainloop()

# 10
# import tkinter
# from random import *
# canvas = tkinter.Canvas(width=600,height = 300,bg ='white')
# canvas.pack()

# farba = ['green', 'blue', 'red', 'yellow']
# entry = tkinter.Entry()
# entry.pack()
# def z():
#     canvas.delete('all')
#     zadaj = entry.get()
#     x = 300 - (len(zadaj) * 5)
#     y = 150
#     for i in range(len(zadaj)):
#         farby = choice(farba)
#         if i % 2 == 0:
#             canvas.create_text(x,y-10,text=zadaj[i],fill=farby,font=30)
#         else:
#             canvas.create_text(x,y+10,text=zadaj[i],fill=farby,font=30)
#         x+=10
    
# button = tkinter.Button(text= 'ok',command=z)
# button.pack()
# canvas.mainloop()

# 11
# ser na to

# 12
# veta = input('napis vetu: ')
# slova = veta.split()
# print(len(slova))
# dlzka = 0
# index = 0
# slovo = []
# for i in range(len(slova)):
#     if len(slova[i]) > dlzka:
#         dlzka = len(slova[i])
#         index = i
#     if len(slova[i]) == dlzka:
#         slovo.append(i)
# print(dlzka , index)
# print(slovo)
# vsetky = []
# for i in range(len(slovo)):
#     v = slovo[i]
#     vsetky.append(slova[v])
# print(vsetky)

# 13
# ser na to

# 14
# s = 'AMnidcrheaal'
# jeden = s[::2]
# druhy = s[1::2]
# print(jeden)
# print(druhy)

# 15
# s = 'Python'
# g =  6
# for i in range(len(s)):
#    sn = '.'*g + s[:i+1]
#    g=g-1
#    print(sn)

# 16
# s = 'Python'
# g = 6
# f = 6
# for i in range(len(s)):
#    sn = '.'*g + s[i::-1]
#    g=g-1
#    sm = s[:i+1:]+'.'*g
#    print(sn + sm)

# 17
# mail = 'michal.velky@mail.pythonsoftware.net'
# index = mail.find("@")
# index2 = mail.rfind('.')
# b = mail.find('.')
# v = mail.find('.', b +1)
        
# d3 = mail[index+1:v]
# d2 = mail[v+1:index2]
# d1 = mail[index2+1:]

# jedna = mail[index2:]
# dva = mail[index+1:]
# trojka = mail[:index]
# print(jedna)
# print(dva)
# print(trojka)
# print(d1 + '\n' + d2 + '\n' + d3)

# 18
# cislo = input('napis rodne cislo: ')
# mesiac = int(cislo[2]+cislo[3])
# den = int(cislo[4]+cislo[5])
# pohlavie = ''
# if mesiac > 12:
#     mesiac -= 50
#     pohlavie = 'zena'
#     datum = str(den)+'.'+str(mesiac)+'.'+'19'+cislo[0]+cislo[1]
#     print(datum)
# else:
#     pohlavie = 'muz'
#     datum = str(den)+'.'+str(mesiac)+'.'+'19'+cislo[0]+cislo[1]
#     print('datum narodenia: '+datum)
# print(pohlavie)

# 19
# ad = 'https://shop.pythonsoftware.com/download/examples'
# domena = ad.rfind('.')
# lom3 = ad[domena:].find('/')
# lom33 = lom3+domena
# print(ad[domena+1:lom33])
# db = ad.find(':')
# protokol = ad[:db]
# print(protokol)
# index = ad.find('/', ad.find('/') + 1)
# c = ad[index+1:lom33]
# print(c)

# 20
# from random import *
# print(ord('z'))
# heslo = ''
# for i in range(9):
#     velke = randrange(65,92)
#     male = randrange(97,123)
#     heslo = heslo + chr(male)
# print(heslo)

# 21
# from random import *
# print(ord('9'))
# heslo = ''
# for i in range(3):
#     velke = randrange(65,92)
#     heslo = heslo + chr(velke)
# for o in range(2):
#     cisla = randrange(48,58)
#     heslo = heslo + chr(cisla)
# for p in range(3):
#     male = randrange(97,123)
#     heslo = heslo + chr(male)
# print(heslo)

# 22
# from random import *
# heslo = ''
# for i in range(8):
#     male = randrange(97,123)
#     heslo += chr(male)
# r = randrange(0,7)
# heslo = heslo[:r] + heslo[r].upper() + heslo[r+1:]
# print(heslo)

# 23
# pismena = ''
# for i in range(97,123):
#     pismena += chr(i) + ', '
# print(pismena)

# 24
# cisla = ''
# for i in range(48,58):
#     cisla += chr(i) + ', '
# for i in range(0,10):
#     cisla += str(i) + ', '
# print(cisla)

# 25
# vstup = input('Zadaj text:')
# sifra = ''
# for znak in vstup:
#     novyznak = znak
#     if 'a' <= znak <= 'y':
#         novyznak = chr(ord(znak)+2)
#     if znak == 'z':
#         novyznak = 'b'
#     if znak == 'y':
#         novyznak = 'a'
#     sifra = sifra+novyznak
# print(sifra)

# 26
# vstup = input('Zadaj text:')
# sifra = ''
# for znak in vstup:
#     novyznak = znak
#     if 'b' <= znak <= 'z':
#         novyznak = chr(ord(znak)-1)
#     if znak == 'a':
#         novyznak = 'z'
#     sifra = sifra+novyznak
# print(sifra)

# 27
# vstup = input('Zadaj text:')
# sifra = ''
# for znak in vstup:
#     novyznak = znak
#     if 'c' <= znak <= 'z':
#         novyznak = chr(ord(znak)-2)
#     if znak == 'a':
#         novyznak = 'y'
#     if znak == 'b':
#         novyznak = 'z'
#     sifra = sifra+novyznak
# print(sifra)

# 28
# vstup = input('Zadaj text:')
# posun = int(input('Zadaj posun: '))
# sifra = ''
# for znak in vstup:
#     novyznak = znak
#     if 'a' <= znak <= 'z':
#         novyznak = chr((ord(znak) - ord('a') + posun) % 26 + ord('a'))
#     sifra = sifra + novyznak
# print(sifra)

# 29
# from random import *
# s = input('zadaj daco: ')
# novy = ''
# for i in range(len(s)):
#     ktory = randrange(len(s))
#     print('Odstraňujem znak', s[ktory])
#     novy = novy+s[ktory]
#     print('Zatiaľ som vytvoril:', novy)
#     s = s[:ktory]+s[ktory+1:]
#     print('Ešte zostali tieto znaky:', s)
#     print('Zamiešané slovo:', novy)

# 30
# from random import *
# s = input('zadaj daco: ')
# org = s
# novy = ''
# def zamiesanie(s,novy):
#     for i in range(len(s)):
#         ktory = randrange(len(s))
#         print('Odstraňujem znak', s[ktory])
#         novy = novy+s[ktory]
#         print('Zatiaľ som vytvoril:', novy)
#         s = s[:ktory]+s[ktory+1:]
#         print('Ešte zostali tieto znaky:', s)
#         print('Zamiešané slovo:', novy)
# for i in range(2):
#     s = org
#     print ('zaklad slova: ' + s )
#     zamiesanie(s,novy)

# 31
# s = 'byvali v byte.'
# pis = ['y','Y','i','I']
# for znak in s:
#     if znak in pis:
#         sp = s.replace(znak,'-')      
# print(sp)
# skus = input('dopln: '  )
# if s != skus:
#     for i in range(len(s)):
#         if s[i] != skus[i]:
#             s = s.replace(s[i],'!')
#         else:
#             continue
# else:
#     print('spravne')
# print(s)

# 1
# podmet = ('Kamarát', 'Spolužiak', 'Andrej', 'Roman')
# prisudok = ('videl', 'prezradil', 'povedal', 'napísal', 'zistil',
# 'nakreslil')
# predmet = ('tajomstvo', 'prekvapenie', 'predsavzatie')
# for i in podmet:
#     for f in prisudok:
#         for g in predmet:
#             print(i +' '+ f +' ' + g)

# 2
# import tkinter
# canvas = tkinter.Canvas(width=400, height=400)
# canvas.pack()
# A = (100, 100)
# B = (200, 100)
# C = (250, 150)
# D = (150, 300)
# def kresli():
#     canvas.delete('all')
#     canvas.create_line(A, B, C, A, fill='blue', width=4)
#     canvas.create_line(D, B, A, D, fill='red', width=4)
#     canvas.create_line(A, C, D, A, fill='green', width=2)
# def zmenC(suradnice):
#     global C
#     C = (suradnice.x, suradnice.y)
#     kresli()
# def zmenD(suradnice):
#     global D
#     D = (suradnice.x, suradnice.y)
#     kresli()
# kresli()
# canvas.bind('<B1-Motion>', zmenD)
# canvas.bind('<B3-Motion>', zmenC)
# canvas.mainloop()

# 3
# import tkinter
# canvas = tkinter.Canvas(width=400, height=400)
# canvas.pack()
# ciara = ()
# def kresli():
#     canvas.delete('all')
#     if len(ciara) >= 4:
#         canvas.create_line(ciara, fill='blue', width=4)
# def pridajbod(suradnice):
#     global ciara
#     ciara = ciara + (suradnice.x, suradnice.y)
#     kresli()
# canvas.bind('<Button-1>', pridajbod)
# canvas.mainloop()

# 3. 1
# subor = open('kodovanie.txt', 'w')
# for i in range(97, 123):
#     subor.write(f"{chr(i)} {i} {' '}\n")

# 2
# import random
# pocet = input('kolko hesiel chces?')
# heslo = ''
# subor = open('hesla.txt', 'w')
# for k in range(int(pocet)):
#         for i in range(8):
#             pismeno = random.randint(97,122)
#             heslo = heslo + chr(pismeno)
#         subor.write(f'{heslo}\n')
#         heslo = ''

# 3
# veta = input('Napíš svoj odkaz, ktorý uložím pre budúcnosť :) :')
# if veta == 'delete':
#     subor = open('odkazy.txt', 'w')
#     subor.close()
# elif veta.strip() != '':
#     subor = open('odkazy.txt', 'a')
#     subor.write(veta+'\n')
#     subor.close()

# 4    
# import tkinter
# import random
# canvas = tkinter.Canvas(width=500,height=500)
# canvas.pack()
# label = tkinter.Label(text= 'meno: ', font=('Helvetica', 15))
# label.place(x=130,y=277)
# entry = tkinter.Entry(font=('Helvetica', 13))
# entry.place(x=200,y=280)

# def ano():
#     subor = open('hodnotenie.txt','a')
#     meno = entry.get()
#     if meno == '':
#         meno = 'anonym'
#     subor.write(meno + ': ' + 'ano'+'\n')
#     subor.close()
# def nie():
#     subor = open('hodnotenie.txt','a')
#     meno = entry.get()
#     if meno == '':
#         meno = 'anonym'
#     subor.write(meno + ': ' + 'nie'+'\n')
#     subor.close()

# canvas.create_text(250,170,text='boli ste spokojny?', font=('Helvetica', 30))
# button1 = tkinter.Button(text= 'ano',command=ano, font=('Helvetica', 20))
# button1.place(x=320, y=330)
# button2 = tkinter.Button(text= 'nie',command=nie, font=('Helvetica', 20))
# button2.place(x=120, y=330)
# canvas.mainloop()

# 5
# import tkinter
# import random
# canvas = tkinter.Canvas(width=500,height=500)
# canvas.pack()

# def kruh(sur):
#     x=sur.x
#     y=sur.y    
#     canvas.create_oval(x-10,y-10,x+10,y+10,fill='pink',outline='pink')
#     print(x,y)
#     subor = open('suradnice.txt','a')
#     subor.write(f'{x}:{y} \n')
# canvas.bind('<Button-1>',kruh)
# canvas.mainloop()



















