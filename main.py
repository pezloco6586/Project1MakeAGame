def distance_from_school():
  response8 = input("How far do you live from school? (in miles) ")
  return response8

def school_function():
  while True:
    print ("Let's go to school! How will you get there? ")
    response4 = input("Say 'car' 'bike' 'bus' or 'walk' ")
    if response4 == "car":
      response9 = input("Do you drive yourself or will someone drive you? Say 'I drive myself' or 'someone else takes me' ")
      if response9 == "I drive myself":
        response10 = input("How long have you had your license for? (number of years) ")
        print(f"{response10} years down, forever to go!")
      break
    elif response4 == "bike":
      response11 = input("What is your go-to gear shift on your bike? (1-7) ")
      if response11 == "4":
        print(f"I also usually bike with my gear at {response4}!")
      elif response11 > 4:
        print(f"wow!! {response4}, you're up for the challenge, huh")
      else:
        print("Okay! I assume your road is super windy.")
      break
    elif response4 == "bus":
      response12 = input("That's super admirable that you use public transportation. Do you ride the bus for 'convenience' or the support the 'environment'")
      if response12 == "convenience":
        print("That's very strategic!")
      elif response12 == "environment":
        print("That is very thoughtful of you")
      else:
        print("Public transportation is a super cool and effective way to get around:) ")
      break
    elif response4 == "walk":
      print("Oh my!! That is a bold choice...")
      response8 = distance_from_school ()
      print(f"Wow! {response8} miles is impressive!!")
      break
    else:
      print("You did not give an imput that I can respond to. Please try again.")


def puddle_fun():
  response7 = input("What color are your rainboots? ")
  if response7 == "pink":
    print(f"WOW!! {response7} is my favorite color:) ")
  else: 
    print("that's super cool! ")

print("Welcome to Choose Your Own Adventure!! How is the weather today?" )
response1 = input("Say 'It's chilly' or 'It's warm' ")
if response1 == "It's chilly":
  print("What will you wear? ")
  response2 = input("Say 'a raincoat and rainboots' or 'a sweater and pants' ")
  if response2 == "a raincoat and rainboots":
    print("Let's go hop in puddles! Will you go with your sister or your brother ")
    female_sibling = "sister"
    response3 = input(f"Say '{female_sibling}' or 'brother' ")
    if response3 == "sister":
      puddle_fun()
    elif response3 == "brother":
      puddle_fun()
  elif response2 == "a sweater and pants":
    school_function()
  else:
    print("I cannot utilize this input. Please try again. ")
elif response1 == "It's warm":
  print("What will you wear? ")
  response5 = input("Say 'shorts and a tank top' or 'swimsuit' ")
  if response5 == "shorts and a tank top":
    school_function()
  elif response5 == "swimsuit":
    place_to_swim = "pool"
    print(f"Let's go to the {place_to_swim}!! Which style will you perfect today? ")
    response6 = input("Say 'breaststroke' 'butterfly' or 'freestyle'")
  else:
    print("I cannot utilize this input. Please try again. ")
else:
  print("I cannot utilize this input. Please try again. ")