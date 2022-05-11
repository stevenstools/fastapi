from fastapi import FastAPI
from pydantic import BaseModel
import time
from ping3 import ping
from datetime import datetime
from typing import Optional
import pytz


class Host(BaseModel):
    hostname: str
    tz: Optional[str] = "UTC"


app = FastAPI()

@app.post("/")
async def pingapi(host: Host):
    hostname = str(host.hostname)
    rttstart = time.time()
    timez = pytz.timezone(host.tz)
    if ping(hostname):
       rttstop = time.time()
       rtt = rttstop-rttstart
    if ping(hostname) == False:
       rtt = "Unable to resolve"
    if ping(hostname) == None:
       rtt = "Time out"
    return {"hostname" : hostname, "rtt" : rtt, "time" : datetime.now(timez)}





