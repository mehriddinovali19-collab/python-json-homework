import json
def calculate_total_spent(data: dict) -> list:
    kilent = json.loads(data)
    result = []
    for user in kilent["users"]:
        total = sum(order["price"] for order in user["orders"])
        result.append([
  {"id": user['id'], "name": user['name'], "total_spent": total}
])
    return result 
data = """{
  "users": [
    {
      "id": 1,
      "name": "Ali",
      "orders": [
        {"id": 101, "price": 100},
        {"id": 102, "price": 150}
      ]
    },
    {
      "id": 2,
      "name": "Vali",
      "orders": []
    }
  ]
}"""
print(calculate_total_spent(data))
    