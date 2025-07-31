# 🐍 My Complete Pydantic Learning Journey – From Beginner to Advanced

Welcome to my documented journey of learning **Pydantic** – a powerful library in Python that changed the way I validate, manage, and serialize data in my applications. This guide is structured to help anyone from beginners to advanced developers understand and use Pydantic effectively.

---

## 📘 What is Pydantic?

> **Pydantic** is a Python library for **data parsing**, **validation**, and **serialization** using Python type hints.

It ensures that the data you're working with is valid, properly structured, and automatically converted to the correct types. It’s widely used in **FastAPI**, **data pipelines**, **APIs**, and even **configuration management**.

---

## 📌 Why Pydantic?

### ✅ Main Benefits:
| Feature                    | Explanation |
|----------------------------|-------------|
| **Runtime Validation**     | Automatically validates data at runtime based on type hints. |
| **Type Conversion**        | Converts input types (like `"123"` → `123`) when possible. |
| **Detailed Errors**        | Shows clear and helpful error messages when validation fails. |
| **Serialization Support**  | Easily convert models to dictionaries or JSON strings. |
| **Nested Models**          | Supports complex, deeply nested objects. |
| **High Performance**       | Fast and efficient validation. |
| **Framework Integration**  | Works perfectly with modern frameworks like FastAPI. |

---

## 🧱 Pydantic Basics

### 1. 🔹 `BaseModel` – The Core Building Block

All models in Pydantic inherit from `BaseModel`.

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True

user = User(id=1, name="Sourabh", email="sourabh@example.com")
print(user.name)  # Sourabh
````

➡️ If wrong types are passed, Pydantic will raise an error.

---

### 2. 🔸 `Field()` – Control Field Behavior

Use `Field()` for validation rules, default values, constraints, and metadata.

```python
from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    quantity: int = Field(default=0, ge=0)
    description: Optional[str] = Field(None, max_length=500)
```

➡️ The `...` means the field is **required**.

---

### 3. 🔍 Validation with `@validator` and `@root_validator`

Create custom validation rules.

```python
from pydantic import BaseModel, validator

class Profile(BaseModel):
    username: str
    email: str

    @validator("username")
    def no_space(cls, v):
        if " " in v:
            raise ValueError("Username must not contain spaces")
        return v

    @validator("email")
    def check_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email")
        return v
```

---

### 4. ⚙️ Model Configuration with `Config`

Change model behavior using a nested class:

```python
class User(BaseModel):
    name: str
    age: int

    class Config:
        extra = 'forbid'  # Do not allow extra fields
        validate_assignment = True
```

---

## 🔄 Serialization & Deserialization

Serialization = Convert models to dictionary or JSON.
Deserialization = Create models from dict or JSON.

### ➕ Model to Dictionary

```python
event_dict = user.model_dump()
```

### ➕ Model to JSON

```python
event_json = user.model_dump_json()
```

### ➕ Model from JSON

```python
User.model_validate_json('{"id": 1, "name": "Alice", "email": "alice@example.com"}')
```

---

## 🧩 Intermediate to Advanced Features

### 1. 🔁 Nested Models

You can use models inside other models.

```python
class Address(BaseModel):
    city: str
    state: str

class User(BaseModel):
    name: str
    address: Address

data = {
    "name": "Sourabh",
    "address": {
        "city": "Delhi",
        "state": "Delhi"
    }
}

user = User(**data)
print(user.address.city)  # Delhi
```

---

### 2. 🧠 Optional, Union, and Enum Fields

```python
from typing import Optional, Union
from enum import Enum

class UserType(str, Enum):
    ADMIN = "admin"
    USER = "user"

class User(BaseModel):
    name: str
    age: Optional[int]
    user_type: UserType = UserType.USER
    data: Union[dict, str, None]
```

---

### 3. ⚙️ Environment Config with `BaseSettings`

Great for `.env` file and secret management.

```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
print(settings.app_name)
```

---

### 4. 🔬 Advanced Patient System (Nested + Validation + Enum)

```python
from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime, date
from enum import Enum

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class Address(BaseModel):
    city: str
    state: str
    pin: str

class MedicalHistory(BaseModel):
    condition: str
    diagnosed_date: date

class Patient(BaseModel):
    name: str
    age: int
    gender: Gender
    address: Address
    medical_history: List[MedicalHistory] = []
    registered_at: datetime = Field(default_factory=datetime.now)

    @validator("age")
    def validate_age(cls, v):
        if v < 0:
            raise ValueError("Age must be positive")
        return v
```

---

## 🔧 Error Handling

```python
from pydantic import ValidationError

try:
    user = User(id="abc", name="123", email="notemail")
except ValidationError as e:
    print(e.json(indent=2))
```

---

## 🔁 Migration from Pydantic v1 to v2

| Pydantic v1   | Pydantic v2 Equivalent  |
| ------------- | ----------------------- |
| `.dict()`     | `.model_dump()`         |
| `.json()`     | `.model_dump_json()`    |
| `parse_obj()` | `model_validate()`      |
| `@validator`  | `@field_validator` (v2) |

---

## 🚀 Real-World Use Cases

| Use Case             | How Pydantic Helps                                |
| -------------------- | ------------------------------------------------- |
| 🧾 API Development   | Validates request/response data (e.g., FastAPI)   |
| 🧹 Data Cleaning     | Converts raw data into clean, typed data          |
| ⚙️ Config Management | Loads environment variables with `BaseSettings`   |
| 🔒 Secure Apps       | Validates user input & prevents bad data handling |

---

## ⚡ Performance Tips

* Use `slots = True` in `Config` for memory-efficient models.
* Use `exclude_unset=True` for clean serialized output.
* Avoid using complex custom validators when simple types work.
* Reuse models where possible.

---

## 🎯 Best Practices

1. ✅ Always use clear type annotations.
2. 🚫 Avoid unnecessary custom validation.
3. 💬 Use `Field()` for metadata and constraints.
4. 🧠 Separate model structure from business logic.
5. ⚙️ Use `BaseSettings` for config.
6. 🔐 Catch and handle `ValidationError` gracefully.
7. 🧩 Use nested models for clarity in complex data.

---

## 📚 My Learning Summary

| Stage           | What I Learned                                     |
| --------------- | -------------------------------------------------- |
| 🟢 Beginner     | What is Pydantic, BaseModel, Field(), Validation   |
| 🔵 Intermediate | Nested Models, JSON serialization, Error handling  |
| 🔴 Advanced     | Custom validators, Settings, Enums, Best practices |

---

## 🔗 Resources

* 📘 Official Docs: [https://docs.pydantic.dev](https://docs.pydantic.dev)
* 🚀 FastAPI + Pydantic: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)
* 🧪 GitHub Repo: [https://github.com/pydantic/pydantic](https://github.com/pydantic/pydantic)

---

### 💡 Final Note

> *Pydantic taught me how powerful and safe typed data handling can be. This journey not only improved my code but also made me think deeper about structure, clarity, and validation in every Python project I build.*

**– Sourabh Kumar**

---

🌟 *Happy Learning! If this helped you, feel free to build upon it and share it with others.*

