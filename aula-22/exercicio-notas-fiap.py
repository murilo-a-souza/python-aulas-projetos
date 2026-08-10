 
def descarta_menor(cps: list):
    if cps[0] < cps[1] and cps[0] < cps [2]: 
        cps.pop[0]
        return cps
    if cps[1] < cps[0] and cps[1] < cps [2]: 
        cps.pop[1]
        return cps
    if cps[2] < cps[1] and cps[2] < cps [0]:
        cps.pop[2]
        return cps
    cps.pop()
    return cps #previne de não retornar nada se odos forem iguais
    

def calculo_semestral(cp1: float, cp2: float, cp3: float, sprint1: float, sprint2: float, gs: float):
    #retornar menor cp e subtrai ele
    cps = descarta_menor([cp1, cp2, cp3])
    soma = 0
    for x in cps:
        soma += x
    soma /= 2
    return soma*0.2 + sprint1*0.1 + sprint2*0.1 + gs*0.6

def registrar_valores():
    notas = {}
    notas.setdefault("cp1", float(input('Digite a nota do primeiro cp: ')))
    notas.setdefault("cp2", float(input('Digite a nota do segundo cp: ')))
    notas.setdefault("cp3", float(input('Digite a nota do terceiro cp: ')))
    notas.setdefault("sprint1", float(input('Digite a nota da primeira Sprint: ')))
    notas.setdefault("sprint2", float(input('Digite a nota da segunda Sprint: ')))
    notas.setdefault("gs", float(input('Digite a nota da GS: ')))
    return notas
    

def nota_geral(nota1s, nota2s):
    return nota1s*0.4 + nota2s*0.6

def menu_geral():
    cp1 = 0
    cp2 = 0
    cp3 = 0
    sp1 = 0
    sp2 = 0
    gs = 0
    scp1 = 0
    scp2 = 0
    scp3 = 0
    ssp1 = 0
    ssp2 = 0
    sgs = 0
    while True:
        notas = {}
        opcao = int(input(f'CALCULADORA DE NOTAS FIAP\n----------------------------------\nNotas atuais:\nPRIMEIRO SEMESTRE: cp1={cp1:.1f} cp2={cp2:.1f} cp3={cp3:.1f} sp1={sp1:.1f} sp2={sp1:.1f} gs={gs:.1f}\nSEGUNDO SEMESTRE: cp1={scp1:.1f} cp2={scp2:.1f} cp3={scp3:.1f} sp1={ssp1:.1f} sp2={ssp1:.1f} gs={sgs:.1f}\n----------------------------------\nDigite uma opção abaixo:\n1. Calcular notas do primeiro\n2. Calcular notas do segundo\n3. Retornar média geral\n4. Sair'))
        match opcao:
            case 1:
                notas = registrar_valores()
                cp1 = notas.get("cp1")
                cp2 = notas.get("cp2")
                cp3 = notas.get("cp3")
                sp1 = notas.get("sp1")
                sp2 = notas.get("sp2")
                gs = notas.get("gs")
            case 2:
                scp1 = float(notas.get("cp1"))
                scp2 = float(notas.get("cp2"))
                scp3 = float(notas.get("cp3"))
                ssp1 = float(notas.get("sp1"))
                ssp2 = float(notas.get("sp2"))
                sgs = float(notas.get("gs"))
            case 3:
                print('Sua média anual é: ', nota_geral(
                    calculo_semestral(cp1, cp2, cp3, sp1, sp2, gs),
                    calculo_semestral(scp1, scp2, scp3, ssp1, ssp2, sgs)))
            case 4:
                print('Encerrando')
        if opcao == 0:
            break
                



menu_geral()