from sqlalchemy.orm import Session
from sqlalchemy import and_, func

from app.db.models.inventory import InventoryItem
from app.db.models.product import Product
from app.db.models.location import Location


class InventoryRepository:
    @staticmethod
    def get(db: Session, product_id: int, location_id: int) -> InventoryItem | None:
        return db.query(InventoryItem).filter(
            and_(
                InventoryItem.product_id == product_id,
                InventoryItem.location_id == location_id
            )
        ).first()

    @staticmethod
    def get_by_product(db: Session, product_id: int) -> list[tuple[InventoryItem, Location]]:
        return db.query(InventoryItem, Location).join(Location).filter(
            InventoryItem.product_id == product_id
        ).all()

    @staticmethod
    def get_by_location(db: Session, location_id: int) -> list[tuple[InventoryItem, Product]]:
        return db.query(InventoryItem, Product).join(Product).filter(
            InventoryItem.location_id == location_id
        ).all()

    @staticmethod
    def get_low_stock_items(db: Session) -> list[tuple[InventoryItem, Product, Location]]:
        return db.query(InventoryItem, Product, Location) \
            .join(Product) \
            .join(Location) \
            .filter(InventoryItem.quantity < InventoryItem.reorder_point) \
            .all()

    @staticmethod
    def get_total_quantity_by_product(db: Session, product_id: int) -> int:
        return db.query(func.sum(InventoryItem.quantity)).filter(
            InventoryItem.product_id == product_id
        ).scalar() or 0

    @staticmethod
    def update_stock(db: Session, product_id: int, location_id: int,
                     quantity_change: int, reorder_point: int | None = None) -> InventoryItem | None:
        item = InventoryRepository.get(db, product_id, location_id)

        if item:
            new_quantity = item.quantity + quantity_change
            if new_quantity < 0:
                return None

            item.quantity = new_quantity
            if reorder_point is not None:
                item.reorder_point = reorder_point
        else:
            if quantity_change < 0:
                return None

            item = InventoryItem(
                product_id=product_id,
                location_id=location_id,
                quantity=quantity_change,
                reorder_point=reorder_point or 0
            )
            db.add(item)

        db.commit()
        db.refresh(item)
        return item

    @staticmethod
    def set_stock(db: Session, product_id: int, location_id: int,
                  quantity: int, reorder_point: int | None = None) -> InventoryItem:
        item = InventoryRepository.get(db, product_id, location_id)

        if item:
            item.quantity = quantity
            if reorder_point is not None:
                item.reorder_point = reorder_point
        else:
            item = InventoryItem(
                product_id=product_id,
                location_id=location_id,
                quantity=quantity,
                reorder_point=reorder_point or 0
            )
            db.add(item)

        db.commit()
        db.refresh(item)
        return item

    @staticmethod
    def delete(db: Session, product_id: int, location_id: int) -> bool:
        item = InventoryRepository.get(db, product_id, location_id)
        if not item:
            return False

        db.delete(item)
        db.commit()
        return True
