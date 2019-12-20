import copy
import random

operators = ['~', 'v', '^', '@', '$', '->', '<->']

negatedOperators = {'v':'^', '^':'v', '@':'$', '$':'@'}

'''
@: for all, $: there is, ->: implication, <->: bi-implication
'''

CNF = [
    [['~', ['FOOD', 'x']], 'v', ['LIKES', 'Ravi', 'x']],
    [['~', ['EATS', 'x', 'y']], 'v', ['KILLED', 'x'], 'v', ['FOOD', 'y']],
    [['EATS', 'Ajay', 'Peanuts'], '^', ['ALIVE', 'Ajay']],
    [['KILLED', 'x'], 'v', ['ALIVE', 'x']],
    [['~', ['ALIVE', 'x']], 'v', ['~', ['KILLED', 'x']]],
    ['LIKES', 'Ravi', 'Peanuts'],
    ['~', ['LIKES', 'Ravi', 'Peanuts']]
]

'''
Scope of an operator is defined by list followed and succeeded by it,
such as for not operator '~',[] and for and operator [], '^', [].

Each statement in CNF is member of CNF list.

All caps words are predicates such as 'LIKES', 'EATS'.

All small words are variables such as 'x' and 'y'.

All words with first letter capital are constants such as 'Ajay' and 'Peanuts'.

Last two elements of CNF are conclusion and negated conclusion (CNF[-1] and CNF[-2])
'''

EXAMPLE1 = [['@', 'x', [['HOUND', 'x'], '->', ['HOWL', 'x']]],
            ['@', 'x', ['@', 'y', [[['HAVE', 'x', 'y'], '^', ['CAT', 'y']], '->',
                                   ['~', ['$', 'z', [['HAVE', 'x', 'z'], '^', ['MOUSE', 'z']]]]]]],
            ['@', 'x', [['LS', 'x'], '->',
                        ['~', ['$', 'y', [['HAVE', 'x', 'y'], '^', ['HOWL', 'y']]]]]],
            ['$', 'x', [['HAVE', 'John', 'x'], '^', [
                ['CAT', 'x'], 'v', ['HOUND', 'x']]]],
            [['LS', 'John'], '->',
                ['~', ['$', 'z', [['HAVE', 'John', 'z'], '^', ['MOUSE', 'z']]]]]
            ]

EXAMPLE2 = [
    ['MAN', 'Marcus'],
    ['ROMAN', 'Marcus'],
    ['@', 'x', [['MAN', 'x'], '->', ['PERSON', 'x']]],
    ['RULER', 'Caeser'],
    ['@', 'x', [['ROMAN', 'x'], '->',
                [['LOYAL', 'x', 'Caeser'], 'v', ['HATE', 'x', 'Caeser']]]],
    ['@', 'x', ['$', 'y', ['LOYAL', 'x', 'y']]],
    ['@', 'x', ['@', 'y', [[['PERSON', 'x'], '^', ['RULER', 'y'], '^',
                            ['TRYASSASIN', 'x', 'y']], '->', ['~', ['LOYAL', 'x', 'y']]]]],
    ['TRYASSASIN', 'Marcus', 'Caeser']
]


def checkForInsideLists(lst):
    '''
    helper function
    returns number of sub-lists present in lst
    '''
    if type(lst) != list:
        return 0
    count = 0
    for i in lst:
        if type(i) == list:
            count += 1
    return count

def checkForInsideOperators(lst):
    '''
    helper function
    returns number of operators present in lst
    '''
    count = 0
    for i in lst:
        if i in operators:
            count += 1
    return count


'''
#########################################
All the five following functions modify their inputs, so whenever copying
something, use deepcopy from copy module so that the object being copied is not also modified.
#########################################
'''


def bi_implication(statement):
    '''
    @param: statement is a list
    Function for resolving all bi_implications
    '''
    if type(statement) != list:
        # base case
        return statement

    if checkForInsideLists(statement) < 1:
        # base case
        return statement

    if checkForInsideLists(statement) == 2 and len(statement) == 3 and statement[1] == '<->':
        # the case for [[],'<->,[]]
        B = bi_implication(statement.pop())     # calling recursively
        operator = statement.pop()
        # calling recursively
        A = bi_implication(statement.pop())
        statement.append([A, '->', B])
        statement.append('^')
        statement.append([B, '->', A])
        return statement
    else:
        for i in statement:
            bi_implication(i)

    return statement


