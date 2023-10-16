import requests
import json

URI = "https://www.dnd5eapi.co/api/classes"
print(URI)
response = requests.get(URI)

#print(f"GET: {response.text}")
print("0 .- Exit")

response_json = json.loads(response.text)
length = len(response_json['results'])

option = ""
while(option != "Exit" or option != "exit"):
    for num in range(length):
        order = num+1
        print(order,".- "f"{response_json['results'][num]['name']}")



    option = int(input("\nSelecciona el personaje: ")) - 1

    if(option == -1):
        break

    URI = "https://www.dnd5eapi.co/api/classes/"f"{response_json['results'][option]['index']}"

    character_data = requests.get(URI)

    character_data_json = json.loads(character_data.text)
    character_data_length = len(character_data_json['proficiencies'])

    print("Proficiencies: \n")

    for num in range(character_data_length):
        order = num+1
        print(order,".- "f"{character_data_json['proficiencies'][num]['name']}")
    
    print("\n \n")


