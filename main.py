from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class NumbersRequest(BaseModel):
    numbers: List[int]


@app.post("/sum")
async def sum_numbers(request: NumbersRequest):
    try:
        numbers = request.numbers
        result = sum(numbers)
        return {"sum": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


class StringsRequest(BaseModel):
    strings: List[str]


@app.post("/concatenate")
async def concatenate_strings(request: StringsRequest):
    try:
        strings = request.strings
        result = "".join(strings)
        return {"concatenated_string": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