def implication(statement):
    '''
    @param: statement is a list
    Function for resolving all bi_implications
    '''
    if type(statement) != list:
        return statement

    if checkForInsideLists(statement) < 1:
        return statement

    if checkForInsideLists(statement) == 2 and len(statement) == 3 and statement[1] == '->':
        B = implication(statement.pop())
        operator = statement.pop()
        A = implication(statement.pop())
        statement.append(['~', A])
        statement.append('v')
        statement.append(B)
        return statement
    else:
        for i in statement:
            implication(i)

    return statement


def negate(statement):
    '''
    @param: statement is a list
    This function performs negation of a statement, not to be confused
    with a function for moving negation inside.
    Always apply this after bi_implication and implication functions.
    '''
    if type(statement) == list and len(statement) == 2 and checkForInsideLists(statement) == 1 and statement[0] == '~':
        # case for ['~',[A]] return [A]
        return statement[1]

    if type(statement) != list:
        # that is it is a single element
        if statement not in operators:
            # that is it is a constant or predicate
            return statement
        else:
            # that is it is operator
            return negatedOperators[statement]
    
    if type(statement) == list and checkForInsideOperators(statement) < 1:
        # case when inside list is a predicate and its arguments
        return ['~',statement]    
    else:
        for i in range(len(statement)):
            statement[i] = negate(statement[i])        

    return statement

def moveInNegation(statement):
    '''
    @param: statement is a list
    This function moves in the negation till possible.
    Always apply this after bi_implication and implication functions.
    '''
    if type(statement) != list:
        # base case

        # if statement in operators:
        #     return negatedOperators[statement]
        # else:
        #     return statement
        return statement

    if len(statement) == 2 and checkForInsideLists(statement) == 1 and statement[0] == '~' and checkForInsideLists(statement[1]) == 0:
        # also a base case for ['~',['PREDICATE','Arguments']]
        return statement
    elif len(statement) == 2 and checkForInsideLists(statement) == 1 and statement[0] == '~':
        # case for ['~',[]] generic, so we just drop the operator and negate the following list
        return negate(statement[1])
    else:
        for i in range(len(statement)):
            statement[i] = moveInNegation(statement[i])     # calling recursively till we get to the base cases

    return statement


def resolveTillNegation(FOL):
    '''
    @param: a list of list containing statements in FOL form.
    This function resolves bi-implication, implication and negation.
    The last two elements of the modified FOL are conclusion and
    negated conclusion, respectively.
    '''
    for i in FOL:
        bi_implication(i)
        implication(i)
        moveInNegation(i)
    
    conclusion = copy.deepcopy(FOL[-1])             # beware, most of the functions modify their arguments
    FOL.append(moveInNegation(negate(conclusion)))
    
    return FOL

skolemConstantsFunctionsLetters = []

def generateSkolemConstantFunctionLetter(pred):
    global skolemConstantsFunctionsLetters
    asciiValue = random.randint(65,90)
    doubleLetter = chr(asciiValue) + chr(asciiValue)
    letter = chr(asciiValue)
    while (letter in skolemConstantsFunctionsLetters or doubleLetter in skolemConstantsFunctionsLetters):
        asciiValue = random.randint(65,90)
        doubleLetter = chr(asciiValue) + chr(asciiValue)
        letter = chr(asciiValue)
    if len(pred) > 0:
        skolemConstantsFunctionsLetters.append(doubleLetter)
        return doubleLetter
    else:
        skolemConstantsFunctionsLetters.append(letter)
        return letter


def skolemizeVar(var, lst, pred,letter):
    '''
    @param: var-> variable to be skolemized, lst->['$',var,lst]
    and pred contains all previous for all variables.
    This function is sub-function for skolemization aka helper
    '''
    for i in range(len(lst)):
        if type(lst[i]) == list:
            skolemizeVar(var, lst[i], pred,letter)
        if lst[i] == var:
            lst[i] = [letter] + pred
    return lst

def skolemize(statement, pred):
    '''
    @param: statement and pred are lists, pred must passed as [] (empty list)
    This function skolemizes the given statement
    '''
    if type(statement) != list:
        # base case
        return statement

    if type(statement) == list and statement[0] == '@':
        pred.append(statement[1])
        skolemize(statement[2],pred)
    
    if type(statement) == list and statement[0] == '$':
        skolemizeVar(statement[1], statement[2], pred,generateSkolemConstantFunctionLetter(pred))
        return skolemize(statement[2], pred)
    else:
        for i in range(len(statement)):
            statement[i] = skolemize(statement[i],pred)

    return statement

