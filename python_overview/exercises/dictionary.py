person = {
    "username": "nomonim",
    "age": 23,
    "isVip": False,
    "completed_levels": [2, 3, 5]
}

# if person["id"] > 3:
#     print("id>3")




if person.get("id",0)>3:
    print("id>3")
else:
    print("No")