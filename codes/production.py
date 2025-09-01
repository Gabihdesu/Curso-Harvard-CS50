import scipy.optimize

# duas máquinas X1 e X2. A maquina X1 custa 50 e a máquina X2 custa 80
# X1 requer 5 unidades de trabalho
# X2 requer 2 unidades de trabalho
# preciso de no máximo 20 unidades de trabalho
# produzir no mínimo 90 

# Objetivo minimizar o custo total.


# Função objetivo: 50x_1 + 80x_2
# Restrição 1: 5x_1 + 2x_2 <= 20
# Restrição 2: -10x_1 + -12x_2 <= -90 ## produção mínima exigida


result = scipy.optimize.linprog(
    [50, 80], # função custo: 50x_1 + 80x_2
    A_ub=[[5,2], [-10, -12]], # coeficiente para desigualdades
    b_ub=[20, -90], # Restrição para desigualdades
)

if result.success:
    print(f"X1: {round(result.x[0], 2)} hours")
    print(f"X2: {round(result.x[1], 2)} hours")
else:
    print("No solution")
