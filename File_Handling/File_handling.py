from fastapi import FastAPI,File,UploadFile,Form
from typing import List

app=FastAPI()

@app.post("/File-Upload")

async def file_upload(file:UploadFile=File(...)):
    content= await file.read()

    try:
        text_p = content.decode("utf-8")[:200]
    except Exception as e:
        text_p= "cannot be preview"
    

    return {
        "filename":file.filename,
        "content_type":file.content_type,
        "size":len(content),

    }


@app.post("/file-upload-multifiles")

async def multi_files(files:List[UploadFile]=File(...)):
    return [file.filename for file in files]




@app.post("/file_upload_own")
async def upload_file(file:UploadFile=File(...)):
    content = await file.read()
    return{
        "filename":file.filename,
        "content":file.content_type,
        "size":len(content)
    }


