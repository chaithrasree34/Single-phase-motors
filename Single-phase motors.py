# Single-phase-motors
print("Single-Phase Motor Calculator")

V = float(input("Enter voltage (V): "))
I = float(input("Enter current (A): "))
PF = float(input("Enter power factor: "))
efficiency = float(input("Enter efficiency (%): "))

# Calculate input power
Pin = V * I * PF

# Calculate output power
Pout = Pin * (efficiency / 100)

print("\n--- Motor Results ---")
print("Input Power =", Pin, "W")
print("Output Power =", Pout, "W")
print("Efficiency =", efficiency, "%")
