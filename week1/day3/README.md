# Day 3 — Understanding Tokens, Tokenization & Token Usage

Aaj Day 3 mein maine seekha ki LLMs (Large Language Models) text ko kaise process karte hain, tokens kya hote hain, tokenization kaise kaam karti hai aur API response mein token usage ko kaise track karte hain.

Maine Groq API aur Python ka use karke multiple prompts run karna, input/output tokens count karna aur `max_tokens` se response length limit karna bhi seekha.

## 1. What are Tokens?

Token text ki ek basic unit hoti hai jise LLM ka tokenizer process karta hai.

Token ho sakta hai:
- Ek complete word
- Kisi word ka ek part
- Punctuation, jaise comma ya full stop
- Space ya text se related koi unit, tokenizer ke according

**Example:**

```text
Input: I am learning AI Engineering
```

Tokenizer is text ko multiple tokens mein divide karega. Exact tokens aur unki count model ke tokenizer par depend karti hai.

Har word ek token nahi hota, aur har token fixed number of characters ka bhi nahi hota.

### Simple analogy

Socho ek food stall par common ingredients ready rakhe jaate hain. Jab customer koi unusual dish order karta hai, toh available ingredients ko combine karke dish banayi ja sakti hai.

Isi tarah, tokenizer text ko chhoti units mein divide karta hai. LLM in token representations ko process karke response generate karta hai.

*Note: Ye sirf concept samajhne ki analogy hai. Actual tokenization ek algorithmic process hai.*

## 2. Why Do We Need Tokens?

Computer text ko human ki tarah directly process nahi karta. LLMs text ko tokenizer ke through token IDs aur phir numerical representations mein convert karke process karte hain.

Agar har possible word ko ek separate ID dene ki koshish karein, toh kai problems aayengi:

- **Vocabulary problem:** Har possible word, name aur newly created word ko cover karna difficult hai.
- **Spelling variations:** Typos aur unusual spellings ke liye bhi handling chahiye.
- **New words:** Brand names, usernames aur custom words dictionary mein available nahi ho sakte.
- **Efficiency:** Text ko manageable units mein represent karna processing ke liye useful hai.

Tokenization in problems ko handle karne mein help karti hai.

## 3. Character-Based vs Word-Based Tokenization

### Character-based approach

Har character ko separate unit maana jaaye.

Example:

```text
HELLO → H + E + L + L + O
```

Is approach mein long text ko process karne ke liye bahut saari units ban sakti hain.

### Word-based approach

Har complete word ko ek unit maana jaaye.

Example:

```text
I love coding → I + love + coding
```

Is approach ki limitation ye hai ki har possible word ko vocabulary mein store karna practical nahi hai.

### Subword tokenization

Modern LLM tokenizers commonly subword-based approaches use karte hain. Words ko complete units ya smaller reusable pieces mein represent kiya ja sakta hai.

Example, sirf illustration ke liye:

```text
programming → program + ming
```

Actual split tokenizer par depend karega.

**Key takeaway:** Subword tokenization vocabulary ko manageable rakhne aur unseen words ke parts ko represent karne mein help karti hai.

## 4. What is Tokenization?

Tokenization ek process hai jisme input text ko tokens mein divide kiya jaata hai.

General flow:

```text
Text Input
    ↓
Tokenizer
    ↓
Tokens
    ↓
Token IDs
    ↓
LLM Processing
    ↓
Generated Output Tokens
    ↓
Decoded Text Response
```

Example:

```text
Input: I love coding!
```

Tokenizer ise multiple tokens mein divide kar sakta hai. LLM un tokens ko process karta hai aur response generate karta hai, jise baad mein readable text mein decode kiya jaata hai.

Token IDs aur internal model representations ek hi cheez nahi hain; token IDs ko model further process karta hai.

## 5. Word Count vs Token Count

Word count aur token count same nahi hote.

Example:

```text
Word 1: cat
Word 2: internationalization
```

Dono ek-ek word hain, lekin tokenizer inhe different numbers of tokens mein represent kar sakta hai.

Token count depend karta hai:
- Language par
- Word ki spelling aur structure par
- Punctuation aur whitespace par
- Selected model aur tokenizer par

Isliye sirf words ya characters count karke exact API token usage calculate nahi kar sakte.

## 6. Why Are Tokens Important in AI Engineering?

Tokens ko samajhna important hai kyunki ye LLM APIs ke cost, context limits aur response generation se directly related hote hain.

### A. API Cost

Kai LLM APIs input aur output tokens ke basis par billing karti hain.

