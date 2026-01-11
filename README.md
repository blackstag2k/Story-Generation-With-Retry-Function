# Generating a 400 word toddler story with the help of a reference story using **Google Gemini API** and **Python docx** library and saving the output in a **.JSON Folder**

This project is about generating a story for toddlers (3-4 years of age) using the **Google Gemini API** and saving the output in **.JSON File**

## Workflow

```flowchart TD
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

git clone: https://github.com/blackstag2k/Retry-Blog-Evaluation.git

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
| story_content | final_story |
|------|------|
| # Story DNA & Style DNA
## 🌱 Story DNA

**Core Theme**  
Small acts of sharing foster community connection and amplify joy.

**Emotional Arc**  
Wonder → Worry → Hope → Surprise → Choice → Warm Joy

**Protagonist Age**  
4 years old

**Setting**  
A Himalayan mountain village with stone-paved lanes, terraced fields, and sensory details like pine, chai, and goat bells.

**Genre**  
Community Story + Lost-and-Found Tale

**Conflict Type**  
Internal conflict — Taru’s desire to reclaim a lost item vs. empathy for a hungry creature.

**Resolution Style**  
Empathetic sharing, resolving internal conflict through generosity and community support.

---

## 🎨 Style DNA

**Tone**  
Joyful, enthusiastic, and comforting, with expressive use of emojis to amplify emotion.

**Rhythm**  
Flowing and lively, with a playful, slightly rhythmic cadence achieved through repetition and varied sentence lengths, often accelerating with excitement.

**Repetition**  
Key phrases and sounds (e.g., *“Choo-choo!”*, *“loved it, loved it, loved it”*, *“Sharing is fun!”*) are repeated to emphasize emotion and create a musical quality.

**Dialogue Style**  
Simple, direct, and emotionally expressive.  
Adult dialogue is gently guiding, while children’s dialogue is immediate and reflects their feelings directly.

**Emotional Pacing**  
Quick shifts from initial joy to mild sadness or hesitation, then a rapid and clear resolution to shared happiness and contentment.

**Warmth Level**  
Very high — infused with overt expressions of warmth, comfort, and nurturing through physical touch, gentle guidance, and descriptions of internal emotional warmth.| # Taru’s Shiny Apple

Taru, 4 years old, skipped down the stone lane, holding her shiny red apple.  
"Zoom! Zoom! 🍎" she sang.  
It was *so* red! So shiny!  
She loved it, loved it, loved it!  

The scent of fresh pine needles danced in the air, and far-off goat bells went *ting-a-ling!*  
This apple was going to be the *best*!

---

## 🍎 The Apple Rolls Away

Oops! 😱  
The shiny red apple slipped!  
It rolled!  

Down the terraced path it tumbled, past green growing things, right into a patch of sunshine.

"My apple! My apple!"  
Taru’s happy bounce turned into a tiny worry-wiggle.  
"Oh no!"

---

## 🐐 A Hungry Surprise

She tiptoed closer, hope peeking in her eyes.  
There it was!  

But wait!  
A tiny baby goat, all fluffy white, was nibbling her apple!

"Baa-baa-baa!" cried the goat, looking so, so hungry.

Taru's heart felt a little tug.  
She wanted her apple back.  
It was *hers*! 🥺  

But the baby goat's eyes were big and sad, and its little nose twitched.

---

## ☕ Mama’s Wise Words

Mama appeared, a warm mug of chai in her hands.

"What troubles you, my little sunbeam?" she asked, her voice soft and comforting.

Taru pointed.  
"My apple... but the goat is hungry, Mama!"

Mama knelt, giving Taru a warm squeeze.

"Sometimes, sharing makes everything bloom," she whispered.  
"It makes your heart glow with warmth."

---

## 🍏 A Brave Choice

Taru looked at her apple, then at the baby goat's wobbly legs.

Sharing…

"Okay!" she decided, a brave, warm feeling bubbling in her chest.

She carefully broke the apple in half, offering a piece to the goat.

"Here you go, baa-baa! For you!"

---

## 🎉 Joy Grows

"Baa!" said the goat, munching happily!

Mama smiled, a wide, joyful smile.

Other villagers walking by saw.

"A hungry goat!"  
Uncle Pemba brought a handful of fresh greens.  
Auntie Dawa shared a piece of flatbread.

Soon, everyone was sharing!  
More goats came, more happy giggles! 🎉

Taru felt her heart burst with warm joy.

"Sharing is fun!  
Sharing is *so* fun!" she beamed, snuggling into Mama's side.

The whole stone lane felt sparkly and warm, like sunshine in a hug.|

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







