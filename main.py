'''
usage examples of SFCLibrary
'''

#a static example

from SFCLibrary import calc

operations = "098.78848+056.8900/0.75"

result = calc(operations)

print(result)

#a dinamic example

from SFCLibrary import calculator

calculator() #(please write an input in the console)