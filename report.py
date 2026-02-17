
David = ("David", (85, 78, 92, 88, 90))
George = ("George", (75, 82, 69, 91, 87))

print("Student Report Card")

name = input("\nEnter student name: ")

if name == David[0]:
    print(f"\nName = {David[0]}")
    print(f"English = {David[1][0]}")
    print(f"Maths = {David[1][1]}")
    print(f"Science = {David[1][2]}")
    print(f"History = {David[1][3]}")
    print(f"French = {David[1][4]}")

elif name == George[0]:
    print(f"\nName = {George[0]}")
    print(f"English = {George[1][0]}")
    print(f"Maths = {George[1][1]}")
    print(f"Science = {George[1][2]}")
    print(f"History = {George[1][3]}")
    print(f"French = {George[1][4]}")

else:
    print("Student not found")
