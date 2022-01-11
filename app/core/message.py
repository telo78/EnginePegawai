from fastapi import HTTPException, status


def sendMessage(statuskd: status, message: str):
    raise HTTPException(status_code=statuskd,
                        detail=message)
