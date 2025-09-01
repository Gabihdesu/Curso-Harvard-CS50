VARIABLES = ["A", "B", "C", "D", "E", "F", "G"]

RESTRICOES = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]

CORES = ["Mon", "Tue", "Wed"]

def consistente(variavel, cor, assignment):
    for (x, y) in RESTRICOES:
        if variavel == x:
            vizinho = y
        elif variavel == y:
            vizinho = x
        else:
            continue

        if vizinho in assignment and assignment[vizinho] == cor:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(VARIABLES):
        return assignment

    for var in VARIABLES:
        if var not in assignment:
            for cor in CORES:
                if consistente(var, cor, assignment):
                    assignment[var] = cor
                    resultado = backtrack(assignment)
                    if resultado:
                        return resultado
                    del assignment[var]
            return None
    return None

solucao = backtrack({})

if solucao:
    for var in VARIABLES:
        print(f"{var}: {solucao[var]}")
else:
    print("Nenhuma solução encontrada.")
