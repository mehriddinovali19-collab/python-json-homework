import json
def is_valid_user(user: dict) -> bool:
    return user["name"] != " " and "@" in user["email"] and user["age"] > 0

def split_users(data: list) -> dict:
        valid_user = []
        not_valid_user = []
        for user in data:
             if is_valid_user(user):
                valid_user.append(user)
             else:
                  not_valid_user.append(user)
        return {"valid user": valid_user,
                "not valid user": not_valid_user}
data = """[
  {"name": "Ali", "email": "ali@example.com", "age": 20},
  {"name": "", "email": "invalid-email", "age": -5},
  {"name": "Vali", "email": "vali@example.com", "age": 25}
]"""
parsed_data = json.loads(data)
print(split_users(parsed_data))