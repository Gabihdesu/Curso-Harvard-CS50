from pomegranate import *

from pomegranate import HiddenMarkovModel
from pomegranate.distributions import DiscreteDistribution

# Define the emission probabilities
sun = DiscreteDistribution({
    "umbrella": 0.2,
    "no umbrella": 0.8
})

rain = DiscreteDistribution({
    "umbrella": 0.9,
    "no umbrella": 0.1
})


# Build the HMM
model = HiddenMarkovModel(name="Weather HMM")

# Add states to the model
model.add_states(("sun", sun), ("rain", rain))

# Define transitions
model.add_transition(model.start, "sun", 0.5)
model.add_transition(model.start, "rain", 0.5)

model.add_transition("sun", "sun", 0.8)
model.add_transition("sun", "rain", 0.2)
model.add_transition("rain", "rain", 0.7)
model.add_transition("rain", "sun", 0.3)

# Finalize the model
model.bake()

# Observed data
observations = [
    "umbrella",
    "umbrella",
    "no umbrella",
    "umbrella",
    "umbrella",
    "umbrella",
    "umbrella",
    "no umbrella",
    "no umbrella"
]

# Predict the hidden states
predictions = model.predict(observations)

# Print the predicted states
for prediction in predictions[1:]:  # Skip the initial state
    print(model.states[prediction].name)
