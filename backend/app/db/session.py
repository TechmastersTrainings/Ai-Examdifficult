"""Database connection engine and session factory."""

import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.app.core.config import settings

import logging

logger = logging.getLogger("uvicorn.error")

active_db_url = settings.DATABASE_URL
if active_db_url.startswith("postgres://"):
    active_db_url = active_db_url.replace("postgres://", "postgresql+psycopg2://", 1)
elif active_db_url.startswith("postgresql://") and not active_db_url.startswith("postgresql+"):
    active_db_url = active_db_url.replace("postgresql://", "postgresql+psycopg2://", 1)

connect_args = {}

if active_db_url.startswith("postgresql"):
    try:
        test_engine = create_engine(active_db_url, connect_args={}, pool_pre_ping=True)
        with test_engine.connect():
            pass
        engine = test_engine
        logger.info("Successfully connected to PostgreSQL database cluster.")
    except Exception as exc:
        logger.warning(
            f"PostgreSQL at {active_db_url.split('@')[-1]} not reachable ({exc}). "
            "Using persistent fallback SQLite store at ./data/app.db"
        )
        active_db_url = "sqlite:///./data/app.db"
        os.makedirs("./data", exist_ok=True)
        connect_args = {"check_same_thread": False}
        engine = create_engine(active_db_url, connect_args=connect_args, pool_pre_ping=True)
elif active_db_url.startswith("sqlite"):
    db_path = active_db_url.replace("sqlite:///", "")
    db_dir = os.path.dirname(db_path)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)
    connect_args = {"check_same_thread": False}
    engine = create_engine(active_db_url, connect_args=connect_args, pool_pre_ping=True)
else:
    engine = create_engine(active_db_url, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency yielding a transactional SQLAlchemy session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
