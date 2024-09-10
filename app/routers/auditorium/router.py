from fastapi import APIRouter

from app.routers.auditorium.schemas import SAuditorium
from app.routers.auditorium.dao import AuditoriumDAO


router = APIRouter(prefix='/auditorium',
                   tags=['Auditoriums'])


@router.post('/create')
async def create_auditorium(data: SAuditorium) -> None:
    await AuditoriumDAO.create(number=data.number)


@router.get('/get')
async def get_auditorium(number: str) -> SAuditorium:
    auditorium = await AuditoriumDAO.get_by_filter(number=number)
    return auditorium


@router.put('/update')
async def update_auditorium(id: int, data: SAuditorium) -> None:
    await AuditoriumDAO.update_by_id(id, number=data.number)


@router.delete('/delete')
async def delete_auditorium(number: str) -> None:
    await AuditoriumDAO.delete_by_filter(number=number)
