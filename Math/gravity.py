# WAP to  find gravitational force between two objects 
m1 = float(input("Enter mass of First Object: "))
m2 = float(input("Enter mass of Second Object: "))
r = float(input("Enter distance between two objects: "))
G = 6.673*(10**-11)
f = (G*m1*m2) / (r**2)
print(f"The Gravitational Force between two Objects are {f}")
print(f"The Gravitational Force between two Objects are {round(f,2)}")
print("Gravitational Force is ", round(f,2))