Long prompts aur long responses generally zyada token usage create karte hain.

Actual cost model ki pricing aur input/output token rates par depend karti hai.

### B. Context Window

Model ki context window batati hai ki ek request mein model kitne tokens tak ka context handle kar sakta hai.

Ismein prompt, conversation history aur applicable output budget jaise components count ho sakte hain.

### C. Response Length

Output token limit se generated response ki maximum length restrict ki ja sakti hai.

Agar limit bahut kam hai, toh answer incomplete ho sakta hai.

### D. Performance and Efficiency

Unnecessary prompt content aur excessively long responses ko reduce karne se token usage aur cost optimize karne mein help mil sakti hai.

## 7. Input Tokens, Output Tokens & Total Tokens

API response mein token usage ko generally teen parts mein samajh sakte hain.

| Term | Meaning |
|---|---|
| `prompt_tokens` | Input prompt mein use hue tokens |
| `completion_tokens` | Generated response mein use hue tokens |
| `total_tokens` | Input aur output ka total token usage |

Basic relationship:

```text
Total Tokens = Prompt Tokens + Completion Tokens
```

Example:

```text
Prompt Tokens     = 100
Completion Tokens = 200
Total Tokens      = 300
```

Yahan request ka total usage 300 tokens hai.

Actual billing mein model-specific pricing aur additional token categories, jaise cached tokens, apply ho sakti hain.

## 8. Practical Setup Using Python and Groq

Day 3 mein maine previous day's project structure ko reuse karke ek new project banaya.

### Step 1: Create the project

```bash
uv init day3
cd day3
uv venv --python 3.11
source .venv/bin/activate
uv add groq python-dotenv
```

Agar Groq SDK aur `python-dotenv` pehle se install hain, toh unhe dobara install karne ki zaroorat nahi hai.

### Step 2: Configure the API key

`.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

API key ko public GitHub repository par upload mat karna.

### Step 3: Create the Python file

Transcript mein `token.py` naam ki file se import conflict aaya tha. Isliye file ka naam `tokens.py` ya `token_usage.py` rakho.

`token_usage.py`:

```python
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

model = "your-supported-groq-model"

prompts = [
    "Hi",
    "Explain time travel in detail.",
    "Write an essay about Machine Learning."
]

for prompt in prompts:
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    usage = response.usage

    print("\nPrompt:", prompt)
    print("Response:", response.choices[0].message.content)

    if usage:
        print("Prompt Tokens:", usage.prompt_tokens)
        print("Completion Tokens:", usage.completion_tokens)
        print("Total Tokens:", usage.total_tokens)
```

`your-supported-groq-model` ko apne Groq account mein available model ID se replace karna.

### Step 4: Run the program

```bash
python3 token_usage.py
```

Program har prompt ke liye:
1. API request send karega.
2. AI response receive karega.
3. Prompt tokens print karega.
4. Completion tokens print karega.
5. Total tokens print karega.

Token counts actual model response aur tokenizer par depend karenge.

## 9. Running Multiple Prompts Using a Loop

Agar humein multiple prompts test karne hain, toh har prompt ke liye alag API code likhne ki zaroorat nahi hai.

Python list aur `for` loop use kar sakte hain.

```python
prompts = [
    "Hi",
    "Explain time travel in detail.",
    "Write an essay about Machine Learning."
]

for prompt in prompts:
    print("Processing:", prompt)
```

Is example mein har iteration par `prompt` variable ko list ka next element milta hai.

Isi approach ko API request ke saath combine karne se multiple prompts automatically process ho sakte hain.

**Important:** Har prompt par alag API call karne se multiple requests aur unke associated token costs generate honge.

## 10. Limiting Output with `max_tokens`

Kabhi-kabhi humein AI ka response limited length mein chahiye hota hai.

Iske liye API request mein output token limit set ki ja sakti hai.

Example:

```python
response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=100
)
```

Is setting ka matlab hai ki generated completion ko specified token limit ke andar rakhne ki koshish ki jayegi.

Agar model ko aur response generate karna tha lekin token limit reach ho gayi, toh response beech mein truncate ho sakta hai.

**Note:** Supported parameter names aur limits model/API ke according vary kar sakte hain. Kuch newer APIs mein `max_completion_tokens` jaise parameters bhi use hote hain.

### When should we limit output tokens?

- Short answers generate karne ke liye
- Unnecessarily long responses avoid karne ke liye
- API usage ko control karne ke liye
- Response length ko application requirements ke according restrict karne ke liye

Output limit ko bahut low set karne se useful information cut ho sakti hai.

## 11. Understanding `finish_reason`

API response mein `finish_reason` batata hai ki model ne generation kyun stop ki.

Common examples:

| Finish reason | Meaning |
|---|---|
| `stop` | Model ne normally response complete kiya |
| `length` | Output token limit reach hone ki wajah se generation stop hui |

Example:

```python
choice = response.choices[0]

