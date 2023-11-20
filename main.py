from fastapi import FastAPI, File, UploadFile
import os 

app = FastAPI()

@app.post("/uploadfile")
async def creat_upload_file(file : UploadFile):
    if not file:
        return {"message": "파일이 존재하지 않음"}
    else:
        file_path = "./imges"
        os.makedirs(file_path)
        path = os.path.join(file_path, file.filename)
        with open(path, 'wb') as f:
            f.write(file.file.read())
        return {"success": "ok"}