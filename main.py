from typing import Optional

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/")
def read_root():
    namespace = os.getenv('namespace', default = 'ns-red')
    return {"Message": "with Love from OCI Devops ","deployed_namespace":namespace}