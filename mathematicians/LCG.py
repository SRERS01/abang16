# Verification of Lattice space mapping for the 3 observed slices
import numpy as np

m = 2147483647
a = 16807
c = 0

# Observed outputs
Y = [4, 7, 1]

# Reconstructing the hidden short vectors using a basic search space 
# to mimic the LLL lattice reduction output for this specific sequence:
for potential_X1 in range(4, m, 10):
    X1 = potential_X1
    X2 = (a * X1 + c) % m
    X3 = (a * X2 + c) % m
    if X2 % 10 == Y[1] and X3 % 10 == Y[2]:
        print(f"✅ State Found! Raw X1: {X1}, Raw X2: {X2}, Raw X3: {X3}")
        # Predict Spin 4
        X4 = (a * X3 + c) % m
        predicted_slice = X4 % 10
        print(f"🔮 Next Predicted Slice: {predicted_slice}")
        break
