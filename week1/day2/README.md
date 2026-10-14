# Day 2 — System Message & Temperature in LLMs

Aaj Day 2 mein maine seekha ki LLM (Large Language Model) ke responses ko **System Message aur Temperature** ki help se kaise customize kar sakte hain. Saath hi, Groq API aur Python ka use karke in concepts ko practically implement karna bhi seekha.

## 1. Understanding Message Roles

LLM ke saath conversation karte time messages ke saath unka role bhi define kiya jaata hai.

Mainly 3 roles use kiye jaate hain:

| Role | Meaning |
|---|---|
| `system` | AI ko instructions dena aur uska behaviour guide karna |
| `user` | User ki taraf se question ya input |
| `assistant` | AI ki taraf se generated response |

**Example:**

- `system`: You are a helpful coding teacher.
- `user`: Explain Python loops.
- `assistant`: Python loops allow us to repeat a block of code.

Yahan System Message AI ko coding teacher ki tarah answer dene ke liye guide karta hai.

## 2. What is a System Message?

System Message ek instruction hota hai jo AI ko batata hai ki use kis role mein kaam karna hai, kis tarah behave karna hai aur response kis style mein dena hai.

### Example 1: Girlfriend Role

```python
messages = [
    {
        "role": "system",
        "content": "You are my loving girlfriend."
    },
    {
        "role": "user",
        "content": "I love you, baby!"
    }
]
```

Is example mein AI ko loving aur caring style mein reply dene ke liye instruct kiya gaya hai.

### Example 2: Office Colleague Role

```python
messages = [
    {
        "role": "system",
        "content": "You are my strict office manager. "
                   "Maintain professional boundaries."
    },
    {
        "role": "user",
        "content": "I love you, baby!"
    }
]
```

Ab AI ka response professional aur situation ke according ho sakta hai.

**Important:** System Message response ko guide karta hai, lekin exact response ki guarantee nahi deta.

## 3. Real-World Use of System Messages

Companies mein different AI agents ko different responsibilities di ja sakti hain.

| AI Agent | System Message ka example | Main responsibility |
|---|---|---|
| Developer | You are a software developer. | Code likhna aur bugs fix karna |
| Architect | You are a senior system architect. | System design, scalability aur security |
| Tester | You are a QA engineer. | Bugs aur edge cases identify karna |
| Manager | You are a project manager. | Planning aur task coordination |

Agar ek company multiple AI agents use karti hai, toh System Message ki help se unke roles aur instructions alag define kiye ja sakte hain.

Isse har agent ko uske specific task ke according response dene mein help milti hai.

## 4. What is Temperature?

Temperature ek parameter hai jo LLM ke next-token selection mein randomness ko influence karta hai.

Simple words mein, Temperature control karta hai ki model apne possible next words ya tokens mein se kitne predictable ya varied choices kare.

- **Low Temperature:** Responses generally zyada predictable aur consistent hote hain.
- **High Temperature:** Responses mein zyada variety aur randomness aa sakti hai.

Temperature ka matlab AI ki intelligence ya knowledge badhana nahi hai.

### Temperature Examples

| Temperature | General behaviour | Suitable use cases |
|---|---|---|
| `0` | More predictable output | Structured answers, predictable tasks |
| `1` | More variation | General content generation |
| `2` | High randomness, if supported | Experimental creative generation |

Ye simplified examples hain. Actual behaviour model aur API par depend karta hai. Temperature `0` par bhi har model mein perfect determinism guaranteed nahi hota.

**Note:** Temperature ki valid range model-specific hoti hai. Groq ke kai supported models mein range `0` se `2` hoti hai, lekin har model ko `2` support karna zaroori nahi hai.

## 5. System Message vs Temperature

Ye dono concepts alag hain.

| System Message | Temperature |
|---|---|
| AI ko role aur instructions deta hai | Output ki randomness ko influence karta hai |
| Batata hai ki AI ko kaise behave karna chahiye | Batata hai ki output generation kitni varied ho sakti hai |
| Example: You are a senior developer | Example: `temperature=0.7` |
| Response ka context aur style guide karta hai | Possible outputs ki variety influence karta hai |

**Easy way to remember:**

System Message = AI ko kya role aur instructions follow karne hain.

Temperature = AI ka response kitna predictable ya varied ho sakta hai.

## 6. Real-World Use of Temperature

Temperature ko use case ke according adjust kiya ja sakta hai.

### Low Temperature

Jab predictable aur consistent output important ho.

Examples:
- Structured data extraction
- Classification
- Fixed-format responses
- Technical questions jahan consistency important hai

Dhyan rahe: Low Temperature factual accuracy guarantee nahi karta.

### Higher Temperature

Jab different ideas aur creative outputs chahiye hon.

Examples:
- Story writing
- Marketing ideas
- Brand name suggestions
- Creative brainstorming
- Different captions aur taglines generate karna

Agar AI se clothing brand ka naam generate karwana hai, toh higher Temperature se alag-alag naming ideas mil sakte hain.

Lekin high Temperature par irrelevant ya nonsensical suggestions bhi aa sakte hain.

## 7. Understanding LLM Predictions

LLM ko simple terms mein next-token prediction model samajh sakte hain.

Example:

Input:

`Sunday, Monday, ...`

Possible prediction:

`Tuesday`

Model apne learned patterns aur current context ke basis par next token predict karta hai.

