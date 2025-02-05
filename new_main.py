from story_generation import create_story_agent, format_json_agent
from image_prompt_generation import process_json2
from imagetopanel import convert_to_panel
from pagestopdf import convert_to_pdf
import json
input_text='''Make a comic on photosynthesis
Definition: Photosynthesis is the process by which plants make their own food using sunlight, water, and air.
Process: Plants take in sunlight, water from the soil, and a gas called carbon dioxide from the air. They use these to make food and release oxygen, which we breathe.
Equation:
Sunlight + Water + Air (Carbon Dioxide) → Food (Glucose) + Oxygen
Examples: Trees, grass, and flowers make their own food using photosynthesis.
'''

story_text=create_story_agent(input_text)
json_output=format_json_agent(story_text)
with open("generated_story.json", "w") as file:
    json.dump(json_output, file, indent=4) 
image_gen=process_json2(json_output)
convert_to_panel(json_output)
convert_to_pdf()


