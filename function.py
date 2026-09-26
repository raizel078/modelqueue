from database import insert_job
import uuid




def job_id_maker( mori, loc):
    with open(loc, 'wb')as saved_file:
        saved_file.write(mori)

    job_id = str(uuid.uuid4())
    insert_job(job_id, loc.name)

    return job_id

def detection_video(loc, model):

    results = model.track(
        source=str(loc),
        stream=True,
        persist=True
    )

    detected_object ={}

    for result in results:
        for box in result.boxes:
            if box.id is not None:
                unique_id = int(box.id.item())
                class_id = int(box.cls.item())
                class_name = result.names[class_id]

                if unique_id not in detected_object:
                    detected_object[unique_id]= class_name


    class_count = {}

    for class_name in detected_object.values():
        class_count[class_name] = class_count.get(class_name,0)+1

    return class_count









