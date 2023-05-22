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
print("How much cup of semolina you have at home?")
print("Type under here:")
est = input()
print("You have ", est, "cup of semolina!")
print("And now! How much cup of yoghurt you have in the fridge?")
ist = input()
print("You have", ist, "cup of yoghurt in the fridge!")
print("And lastly! How much of vegetables are in your home in grams?")
vst = input()
print(f"You have  {vst} grams of vegetables!")
print("Thank you for your time, now we start to calculate...")
input()

print("Calculation started...")

if float(est) < amounts[0]:
    print(f"You need {amounts[0] - float(est)} more semolina")
else:
    if float(ist) < amounts[1]:
        print(f"You need {amounts[1] - float(ist)} more yoghurt")
    else:
        if float(vst) < amounts[3]:
            print(f"You need {amounts[3] - float(ist)} more grams of fresh veggies")
        else:
            print(float(est) / amounts[0])
            print(float(ist) / amounts[1])
            print(float(vst) / amounts[3])
            values = (float(est) / amounts[0]) // (float(ist) / amounts[1]) // (float(vst) / amounts[3])
            print(f"You can make Uttapam pancakes for {values} people!")
            print("I hope you will make a good cooking")
input()
    
print("Program is closing...")