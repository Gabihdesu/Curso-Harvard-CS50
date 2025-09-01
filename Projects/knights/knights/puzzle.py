from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
     Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # A diz: "Sou cavaleiro e patife"
    Implication(AKnight, And(AKnight, AKnave))  # Se A é cavaleiro, ele diz a verdade

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
     Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, And(BKnave, AKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # A diz: "Somos do mesmo tipo" => (AKnight <-> BKnight)
    Implication(AKnight, Biconditional(AKnight, BKnight)),
    Implication(AKnave, Not(Biconditional(AKnave, BKnave))),

    # B diz: "Somos de tipos diferentes" => (AKnight != BKnight)
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),
    Implication(BKnave, Biconditional(AKnight, BKnight))
)
# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
A_disse_knight = Symbol("A disse que é um Cavaleiro")
Adisse_knave = Symbol("A disse que é um patife")

knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # A diz que é um cavaleiro ou um patife, mas não sabemos qual
    Or(A_disse_knight, Adisse_knave),
    Not(And(A_disse_knight, Adisse_knave)),

    # Se A disse que é um cavaleiro
    Implication(A_disse_knight, Biconditional(AKnight, AKnight)),
    # Se A disse que é um patife
    Implication(Adisse_knave, Biconditional(AKnight, AKnave)),

    # B diz que A disse que é Patife
    Implication(BKnight, Adisse_knave),
    Implication(BKnave, Not(Adisse_knave)),

    # C diz que A é cavaleiro
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
