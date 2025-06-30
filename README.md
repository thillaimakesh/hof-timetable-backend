# 📅 HOF Timetable Alexa Skill – Flask Backend

This is the backend service for an Alexa skill that provides timetable information for students based on **department**, **date**, and **time** using `.ics` calendar files hosted on PRIMUSS.

---

## 🚀 Features

- Supports multiple departments with unique `.ics` URLs
- Filters classes by specific date and time (optional)
- Returns clean JSON output for Alexa integration
- Provides default fallback if no department is specified

---

## 🧪 API Endpoint

```
GET /timetable?date=YYYY-MM-DD&department=DepartmentName&time=HH:MM
```

### 🔁 Example:
```
/timetable?date=2025-07-01&department=Software Engineering&time=10:00
```

---

## 🗂 Departments & URLs

| Department              | Type |
|-------------------------|------|
| Software Engineering    | `type=4` |
| Operational Excellence  | `type=1&typeid=5` |
| Artificial Intelligence | `type=1&typeid=251` |

---

## 📄 Sample JSON Response

```json
{
  "department": "Software Engineering",
  "date": "2025-07-01",
  "entries": [
    {
      "title": "Data Mining",
      "start": "10:00",
      "end": "11:30",
      "location": "Room A302",
      "description": "Dr. Müller"
    }
  ]
}
```

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hof-timetable-backend.git
cd hof-timetable-backend
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Server

```bash
python app.py
```

Runs on:  
`http://127.0.0.1:5000/timetable`

---

## 📦 Requirements

Make sure your `requirements.txt` includes:

```txt
Flask
requests
ics
```

You can generate it with:

```bash
pip freeze > requirements.txt
```

---
