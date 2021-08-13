from typing import List

from app.schemas import work_group as wg_sch


class WorkGroupComponent:
    """Компонент для работы с сущностью события"""

    def create(self, wg: wg_sch.WorkGroupToDb) -> wg_sch.WorkGroupFromDb:
        """Создать событие на дороге"""
        return wg.insert()

    def read(self, pk) -> wg_sch.WorkGroupFromDb:
        """Получить полную информацию о событие"""
        return wg_sch.WorkGroupFromDb.by_pk(pk)

    def read_all(self) -> List[wg_sch.WorkGroupGeoFromDB]:
        """Получить все доступные события пользователя"""
        return wg_sch.WorkGroupGeoFromDB.get_all()

    def update(self, pk: int, wg: wg_sch.WorkGroupToDb) -> wg_sch.WorkGroupFromDb:
        """Обновить событие"""
        wg = wg.update(pk)
        return wg

    def delete(self, wg: wg_sch.WorkGroupDelete):
        """Удалить событие"""
        wg.delete()

    def filter(self, wg_filter: wg_sch.WorkGroupFilter) -> List[wg_sch.WorkGroupGeoFromDB]:
        """Отфильтровать"""
        return wg_filter.filter()
