from typing import Optional

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/details")
def read_root():
    version="1.1"
    namespace = os.getenv('POD_NAMESPACE', default = 'ns-red')
    return {"Message": "with Love from OCI Devops ","Version":version,"Served via":namespace}