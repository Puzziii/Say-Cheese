import anthropic
import base64
import os
import json

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
def analyze_scene(image_bytes, media_type):
    image_b64 = base64.standard_b64encode(image_bytes).decode("utf-8")
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=500,
        system="""You are a scene analysis AI. Look at the image and identify 
        the background environment. Respond ONLY with valid JSON, no markdown:
        {
          "scene": "brief scene name e.g. Beach at sunset",
          "scene_type": "one of: beach, cafe, mountain, urban, indoor, forest, rooftop, other",
          "lighting": "one of: golden_hour, bright_daylight, overcast, indoor_warm, indoor_cool, night",
          "mood": "2-3 word vibe e.g. relaxed and warm",
          "scene_emoji": "single relevant emoji"
        }""",
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": media_type,
                        "data": image_b64
                    }
                },
                {"type": "text", "text": "Analyze the background scene in this photo."}
            ]
        }]
    )
    raw = response.content[0].text.strip()
    return json.loads(raw)

def suggest_poses(scene_data):
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1500,
        system="""You are an expert photography pose director. 
        Given a scene description, suggest 3 natural poses that fit the environment.
        Respond ONLY with valid JSON, no markdown:
        {
          "poses": [
            {
              "name": "Pose name",
              "vibe": ["tag1", "tag2"],
              "description": "One sentence describing the pose",
              "steps": [
                "Step 1 instruction",
                "Step 2 instruction",
                "Step 3 instruction",
                "Step 4 instruction"
              ]
            }
          ]
        }""",
        messages=[{
            "role": "user",
            "content": f"""Suggest poses for this scene:
Scene: {scene_data['scene']}
Type: {scene_data['scene_type']}
Lighting: {scene_data['lighting']}
Mood: {scene_data['mood']}"""
        }]
    )
    raw = response.content[0].text.strip()
    return json.loads(raw)