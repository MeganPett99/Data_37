# data_eng_37 = {
#     "course_name": "Data Engineering 37",
#     "client": "Home Office",
#     "trainer": "David boi",
# }
#
# print(data_eng_37, type(data_eng_37))
#
# print(data_eng_37["client"])
#
# data_eng_37["trainer"] = "David boi H"
# data_eng_37["trainee"] = ["someone", "someone", "someone"]
# print(data_eng_37)
#
# print(data_eng_37.get("course_name"))
# data_eng_37.update({"course_length": "8 weeks"})

Hunter_X_Hunter = {
    "Main_characters": "Killua",
    "Killua_Nen_type": "Transmute",
    "Main_OG_character": "Gon",
    "Gon_Nen_type": "Enhancement",
    "trainer": "Biscuit Kreuger",
    "trainer_nen_style": "Transmute",

}

Hunter_X_Hunter["The weirdest character"] = ["Hisoka"]
print(Hunter_X_Hunter.get("Main character"))

print(Hunter_X_Hunter)
print(Hunter_X_Hunter.keys())
print(Hunter_X_Hunter.values())
print(Hunter_X_Hunter.items())

print(f"Megan favourite character's {Hunter_X_Hunter['Main_characters']} and {Hunter_X_Hunter['Main_OG_character']}")