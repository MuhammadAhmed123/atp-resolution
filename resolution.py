input_list = [['~', ['HOUND','x'], ['HOWL', 'x']],
          ['~', ['HAVE', 'y', 'z'], '~', ['CAT','z'],'~', ['HAVE', 'y', 'p'],'~', ['MOUSE', 'p']],
          ['~', ['LS', 'q'], '~', ['HAVE', 'q', 'r'], '~', ['HOWL', 'r']],
          [['HAVE', 'John', 'A']],
          [['CAT', 'B'], ['HOUND', 'B']],
          [['LS', 'John']],
          [['HAVE', 'John', 'C']],
          [['MOUSE', 'D']]
         ]

prem, conc = 5, 3

answer = []

#print(len(input_list))
#helper functions 
def is_not_function(term):
    if len(term) == 2 and (65 <= ord(term[0]) <= 90) and (65 <= ord(term[1]) <= 90):
            return False
    return True


def is_constant(term):
    #print("the term rn is: ", term)
    if len(term) > 1:
        if (65 <= ord(term[0]) <= 90) and (97 <= ord(term[1]) <= 122):
            return True
    if len(term) == 1:
        if (65 <= ord(term[0]) <= 90):
            return True
    return False


def is_variable(term):
    if len(term) == 1:
        if (97 <= ord(term[0]) <= 122):
            return True
    return False

def is_not_predicate(term):
    if len(term) > 2:
        if (65 <= ord(term[0]) <= 90) and (65 <= ord(term[1]) <= 90):
            return False
    return True


def apply_subs(subs, exp):
    #print(subs)
    for i in range(len(exp)):
        if type(exp[i]) is list:
            for j in range(len(exp[i])):
                if exp[i][j] == subs[1]:
                    exp[i][j] = subs[0]
                else:
                    if exp[i] == subs[1]:
                        exp[i] = subs[0]
    #return exp

def clean_set(ans):
    for a in ans:
        if is_variable(a[0]) and is_variable(a[1]):
            for b in ans:
                if b[1] == a[0] and is_constant(b[0]):
                    a[0] = b[0]
    

term1 = ['KNOWS', 'x', 'x']
term2 = ['KNOWS', 'A', 'y']

#f(g(X)) = f(Y)
#f(g(X),X) = f(Y,a)
#
#{p(b, X, f(g(Z))) and p(Z, f(Y), f(Y))}
#{p (X, X), and p (Z, f(Z))
#(a, g(x, a), f(y)), Q(a, g(f(b), a), x)

def unify(t1, t2, answer):
    if (type(t1) is not list) or (type(t2) is not list):
        #print("Not a function.")
        if t1 == t2:
            return []
        if is_variable(t1):
            return [t2, t1]
        if is_variable(t2):
            return [t1, t2]
        else:
            return False
    if t1[0] != t2[0]:
        #print("Predicate not same.")
        return False
    if len(t1) != len(t2):
        #print("Paramaters different.")
        return False
    #subs = []
    for i in range(1, len(t1)):
        result = unify(t1[i], t2[i], answer)
        if result == False:
            #print("Nothing to see here lol.")
            return False
        if result != []:
            apply_subs(result, t1[i:])
            apply_subs(result, t2[i:])
            for a in answer:
                apply_subs(result, answer)
            answer.append(result)

            
    clean_set(answer)
    for a in answer:
        if a[0] in a[1]:
            return False
        if len(a[0]) == 1 and len(a[1]) == 1 and (65 <= ord(a[0]) <= 90) and (65 <= ord(a[1]) <= 90):
            return False
    return answer

#print(unify(term1, term2, answer))
#print(len(answer))


resolution = []

index = prem
#print(index)

current = input_list[prem+conc-1]
answer = []
for j in range(len(input_list)):
    for i in range(len(input_list[j])):
        if input_list[j][i][0] == current[0][0] and input_list[j][i-1] == '~':
            poss = unify(current[0], input_list[j][i], answer)
            if poss != False:
                print("It can work.")
                print(poss)
                break
        
def resolute(lst):
    answer = []
    steps = []
    premises = lst[:-1]
    current = lst[-1]
    verdict = 0

    while (verdict == 0):
        while(len(current) > 0 and premises):
            for p in range(len(premises)):
                for t in range(len(premises[p])):
                    if premises[p][t] == current[c]:
                        result = unify(premises[p][t], current[c], answer)
                        if result != False:
                            was_cur = current[c]
                            #current.remove(t)
                            current.remove(current[c])
                            was_per = premises[p]
                            premises[p].remove(premises[p][t])
                            premises[p].remove(premises[p][t-1])
                            new = current + premises[p]
                            apply_subs(result, new)
                            current = new
                            premises

                            
                            
                            
                
