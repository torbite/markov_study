#
#
#
# ------ INICIO ------
#    1     2
# 1 0.5 , 0.5
# 2 0.5 , 0.5
#
# ------ FINAL ------
#    1     2
# 1 0.0 , 1.0
# 2 1.0 , 0.0
import copy
import random

markov = {'1' : {'1' : 50,'2' : 50},
          '2' : {'1' : 50,'2' : 50}}

melhorMak = [markov, 50]

AIs = {'1' : [markov, 50]}
qtd = 1
def testAI(mk):
    acuracias = []
    for i in range(100):
        acertos = 0
        for x in range(100):
        
            number = random.randint(1,2)

            if number == 1:
                next = 2
            else:
                next = 1


            AIchoices = mk[str(number)]


            choice = random.randint(0,100)

            if choice < AIchoices['1']:
                FNchoice = 1
            
            else:
                FNchoice = 2
            
            if FNchoice == next:
                acertos += 1
        
        

        acuracias.append((acertos/100) * 100) 
    
    #print(f'acuracia: {acuracia}\n acerto: {acertos}')
    acuracia = sum(acuracias)/100

    return acuracia

#print(f'{testAI(markov)}')
#input()


for k in range(100):
    markovesTestes = []
    
    for j in range(10):
        
        markov = copy.deepcopy( melhorMak[0])
        #print(f'markov : {markov}')
        #print(f'markov 1 : {markov["1"]}')
        
        for i in markov:
            
            
            mk = copy.deepcopy(markov)
            qtd +=1
            aumento = random.randint(1,2)
            qualMais = random.randint(1,2)
            
            if qualMais == 1 and mk[i]['1'] < 99:
                mk[i]['1'] += aumento
                mk[i]['2'] -= aumento
            elif qualMais == 2 and mk[i]['2'] < 99:
                mk[i]['2'] += aumento
                mk[i]['1'] -= aumento
            
            
            markovesTestes.append ([mk, testAI(mk)])

            
            
        
        
        for i in markovesTestes:
            
            
            
            if i[1] > melhorMak[1]:
                #print(f'markovTestes[i] : {markovesTestes[i]}')
                
                melhorMak[0] = copy.deepcopy(i[0])
                melhorMak[1] = copy.deepcopy(i[1])
                markov = copy.deepcopy( melhorMak[0])
#print(melhorMak[0],':' ,melhorMak[1])
            
markov = melhorMak[0]


act = 0
for i in range(10):
    number = random.randint(1,2)

    if number == 1:
        next = 2
    else:
        next = 1


    AIchoices = markov[str(number)]
    fstnm = str(next)


    choice = random.randint(0,100)

    if choice < AIchoices['1']:
        FNchoice = 1
        lastChoice = '1'
    else:
        FNchoice = 2
        lastChoice = '2'


    if next == FNchoice:
        act += 1
    print(f'{number} : {FNchoice} ||||| {act}')

print()
print(f'acurácia: {act/10 * 100}')
print()
for i in melhorMak[0]:
    for x in melhorMak[0][i]:
        print(f'{i} : {x} : {melhorMak[0][i][x]}')

print(melhorMak[1])
print(testAI(melhorMak[0]))
input()
