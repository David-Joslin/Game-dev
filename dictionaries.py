world_capitals = {
    "Ireland" : "Dublin",
    "India" : "New Delhi",
    "France" : "Paris"
}
print(world_capitals)
print(type(world_capitals))

#adding values
world_capitals["Japan"] = "Tokyo"
print(world_capitals)

#update values
world_capitals["France"] = "paris"
print(world_capitals)

#accesing values
print(world_capitals["Japan"])

#removing elements
del world_capitals["France"]
print(world_capitals)

#checking for membership
if "America" in world_capitals:
    print("Key is present")
    

else:
 print("key is not present")

#itrating over values
for key in world_capitals.keys():
   print(key)

for value in world_capitals.values():
   print(value)

#finding length
print(len(world_capitals))


