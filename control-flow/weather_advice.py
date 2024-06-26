# promptting user 
weather = input("what's the weather like today? (sunny/rainy/cold): ")

#Recommendations
sunny = "Wear a t-shirt and sunglasses."
rainy = "Don't forget your umbrella and a raincoat."
cold = "Make sure to wear a warm coaat and a scarf."

#wheather checker and prints recommendations
if weather == "sunny":
    print(sunny)
elif weather == "rainy":
    print(rainy)
elif weather == "cold":
    print(cold)
else:
    print("Sorry, I don't have recommendations for this wether.")

