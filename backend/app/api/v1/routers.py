from fastapi import APIRouter

from .block_routes import router as block_router
from .journal_router import router as journal_router
from .user_router import router as user_router

router = APIRouter()


router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(journal_router, prefix="/journals", tags=["Journals"])
router.include_router(block_router, prefix="/blocks", tags=["Blocks"])
