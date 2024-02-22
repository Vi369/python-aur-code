# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).


pet_species = 'Dog'

pet_age = 1

if(pet_species == "Dog" and pet_age < 2):
    recomend_food = "puppy food"
    print("for your pet:", recomend_food)


if (pet_species == "Cat" and pet_age > 5):
    recomend_food = "Senior cat food"
    print("for your pet:", recomend_food)




