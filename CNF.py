
CNF = 
	[
    [['~', ['FOOD', 'x'], 'v', ['LIKES', 'Ravi', 'x']]],
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