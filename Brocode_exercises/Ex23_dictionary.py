# Dictionary
# dictionary = {keys :object}


capitals = {"Usa" : "washington DC",
            "India" : "New Delhi",
            "Russia" : "Moscow"}
# capital = capitals.get("Usa")
# print(capital)
if capitals.get("Usa"):
    print("capital exist")
capitals.update({"Srilanka":"colombo"})
capitals.update({"Usa":"Valluvarkotam"})
#capitals.pop("Usa") # clear the item
#capitals.popitem() # clears the last item

for keys in capitals.keys():
    print(keys,end=" ")
print()
for value in capitals.values():
    print(value,end=" ")
print()
for key,value in capitals.items():
    print(f"{key}:{value}")
print(capitals)