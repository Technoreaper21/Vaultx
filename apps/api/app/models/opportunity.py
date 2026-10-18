from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from app.db.base import Base

class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    eligibility_rules = Column(Text)  # JSON string for simplicity
    is_placeholder = Column(Boolean, default=True)
    source_url = Column(String, nullable=True)
    last_verified_at = Column(DateTime, nullable=True)
EOF