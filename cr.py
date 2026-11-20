class materia:
    def __init__(self, credito, nota):
        self.credito = credito
        self.nota = nota
        self.ponto = credito*nota
        self.nome = self
#Primeiro período
alg_e_prog = materia(5,7)
cl = materia(5,7.9)
fisexp = materia(1,8.2)
fisica_1 = materia(4, 9)
ieci = materia(2,10)
pre_cal = materia(4,7.9)
P1 = [alg_e_prog, cl, fisexp, fisica_1, ieci, pre_cal]

#Segundo periodo
fisica_2 = materia(4,7)
calc_1 = materia(6,7)
ling = materia(5,8.5)
alglin = materia(4,9)
sd = materia(5,8)
P2 = [fisica_2, calc_1, ling, alglin, sd]

#Terceiro período

#Pontos, lista e créditos globais
LG = P1 + P2
PG = 0
CG = 0
for x in LG:
    PG += x.ponto

for x in LG:
    CG += x.credito

#CR
CR = round(PG/CG,1)
print (CR)