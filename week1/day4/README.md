# Day 5 — Structured Output, JSON & Pydantic

## 1. Today's Learning Goals

Aaj ke lecture mein humne seekha:

- Structured Output kya hota hai aur kyun zaroori hai.
- Unstructured text aur structured data mein difference.
- JSON (JavaScript Object Notation).
- Pydantic aur `BaseModel`.
- Schema kya hota hai.
- LLM se fixed format mein output kaise lena hai.
- JSON data ko Python object mein kaise convert karte hain.
- Customer Ticket Extraction System.
- Resume Parser AI Agent ka mini-project idea.

---

## 2. The Problem: Normal LLM Output

Abhi tak hum LLM ko prompt dete the aur uska response print kar dete the.

Example:

**Prompt:**

```text
Extract the name, email, and issue from this customer complaint.
```

**LLM Response:**

```text
Sure! Here is the extracted information.

The customer's name is Rahul.
His email is rahul@example.com.
His issue is that his iPhone is not working.
```

Insaan is response ko easily samajh sakta hai. Lekin agar is response ko koi doosra program consume kare, toh problem ho sakti hai.

Program ko sirf ye chahiye:

- Name
- Email
- Issue

Lekin LLM extra sentences, headings, formatting ya unexpected information bhi return kar sakta hai.

Is text se exact values extract karne ke liye additional parsing logic likhna pad sakta hai.

### Solution: Structured Output

LLM se output ek predefined format mein lena, jisse doosra program usse easily access kar sake.

---

## 3. Structured vs Unstructured Output

### Unstructured Output

```text
The customer is Rahul. His email is
rahul@example.com and his iPhone is not working.
```

Problems:
- Information fixed format mein nahi hai.
- Extra text aa sakta hai.
- Parsing complicated ho sakti hai.
- Output format badalne par code break ho sakta hai.

### Structured Output

```json
{
  "name": "Rahul",
  "email": "rahul@example.com",
  "issue": "iPhone not working"
}
```

Benefits:
- Har value ka ek fixed key hai.
- Data access karna easy hai.
- Doosre programs ke saath integration simple hota hai.
- Validation aur automation mein help milti hai.

**Remember:** Structured output ka main purpose LLM ke response ko predictable aur machine-readable banana hai.

---

## 4. What Is JSON?

JSON stands for **JavaScript Object Notation**.

It is a lightweight data-interchange format used to store and exchange structured data between applications.

JSON JavaScript se inspired hai, lekin sirf JavaScript tak limited nahi hai. Python, Java, C++, JavaScript aur bahut si languages JSON data ke saath kaam kar sakti hain.

### Example

```json
{
  "name": "Rahul",
  "email": "rahul@example.com",
  "phone": 9876543210,
  "issue": "iPhone not working"
}
```

### Important JSON Rules

1. Objects `{}` ke andar define hote hain.
2. Data `key: value` format mein hota hai.
3. Keys double quotes mein honi chahiye.
4. String values double quotes mein hoti hain.
5. Key-value pairs ke beech comma hota hai.
6. Last property ke baad trailing comma nahi lagate.
7. JSON mein comments allowed nahi hote.

### Common JSON Data Types

| Type | Example |
|---|---|
| String | `"name": "Rahul"` |
| Number | `"age": 22` |
| Boolean | `"active": true` |
| Null | `"address": null` |
| Array | `"skills": ["Python", "C++"]` |
| Object | `"user": {"name": "Rahul"}` |

### Why JSON?

Agar kisi program ko customer ka email chahiye, toh structured JSON mein woh direct key se access kar sakta hai:

```python
customer["email"]
```

Isse poore paragraph mein email search karne ki zaroorat nahi hoti.

---

## 5. What Is Structured Output in LLMs?

Structured output ka matlab hai LLM ke response ko predefined structure ke according return karwana.

For example, hum chahte hain ki har customer ticket mein sirf ye fields hon:

```json
{
  "name": "Rahul",
  "email": "rahul@example.com",
  "issue": "iPhone not working"
}
```

Agar customer complaint mein address, age aur family details bhi hain, lekin humne schema mein un fields ko define nahi kiya, toh woh required output ka part nahi honge.

**Important:** Sirf prompt mein JSON maangne se har API aur model par perfect schema compliance guarantee nahi hoti. Reliable applications mein supported structured-output features aur validation use karna chahiye.

---

## 6. What Is Pydantic?

Pydantic ek Python library hai jo data ko predefined rules ke according validate aur structure karne mein help karti hai.

