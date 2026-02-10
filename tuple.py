my_tuple = (3,4.6,"david")
print(my_tuple)

#nested tuple
n_tuple = ("david",[1,2,3],(7,8,9))
print(f"\nnested_tuple = {n_tuple}")
print(f"\ntotal items in nested tuples = {len(n_tuple)}")

#retrieving items from a nested tuple
print(f"\n item 1 in nested_tuple = {n_tuple[0]}")
print(f"\n item 2 from the list in nested_tuple = {n_tuple[1][1]}")
print(f"\n item 3 from the tuple in nested_tuple = {n_tuple[2][2]}")
print(f"\n item 1 last 3 alphabet from nested_tuple = {n_tuple[0][2:5]}")

# my_tuple[0] = 4 #tuples cannot be changed,because they are immutable
#print(my_tuple)
