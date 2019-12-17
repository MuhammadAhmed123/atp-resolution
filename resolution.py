
class Operator:
	"""
	Represents operators used in resolution
	"""

    operators = ['~', 'v', '^', 'A', 'E', '->', '<->']

    '''
    A: for all, E: there is, ->: implication, <->: bi-implication
    '''

    def __init__(self, operatorString):
        if operatorString not in Operator.operators:
            print("Error: %s no such operator defined", operatorString)
            self.operator = None
        else:
            self.operator = operatorString

# declaration of variable
forall = Operator('A')
thereis = Operator('E')
implication = Operator('->')
negation = Operator('~')

def eliminateUniversalQuant(FOLStatement):
	'''
	FOL statemet should have all Universal Quantifiers
	in outermost scope
	FOLStatement format: ['A', ['A', []]]
	'''
	lst = FOLStatement
	while len(lst) == 2 and lst[0] == forall.operator:
		lst = lst[1]
    return lst


def eliminateExistentialQuant(FOLStatement):
	'''
	requires skolemization
	'''
	return FOLStatement

def Skolemize(FOLStatement):
	'''
	not implemented
	'''
	return FOLStatement

def eliminateBiimplication(FOLStatment):

	return FOLStatment

def eliminateImplication(FOLStatement):
    # given a FOL statement, it eliminates implication
    # and modifies FOL statement
	# assumed input format [[], '->', []]
	lst = []
	if FOLStatement[1] != implication.operator or len(FOLStatement) < 2:
		return none
	a = FOLStatement[0]
	b = FOLStatement[-1]
	lst.append(['~', a])
	lst.append('v')
	lst.append([b])
    return lst


def negate(FOLStatement):
	'''
	FOL statement negated, i.e. negation operator moved inwards
	'''
	return FOLStatement
