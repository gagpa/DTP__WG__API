from app.schemas import shape


class ShapeComponent:
    """Shape component"""

    def read(self, pk) -> shape.ShapeData:
        """Получить полную информацию о событие"""
        return shape.ShapeData.by_pk(pk)
