#! python 3

#This code randomly generates string 27 char long from 26 letters
#and space. A function will generate and score the random vs:
#target sentence: “methinks it is like a weasel”

#After 1000 tries, print best string so far + score

#TODO: Generate string
def char28():
    import random
    chars = 'abcdefghijklmnopqrstuvwxyz '
    ch_list = []
    rand_sent = ''
    for i in range(len(chars)):
        ch_list.append(chars[i])
    for i in range(28):
        rand_sent += random.choice(ch_list)
        
    return rand_sent

#TODO: Score random string vs target
def score(target, rand_sent):
    total = len(target)
    if len(target) != len(rand_sent):
        print('Target and random sentences have different # characters!!!')
    matches = 0
    for i in range(len(target)):
        if target[i] == rand_sent[i]:
            matches += 1
    score = matches / total
    return score, rand_sent
        
#TODO: Print best string so far + score every 1000x
def monkey(trials, target):
    print('Passed in target is: ' + target)
    best = [0, 'none'] #initial values
    for i in range(trials):
        if (i != 0) and (i % 1000 == 0): #correct ver.: (i!=0)
            print('We are on trial %s.\nBest score is %s%%.\nIt is "%s".\n' % (i, best[0], best[1]))
        trial = list(score(target, char28()))
        if (trial[0] > best[0]):
            best = trial
            
#TODO: Main fn.
target = 'methinks it is like a weasel'
monkey(100001, target)
print('Official Target is "%s".' % target)

#DONE! However observe output with grain of salt,
#may be bug or rounding errors in score calculations
