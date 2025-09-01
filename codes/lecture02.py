from pomegranate.distributions import *
from pomegranate import DiscreteDistribution, BayesianNetwork, ConditionalProbabilityTable, Node
from pomegranate import *


# ------------------------------------------------------
# Inferência em redes bayesianas:
# - X: variável de interesse (query)
# - E: variáveis de evidência (observadas)
# - Y: variáveis ocultas (não observadas, não são X nem E)
# Objetivo: Calcular P(X | E)
# ------------------------------------------------------

# Nó "rain" (chuva), sem pais
rain = Node(DiscreteDistribution({
    "none": 0.7,
    "light": 0.2,
    "heavy": 0.1
}), name='rain')

# Nó "maintenance" (manutenção), condicional à chuva
maintenance = Node(ConditionalProbabilityTable([
    ["none", "yes", 0.4],
    ["none", "no", 0.6],
    ["light", "yes", 0.2],
    ["light", "no", 0.8],
    ["heavy", "yes", 0.1],
    ["heavy", "no", 0.9]
], [rain.distribution]), name="maintenance")

# Nó "train" (trem), condicional à chuva e manutenção
train = Node(ConditionalProbabilityTable([
    ["none", "yes", "on time", 0.8],
    ["none", "yes", "delayed", 0.2],
    ["none", "no", "on time", 0.9],
    ["none", "no", "delayed", 0.1],
    ["light", "yes", "on time", 0.6],
    ["light", "yes", "delayed", 0.4],
    ["light", "no", "on time", 0.7],
    ["light", "no", "delayed", 0.3],
    ["heavy", "yes", "on time", 0.4],
    ["heavy", "yes", "delayed", 0.6],
    ["heavy", "no", "on time", 0.5],
    ["heavy", "no", "delayed", 0.5]
], [rain.distribution, maintenance.distribution]), name='train')

# Nó "appointment" (compromisso), condicional ao estado do trem
appointment = Node(ConditionalProbabilityTable([
    ["on time", "attend", 0.9],
    ["on time", "miss", 0.1],
    ["delayed", "attend", 0.6],
    ["delayed", "miss", 0.4]
], [train.distribution]), name='appointment')

# Create a Bayesian Network and ad states
# criar a rede

model = BayesianNetwork()
model.add_states(rain, maintenance, train, appointment)

# Add edges connecting nodes
model.add_edge(rain, maintenance)
model.add_edge(rain, train)
model.add_edge(maintenance, train)
model.add_edge(train, appointment)

# Finalize model
model.bake()

#calculate probability for a given observation
probability = model.probability(["none", "no", "on time", "attend"])

# mostrar distribuições marginais para os nós restantes
beliefs = model.predict_proba({'rain': 'none', 'maintenance': 'no'})
print(beliefs)  

print(probability)