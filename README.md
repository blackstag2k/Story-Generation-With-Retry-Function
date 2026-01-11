# Generating a 400 word toddler story with the help of a reference story using **Google Gemini API** and **Python docx** library and saving the output in a **.JSON Folder**

This project is about generating a story for toddlers (3-4 years of age) using the **Google Gemini API** and saving the output in **.JSON File**

## Workflow

```mermaid
flowchart TD
A([Start]) --> B[Initialize Gemini Client]

B --> C[Load DOCX files]
C --> D1[Read Taru story]
C --> D2[Read Reference story]

D1 --> E[Extract text]
D2 --> E

E --> F[Generate Story and Style DNA]
F --> G[Gemini API call]

G -->|Retry on failure| F
G --> H[Structured Story DNA]

H --> I[Generate Final Story]
I --> J[Gemini API call]

J -->|Retry on failure| I
J --> K[Story plus Critique plus Rewrite]

K --> L[Create JSON Output]
L --> M[Write taru_apple_puppy.json]
M --> N([End])
```

## Steps to Run the Code

1. Cloning the repository:

git clone: https://github.com/blackstag2k/Story-Generation-With-Retry-Function.git

2. Installing the Dependencies for the project:

* dependencies listed in the requirements.txt

pip install -r requirements.txt 

* If you want to execute the installed pip module instead of a script file, then use the command below in Command Window

pip -m install -r requirements.txt

### Example:

- python -m pip install google-generativeai

3. Add your API Key 

* Google AI API, Open AI API, etc. generated from any platform. Google GenAI key is used here. I have hardcoded the API key. However, I won't recommend hardcoding, rather you can save it as an environment variable. 

export GOOGLE_API_KEY="YOUR_KEY"

4. Run

python main.py

**Output**

Output JSON:
## 🧠 LLM Story Control System

This table demonstrates how a **structured prompt (Story + Style DNA)** is transformed into a **controlled narrative output** by an LLM.

| **Prompt Seed (Story + Style DNA)** | **LLM Output (Generated Story)** |
|-----------------------------------|----------------------------------|
| **Core Theme**  <br> Small acts of sharing foster community connection and amplify joy.  <br><br> **Emotional Arc**  <br> Wonder → Worry → Hope → Surprise → Choice → Warm Joy  <br><br> **Protagonist**  <br> Taru (4 years old)  <br><br> **Setting**  <br> Himalayan mountain village with stone-paved lanes, terraced fields, pine scent, chai steam, and goat bells  <br><br> **Genre**  <br> Community story + lost-and-found tale  <br><br> **Conflict**  <br> Taru wants her shiny apple back but a hungry baby goat needs it  <br><br> **Tone & Style**  <br> Joyful, warm, emotionally expressive, rhythmic, repetition-driven, emoji-assisted | **Taru’s Shiny Apple**  <br><br> Taru, 4 years old, skipped down the stone lane, holding her shiny red apple. “Zoom! Zoom! 🍎” she sang. It was *so* red! So shiny! She loved it, loved it, loved it! The scent of fresh pine needles danced in the air, and far-off goat bells went *ting-a-ling!* This apple was going to be the *best*!  <br><br> Oops! 😱 The shiny red apple slipped! It rolled! Down the terraced path it tumbled, past green growing things, right into a patch of sunshine. “My apple! My apple!” Taru’s happy bounce turned into a tiny worry-wiggle. “Oh no!”  <br><br> She tiptoed closer, hope peeking in her eyes. There it was! But wait! A tiny baby goat, all fluffy white, was nibbling her apple! “Baa-baa-baa!” cried the goat, looking so, so hungry. Taru’s heart felt a little tug. She wanted her apple back. It was *hers*! 🥺 But the baby goat’s eyes were big and sad, and its little nose twitched.  <br><br> Mama appeared, a warm mug of chai in her hands. “What troubles you, my little sunbeam?” she asked, her voice soft and comforting. Taru pointed. “My apple… but the goat is hungry, Mama!” Mama knelt, giving Taru a warm squeeze. “Sometimes, sharing makes everything bloom,” she whispered. “It makes your heart glow with warmth.”  <br><br> Taru looked at her apple, then at the baby goat’s wobbly legs. Sharing… “Okay!” she decided, a brave, warm feeling bubbling in her chest. She carefully broke the apple in half, offering a piece to the goat. “Here you go, baa-baa! For you!”  <br><br> “Baa!” said the goat, munching happily! Mama smiled, a wide, joyful smile. Other villagers walking by saw. “A hungry goat!” Uncle Pemba brought a handful of fresh greens. Auntie Dawa shared a piece of flatbread. Soon, everyone was sharing! More goats came, more happy giggles! 🎉 Taru felt her heart burst with warm joy. “Sharing is fun! Sharing is *so* fun!” she beamed, snuggling into Mama’s side. The whole stone lane felt sparkly and warm, like sunshine in a hug. |

## Tools Used

- Google AI API (Gemini)
- Python 3.14

## Lessons to be Learned

- Using two different docuement files, one of the Taru story and the other as a reference file of the Big Blue Friendship Train through the *Python docx* library.
- Learning how to use *retry* process and understanding the usage of *MAX_RETRIES*, *except*, and *RETRY_DELAY*.
- Using prompt engineering basics to seperate system and user prompts. The former stays the same and the latter variable or dynamic.
- Executing the code through a virtual environment (.venv) like VS Code.
- Prompt chaining to execute a prompt (system and user prompt) and get the best results.


Documented during the Prompt Engineering Course for Prompt Chaining and Content Generation