Temperature next-token selection ki randomness ko affect karta hai. Low Temperature par high-probability tokens ko zyada preference milti hai, jabki higher Temperature par lower-probability alternatives select hone ki possibility badh sakti hai.

Isi wajah se same prompt se different outputs mil sakte hain.

**Important:** LLM sirf search engine ki tarah stored facts retrieve nahi karta. Ye generated responses mein mistakes ya hallucinations bhi kar sakta hai.

## 8. Practical Implementation Using Python and Groq

Is lesson mein maine Groq API ka use karke System Message aur Temperature ko practically implement karna seekha.

### Step 1: Project Setup

```bash
uv init day2
cd day2
uv venv --python 3.11
source .venv/bin/activate
uv add groq
```

Agar previous day's project se `.env` file copy kar rahe ho, toh usmein apni API key securely configure karo.

### Step 2: Environment Variable

`.env` file mein:

```env
GROQ_API_KEY=your_groq_api_key
```

API key ko GitHub par upload mat karna.

### Step 3: Python Code

`system-temp.py` file mein:

```python
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

model = "your-supported-groq-model"

messages = [
    {
        "role": "system",
        "content": "You are a creative brand naming expert."
    },
    {
        "role": "user",
        "content": "Suggest one unique name for my food brand."
    }
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.7
)

print(response.choices[0].message.content)
```

Agar `python-dotenv` install nahi hai, toh use install karna hoga:

```bash
uv add python-dotenv
```

`your-supported-groq-model` ki jagah apne Groq account par available supported model ka exact ID use karo.

### Step 4: Run the Program

```bash
python3 system-temp.py
```

Expected behaviour: Model ek food brand name suggest karega. Exact output har run mein same hona zaroori nahi hai.

## 9. Experiment with Temperature

Same prompt ko different Temperature values ke saath run karke compare kar sakte hain.

```python
temperature = 0
```

Iske baad try karo:

```python
temperature = 1
```

Aur phir:

```python
temperature = 2
```

Temperature `2` tabhi use karna jab tumhara selected model ise support karta ho.

Observe karo:
- Kya response zyada predictable hai?
- Kya suggestions mein variety aa rahi hai?
- Kya higher Temperature par irrelevant outputs aa rahe hain?

Fair comparison ke liye same model, same prompt aur same System Message rakho. Sirf Temperature change karo.

## 10. Common Errors During Setup

Day 2 mein practical coding karte waqt kuch common errors aa sakte hain.

| Error | Possible reason | Solution |
|---|---|---|
| `ModuleNotFoundError: No module named 'groq'` | Groq package install nahi hai | `uv add groq` |
| `ModuleNotFoundError: No module named 'dotenv'` | `python-dotenv` missing hai | `uv add python-dotenv` |
| API key error | Key missing ya invalid hai | `.env` aur environment variable check karo |
| Invalid temperature | Model requested value support nahi karta | Model ki supported range check karo |
| Model not found | Model ID invalid ya unavailable hai | Current supported model ID use karo |
| Syntax error | Code mein spelling, brackets ya formatting ki problem hai | Error message aur relevant line check karo |

**Debugging tip:** Error aane par panic mat karo. Pehle error message padho, phir command, spelling, file path aur environment check karo.

## 11. Important Interview Questions

### Q1. What is a System Message?

System Message ek instruction hota hai jo LLM ke behaviour, role, response style aur task ko guide karta hai.

### Q2. What is Temperature in an LLM?

Temperature ek sampling parameter hai jo next-token selection ki randomness ko influence karta hai.

### Q3. What is the difference between System Message and Temperature?

System Message model ko instructions deta hai, jabki Temperature generated output ki randomness ko control karne mein help karta hai.

### Q4. Does higher Temperature mean better answers?

Nahi. Higher Temperature se output mein variety badh sakti hai, lekin accuracy ya quality automatically improve nahi hoti.

### Q5. Why do we use different System Messages for different AI agents?

Taaki har agent ko uske specific role aur task ke according instructions mil sakein, jaise Developer, Architect ya Tester.

### Q6. Does Temperature 0 guarantee correct answers?

Nahi. Low Temperature output ko more predictable bana sakta hai, lekin model phir bhi galat information generate kar sakta hai.

### Q7. Can every LLM use Temperature 0 to 2?

Nahi. Supported range model aur API par depend karti hai.

## 12. Quick Revision Notes

- `system` → AI ke role aur instructions ko guide karta hai.
- `user` → User ka input.
- `assistant` → AI ka response.
- `temperature` → Output generation ki randomness ko influence karta hai.
- Low Temperature → Generally more predictable output.
- High Temperature → Generally more varied output.
- System Message aur Temperature ek-doosre ke alternatives nahi hain; dono saath use ho sakte hain.
- LLM generated response galat bhi ho sakta hai.
- API key ko `.env` mein rakho aur GitHub par expose mat karo.
- Har model ki supported parameters aur limits alag ho sakti hain.

## Final Summary

Day 2 mein maine seekha ki LLM ko sirf prompt dena hi enough nahi hai. Uske role aur instructions ko System Message se guide kiya ja sakta hai, aur Temperature se response ki randomness ko influence kiya ja sakta hai.

Python aur Groq API ke through maine in concepts ko implement karna, different outputs observe karna aur common coding errors debug karna seekha.

**Key takeaway:** System Message defines the intended role and instructions; Temperature influences the randomness of generated responses.
