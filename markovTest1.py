#
#     1  |  2  |  3  |  4
# 1 0,25  0,25  0,25  0,25
# 1 0,25  0,25  0,25  0,25
# 1 0,25  0,25  0,25  0,25
# 1 0,25  0,25  0,25  0,25
#
#
#     1  |  2  |  3  |  4
# 1 0,25  0,25  0,25  0,25
# 1 0,25  0,25  0,25  0,25
# 1 0,25  0,25  0,25  0,25
# 1 0,25  0,25  0,25  0,25
#
import copy
import random



def respostaIA(mk : dict, inputComp : int):
    checkDict = markov[str(inputComp)]
    choice = random.randint(0,100)
    
    if choice < checkDict['1']:
        return '1'
    elif choice < checkDict['2'] + checkDict['1']:
        return '2'
    elif choice < checkDict['3'] + checkDict['2'] + checkDict['1']:
        return '3'
    else:
        return '4'

def testIA(mk):
    
    qtdTestes = 100
    qtd2testes = 100
    sumAur = 0
    for x in range(qtd2testes):
        acerto = 0
        for i in range(qtdTestes):
            number = random.randint(1,4)
            next = number + 1
            if next == 5:
                next = 1
            resposta = int(respostaIA(mk, number))
            if resposta == next:
                acerto +=1
        
        
        acuracia = (acerto/qtdTestes) * 100
        sumAur += acuracia
    sumAur = sumAur/qtd2testes
    return sumAur

markov = {'1' : {'1' : 25, '2' : 25, '3' : 25, '4' : 25},
          '2' : {'1' : 25, '2' : 25, '3' : 25, '4' : 25},
          '3' : {'1' : 25, '2' : 25, '3' : 25, '4' : 25},
          '4' : {'1' : 25, '2' : 25, '3' : 25, '4' : 25}}

melhorMak = [markov, testIA(markov)]

alert = 0
for i in range(1000):
    alert += 1
    
    if alert % 100 == 0:
        print(alert)
    markoves = []
    for x in range(10):
        
        mk = copy.deepcopy(melhorMak[0])
        for y in mk:
            
            qtdAumento = random.randint(1,15)
            numerosAumento = []
            numerosNaoAumento = []
            opcs = ['1','2','3','4']

            nm = random.randint(0,3)
            numerosAumento.append(opcs[nm])
            opcs.pop(nm)
            nm = random.randint(0,2)
            numerosNaoAumento.append(opcs[nm])
            
            
            
            for v in numerosAumento:

                if mk[y][v] < 85:
                    mk[y][v] += qtdAumento
                
            
            for v in numerosNaoAumento:
                if mk[y][v] > 15:
                    mk[y][v] -= qtdAumento
                
            
            
        markoves.append([copy.deepcopy(mk), testIA(mk)])
        #kjh = 0
        #for i in markoves:
        #    print()
        #    kjh +=1
        #    print(f'IA {kjh}')
        #    for z in i[0]:
        #        print(i[0][z])
    for l in markoves:

        if l[1] > melhorMak[1]:
            melhorMak[0] = copy.deepcopy(l[0])
            melhorMak[1] = copy.deepcopy(l[1])
            
        
        
        
for i in melhorMak[0]:
    print(melhorMak[0][i])
print(melhorMak[1])
print(testIA(melhorMak[0]))