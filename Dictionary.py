capitals = {"USA":"Washington", "UK":"United Kingdom", "India":"New Delhi", "Canada":"Ottawa"}

country = "India"

if capitals.get(country):
    print("Capital Exists and is: ", capitals.get(country))
else:
    print("Capital Not Exists")

capitals.update({"France":"Paris"})
capitals.update({"Canada":"Toronto"})
print(capitals)
capitals.pop("France")
print(capitals)
#removes latest
capitals.popitem()
print(capitals)
#capitals.clear()
print(capitals)

for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)
print()
#print key value pairs
for key, value in capitals.items():
    print(f"{key} : {value}")


