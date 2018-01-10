import random

sets1 = ['GCAD','CAGD','DGAC','CDGA','ADCG','DGCA','AGDA','ACGD']
sets2 = ['GCADGCAD','CAGDCAGD','DGACDGAC','CDGACDGA','ADCGADCG','DGCADGCA','AGDAAGDA','ACGDACGD']
sets3 = ['GCADGCADGCAD','CAGDCAGDCAGD','DGACDGACDGAC','CDGACDGACDGA','ADCGADCGADCG','DGCADGCADGCA','AGDCAGDCAGDC','ACGDACGDACGD']
letters = ['G', 'C', 'D', 'A', 'GC', 'CD', 'DA', 'GA', 'GD', 'AC', 'GCD', 'CDA', 'GDA', 'GCA' ]
dupli_letters = ['GG', 'CC', 'DD', 'AA', 'GCGC', 'CDCD', 'DADA', 'GAGA', 'GDGD', 'ACAC', 'GCDGCD', 'CDACDA', 'GDAGDA', 'GCAGCA']
inver_letters = ['G', 'C', 'D', 'A', 'CG', 'DC', 'AD', 'AG', 'DG', 'DCG', 'ADC', 'ADG', 'ACG']
rand = random.randint(0,13)
rand3 = random.randint(3,13)

def deletion(chosen):  
    new = chosen.replace(letters[rand], "")
    return new
            
def duplication(chosen): 
    if difficulty == 1: 
        randb = random.randint(0,3)
    elif difficulty == 2: 
        randb = random.randint(0,10)
    elif difficulty == 3: 
        randb = random.randint(0,13)
    new = chosen.replace(letters[randb], dupli_letters[randb])
    return new

def inversion(chosen): 
    if difficulty == 1: 
        return 'this is a bug i cannot fix right now can you skip this number'
    new = chosen.replace(letters[rand3], inver_letters[rand3])
    return new

def translocation(chosen): 
    if difficulty == 1: 
        randa = random.randint(1,3)
    elif difficulty == 2: 
        randa = random.randint(1,7)
    elif difficulty == 3: 
        randa = random.randint(1,11)
    chosena = chosen[0:randa]
    new = chosen.replace(chosena, "")
    new += chosena
    return new

print('Welcome to this mini game based on the alteration of the chromosome structure')
while True: 
    print('Enter your difficulty (1, 2, 3): ')
    difficulty = input()
    if (difficulty == 1) or (difficulty == 2) or (difficulty == 3): 
        break

while True: 
    correct_answer = random.randint(1, 4) 
    set_selected = random.randint(0, 7) 
    print('You can always enter q to quit the game: ')
    print('You can answer by typing (1: deletion, 2: duplication, 3: inversion, 4: translocation: ')

    if difficulty == 1: 
        print('The given is: ' + sets1[set_selected])
        semifinal_set = sets1[set_selected]
    elif difficulty == 2: 
        print('The given is: ' + sets2[set_selected])
        semifinal_set = sets2[set_selected]
    elif difficulty == 3:
        print('The given is: ' + sets3[set_selected])
        semifinal_set = sets3[set_selected]
        
    if correct_answer == 1: 
        set2 = deletion(semifinal_set)
    elif correct_answer == 2: 
        set2 = duplication(semifinal_set)
    elif correct_answer == 3: 
        set2 = inversion(semifinal_set)
    elif correct_answer == 4: 
        set2 = translocation(semifinal_set)
    print('The alteration is: ' + set2)

    answer = input()
    if answer == correct_answer: 
        print('Correct Answer')
    elif answer == 'q': 
        print('Thank you for playing the game')
        break
    else: 
        print('Wrong Answer. Try again')
        