LLM applications mein hum Pydantic ka use karke define kar sakte hain:

- Kaun se fields required hain.
- Har field ka expected data type kya hai.
- Data valid hai ya nahi.
- Data ko Python object ke form mein kaise represent karna hai.

### Installation

Agar project mein `uv` use kar rahe ho:

```bash
uv add pydantic
```

Agar normal pip use kar rahe ho:

```bash
pip install pydantic
```

### Basic Example

```python
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    email: str
    issue: str
```

Yahan:

- `Ticket` ek Python class hai.
- `BaseModel` Pydantic se aata hai.
- `name: str` ka matlab name string hona chahiye.
- `email: str` ka matlab email field string hai.
- `issue: str` ka matlab issue string hai.

Ye class humare data ka structure define karti hai.

---

## 7. What Is a Schema?

Schema data ka blueprint ya framework hota hai. Ye define karta hai ki data ka structure kaisa hona chahiye.

Example:

```python
class Ticket(BaseModel):
    name: str
    email: str
    issue: str
```

Is class se pata chalta hai ki Ticket mein `name`, `email` aur `issue` fields expected hain.

### Real-Life Analogy

Socho college admission form mein ye fields required hain:

- Name
- Email
- Roll Number

Form ka structure schema ki tarah kaam karta hai. Student extra information likh sakta hai, lekin required fields ka structure predefined hai.

### Schema vs Data

**Schema:**

```text
name: string
email: string
issue: string
```

**Actual Data:**

```json
{
  "name": "Rahul",
  "email": "rahul@example.com",
  "issue": "iPhone not working"
}
```

Schema batata hai ki data kaisa hona chahiye; data actual values contain karta hai.

---

## 8. Required Fields and Data Validation

Pydantic model mein fields ko type annotations ke saath define karte hain.

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
```

Valid example:

```python
student = Student(name="Rahul", age=22)

print(student.name)
print(student.age)
```

Output:

```text
Rahul
22
```

Invalid example:

```python
student = Student(name="Rahul")
```

Ismein `age` missing hai, isliye Pydantic validation error raise karega.

**Important:** Pydantic kuch compatible input types ko convert bhi kar sakta hai. Agar strict type checking chahiye, toh strict validation configure karni pad sakti hai.

---

## 9. Pydantic Model to JSON Schema

Pydantic model se JSON Schema generate kar sakte hain.

```python
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema = Ticket.model_json_schema()

print(schema)
```

`model_json_schema()` ek schema dictionary return karta hai jo model ki expected fields aur types describe karta hai.

Ye schema compatible LLM APIs ko output structure batane mein useful ho sakta hai.

**Quick Revision:**

- `BaseModel` → data model banane ke liye.
- `Ticket` → apna custom model.
- `model_json_schema()` → model ka JSON Schema generate karne ke liye.

---

## 10. System Prompt vs User Prompt

LLM applications mein different message roles hote hain.

### System Message

Model ko instructions, behaviour aur task rules batata hai.

Example:

```python
system_prompt = """
You are a customer support assistant.
Extract the customer's name, email, and issue.
Return the information as JSON matching the required schema.
"""
```

### User Message

Actual input ya task data provide karta hai.

Example:

```python
user_prompt = """
My name is Rahul.
My email is rahul@example.com.
My iPhone is not working.
"""
```

### Difference

| System Prompt | User Prompt |
|---|---|
| Behaviour aur rules define karta hai | Actual task/input deta hai |
| Expected response guide karta hai | Customer complaint contain karta hai |
| Instructions provide karta hai | Data provide karta hai |

---

## 11. Customer Ticket Extraction — Complete Concept

Suppose customer ne email bheja:

```text
Hello, my name is Rahul.
My email is rahul@example.com.
I purchased an iPhone, but it stopped working.
My address is Delhi.
```

Humara program sirf name, email aur issue chahta hai.

### Step 1: Define the Schema

```python
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    email: str
    issue: str
```

### Step 2: Send Instructions to the LLM

Model ko clearly batana hai ki complaint se required information extract karo aur expected structure follow karo.

### Step 3: Receive Structured Data

Agar model/API supported structured-output mode mein response deta hai, toh result expected schema ke according ho sakta hai.

Example:

```json
{
  "name": "Rahul",
  "email": "rahul@example.com",
  "issue": "iPhone stopped working"
}
```

### Step 4: Parse the JSON

```python
import json

