# Function that reads values and saves them in a dictionary
def person():
    values = {}
    values['name'] = input('Digite o nome: ')
    values['age'] = int(input('Digite a idade: '))
    values['sex'] = input('Digite o sexo [F/M]: ').upper()
    return values

# List of people
people = list()

# Add people to the list while the user wants to
while True:
    if input("Adicionar pessoa? [S/N]").upper() == 'S':
        person1 = person()
        if person1 not in people:
            people.append(person1)
    else:
        break

# Show how many people were added
print(f'Foram adicionadas {len(people)} pessoas')

# Show the media of age
age = 0
for person in people:
    age += int(person['age'])
print(f'A média de idade é {age/len(people)}')

# Create a list of people with the age greater than the media
people_above_media = list()
for person in people:
    if person['age'] > age/len(people):
        people_above_media.append(person)

print(people_above_media)

# Create a list of people where sex == F
females = []
for person in people:
    if person['sex'] == 'F':
        females.append(person)

print(females)

