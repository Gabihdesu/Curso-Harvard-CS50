import random

class Space:

    def __init__(self, height, width, num_hospitals):
        """Cria um novo espaço com as dimensões fornecidas."""
        self.height = height
        self.width = width
        self.num_hospitals = num_hospitals
        self.houses = set()
        self.hospitals = set()

    def add_house(self, row, col):
        """Adiciona uma casa em um local específico no espaço."""
        self.houses.add((row, col))

    def available_spaces(self):
        """Retorna todas as células não ocupadas por casas ou hospitais."""
        candidates = set(
            (row, col)
            for row in range(self.height)
            for col in range(self.width)
        )

        candidates -= self.houses
        candidates -= self.hospitals

        return candidates

    def get_neighbors(self, row, col):
        """Retorna os vizinhos válidos (em cima, baixo, esquerda, direita)."""
        neighbors = []

        if row > 0:
            neighbors.append((row - 1, col))
        if row < self.height - 1:
            neighbors.append((row + 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if col < self.width - 1:
            neighbors.append((row, col + 1))

        # Remove vizinhos que já têm casa ou hospital
        return [n for n in neighbors if n not in self.houses and n not in self.hospitals]

    def get_cost(self, hospitals):
        """Calcula o custo como a soma das distâncias de cada casa ao hospital mais próximo."""
        total = 0
        for house in self.houses:
            distances = [abs(house[0] - hospital[0]) + abs(house[1] - hospital[1]) for hospital in hospitals]
            total += min(distances)
        return total

    def output_image(self, filename):
        """Placeholder: função para gerar imagens do estado atual (não implementada aqui)."""
        pass  # Aqui você poderia usar PIL, matplotlib, etc.

    def hill_climb(self, maximum=None, image_prefix=None, log=False):
        """Aplica o algoritmo Hill Climbing para encontrar uma solução."""
        count = 0

        # Inicializa hospitais em locais aleatórios disponíveis
        self.hospitals = set()
        for _ in range(self.num_hospitals):
            self.hospitals.add(random.choice(list(self.available_spaces())))

        if log:
            print("Initial state: cost", self.get_cost(self.hospitals))
        if image_prefix:
            self.output_image(f"{image_prefix}{str(count).zfill(3)}.png")

        while maximum is None or count < maximum:
            count += 1
            best_neighbors = []
            best_neighbors_cost = None

            for hospital in self.hospitals:
                for replacement in self.get_neighbors(*hospital):
                    neighbor = self.hospitals.copy()
                    neighbor.remove(hospital)
                    neighbor.add(replacement)

                    cost = self.get_cost(neighbor)
                    if best_neighbors_cost is None or cost < best_neighbors_cost:
                        best_neighbors_cost = cost
                        best_neighbors = [neighbor]
                    elif cost == best_neighbors_cost:
                        best_neighbors.append(neighbor)

            if best_neighbors_cost >= self.get_cost(self.hospitals):
                return self.hospitals
            else:
                if log:
                    print(f"Found better neighbor: cost {best_neighbors_cost}")
                self.hospitals = random.choice(best_neighbors)

            if image_prefix:
                self.output_image(f"{image_prefix}{str(count).zfill(3)}.png")

    def random_restart(self, maximum, image_prefix=None, log=False):
        """Executa Hill Climbing várias vezes com reinícios aleatórios."""
        best_hospitals = None
        best_cost = None

        for i in range(maximum):
            if log:
                print(f"\nRestart {i + 1}/{maximum}")
            prefix = f"{image_prefix}_restart{i}_" if image_prefix else None

            self.hill_climb(image_prefix=prefix, log=log)
            current_cost = self.get_cost(self.hospitals)

            if best_cost is None or current_cost < best_cost:
                best_cost = current_cost
                best_hospitals = self.hospitals.copy()

        self.hospitals = best_hospitals
        return self.hospitals

# ===== Teste do código corrigido =====

s = Space(height=10, width=20, num_hospitals=3)

# Adiciona 15 casas em posições aleatórias
for _ in range(15):
    s.add_house(random.randrange(s.height), random.randrange(s.width))

# Executa Hill Climbing
hospitals = s.hill_climb(image_prefix="hospitals", log=True)
print("Hospitals found:", hospitals)
