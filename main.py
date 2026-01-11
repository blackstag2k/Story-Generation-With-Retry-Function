import google.genai as genai
import json
import time
from pathlib import Path
from docx import Document

client = genai.Client(api_key="ENTER_API_KEY")

DOCUMENT_1 = Path(r"C:\Users\Bhaskar Rana\OneDrive\Desktop\little_taru_and_the_puppy_friend.docx")
DOCUMENT_2 = Path(r"C:\Users\Bhaskar Rana\OneDrive\Desktop\a_big_blue_friendship_train.docx")

MAX_RETRIES = 3
RETRY_DELAY = 5

def read_doc_text(file_path: Path):
    doc = Document(file_path)
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    return"\n".join(paragraphs)

def generate_story_content(reference_story, taru_story):    
    prompt_1 = f"""You are a professional narrative engineer.

SOURCE STORY:
{taru_story}

REFERENCE STYLE STORY:
{reference_story}

Extract a Story DNA object with:
- core_theme
- emotional_arc
- protagonist_age
- setting
- genre
- conflict_type
- resolution_style

Extract Style DNA from the reference:
- tone
- rhythm
- repetition
- dialogue_style
- emotional_pacing
- warmth_level"""
    for attempt in range(1, MAX_RETRIES +1):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_1
                )
            
            return response.text
        
        except Exception as e:
            time.sleep(RETRY_DELAY)
            print(
                f"taru_story is not generated: {attempt}/{MAX_RETRIES}"
                f"error: {e}"
            )

    return None

def generate_final_story(story_dna):
    prompt_2 = f"""You are a children's book author.

Using ONLY this Story DNA:
{story_dna}

Write a completely original children's story.

Rules:
- Max 400 words
- Must follow the theme, age, emotion, and setting
- Must follow the Style DNA
- Must not copy wording or scenes from the reference

After writing the story:
1. Critique it (emotion, clarity, rhythm, payoff)
2. Rewrite it once to produce the final gold-standard version"""
    for attempt in range(1, MAX_RETRIES +1):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_2
                )
            
            return response.text
        
        except Exception as e:
            time.sleep(RETRY_DELAY)
            print(
                f"Final story is not generated: {attempt}/{MAX_RETRIES}"
                f"error: {e}"
            )

    return None

output = []

taru_story = read_doc_text(DOCUMENT_1)
reference_story = read_doc_text(DOCUMENT_2)

story_dna = generate_story_content(reference_story, taru_story)

if not story_dna:
    raise RuntimeError("Story DNA generation failed")

final_story = generate_final_story(story_dna)

output.append(
    {
    "story_content": story_dna,
    "final_story": final_story
    }
    )

with open("taru_apple_puppy.json", "w", encoding="utf-8")as f:
    json.dump(output, f, ensure_ascii=False, indent=4)

print(f"The taru_apple_puppy.json is generated")
