import numpy as np
import matplotlib.pyplot as plt

#The code will take some time to run


# Parameters
L = 1.0  # Length of the wall (m)
T_hot = 65  # Temperature of hot side (°C) - adjusted for realism
T_cold = 35  # Temperature of cold side (°C)
n = 100  # Number of spatial steps
dx = L / n  # Spatial step size


# Solar radiation parameters
solar_radiation = 100  # Solar radiation intensity (W/m^2)
solar_area = 0.5  # Area of the wall exposed to solar radiation (m^2)


# Time parameters
t_max = 3600  # Maximum simulation time (s)
dt = 0.1  # Time step size
nt = int(t_max / dt)  # Number of time steps

# Initialize temperature arrays
T_fiberglass = np.ones(n) * T_cold
T_foam = np.ones(n) * T_cold
T_foil = np.ones(n) * T_cold
T_cardboard = np.ones(n) * T_cold

# Apply boundary conditions
T_fiberglass[0] = T_hot
T_foam[0] = T_hot
T_foil[0] = T_hot
T_cardboard[0] = T_hot

# Perform simulation for fiberglass
k_fiberglass = 0.04
alpha_fiberglass = k_fiberglass / (1200 * 401) 
for t in range(nt):
    T_new = np.copy(T_fiberglass)
    for i in range(1, n - 1):
        T_new[i] = T_fiberglass[i] + alpha_fiberglass * dt / dx**2 * (T_fiberglass[i+1] - 2*T_fiberglass[i] + T_fiberglass[i-1])
    # Add solar radiation effect
    T_new += solar_radiation * solar_area * dt / (1200 * 896)  # Assuming average density and specific heat capacity
    T_fiberglass = np.copy(T_new)

# Perform simulation for foam
k_foam = 0.03
alpha_foam = k_foam / (1200 * 32)
for t in range(nt):
    T_new = np.copy(T_foam)
    for i in range(1, n - 1):
        T_new[i] = T_foam[i] + alpha_foam * dt / dx**2 * (T_foam[i+1] - 2*T_foam[i] + T_foam[i-1])
    # Add solar radiation effect
    T_new += solar_radiation * solar_area * dt / (1200 * 30)  # Assuming average density and specific heat capacity
    T_foam = np.copy(T_new)

# Perform simulation for foil
k_foil = 0.05
alpha_foil = k_foil / (1200 * 40)
for t in range(nt):
    T_new = np.copy(T_foil)
    for i in range(1, n - 1):
        T_new[i] = T_foil[i] + alpha_foil * dt / dx**2 * (T_foil[i+1] - 2*T_foil[i] + T_foil[i-1])
    # Add solar radiation effect
    T_new += solar_radiation * solar_area * dt / (1200 * 2700)  # Assuming average density and specific heat capacity
    T_foil = np.copy(T_new)

# Perform simulation for cardboard
k_cardboard = 0.034
alpha_cardboard = k_cardboard / (1200 * 50)
for t in range(nt):
    T_new = np.copy(T_cardboard)
    for i in range(1, n - 1):
        T_new[i] = T_cardboard[i] + alpha_cardboard * dt / dx**2 * (T_cardboard[i+1] - 2*T_cardboard[i] + T_cardboard[i-1])
    # Add solar radiation effect
    T_new += solar_radiation * solar_area * dt / (1200 * 750)  # Assuming average density and specific heat capacity
    T_cardboard = np.copy(T_new)

# Plot results
plt.plot(np.linspace(0, L, n), T_fiberglass, label='Fiberglass')
#plt.plot(np.linspace(0, L, n), T_foam, label='Foam')
plt.plot(np.linspace(0, L, n), T_foil, label='Reflective Foil')
plt.plot(np.linspace(0, L, n), T_cardboard, label='Foam')
plt.xlabel('Distance (10\u00b2 mm)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution Across Wall with Solar Radiation')
plt.legend()
plt.grid(True)
plt.show()












