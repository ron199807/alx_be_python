# promptting user 
weather = input("What's the weather like today? (sunny/rainy/cold): ")

#wheather checker and prints recommendations
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coaat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this wether.")

