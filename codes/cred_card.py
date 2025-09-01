# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
for i in range(N):
    credit_number_s = str(input())
    invalid = False
    
for i in range(N):
    lista = []
    pattern = r'^\d(-\d)*$'
    
    if credit_number_s[0] not in(['4', '5', '6']):
        invalid = True
    if len(credit_number_s) != 16: 
        invalid = True
        
    
    if re.match(pattern, credit_number_s):
        invalid = True
  
    groups = credit_number_s.strip().split()
    for group in groups:
        if len(group) >= 4 and any(group[i] == group[i+1] == group[i+2] == group[i+3] for i in range(len(group)-3)):
            invalid = True
    
    if invalid == True:
        print("Invalid")
    else:
        print("Valid")