raw_json = """
{
  "name": "Rahul",
  "email": "rahul@example.com",
  "issue": "iPhone stopped working"
}
"""

data = json.loads(raw_json)

print(data["name"])
print(data["email"])
print(data["issue"])
```

Output:

```text
Rahul
rahul@example.com
iPhone stopped working
```

### Step 5: Validate Using Pydantic

```python
ticket = Ticket.model_validate(data)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
```

Ab data Python object ke form mein available hai.

**Important difference:** `json.loads()` JSON text ko Python data mein convert karta hai. `Ticket.model_validate()` us data ko Pydantic model ke against validate karta hai.

---

## 12. JSON vs Python Dictionary

Dono similar dikh sakte hain, lekin same cheez nahi hain.

### JSON

```json
{
  "name": "Rahul",
  "age": 22
}
```

JSON ek data format hai.

### Python Dictionary

```python
student = {
    "name": "Rahul",
    "age": 22
}
```

Dictionary Python ka built-in data structure hai.

### Conversion

**JSON string to Python dictionary:**

```python
import json

raw_json = '{"name": "Rahul", "age": 22}'

student = json.loads(raw_json)

print(student["name"])
```

**Python dictionary to JSON string:**

```python
json_string = json.dumps(student)

print(json_string)
```

Remember:

- `json.loads()` → JSON string to Python object.
- `json.dumps()` → Python object to JSON string.
- `model_validate()` → Python data ko Pydantic model ke against validate karta hai.

---

## 13. LLM Structured Output: API Integration

Lecture mein Groq API, Pydantic aur response format ka concept cover hua.

High-level flow:

```text
Customer Complaint
        ↓
System Prompt + User Prompt
        ↓
LLM API
        ↓
Structured JSON Response
        ↓
JSON Parsing / Pydantic Validation
        ↓
Python Object
        ↓
Application Logic
```

Groq setup ke liye example installation:

```bash
uv add groq pydantic python-dotenv
```

API key ko `.env` file mein rakh sakte ho:

```env
GROQ_API_KEY=your_api_key_here
```

API key ko GitHub par commit mat karna.

**API integration note:** Lecture ka main concept `response_format` ke through JSON output request karna hai. Exact parameters aur Pydantic integration installed SDK aur selected model par depend karte hain. Agar API JSON Schema support karti hai, toh supported schema mode use karo. Agar sirf JSON-object mode available hai, toh output JSON hone ki request ki ja sakti hai, lekin har schema rule automatically enforce hona guaranteed nahi hai. Hamesha final output validate karo.

---

## 14. Why Is Pydantic Useful for AI Agents?

Real-world AI agents ka output aksar kisi doosre function, API, database ya software system ko use karna hota hai.

Examples:

- Customer complaint classification.
- Resume parsing.
- Invoice data extraction.
- Product recommendation systems.
- Lead qualification.
- Document processing.
- Automated support ticket creation.

Agar output predictable format mein hoga, toh downstream code ko data consume karna easier hoga.

Example:

```python
if ticket.issue:
    print("Ticket can be processed")
