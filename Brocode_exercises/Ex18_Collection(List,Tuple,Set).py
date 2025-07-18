# Collection (List , Tuple ,SEt)

# List = [] ordered and changeable. Duplicates Ok
# Set = {} unordered and immutable , but Add/Remove Ok . No duplicates
# Tuple = () ordered and unchangeable . Duplicates Ok . FASTER

# Lists []
fruits = ["Apple","Bannana","Orange","Pineapple"]

for i in fruits:
    print(i)
fruits[0]= "Mango"
total_fruits =len(fruits)
fruits.sort()
fruits.reverse()
fruits.insert(-1,"Watermelon")
fruits.append("Guava")
print(fruits)

# set {}

Cars = {"audi","bugati","BMW","Benz"}

Cars.add("Toyotta")
#Cars.pop() #1st element removed
# Cars.clear()
Cars.remove("audi")
print(Cars)
print(dir(Cars))

#Tuple (faster)

bikes  = ("hero","suzuki","ninja","harley","RE")
print(len(bikes))
print("tvs" in bikes)
