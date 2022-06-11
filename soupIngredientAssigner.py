import random
peeps = ['wyatt', 'darrin', 'shivan', 'justin', 'zach', 'jesse', 'harsh', 'jon', 'donnie']
#the ingredients and how much of each we want
ingredientRatioDict = {"protein": 3, "veggies": 4, "carb": 1, "carb&veg": 1}
#shuffle the list, idk why, why not
random.shuffle(peeps)
#put shivan at the front since we dont want to find him at the end and assign him protein if all the protein spots have been filled
peeps.insert(0, peeps.pop(peeps.index("shivan")))
print(peeps)
#will be the same length as peeps and match each peeps ingredient to the peep by index, ex peeps[0] ingrediend will be ingredient [0]
ingredients = []
#test random choice from dict keys
# print(random.choice(list(ingredientRatioDict.keys())))
#for each person
for peep in peeps:
    #if shivan, protein (ye gains)
    if peep == "shivan":
        ingredient = "protein"
    else:
        #assign a random ingredient from the dict keys
        ingredient = random.choice(list(ingredientRatioDict.keys()))
    #if we have as much as we need already
    if ingredients.count(ingredient) >= ingredientRatioDict[ingredient]:
        #randomly pick ingredients until we choose one we dont have enough of yet
        while ingredients.count(ingredient) > ingredientRatioDict[ingredient]:
            ingredient = random.choice(list(ingredientRatioDict.keys()))
    #add it to ingredients list
    ingredients.append(ingredient)
#print results
for i in range(len(peeps)):
    print(peeps[i], ": ", ingredients[i])