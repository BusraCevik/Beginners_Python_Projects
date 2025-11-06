#string concatenation
#we suppose want to create a string that says "subscribe to ------"

#youtuber = "busra"
#print("subscribe to "+ youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

adj = input("Enter a adjective: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter a verb: ")
famous_person = input("Enter a famous person:")

madlib = (f"Computer programming is so {adj}! "
          f"It makes me so excited all the time because I love to {verb1}. "
          f"Stay hydrated and {verb2} like you are {famous_person}")

print(madlib)
