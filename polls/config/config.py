import json
from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'config_file'

file = file_location.open()
data = json.loads(file.read())
file.close()

num_of_question_per_page = data['num_of_question_per_page']
