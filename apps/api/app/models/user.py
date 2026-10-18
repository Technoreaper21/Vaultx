from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)  # student, facilitator, mentor, admin
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False)
    # Relationships
    responses = relationship("Response", back_populates="user")
EOF