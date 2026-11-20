from calculo_cr import materia, imp

#Primeiro período
alg_e_prog = materia("algorítmos e Programação",5,7)
cl = materia('Circuitos Lógicos',5,7.9)
fisexp = materia('Fisexp' ,1,8.2)
fisica_1 = materia('Física 1',4, 8)
ieci = materia('introdução a ECI',2,10)
pre_cal = materia('Pré Cálculo',4,9)
P1 = [alg_e_prog, cl, fisexp, fisica_1, ieci, pre_cal]

#Segundo periodo
fisica_2 = materia('Física 2',4,7.5)
calc_1 = materia('Cálculo 1',6,7.5)
ling = materia('Linguagem de Programação',5,8.5)
alglin = materia('Álgebrar Linear',4,9)
sd = materia('Sistemas Digitais',5,9)
P2 = [fisica_2, calc_1, ling, alglin, sd]

#####
lg = [P1, P2]
imp(lg)