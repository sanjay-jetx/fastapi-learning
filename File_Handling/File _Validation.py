from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/File-Validation")
async def File_Validation(file: UploadFile = File(...)):

    if file.content_type != "image/png":
        return {"error": "Only PNG files allowed"}

    content = await file.read()

    return {
        "filename": file.filename,
        "type": file.content_type,
        "size": len(content)
    }