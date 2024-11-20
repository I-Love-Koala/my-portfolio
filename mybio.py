import sys
import time

name = input("Hello, I am Kim Pirun, What about you? ")
print("It's nice to meet you,", name)

age = input("I am 10 years old, what about you? Note: don't add 'years old', only add the number: ")
print("Oh, you are", age)

if age == "10":
    print("COOL, You Are The Same Age As Me!")

favourite_food = input("My favourite food is Spaghetti Carbonara, What about you? ")
print("Oh!, your favourite food is", favourite_food)

if favourite_food.lower() == "spaghetti carbonara":
    print("YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO! your favourite food is also Spaghetti Carbonara? Damn!")

hobby = input("I have two hobbies, those hobbies are Coding and Reading! What about you? ")
print("Ohh! You like to", hobby)

if hobby.lower() in ["coding", "reading"]:
    print("Yay! We have a similar hobby!")
    coding = input("In programming I can code more than two languages, those languages are... HTML (For Web Development), CSS (Styling For Web Development), Python, a little bit of Java and C, what languages do you know how to code in? ")
    print("Cool! so you code:", coding)
    
    if "HTML" in coding and "CSS" in coding and "Python" in coding and "a little bit of Java and C" in coding:
        print("WHATTTTTTTTTTTTTTTTT!?!?!?!?, YOU CODE THE SAME LANGUAGES AS ME?!? That's crazy!")
        print("Goodbye, for now.")

    print("\nThe program will close in 20 seconds...")
    for i in range(20, 0, -1):
        print(f"Closing in {i} seconds...")
        time.sleep(1)  # Delay for 1 second
    
    print("Goodbye!")
    sys.exit()