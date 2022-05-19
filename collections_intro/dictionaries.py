data_eng_37 = {
    "course_name": "Data Engineering 37",
    "client": "Home Office",
    "trainer": "David boi",
}

print(data_eng_37, type(data_eng_37))

print(data_eng_37["client"])

data_eng_37["trainer"] = "David boi H"
data_eng_37["trainee"] = ["someone", "someone", "someone"]
print(data_eng_37)

print(data_eng_37.get("course_name"))
data_eng_37.update({"course_length": "8 weeks"})