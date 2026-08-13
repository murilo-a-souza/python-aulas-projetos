def calcular_media_cps(notas_cp):
    menor_nota = notas_cp[0]
    soma_total = 0
    for nota in notas_cp:
        if nota < menor_nota:
            menor_nota = nota
        soma_total += nota
    soma_total -= menor_nota
    return soma_total


def calcular_media_sprints(sprints):
    soma_total = 0
    for nota in sprints:
        soma_total += nota
    media = soma_total / len(sprints)
    return media

def calcular_media_semestre(notas_cp, sprints, gs):
    media_semestre = calcular_media_cps(notas_cp)*0.2 + calcular_media_sprints(sprints)*0.2 + gs*0.6
    return media_semestre

def receber_valores():
    while True:
        opcao = int(input('Digite qual valor você quer adicionar:\n1. Todos (CPs, Sprints e GS)\n2. Apenas CPs\n3. Apenas Sprints\n4. Apenas GS\n5. Voltar\n'))
        notas = {}
        match opcao:
                case 1:
                    notas.setdefault('cp1', int(input('Digite a nota do CP1: ')))
                    notas.setdefault('cp2', int(input('Digite a nota do CP2: ')))
                    notas.setdefault('cp3', int(input('Digite a nota do CP3: ')))
                    notas.setdefault('sp1', int(input('Digite a nota da Sprint 1: ')))
                    notas.setdefault('sp2', int(input('Digite a nota da Sprint 2: ')))
                    notas.setdefault('gs', int(input('Digite a nota da GS: ')))
                    return notas.items()
                case 2:
                    notas.setdefault('cp1', int(input('Digite a nota do CP1: ')))
                    notas.setdefault('cp2', int(input('Digite a nota do CP2: ')))
                    notas.setdefault('cp3', int(input('Digite a nota do CP3: ')))
                    return notas.items()
                case 3:
                    notas.setdefault('sp1', int(input('Digite a nota da Sprint 1: ')))
                    notas.setdefault('sp2', int(input('Digite a nota da Sprint 2: ')))
                    return notas.items()
                case 4:
                    notas.setdefault('gs', int(input('Digite a nota da GS: ')))
                    return notas.items()
                case 5:
                    return {}
                case _:
                    print('Opção inválida!')

def calcular_media_final(semestre1, semestre2):
    media_final = semestre1*0.4 + semestre2['media']*0.6
    return media_final

def menu_relatorio():
    notas1 = dict.fromkeys(['cp1', 'cp2', 'cp3', 'sp1', 'sp2', 'gs', 'media'], 0)
    notas2 = dict.fromkeys(['cp1', 'cp2', 'cp3', 'sp1', 'sp2', 'gs', 'media'], 0)
    media_final = 0
    situacao = 'N/A'
    while True:
        print(f"------------------------------------------------------------------------------\nCALCULADORA DE MÉDIA FIAP\n------------------------------------------------------------------------------\nNotas 1ºSemestre:\ncp1= {notas1.get('cp1'):.2f}; cp2= {notas1.get('cp2'):.2f}; cp3= {notas1.get('cp3'):.2f}; sp1= {notas1.get('sp1'):.2f}; sp2= {notas1.get('sp2'):.2f}; gs= {notas1.get('gs'):.2f}; media= {notas1.get('media'):.2f}\n\nNotas 2ºSemestre:\ncp1= {notas2.get('cp1'):.2f}; cp2= {notas2.get('cp2'):.2f}; cp3= {notas2.get('cp3'):.2f}; sp1= {notas2.get('sp1'):.2f}; sp2= {notas2.get('sp2'):.2f}; gs= {notas2.get('gs'):.2f}; media= {notas2.get('media'):.2f}\n\nMédia final= {media_final:.2f}; Situação= {situacao}\n------------------------------------------------------------------------------")
        opcao = int(input('Digite uma opção:\n1. Primeiro semestre\n2. Segundo semestre\n3. Sair\n'))
        match opcao:
            case 1:
                novas_notas = receber_valores()
                for chave, item in novas_notas:
                    notas1[chave] = item
                notas1['media'] = calcular_media_semestre([notas1.get('cp1'), notas1.get('cp2'), notas1.get('cp3')], [notas1.get('sp1'), notas1.get('sp2')], notas1.get('gs'))
                print(f'Média semestral: {calcular_media_semestre([notas1.get('cp1'), notas1.get('cp2'), notas1.get('cp3')], [notas1.get('sp1'), notas1.get('sp2')], notas1.get('gs'))}')
            case 2:
                novas_notas = receber_valores()
                for chave, item in novas_notas:
                    notas2[chave] = item
                notas2['media'] = calcular_media_semestre([notas2.get('cp1'), notas2.get('cp2'), notas2.get('cp3')], [notas2.get('sp1'), notas2.get('sp2')], notas2.get('gs'))
            case 3:
                return
        media_final = calcular_media_final( notas1['media'], notas2['media'])
        if media_final > 6:
            situacao = 'APROVADO!'
        else:
            situacao = 'REPROVADO!'
            

menu_relatorio()