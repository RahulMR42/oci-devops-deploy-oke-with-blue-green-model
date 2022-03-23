from typing import Optional

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/v0")
def read_root():
    version="1.1"
    deployed_pod = os.getenv('HOSTNAME', default = 'ns-red')
    return {"Message": "with Love from OCI Devops ","version":"version","deployed_pod":deployed_pod}