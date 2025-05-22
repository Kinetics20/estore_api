from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.location import location_repository
from app.db.session import get_db
from app.schemas.location import LocationCreate

router = APIRouter(
    prefix="/locations",
    tags=["Locations"]
)


@router.get("/")
def list_locations(
        search: str | None = None,
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
):
    if search:
        return location_repository.search(db, search, skip=skip, limit=limit)
    else:
        return location_repository.get_all(db, skip=skip, limit=limit)


@router.post('/')
def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    return location_repository.create(
        db,
        name=location.name,
        address=location.address,
        capacity=location.capacity
    )
