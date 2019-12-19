import copy

operators = ['~', 'v', '^', '@', '$', '->', '<->']

negatedOperators = {'v':'^', '^':'v', '@':'$', '$':'@'}

'''
@: for all, $: there is, ->: implication, <->: bi-implication
'''

CNF = [
    [[['~', ['FOOD', 'x']], 'v', ['LIKES', 'Ravi', 'x']]],
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
    # returns number of sub-lists present in lst
    count = 0
    for i in lst:
        if type(i) == list:
            count += 1
    return count

def checkForInsideOperators(lst):
    # returns number of operators present in lst
    count = 0
    for i in lst:
        if i in operators:
            count += 1
    return count


def bi_implication(statement):
    '''
    @param: statement is a list
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
    with a function for moving negation inside
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

def moveNegation(statement):

    return statement


def main():
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

    conclusion = [['LS', 'John'], '->',
                ['~', ['$', 'z', [['HAVE', 'John', 'z'], '^', ['MOUSE', 'z']]]]]

    print(bi_implication(conclusion))
    print(implication(conclusion))
    print(negate(conclusion))

    return None


if __name__ == "__main__":
    main()
