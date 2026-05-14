from fastapi import APIRouter, UploadFile, File, HTTPException
from services.claude import analyze_scene, suggest_poses
router = APIRouter()
ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp"}
@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Only JPEG, PNG or WebP allowed.")
    
    image_bytes = await file.read()
    
    if len(image_bytes) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Image too large. Max 10MB.")
    scene = analyze_scene(image_bytes, file.content_type)
    poses = suggest_poses(scene)

    return {
        "scene": scene,
        "poses": poses["poses"]
    }