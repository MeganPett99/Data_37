age = 15
has_ticket = True

if has_ticket:
    if age >= 15:
        print("you can see this film")
    else:
        print("come back when you're older")
else:
    print("you need a ticket hun ")

film_rating = "U"

if film_rating == "U":
    print("You're age is suitable for viewing")
elif film_rating == "PG":
    print("Suitable for general viewing, but some scenes may be suitable for younger children")
elif film_rating == "12" or film_rating == "12a":
    print("Suitable for general viewing, but some scenes may be suitable for younger children")
else:
    film_rating == "18"
    print("Adults only, sorry")



