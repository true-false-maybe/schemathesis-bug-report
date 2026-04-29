from fastapi import FastAPI, Query, HTTPException
from typing import Annotated, List

app = FastAPI(
    title="My API",
    description="API",
    version="v1",
    servers=[
        {"url": "http://127.0.0.1"}
    ],
    openapi_version="3.1.0",
)


@app.get(
    "/box",
    description="Endpoint",
    response_model=str,
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "schema": {"type": "string"}
                }
            },
        }
    },
)
def get_box(
    box: Annotated[
        List[float],
        Query(
            description="Four values of latitude and longitude to form a Bounding-Box.",
            min_length=4,
            max_length=4,
            examples=[[-180, -90, 180, 90]],
        ),
    ]
):
    if len(box) != 4:
        raise HTTPException(
            status_code=422,
            detail="box must contain exactly 4 values",
        )

    min_lon, min_lat, max_lon, max_lat = box

    # Match schema constraints
    if not (-180 <= min_lon <= 180):
        raise HTTPException(status_code=422, detail="First value must be longitude [-180, 180]")

    if not (-90 <= min_lat <= 90):
        raise HTTPException(status_code=422, detail="Second value must be latitude [-90, 90]")

    if not (-180 <= max_lon <= 180):
        raise HTTPException(status_code=422, detail="Third value must be longitude [-180, 180]")

    if not (-90 <= max_lat <= 90):
        raise HTTPException(status_code=422, detail="Fourth value must be latitude [-90, 90]")

    return "OK"
