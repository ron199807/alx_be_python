# promptting user 
weather = input("what's the weather like today?(suuny/rainy/cold): ")

#wheather checker and prints recommendations
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coaat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this wether.")

