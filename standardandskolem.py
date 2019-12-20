operators = ['~', 'v', '^', '@', '$', '->', '<->']

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
    ['~', ['LIKES', 'Ravi', 'Peanuts']],
    (6,1)
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
EXAMPLE1 = [
['@', 'x', [['~', ['HOUND', 'x']], 'v', ['HOWL', 'x']]],
['@', 'x', ['@', 'y', [[['~', ['HAVE', 'x', 'y']], 'v', ['~', ['CAT', 'y']]], 'v', ['@', 'z', [['~', ['HAVE', 'x', 'z']], 'v', ['~', ['MOUSE', 'z']]]]]]],
['@', 'x', [['~', ['LS', 'x']], 'v', ['@', 'y', [['~', ['HAVE', 'x', 'y']], 'v', ['~', ['HOWL', 'y']]]]]],
['$', 'x', [['HAVE', 'John', 'x'], '^', [['CAT', 'x'], 'v', ['HOUND', 'x']]]],
[['~', ['LS', 'John']], 'v', ['@', 'z', [['~', ['HAVE', 'John', 'z']], 'v', ['~', ['MOUSE', 'z']]]]]]

EXAMPLE2 = [
['MAN', 'Marcus'],
['ROMAN', 'Marcus'],
['@', 'x', [['~', ['MAN', 'x']], 'v', ['PERSON', 'x']]],
['RULER', 'Caeser'],
['@', 'x', [['~', ['ROMAN', 'x']], 'v', [['LOYAL', 'x', 'Caeser'], 'v', ['HATE', 'x', 'Caeser']]]],
['@', 'x', ['$', 'y', ['LOYAL', 'x', 'y']]],
['@', 'x', ['@', 'y', [[['~', ['PERSON', 'x']], 'v', ['~', ['RULER', 'y']], 'v', ['~', ['TRYASSASIN', 'x', 'y']]], 'v', ['~', ['LOYAL', 'x', 'y']]]]],
['TRYASSASIN', 'Marcus', 'Caeser']]

def StateSkolemExist(statement, stack, EQnumberlist, skolemseen, skolemfuncs):  #GETTING THERE :'(
	variables = ['x', 'y', 'z', 'p', 'q', 'r', 's', 't', 'u', 'w', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'a', 'b', 'c', 'd', 'e', 'f', 'g']  # except o p and v
	#skolemseen = {}
	#skolemfuncs = ['XX', 'YY', 'ZZ', 'PP', 'QQ', 'RR', 'SS', 'TT', 'UU', 'WW', 'HH', 'II', 'JJ', 'KK', 'LL', 'MM', 'NN', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG']
	stackswitch = False
	# EQnumberlist
	# stack = []
	EQnumber = 0
	statementlen = len(statement)
	while elementn != statementlen:
		element = statement[elementn]
		if type(element) == type(listtype):
			stackswitch = False
			if EQnumber > 0:
				EQnumberlist.append(EQnumber)
			statement[elementn] = StateSkolemExist(element, stack, EQnumberlist, skolemseen, skolemfuncs)
		
		elif element == '$':
			stackswitch = True
			statement.pop(elementn)
			statementlen = statementlen - 1

		elif element in variables and stackswitch:
			stack.append(element)
			EQnumber = EQnumber + 1

			statement.pop(elementn)
			statementlen = statementlen - 1

		elif element in variables and not stackswitch:
			EQtn = EQnumberlist.top()
			for i in range(1,EQtn + 1):
				if stack[0 - EQtn] == element: 
					if element not in variableseen:
						swapvar = [skolemfuncs.pop(0)]
						statement[elementn] = swapvar
						variableseen[element] = swapvar
					else:
						statement[elementn] = variableseen[element]

		elementn = elementn + 1

	EQtn = EQnumberlist.pop()
	for i in range(EQtn):
		stack.pop()

	return statement


def MakeClauses(lst):  #DIVIDES INTO CLAUSES AT '^'
	# premisen = 0
	# conclusionn = 0
	lstlen = len(lst)
	statementn = 0

	#For premises
	while statementn != lstlen - 1:
		inlstlen = len(lst[statementn])
		elementn = 0
		while elementn != inlstlen:
			if lst[statementn][elementn] == '^':
				newlst = lst.pop(statementn)
				a = newlst[0:elementn]
				if len(a) > 1:
					lst.insert(statementn, a)
				else:
					lst.insert(statementn, a[0])

				b = newlst[elementn + 1:inlstlen]
				if len(b) > 1:
					lst.insert(statementn + 1, b)
				else:
					lst.insert(statementn + 1, b[0])  
				lstlen = lstlen + 1
			elementn = elementn + 1
		statementn = statementn + 1

	# premisen = len(lst[0:statementn])
	constart = statementn

	#For Conclusion
	while statementn != lstlen:
		inlstlen = len(lst[statementn])
		elementn = 0
		while elementn != inlstlen - 1:
			if lst[statementn][elementn] == '^':
				newlst = lst.pop(statementn)
				a = newlst[0:elementn]
				if len(a) > 1:
					lst.insert(statementn, a)
				else:
					lst.insert(statementn, a[0])

				b = newlst[elementn + 1:inlstlen]
				if len(b) > 1:
					lst.insert(statementn + 1, b)
				else:
					lst.insert(statementn + 1, b[0])  
				lstlen = lstlen + 1
			elementn = elementn + 1
		statementn = statementn + 1

	# conclusionn = len(lst[constart:statementn])

	# lst.append((premisen, conclusionn))
	print(lst)


def StateStandard(statement, variableseen, variables):  #HELPER FUNCTION
	listtype = []
	chartype = 'c'
	statementlen = len(statement)
	for elementn in range(statementlen):
		element = statement[elementn]
		if type(element) == type(listtype):
			statement[elementn] = StateStandard(element, variableseen, variables)
		elif type(element) == type(chartype) and len(element) == 1 and element not in "@$~v^":
			if element not in variableseen:
				swapvar = variables.pop(0)
				statement[elementn] = swapvar
				variableseen[element] = swapvar
			else:
				statement[elementn] = variableseen[element]
	return statement

def Standard(lst):  #FUNCTION FOR STANDARDIZATION
	variables = ['x', 'y', 'z', 'p', 'q', 'r', 's', 't', 'u', 'w', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'a', 'b', 'c', 'd', 'e', 'f', 'g']   # except o p and v
	lstlen = len(lst)
	for statementn in range(lstlen):
		variableseen = {}
		newstate = StateStandard(lst[statementn], variableseen, variables)
		lst[statementn] = newstate
		print(newstate)
	print(lst)

Standard(EXAMPLE1)
