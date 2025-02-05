# This is Mad Libs - Cook, Serve, Delicious! 2!! Edition
print("""
    Welcome to Mad Libs - Cook, Serve, Delicious! 2!! Edition.
    Enter some needed words here to add flavor for your adventure!
    Good luck, and enjoy! :D
      """)
print("-----")

# This section covers the Teragon Tower Incident scenario
any_csd2_restaurant = input("Enter any CSD 2 resto: ")
adjective = input("Enter an adjective: ")
item = input("Enter an item: ")
ing_verb = input("Enter a verb that ends with -ing: ")
emotion = input("Enter an emotion: ")
action = input("Enter any action: ")
verb = input("Enter a verb: ")

scenario1 = f"Today is my first day at {any_csd2_restaurant}, but I am very late today. \
I encountered a {adjective} {item} on my way to work. What's worse, it was {ing_verb}! \
I was so {emotion}, so I {action}, it affected my commute to work. I was so {emotion}, \
that I {verb}. Whoops."

print("Scenario 1: The Teragon Tower Incident")
print(scenario1)

print("-----")

# This section covers the Suckerpunch Me Movie Screening scenario
adjective2 = input("Enter an adjective: ")
adjective3 = input("Enter another adjective: ")
body_part = input("Enter a body part: ")
verb2 = input("Enter a verb: ")
adjective4 = input("Enter another adjective: ")
person_name = input("Enter a person's name: ")
item2 = input("Enter an item: ")
adjective5 = input("Enter another adjective: ")
integer = input("Enter an integer number: ")
adjective6 = input("Enter another adjective: ")

scenario2 = f"I saw Suckerpunch Me today. It was {adjective}! The scenes are {adjective3}, \
and they made my {body_part} {verb2}. Wow. I've never seen a documentary so {adjective4}, \
especially that part where {person_name}'s {item2} was {adjective5}. {integer} out of 10. \
Would {adjective6} it again."

print("Scenario 2: The Suckerpunch Me Movie Screening")
print(scenario2)