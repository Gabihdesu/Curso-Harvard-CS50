import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action 

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):  # adiciona um novo estado à fronteira
        self.frontier.append(node)

    def contains_state(self, state):  # verifica se estado já está na fronteira
        return any(node.state == state for node in self.frontier)

    def empty(self):  # checa se a fronteira está vazia
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]  # remove o último item (estilo pilha)
            self.frontier = self.frontier[:-1]
            return node

#
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]  # remove o primeiro item (estilo fila)
            self.frontier = self.frontier[1:]
            return node

class Labirinto():
    def __init__(self, filename):
        # Lê o arquivo e define walls, start e goal
        with open(filename) as f:
            contents = f.read()

        # Verifica se há exatamente um S (start) e um E (end/goal)
        if contents.count("S") != 1:
            raise Exception("labirinto deve conter exatamente um ponto de início")
        if contents.count("E") != 1:
            raise Exception("labirinto deve conter exatamente um ponto de chegada")

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    char = contents[i][j]
                except IndexError:
                    char = " "
                if char == "S":
                    self.start = (i, j)
                    row.append(False)
                elif char == "E":
                    self.goal = (i, j)
                    row.append(False)
                elif char == " ":
                    row.append(False)
                else:
                    row.append(True)
            self.walls.append(row)

        self.solution = None

    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.walls[i][j]:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("S", end="")
                elif (i, j) == self.goal:
                    print("E", end="")
                elif self.solution is not None and (i, j) in self.solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self):
        # Inicializa a fronteira com o estado inicial
        start = Node(state=self.start, parent=None, action=None)
        #frontier = StackFrontier()  # ou QueueFrontier() para BFS
        frontier = QueueFrontier()
        frontier.add(start)

        self.explored = set()

        while True:
            if frontier.empty():
                raise Exception("sem solução")

            node = frontier.remove()
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = cells
                return

            self.explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

# Exemplo de uso:
if __name__ == "__main__":
    n = 2
    filename = f"C:/Users/GSANTIA6/OneDrive - Gerdau/Gabriela/curso Harvard/maze{n}.txt"
    m = Labirinto(filename)
    print("Labirinto:")
    m.print()
    m.solve()
    print("\nSolução:")
    m.print()
