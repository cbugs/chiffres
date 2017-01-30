import sys
import itertools
import __future__

def chiffres(numbers, result):
    answers = []
    #no operations for only 1 number
    if len(numbers) < 2:
        return
    #get all possible operations for permuatation
    operations = [ '+' , '-' , '*' , '/' ] * (len(numbers) - 1)
    #permute operations
    for operationList in itertools.permutations(operations, len(numbers) - 1):
        #string for eval phase and check if match result
        combinationString = '('
        for index,operation in enumerate(operationList):
            combinationString += str(numbers[index % (len(numbers) - 1)])
            if( index>0 ):
                combinationString += ')'
                combinationString = '(' + combinationString
            if index == len(numbers) - 2:
                combinationString += str(operation) + (str(numbers[index + 1]))
            else:
                combinationString += str(operation)
        combinationString += ')'
        #check if no duplicates and check if same as result
        if( combinationString not in answers):  
            if(eval(compile(combinationString, '<string>', 'eval', __future__.division.compiler_flag)) == result):
                answers.append(combinationString)
    return answers

if len(sys.argv) < 2:
    print 'Missing arguments: <numbers> <result> <limit>(default = 5)'
    exit()

numbs = map(int, (sys.argv[1]).split(',')) #example: [4,5,7,10,2,1]
result = int(sys.argv[2]) #example: 215
#loop limit over subset of numbs
try:
    limit = int(sys.argv[3]) #example: 5
except:
    limit = 5

returns = []

#permute all numbers from numbs
for numb in range(0, len(numbs) + 1):
    if len(returns) >= limit:
        break  
    for subset in itertools.permutations(numbs, numb):
        chiffre = chiffres(subset, result)
        #check if not duplicate
        if chiffre not in returns:
            returns.append(chiffre)
        returns = filter(None, returns)
        if len(returns) >= limit:
            break

print returns
