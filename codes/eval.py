# Enter your code here. Read input from STDIN. Print output to STDOUT

expressao = str(input())
if len(expressao) > 100:
    expressao = str(input())
else:
    eval(expressao)

#print(result)