import math

def calculate_volume_of_sphere(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume

radii = [30, 40]
print("Radius\tVolume")
for r in radii:
    volume = calculate_volume_of_sphere(r)
    print(f"{r}\t{volume:.2f}")