from app.schemas import work_group as wg_sch
from typing import List


class WorkGroupComponent:
    """Компонент для работы с сущностью события"""

    def create(self, wg: wg_sch.WorkGroupToDB) -> wg_sch.WorkGroupFromDB:
        """Создать событие на дороге"""
        return wg.insert()

    def read(self, pk) -> wg_sch.WorkGroupDataFromDB:
        """Получить полную информацию о событие"""
        return wg_sch.WorkGroupDataFromDB.by_pk(pk)

    def read_all(self) -> List[wg_sch.WorkGroupShortFromDB]:
        """Получить все доступные события пользователя"""
        return wg_sch.WorkGroupShortFromDB.get_all()

    def update(self, pk: int, wg: wg_sch.WorkGroupToDB) -> wg_sch.WorkGroupFromDB:
        """Обновить событие"""
        wg = wg.update(pk)
        return wg

    def delete(self, wg: wg_sch.WorkGroupDelete):
        """Удалить событие"""
        wg.delete()

    def filter(self, wg_filter: wg_sch.WorkGroupFilter) -> List[wg_sch.WorkGroupShortFromDB]:
        """Отфильтровать"""
        return wg_filter.filter()
