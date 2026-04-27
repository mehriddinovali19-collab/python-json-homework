# 🧩 Task 1 — JSON parsing + filtering (Junior → Mid daraja)

### 📌 Problem

Sizga quyidagi JSON berilgan:

```json
[
  {"id": 1, "name": "Ali", "age": 17, "is_student": true},
  {"id": 2, "name": "Vali", "age": 22, "is_student": false},
  {"id": 3, "name": "Hasan", "age": 19, "is_student": true}
]
```

---

### 🎯 Vazifa

1. JSON ni Python object ga parse qiling
2. Faqat `is_student=True` bo‘lganlarni ajrating
3. Ularning **o‘rtacha yoshini** hisoblang
4. Natijani quyidagi formatda qaytaring:

```python
{
    "count": 2,
    "average_age": 18.0
}
```

---

### 🔧 Requirements

* `json.loads`
* `list comprehension` yoki `filter`
* alohida function yozish:

```python
def get_student_stats(data: str) -> dict:
    ...
```

---

### 💡 Nima uchun bu task muhim?

* JSON → Python mapping (`dict`, `list`)
* Data filtering (backend’da eng ko‘p ishlatiladigan pattern)
* Aggregation logic (analytics foundation)

---

# 🧩 Task 2 — Nested JSON + transform (Mid daraja)

### 📌 Problem

```json
{
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
}
```

---

### 🎯 Vazifa

Har bir user uchun:

* jami order summasini hisoblang
* yangi structure qaytaring:

```python
[
  {"id": 1, "name": "Ali", "total_spent": 250},
  {"id": 2, "name": "Vali", "total_spent": 0}
]
```

---

### 🔧 Requirements

* Nested list/dict traversal
* `sum()` + generator expression
* function yozish:

```python
def calculate_total_spent(data: dict) -> list:
    ...
```

---

### 💡 Nima uchun bu task muhim?

* Real backend JSON’lar doim nested bo‘ladi
* Data transformation (DTO mapping)
* Edge case: empty list (`orders: []`)

---

# 🧩 Task 3 — JSON validation + business logic (Mid+ / Senior mindset)

### 📌 Problem

Input JSON:

```json
[
  {"name": "Ali", "email": "ali@example.com", "age": 20},
  {"name": "", "email": "invalid-email", "age": -5},
  {"name": "Vali", "email": "vali@example.com", "age": 25}
]
```

---

### 🎯 Vazifa

1. Har bir userni validate qiling:

   * `name` bo‘sh bo‘lmasin
   * `email` ichida `@` bo‘lsin
   * `age > 0`

2. Natijani 2 ga ajrating:

```python
{
  "valid_users": [...],
  "invalid_users": [...]
}
```

---

### 🔧 Requirements

* Validation function:

```python
def is_valid_user(user: dict) -> bool:
    ...
```

* Main function:

```python
def split_users(data: list) -> dict:
    ...
```
