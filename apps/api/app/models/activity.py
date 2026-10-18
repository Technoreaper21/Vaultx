from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    is_placeholder = Column(Boolean, default=True)
    source_url = Column(String, nullable=True)
    last_verified_at = Column(DateTime, nullable=True)
    # Relationships
    responses = relationship("Response", back_populates="activity")
EOF