import json
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
#print(person_json)
person_dct = json.loads(person_json)
print(person_dct)
print("")
print(type(person_dct))
print("")
print(person_dct['name'])