print("Finish Reason:", choice.finish_reason)
```

Agar `finish_reason` ki value `length` hai, toh check karo ki response incomplete toh nahi hai.

Agar `stop` hai, toh model ne normal stopping condition reach ki. Iska matlab ye nahi ki response factually correct bhi hai.

## 12. Common Errors and Debugging

### Error 1: `ModuleNotFoundError`

Possible reason: Required package install nahi hai ya incorrect Python environment active hai.

Solution:

```bash
uv add groq python-dotenv
```

Ensure karo ki correct virtual environment active hai.

### Error 2: Circular Import

Agar file ka naam `token.py` hai, toh Python ke standard library ke `token` module ke saath naming conflict ho sakta hai.

Solution:

- File ka naam `tokens.py` ya `token_usage.py` rakho.
- Agar purana `token.py` hai, toh use rename karo.
- Agar us file se `__pycache__` create hua hai, toh zaroorat padne par stale cache remove karo.
- Program ko dobara run karo.

### Error 3: API Key Missing

Possible reason: `.env` file load nahi hui ya environment variable missing hai.

Solution:

```python
print(bool(os.getenv("GROQ_API_KEY")))
```

Ye sirf `True` ya `False` print karega, API key expose nahi karega.

### Error 4: Invalid Model or Parameter

Possible reason: Model ID invalid hai ya selected model requested parameter support nahi karta.

Solution: Apne provider ke current model documentation mein model ID aur supported parameters verify karo.

**Debugging lesson:** Har error code ki problem nahi hoti. File naming, imports, environment aur command syntax bhi check karne chahiye.

## 13. Quick Revision Notes

- LLM = Large Language Model.
- Token = Text ki tokenizer-defined unit.
- Tokenization = Text ko tokens mein divide karna.
- Token IDs = Tokens ki numerical representations.
- Word count aur token count different hote hain.
- `prompt_tokens` = Input token usage.
- `completion_tokens` = Output token usage.
- `total_tokens` = Total input aur output tokens.
- `max_tokens` = Supported APIs mein output generation ki limit set karne ke liye parameter.
- `finish_reason="stop"` = Normal stopping condition.
- `finish_reason="length"` = Output limit reach hone ki wajah se stopping.
- Python `for` loop ki help se multiple prompts process kar sakte hain.
- Python files ke naam standard library modules jaise `token.py` nahi rakhne chahiye, jab naming conflict ho sakta ho.
- Token usage se API cost estimate karne mein help milti hai.

## 14. Interview Questions

**Q1. What is a token in an LLM?**

Token text ki ek unit hai jise tokenizer model ke liye processable representation mein convert karta hai.

**Q2. What is tokenization?**

Tokenization input text ko tokens mein divide karne ka process hai.

**Q3. Why don't we use one token for every possible word?**

Kyuki possible words, names, spelling variations aur newly created words ki vocabulary bahut large ho sakti hai. Subword tokenization is problem ko manage karne mein help karti hai.

**Q4. What is the difference between prompt tokens and completion tokens?**

Prompt tokens input request se related hote hain, jabki completion tokens generated response se related hote hain.

**Q5. How do tokens affect API cost?**

Jab API token-based billing use karti hai, toh input aur output token usage ke according cost calculate hoti hai.

**Q6. What does `max_tokens` do?**

Supported APIs mein ye generated completion ki maximum token length limit karne mein help karta hai.

**Q7. What is `finish_reason="length"`?**

Iska matlab generation token-length limit reach hone ki wajah se stop hui. Response incomplete ho sakta hai.

**Q8. Why should we avoid naming a file `token.py`?**

Python standard library ke `token` module ke saath naming conflict ho sakta hai, jisse import errors ya circular import problems aa sakti hain.

## Final Summary

Day 3 mein maine LLM tokenization, input/output token usage, token-based cost estimation aur response length control ke concepts seekhe.

Python aur Groq API ke through maine multiple prompts execute karna, `response.usage` se token statistics access karna, `max_tokens` se output limit karna aur `finish_reason` inspect karna seekha.

**Key takeaway:** LLM application develop karte waqt sirf response generate karna important nahi hai. Token usage, cost, context limits aur response completeness ko track karna bhi AI Engineering ka important part hai.
