print("Program is starting...")
input()

print("It is a cook helping program, so lets get started!")
print("We are gonna make an south African Uttapam pancake!")
ingredients = ['semolina', 'yoghurt', 'water', 'fresh vegetables', 'salt']
amounts = [1, 0.5, 0.5, 200, 0 ]
inwat = ['cup', 'cup', 'cup', 'grams', 'some' ]
len_array = len(ingredients)
input()
print("The ingredients that we need are: ")
for x in range(len_array):
    print(amounts[x], inwat[x], ingredients[x])
input()
print("How much of semolina you have at home?")
print("Type under here:")
est = input()
print("You have ", est, "cup of semolina!")
print("And now! How much yoghurt you have at fridge?")
ist = input()
print("You have", ist, "cup of yoghurt!")
print("And lastly! How much of vegetables are in your home?")
vst = input()
print("Grams or kilograms?")
wst = input()
print("You have ", vst, wst, " of vegetables!")
print("Thank you for your time, now we start to calculate...")


    
print("I hope you made a good cooking")
print("Program is closing...")