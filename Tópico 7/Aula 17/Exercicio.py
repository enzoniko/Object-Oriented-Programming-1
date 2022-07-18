# Function that reads values and saves them in a dictionary
def person():
    values = {'name': input('Digite o nome: ')}
    values['age'] = int(input('Digite a idade: '))
    values['sex'] = input('Digite o sexo [F/M]: ').upper()
    return values

# List of people
people = []

# Add people to the list while the user wants to
while input("Adicionar pessoa? [S/N]").upper() == 'S':
    person1 = person()
    if person1 not in people:
        people.append(person1)
# Show how many people were added
print(f'Foram adicionadas {len(people)} pessoas')

# Show the media of age
age = sum(int(person['age']) for person in people)
print(f'A média de idade é {age/len(people)}')

# Create a list of people with the age greater than the media
people_above_media = [
    person for person in people if person['age'] > age / len(people)
]

print(people_above_media)

# Create a list of people where sex == F
females = [person for person in people if person['sex'] == 'F']
print(females)

