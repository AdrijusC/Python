# print("Pirmas kartas")

# paz = int(input('paz = ....'))
# if paz >= 1 and paz <=3:
#     print('blogai')
# elif 4 <=paz<=6:
#     print('Patenkinamai')
# elif 7<=paz<=9:
#     print('gerai')
# elif paz == 10:
#     print('puiku')
# else:
#     print('negalimas')

#07 pakartokim
###ivedamas menseis skaiciumi Atspausdinti jo pavadinima
    
# men = input('men = ...')
# match men:
#     case '1':
#         txt = 'Sausis'
#     case '2':
#         txt = 'Vasaris'
#     #.....................
#     case _:
#         txt = 'Blogai ivesti duomenys'

# print(f'{men} -----> {txt}')

#07 pakartokim
###ivedamas menseis skaiciumi Atspausdinti jo 

# men = int(input('men = ...'))
# match men:
#     case 12|1|2:
#         txt = 'Ziema'
#     case 3|4|5:
#         txt = 'Pavasaris'
#     #.....................
#     case _:
#         txt = 'Blogai ivesti duomenys'

# print(f'{men} -----> {txt}')

###Funkcija // funkcija veikia su parametrais () tarp skliaustu buna
# def labas(txt):
#     print('Labas', txt)

# labas('Algis')

### def skaiciuoti(a,b):
#     '''
#     do
#     ku
#     men
#     ta 
#     ci
#     ja
#     '''
#     rez = a - b
#     return rez

# sk1, sk2, = 5,8
# print (skaiciuoti(sk1, sk2))
# # ats = skaiciuoti(sk1, sk2)
# # print(ats)

# print(skaiciuoti(b= sk2, a = sk1))

###      apskaiciuoti kazkiek prekiu pvm\

# def mokesciai(*args, **kwargs):
#     return sum(args)*0.21

# print(mokesciai(5, 5.21, 8.7, 4, 7))
# print(mokesciai(5, 5.21, 8.7))
# print(mokesciai(5, 5.21, 8.7, 4, 7, 8, 6))

### Petriuko 3 pazymiai. rasti vidurki

# def ivedimas(txt):
#     p = int(input(f'{txt}=...'))
#     if not(1<=p1<=10):
#         print('Blogas. Kartokite ivedima')
#         return ivedimas(txt)
#     return p
###

# p1 = int(input('p1 = ...'))
# if not(1<=p1<=10):
#     print('Blogas. Kartokite ivedima')
# p2 = int(input('p2 = ...'))
# p3 = int(input('p3 = ...'))
# suma = p1 + p2 + p3
# vid = suma / 3
# print(vid)

### Ciklai
# kiek zodziu
# txt = 'Labas Rytas'
# pirstas = 0
# for i in txt:
#     if pirstas == 0:
#         pirstas += 1
#     if i == ' ':
#         pirstas+=1

# print(f'"{txt}" sakinyje yra {pirstas} zod.')

# range(start, stop, step)
# a = range(2, 25, 3)
# print(a)
## For ciklas
# for i in range(25):
#     print(i,end=',')
#     print('labas',end=',')
# print('Labas'*25)

#n pazymiu. Rasti vidurki
# n = int(input('n=...'))
# suma = 0
# for i in range(n):
#     paz = int(input(f'Koks {i}-as pazymys'))
#     if 1<=paz<=10:
#         suma += paz
#     else:
#         print('Kartokite ivedima')
#         i = i - 1
# vid = suma / n
# print(vid)
