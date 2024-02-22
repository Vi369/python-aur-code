#Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = 100

if distance < 3:
    transport = "walk"
elif distance < 15:
    transport = "Bike"
elif distance >15:
    transport = "Car"

print ("Aisa hai to aap isaka use kariye:",transport)