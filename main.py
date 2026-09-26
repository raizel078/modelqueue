from fastapi import FastAPI, UploadFile
from pathlib import Path
from function import job_id_maker , detection_video
from database import initialize_database
from ultralytics import YOLO


initialize_database()

model_path = Path('/home/nowa/Desktop/Project/models/yolo11n.pt')
model = YOLO(model_path)

app = FastAPI(title="Trial API V1.0")


@app.post("/files/")
async def upload_file(file: UploadFile):
    mori: bytes = await file.read()
    loc = Path(f'/home/nowa/Downloads/{file.filename}')

    filename =loc.name

    job_id = job_id_maker(mori, loc)

    results = detection_video(loc, model)



    return {
        "filename": filename,
        "job_id": job_id,
        "Status": 'Processing',
        "results": results
    }

