word1 = input()
word2 = input()
word3 = input()

# vertebrado
if word1 == 'vertebrado':
    if word2 == 'ave':
        if word3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if word3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
# invertebrado
else:
    if word2 == 'inseto':
        if word3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if word3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca') 