from fastapi import APIRouter

router = APIRouter(
	prefix="/api/auth",
	tags=["auth"],
	)

@router.get("/test")
def test_auth():
    return {"status": "auth works"}
