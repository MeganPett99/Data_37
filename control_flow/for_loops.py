alphabet = ["A", "B", "C", "D", "E"]

for letter in alphabet:
    print("The next letter is:")
    print(letter.lower())
    if letter == "o":
        print("ohh nooo")



nest = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

for sublist in nest:
    print(sublist)
    for number in sublist:
        print(number)

hi ="Hello world!"
for c in hi:
    print(c)


Hunter_X_Hunter = {
    "Main_characters": "Killua",
    "Killua_Nen_type": "Transmute",
    "Main_OG_character": "Gon",
    "Gon_Nen_type": "Enhancement",
    "trainer": "Biscuit Kreuger",
    "trainer_nen_style": "Transmute",

}

for keys in Hunter_X_Hunter:
    print(keys)

for trainer in Hunter_X_Hunter['trainer']:
    print(trainer)

for something in Hunter_X_Hunter.items():
    print(something, type(something))

for i in range(5):
    print(f"This is line number: {i +1}")
