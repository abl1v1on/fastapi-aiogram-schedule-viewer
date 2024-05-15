from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


from core import settings


class DataBaseHelper:
    def __init__(self, url: str, echo: bool) -> None:
        self.async_engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.async_engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )
    
    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session
            await session.close()


db_helper = DataBaseHelper(
    url=settings.DB_URL,
    echo=settings.DB_ECHO
)
