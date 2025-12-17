from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker
import hashlib

Base = declarative_base()

class HealingMemory(Base):
    __tablename__ = "healing_memory"

    id = Column(Integer, primary_key=True)
    error_hash = Column(Text, index=True)
    original_code_hash = Column(Text)
    fixed_code = Column(Text)

engine = create_engine("sqlite:///healing_memory.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)


def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def save_fix(error_text, original_code, fixed_code):
    db = SessionLocal()
    record = HealingMemory(
        error_hash=hash_text(error_text),
        original_code_hash=hash_text(original_code),
        fixed_code=fixed_code
    )
    db.add(record)
    db.commit()
    db.close()


def get_previous_fix(error_text, original_code):
    db = SessionLocal()
    error_hash = hash_text(error_text)
    code_hash = hash_text(original_code)

    record = db.query(HealingMemory).filter(
        HealingMemory.error_hash == error_hash,
        HealingMemory.original_code_hash == code_hash
    ).first()

    db.close()
    return record.fixed_code if record else None
