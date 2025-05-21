from sqlalchemy.orm import Session
from sqlalchemy import func, or_

from app.db.models.location import Location
from app.db.models.inventory import InventoryItem


class LocationRepository:
    @staticmethod
    def get(db: Session, location_id: int) -> Location | None:
        return db.query(Location).filter(Location.id == location_id).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> list[type[Location]]:
        return db.query(Location).offset(skip).limit(limit).all()

    @staticmethod
    def search(db: Session, term: str, skip: int = 0, limit: int = 100) -> list[type[Location]]:
        return db.query(Location).filter(
            or_(
                Location.name.ilike(f"%{term}%"),
                Location.address.ilike(f"%{term}%")
            )
        ).offset(skip).limit(limit).all()

    @staticmethod
    def get_with_stock_count(db: Session, location_id: int) -> tuple[Location, int] | None:
        location = db.query(Location).filter(Location.id == location_id).first()
        if not location:
            return None
        total_stock = db.query(func.sum(InventoryItem.quantity)).filter(
            InventoryItem.location_id == location_id
        ).scalar() or 0
        return location, total_stock

    @staticmethod
    def get_all_with_stock_counts(db: Session, skip: int = 0, limit: int = 100) -> list[tuple[Location, int]]:
        locations = db.query(Location).offset(skip).limit(limit).all()
        result = []
        for loc in locations:
            stock = db.query(func.sum(InventoryItem.quantity)).filter(
                InventoryItem.location_id == loc.id
            ).scalar() or 0
            result.append((loc, stock))
        return result

    @staticmethod
    def create(db: Session, name: str, address: str, capacity: int) -> Location:
        location = Location(name=name, address=address, capacity=capacity)
        db.add(location)
        db.commit()
        db.refresh(location)
        return location

    @staticmethod
    def update(db: Session, location_id: int,
               name: str | None = None,
               address: str | None = None,
               capacity: int | None = None) -> Location | None:
        location = db.query(Location).filter(Location.id == location_id).first()
        if not location:
            return None

        if name is not None:
            location.name = name
        if address is not None:
            location.address = address
        if capacity is not None:
            location.capacity = capacity

        db.commit()
        db.refresh(location)
        return location

    @staticmethod
    def delete(db: Session, location_id: int) -> bool:
        location = db.query(Location).filter(Location.id == location_id).first()
        if not location:
            return False

        db.delete(location)
        db.commit()
        return True