def main():
    '''
    Funtion for performing all tests
    '''
    # print(checkForInsideLists(
    #     [[], 'a', None, 'ABC', 12.4, [], [None, 3, 3.4]]))

    # test1_bi_implication = [['a'], '<->', ['b']]
    # print(test1_bi_implication)
    # print(bi_implication(test1_bi_implication))
    # print(implication(test1_bi_implication))

    # test2_bi_implication = [[['a'],'<->',['b']],'<->',['c']]
    # print(test2_bi_implication)
    # print(bi_implication(test2_bi_implication))

    # test3_bi_implication = ['~',[['b'],'<->',['c']]]
    # print(test3_bi_implication)
    # print(bi_implication(test3_bi_implication))

    # test1_implication = [['MAN','Marcus'],'->',['MORTAL','Marcus']]
    # print(test1_implication)
    # print(implication(test1_implication))

    # test2_implication = ['@','x',[['ROMAN','x'],'->',[['LOYAL','x','Caeser'],'v',['HATE','x','Caeser']]]]
    # print(test2_implication)
    # print(implication(test2_implication))

    # test3_implication = [[['a'],'->',['b']],'->',['c']]
    # print(test3_implication)
    # print(implication(test3_implication))

    # test1_negation = [['~',[['~',['A']],'v',['B']]],'v',['C']]
    # print(test1_negation)
    # print(negate(test1_negation))

    # test2_negation = ['TRYASSASIN', 'Marcus', 'Caeser']
    # print(test2_negation)
    # print(negate(test2_negation))

    # conclusion = [['LS', 'John'], '->',
    #             ['~', ['$', 'z', [['HAVE', 'John', 'z'], '^', ['MOUSE', 'z']]]]]

    # print(bi_implication(conclusion))
    # print(implication(conclusion))
    # print("---------------------------------")
    # print(negate(conclusion))

    # print("---------------------------------")
    # print(moveInNegation(conclusion))

    # print("---------------------------------")

    # test1_moveInNegation = ['~',[['A'],'v',[['B'],'^',['C']],'v',['~',[['D'],'^',['E']]]]]
    # print(test1_moveInNegation)
    # print(moveInNegation(test1_moveInNegation))

    # test2_moveInNegation = [['A'],'v',[['B'],'^',['C']],'v',['~',[['D'],'^',['E']]]]
    # print(test2_moveInNegation)
    # print(moveInNegation(test2_moveInNegation))

    # print('###############################')
    # [print(i) for i in EXAMPLE1]
    # print('------------------------------')
    # [print(i) for i in resolveTillNegation(EXAMPLE1)]
    
    # print('###############################')
    # [print(i) for i in EXAMPLE2]
    # print('------------------------------')
    # print(resolveTillNegation(EXAMPLE2))
    # global skolemConstantsFunctionsLetters
    # skolemConstantsFunctionsLetters += ['A', 'AA']
    # print(generateSkolemConstantFunctionLetter(['x','y']))
    # print(generateSkolemConstantFunctionLetter(['x','y']))
    # print(generateSkolemConstantFunctionLetter(['x','y']))
    # print(generateSkolemConstantFunctionLetter(['x','y']))
    # print(generateSkolemConstantFunctionLetter(['x','y']))

    test1_skolemize = ['$', 'y', ['@', 'x', ['LOYAL', 'x', 'y']]]
    print(test1_skolemize)
    print(skolemize(test1_skolemize,[]))

    print('------------------------------')

    test2_skolemize = ['@', 'x', ['@', 'y', [[['PERSON', 'x'], '^', ['RULER', 'y'], '^',['TRYASSASIN', 'x', 'y']], '->', ['~', ['LOYAL', 'x', 'y']]]]]
    print(test2_skolemize)
    print(skolemize(test2_skolemize,[]))

    print('------------------------------')

    test3_skolemize = ['$', 'x', [['HAVE', 'John', 'x'], '^', [['CAT', 'x'], 'v', ['HOUND', 'x']]]]
    print(test3_skolemize)
    print(skolemize(test3_skolemize,[]))

    print('------------------------------')

    test4_skolemize = [['LS', 'John'], '->',
                ['~', ['$', 'z', [['HAVE', 'John', 'z'], '^', ['MOUSE', 'z']]]]]
    # implication(test4_skolemize)
    # moveInNegation(test4_skolemize)
    print(test4_skolemize)
    print(skolemize(test4_skolemize,[]))
    
    return None


if __name__ == "__main__":
    main()      # if this file is run, then main() function is called