```

Production systems mein sirf field present hone par depend nahi karna chahiye. Data ko validate karna, missing values handle karna aur invalid output par error handling bhi zaroori hai.

---

## 15. Mini Project: AI Resume Parser

Lecture ka homework ek resume parser banana hai.

### Problem Statement

HR ek resume aur job description provide karegi. Program ko resume se relevant information extract karke job requirements se compare karna hai.

### Input

1. Resume — PDF ya Word document.
2. Job description — required skills, experience, projects aur qualifications.

### Information to Extract

- Candidate name.
- Skills.
- Work experience.
- Projects.
- Relevant qualifications.

### Example Output

```json
{
  "candidate_name": "Rahul Sharma",
  "skills": ["Python", "C++", "JavaScript"],
  "experience_years": 1,
  "relevant_projects": ["Machine Learning Project"],
  "missing_skills": ["Java"],
  "match_percentage": 70
}
```

Ye sirf illustrative output hai; actual match percentage calculate karne ke liye defined scoring rules chahiye.

### Recommended Workflow

1. Resume file read karo.
2. PDF ya DOCX se text extract karo.
3. Job description read karo.
4. Pydantic model mein output fields define karo.
5. LLM se resume information extract karwao.
6. Output ko JSON format mein lo.
7. Pydantic se validate karo.
8. Extracted skills aur experience ko job requirements se compare karo.
9. Defined scoring logic se match score calculate karo.
10. HR ko structured report return karo.

**Important:** LLM ka generated match percentage blindly accept mat karna. Better hai skills, experience aur projects ke liye explicit scoring criteria define karna. Resume mein information missing ho toh guess karne ke bajay missing mark karna chahiye.

---

# Quick Revision — 2 Minutes

| Concept | Meaning |
|---|---|
| Structured Output | Predefined format mein data |
| Unstructured Output | Free-form text ya paragraph |
| JSON | Data exchange format |
| Schema | Expected data structure ka blueprint |
| Pydantic | Python data validation library |
| `BaseModel` | Pydantic model define karne ka base class |
| `model_json_schema()` | JSON Schema generate karta hai |
| `json.loads()` | JSON string ko Python object mein convert karta hai |
| `json.dumps()` | Python object ko JSON string mein convert karta hai |
| `model_validate()` | Data ko Pydantic model ke against validate karta hai |
| System Prompt | Model ko instructions aur behaviour batata hai |
| User Prompt | Actual input ya task deta hai |

## Remember This Flow

**Define Schema → Prompt LLM → Request Structured Output → Parse JSON → Validate with Pydantic → Use Data**

---

# Interview Questions with Answers and Explanations

## Q1. What is structured output in an LLM?

**Answer:** Structured output means asking an LLM to return information in a predefined format, such as JSON, with specific fields and expected types.

**Explanation:** Agar application ko name, email aur issue chahiye, toh paragraph ke bajay fixed keys wala JSON useful hota hai. Isse downstream code data ko easily access kar sakta hai.

---

## Q2. Why is unstructured LLM output a problem in production?

**Answer:** Unstructured output may contain unexpected text, inconsistent formatting or missing information, making it harder for software to parse and process reliably.

**Explanation:** Agar response kabhi `Name: Rahul` aur kabhi `The customer's name is Rahul` aaye, toh simple string parsing unreliable ho sakti hai. Structured output aur validation is problem ko reduce karte hain.

---

## Q3. What is JSON, and why is it used?

**Answer:** JSON stands for JavaScript Object Notation. It is a lightweight, language-independent data format used to exchange structured information.

**Explanation:** Python application JSON ko read kar sakti hai aur JavaScript application bhi. Isliye APIs aur software systems ke beech data exchange mein JSON widely used hai.

---

## Q4. What is the difference between JSON and a Python dictionary?

**Answer:** JSON is a data format, whereas a Python dictionary is a built-in Python data structure.

**Explanation:** JSON ko text ke form mein transmit ya store kiya ja sakta hai. Python dictionary ko program directly use karta hai. `json.loads()` JSON text ko Python object mein convert karta hai.

---

## Q5. What is Pydantic?

**Answer:** Pydantic is a Python library used to validate and structure data using Python type annotations and models.

**Explanation:** Hum `name: str` aur `age: int` define karke expected data structure specify kar sakte hain. Pydantic input ko validate karta hai aur invalid data par validation errors raise kar sakta hai.

---

## Q6. What is `BaseModel` in Pydantic?

**Answer:** `BaseModel` is the base class used to define Pydantic data models.

**Example:**

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

**Explanation:** `User` model batata hai ki user object mein `name` aur `age` fields expected hain. Pydantic model instance banate waqt data validate karta hai.

---

## Q7. What is a schema?

**Answer:** A schema defines the expected structure, fields and constraints of data.

**Explanation:** Schema ek blueprint ki tarah hai. Customer ticket schema mein `name`, `email` aur `issue` required ho sakte hain. Isse application ko pata hota hai ki kaun sa data expected hai.

---

## Q8. What is the difference between a schema and actual data?

**Answer:** A schema defines what the data should look like, whereas actual data contains the real values.

**Example:**

Schema fields: `name`, `email`, `issue`.

Actual data: `name = "Rahul"`, `email = "rahul@example.com"`, `issue = "Phone not working"`.

**Explanation:** Schema rules define karta hai; actual data un rules ke according values provide karta hai.

---

## Q9. What is the difference between a system prompt and a user prompt?

**Answer:** A system prompt provides instructions and behaviour guidelines, while a user prompt provides the actual task or input.

**Explanation:** System prompt keh sakta hai, “Extract customer information as JSON.” User prompt actual customer complaint provide karta hai.

---

## Q10. What does `json.loads()` do?

**Answer:** `json.loads()` converts a valid JSON string into a corresponding Python object, commonly a dictionary or list.

**Example:**

```python
import json

data = json.loads('{"name": "Rahul"}')
print(data["name"])
```

