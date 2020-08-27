import json

f = open("config.json")
data = json.loads(f.read())
f.close()

num_of_question_per_page = data['num_of_question_per_page']
