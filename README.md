# 🚀 FastAPI Patient Management System

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-00a393.svg)](https://fastapi.tiangolo.com)
[![Pydantic V2](https://img.shields.io/badge/Pydantic-V2-e92063.svg)](https://docs.pydantic.dev)
[![uv](https://img.shields.io/badge/uv-latest-8b5cf6.svg)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A modern **FastAPI** application demonstrating REST API development with Python, featuring a patient management system with realistic healthcare data.

## 🎯 About This Project

This repository showcases a complete FastAPI learning journey, building a patient management REST API from scratch. Perfect for developers learning modern Python web development, API design, and data validation patterns.

**🔑 Key Learning Areas:**
- Building RESTful APIs with FastAPI
- Data validation using Pydantic models
- Working with JSON datasets
- API documentation and testing
- Modern Python development practices

---

## 📂 Repository Structure

```
FastAPI/
├── main.py                  # FastAPI application with all endpoints
├── patient_dataset.json     # Sample patient data (50+ records)
├── 00_Introduction.md       # API fundamentals and concepts
├── 01_Pydantic.md          # Pydantic usage and validation guide
├── LICENSE                  # MIT License
└── README.md               # This documentation
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip or uv (recommended for faster installs)

### ⚡ Installation with uv (Recommended)

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Sourabh-Kumar04/FastAPI.git
cd FastAPI

# 2️⃣ Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3️⃣ Install dependencies
uv add fastapi uvicorn

# 4️⃣ Run the development server
uv run uvicorn main:app --reload
```

### 🐍 Alternative Installation with pip

```bash
# Clone and setup
git clone https://github.com/Sourabh-Kumar04/FastAPI.git
cd FastAPI

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn

# Run the server
uvicorn main:app --reload
```

### 🌐 Access Your API

Once running, access your API at:
- **🔥 Interactive API Docs (Swagger UI):** http://localhost:8000/docs
- **📖 Alternative Docs (ReDoc):** http://localhost:8000/redoc
- **⚡ API Base:** http://localhost:8000

---

## 📌 API Endpoints

| Method | Endpoint | Description | Example Response |
|--------|----------|-------------|------------------|
| `GET` | `/` | Welcome message and API info | `{"message": "Welcome to FastAPI Patient Management System"}` |
| `GET` | `/about` | About the API and developer | `{"about": "Patient Management API", "developer": "Sourabh Kumar"}` |
| `GET` | `/view` | Get all patients | Array of patient objects |
| `GET` | `/patient/{id}` | Get specific patient by ID | Single patient object |
| `GET` | `/sort` | Sort patients by criteria | Sorted array of patients |

### 🔍 Query Parameters for `/sort`

| Parameter | Type | Options | Default | Example |
|-----------|------|---------|---------|---------|
| `sort_by` | string | `age`, `name` | `age` | `/sort?sort_by=name` |
| `order` | string | `asc`, `desc` | `asc` | `/sort?order=desc` |

---

## 🌐 API Usage Examples

### 📋 Get All Patients
```bash
curl http://localhost:8000/view
```

### 👤 Get Patient by ID
```bash
curl http://localhost:8000/patient/1
```

### 📊 Sort Patients
```bash
# Sort by age (oldest first)
curl "http://localhost:8000/sort?sort_by=age&order=desc"

# Sort alphabetically by name
curl "http://localhost:8000/sort?sort_by=name&order=asc"
```

### 🐍 Python Example
```python
import requests

# Base URL
base_url = "http://localhost:8000"

# Get all patients
response = requests.get(f"{base_url}/view")
patients = response.json()
print(f"Total patients: {len(patients)}")

# Get specific patient
patient_response = requests.get(f"{base_url}/patient/5")
if patient_response.status_code == 200:
    patient = patient_response.json()
    print(f"Patient: {patient['name']}, Age: {patient['age']}")
else:
    print("Patient not found")

# Get sorted patients
sorted_response = requests.get(f"{base_url}/sort", params={
    "sort_by": "age", 
    "order": "desc"
})
sorted_patients = sorted_response.json()
print(f"Oldest patient: {sorted_patients[0]['name']} ({sorted_patients[0]['age']} years)")
```

---

## 🗄️ Dataset Overview

The `patient_dataset.json` contains **50+ realistic patient records** for testing and development purposes.

### 📊 Data Structure

Each patient record includes:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `id` | Integer | Unique patient identifier | `1` |
| `name` | String | Full patient name | `"Sumer Saini"` |
| `age` | Integer | Patient age | `55` |
| `gender` | String | Gender identity | `"Male"` |
| `contact` | String | Contact number | `"+915335225484"` |
| `email` | String | Email address | `"sahotakiaan@shroff.info"` |
| `address` | String | Complete address | `"H.No. 452, Hora Marg, Hindupur 334089"` |
| `blood_group` | String | ABO blood type | `"A+"` |
| `medical_history` | Array | Medical conditions | `["Cardiac issues", "COVID-19"]` |
| `admission_date` | String | Admission date (YYYY-MM-DD) | `"2025-07-09"` |
| `discharge_date` | String | Discharge date (YYYY-MM-DD) | `"2025-07-19"` |
| `doctor_assigned` | String | Assigned physician | `"Dr. Rohit Nair"` |
| `current_status` | String | Current patient status | `"Discharged"` |

### 📋 Sample Patient Record

```json
{
  "id": 1,
  "name": "Sumer Saini",
  "age": 55,
  "gender": "Male",
  "contact": "+915335225484",
  "email": "sahotakiaan@shroff.info",
  "address": "H.No. 452, Hora Marg, Hindupur 334089",
  "blood_group": "A+",
  "medical_history": [
    "Cardiac issues",
    "COVID-19",
    "Hypertension"
  ],
  "admission_date": "2025-07-09",
  "discharge_date": "2025-07-19",
  "doctor_assigned": "Dr. Rohit Nair",
  "current_status": "Discharged"
}
```

---

## 📚 Learning Resources

This repository includes comprehensive learning materials:

### 📖 [`00_Introduction.md`](./00_Introduction.md)
**API Fundamentals & System Design**
- What are REST APIs and why they matter
- HTTP methods and status codes
- Monolithic vs Microservice architectures  
- API integration with Machine Learning systems
- Testing tools and best practices

### 🔧 [`01_Pydantic.md`](./01_Pydantic.md)
**Advanced Data Validation with Pydantic**
- Pydantic models and type hints
- Data validation and serialization
- Nested models and complex data structures
- Environment variables and settings management
- Custom validators and error handling

### 🎓 Skills You'll Learn

- **FastAPI Framework:** Route definition, request handling, response formatting
- **Pydantic Integration:** Automatic data validation, type conversion, error messages
- **API Design:** RESTful principles, endpoint organization, query parameters
- **Data Handling:** JSON processing, sorting algorithms, error handling
- **Development Tools:** Virtual environments, package management, development servers

---

## 🛠️ Development

### 🧪 Testing Your API

#### Manual Testing
Use the built-in Swagger UI at `http://localhost:8000/docs` to:
- View all available endpoints
- Test API calls directly in the browser
- See request/response schemas
- Understand parameter requirements

#### Command Line Testing
```bash
# Test all endpoints
curl http://localhost:8000/
curl http://localhost:8000/about
curl http://localhost:8000/view
curl http://localhost:8000/patient/10
curl "http://localhost:8000/sort?sort_by=name&order=asc"
```

### 🔄 Development Workflow

```bash
# Make changes to main.py
# Server automatically reloads (thanks to --reload flag)
# Test changes at http://localhost:8000/docs
# Check logs in terminal for any errors
```

### 📦 Adding New Dependencies

```bash
# Using uv (recommended)
uv add package-name

# Using pip
pip install package-name
pip freeze > requirements.txt
```

---

## 🚀 What's Next?

### 🎯 Planned Enhancements

1. **Database Integration**
   - Replace JSON file with PostgreSQL or SQLite
   - Add SQLAlchemy ORM for database operations
   - Implement connection pooling

2. **Advanced Features**
   - POST endpoint to create new patients
   - PUT endpoint to update patient information
   - DELETE endpoint to remove patients
   - Search functionality with filters

3. **Authentication & Security**
   - JWT token-based authentication
   - Role-based access control (Admin, Doctor, Nurse)
   - API rate limiting and security headers

4. **Production Deployment**
   - Docker containerization
   - Environment configuration
   - Logging and monitoring
   - CI/CD pipeline with GitHub Actions

### 💡 Learning Suggestions

- Explore the interactive docs thoroughly
- Try modifying the patient data structure
- Add new endpoints for specific use cases
- Experiment with different query parameters
- Study the error handling patterns

---

## 🤝 Contributing

Feel free to contribute to this learning project! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/new-endpoint`)
3. **Make** your changes and test them
4. **Commit** your changes (`git commit -am 'Add new search endpoint'`)
5. **Push** to the branch (`git push origin feature/new-endpoint`)
6. **Create** a Pull Request

### 🐛 Found Issues?
- Check the existing issues on GitHub
- Create a new issue with detailed description
- Include steps to reproduce the problem

---

## 📖 Additional Resources

### 🔗 Helpful Links
- **FastAPI Documentation:** https://fastapi.tiangolo.com/
- **Pydantic Documentation:** https://docs.pydantic.dev/
- **Python Type Hints:** https://docs.python.org/3/library/typing.html
- **HTTP Status Codes:** https://httpstatuses.com/
- **REST API Design:** https://restfulapi.net/

### 🎥 Recommended Learning
- FastAPI official tutorial
- REST API design principles
- Python async/await concepts
- JSON data handling in Python

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**What this means:**
- ✅ Commercial use allowed
- ✅ Modification allowed  
- ✅ Distribution allowed
- ✅ Private use allowed
- ❗ License and copyright notice required

---

## 👨‍💻 About the Developer

**Sourabh Kumar**  
*CS Student @University of Delhi | AWS AIML Scholar'24*

Passionate about AI/ML and software development, exploring modern web technologies and building practical applications for learning and growth.

- 🌐 **GitHub:** [@Sourabh-Kumar04](https://github.com/Sourabh-Kumar04)
- 🎓 **University:** University of Delhi (Computer Science)
<!-- - 🏆 **Achievement:** AWS AI/ML Scholar 2024
- 💼 **Focus:** Python, C++, AI/ML, Web Development -->

---

## 🌟 Support This Project

If this repository helped you learn FastAPI or understand API development:

- ⭐ **Star this repository** to show your support
- 🍴 **Fork it** to create your own version
- 📢 **Share it** with fellow developers
- 💡 **Contribute** improvements or new features
- 🐛 **Report issues** to help others

---

## 📊 Repository Stats

![GitHub stars](https://img.shields.io/github/stars/Sourabh-Kumar04/FastAPI?style=social)
![GitHub forks](https://img.shields.io/github/forks/Sourabh-Kumar04/FastAPI?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Sourabh-Kumar04/FastAPI?style=social)

---

<div align="center">

**Built with ❤️ using FastAPI and Python**

*Happy Learning! 🚀*

</div>