**Output:**

```text
Rahul
```

**Explanation:** JSON text ko Python mein directly dictionary ki tarah access karne se pehle parse karna hota hai.

---

## Q11. What does `json.dumps()` do?

**Answer:** `json.dumps()` converts a Python object into a JSON-formatted string.

**Example:**

```python
import json

data = {"name": "Rahul"}
result = json.dumps(data)

print(result)
```

**Explanation:** `loads` aur `dumps` ka direction opposite hai. `loads` JSON text ko parse karta hai; `dumps` Python data ko JSON text banata hai.

---

## Q12. What is the purpose of `model_validate()`?

**Answer:** `model_validate()` validates input data against a Pydantic model and returns a model instance if validation succeeds.

**Example:**

```python
ticket = Ticket.model_validate({
    "name": "Rahul",
    "email": "rahul@example.com",
    "issue": "Phone not working"
})
```

**Explanation:** Iske baad values ko `ticket.name` aur `ticket.issue` se access kar sakte hain. Invalid ya missing required data par validation error aa sakta hai.

---

## Q13. Does asking an LLM to return JSON guarantee valid output?

**Answer:** No. A prompt that requests JSON does not by itself guarantee valid JSON or compliance with every schema rule.

**Explanation:** Reliable systems mein supported structured-output API features, JSON parsing, Pydantic validation aur error handling use karni chahiye. API ke supported mode ko check karna important hai.

---

## Q14. How can you generate a JSON Schema from a Pydantic model?

**Answer:** Use the `model_json_schema()` method.

```python
schema = Ticket.model_json_schema()
```

**Explanation:** Ye model ke fields aur types describe karne wala schema dictionary return karta hai. Compatible APIs is schema ko structured-output constraints ke liye use kar sakti hain.

---

## Q15. What happens if a required Pydantic field is missing?

**Answer:** Pydantic normally raises a validation error when a required field is missing.

**Explanation:** Agar model mein `name: str` required hai aur input mein name nahi hai, toh valid model instance nahi banega. Optional fields ko alag se define kiya ja sakta hai.

---

## Q16. How would you build a customer complaint extraction system?

**Answer:** I would define a Pydantic model for the required fields, send the complaint to an LLM using appropriate instructions and structured-output support, validate the returned data, and pass the validated result to the application.

**Explanation:** Is approach mein data extraction, formatting aur validation separate steps hain. Isse unpredictable output ko downstream code tak pahunchne se pehle detect kiya ja sakta hai.

---

## Q17. How would you build an AI resume parser?

**Answer:** I would extract text from the resume, define a schema for skills, experience and projects, use an LLM to extract relevant information, validate the result with Pydantic, and compare the extracted information with job requirements using explicit scoring rules.

**Explanation:** LLM extraction mein help karta hai, Pydantic data validate karta hai aur scoring logic requirements ke saath comparison karta hai. Missing information ko fabricate nahi karna chahiye.

---

## Q18. Why should an application validate LLM output before using it?

**Answer:** Validation helps detect missing fields, incorrect data types and malformed or unexpected values before the application uses them.

**Explanation:** LLM output ko automatically trustworthy nahi maana ja sakta. Validation errors ko handle karne se unreliable data ka risk reduce hota hai.

---

## Q19. Is JSON the only way to create structured output?

**Answer:** No. JSON is one popular format. Other formats and structured representations can also be used depending on the application and API.

**Explanation:** JSON widely supported hai aur easy to read hai, lekin systems CSV, XML, protocol buffers ya other typed formats bhi use kar sakte hain.

---

## Q20. What is the difference between parsing and validation?

**Answer:** Parsing converts data from one representation into another, while validation checks whether the data satisfies specified rules.

**Explanation:** `json.loads()` JSON text ko Python object mein parse karta hai. `Ticket.model_validate()` check karta hai ki Python data expected Ticket model ko satisfy karta hai ya nahi. Dono alag steps hain.

---

# Final Interview Summary

Agar interviewer poochhe ki aaj ke lecture mein kya seekha, toh answer:

"Today, I learned how to make LLM responses more reliable for software applications using structured output. I understood JSON, schemas, Pydantic models, and data validation. I also learned how JSON can be parsed into Python objects and how structured extraction can be used in practical applications such as customer support ticket processing and AI resume parsing."

**Day 5 ka core concept:** LLM se sirf answer generate karwana enough nahi hai. Production application mein output ko predictable format mein lena, validate karna aur phir use karna bhi zaroori hai.
