import json
p = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
p_j = json.dumps(p,indent=4)
print(type(p_j))
print("")
print(p_j)

