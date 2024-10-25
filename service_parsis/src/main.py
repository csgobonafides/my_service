from fastapi import FastAPI, Request, Depends
import asyncio
from src.models.processing_req import proc_req
from src.models.parses_films import data_films
from src.middle_ware.time_middle import MyMiddle

app = FastAPI()
app.add_middleware(MyMiddle)


@app.post('/data_film/{name}')
async def data_film(name, user_info = Depends(proc_req)):
    # if user_info:
    return await data_films(name)
    # else:
    #     return user_info


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8001)