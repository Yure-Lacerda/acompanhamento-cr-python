class materia:
    def __init__(self, nome, credito, nota):
        self.credito = credito
        self.nota = nota
        self.ponto = credito*nota
        self.nome = nome

    def __repr__(self):
        return str(f'-------------------\n'
                f'{self.nome}\n'
                f'    Créditos: {self.credito}\n'
                f'    Nota: {self.nota}\n'
                f'-------------------')

def imp (lista):
    NP = ['Primeiro','Segundo','Terceiro','Quarto','Quinto','Sexto','Sétimo','Oitavo','Nono','Décimo']
    PG = 0
    CG = 0

    for x in lista:
        for y in x:
            PG += y.ponto ; CG += y.credito
   
    CR = round(PG/CG,1)
    print ("~~~~~~~~~~~~~~~~",
        f'|CR total: {CR}|',
        '~~~~~~~~~~~~~~~~',
        sep='\n'
        )   
    CA = 0
    PA = 0
    for x in range(len(lista)):
        CD = 0
        P = 0
        print('=======================',
            f'{NP[x]} Período',
            sep='\n')
        for i in lista[x]:
            CD += i.credito
            P  += i.ponto
            print(i)
        CR_X = round(P/CD,1)
        PA += P ; CA += CD
        CR_A = round(PA/CA,1)
        print('....................',
            f'|CR do Periodo: {CR_X}|',
            f'|CR Acumulado:  {CR_A}|',
              '....................',
              sep ='\n')

    return ''