import json 
def get_student_stats(data: str) -> dict:
    students = json.loads(data)
    filtered = [filt for filt in students if filt["is_student"]]
    count = len(filtered)
    if count == 0:
        average_age = 0
    else: 
        average_age = sum(filt["age"] for filt in filtered) / count 
    return {
    "count": count,
    "average_age": average_age
}

data = """[
  {"id": 1, "name": "Ali", "age": 17, "is_student": true},
  {"id": 2, "name": "Vali", "age": 22, "is_student": false},
  {"id": 3, "name": "Hasan", "age": 19, "is_student": true}
]"""

print(get_student_stats(data))