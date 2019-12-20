'''
main file for the project
'''

import copy

import CNF              # all examples are in this
import resolution
import standardandskolem

def main():
    test = copy.deepcopy(CNF.EXAMPLE2)
    CNF.resolveTillNegation(test)

    print(test)


    return None


if __name__ == "__main__":
    main()