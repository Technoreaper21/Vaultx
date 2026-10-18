from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base import Base

class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    activity_id = Column(Integer, ForeignKey("activities.id"))
    response_data = Column(Text)  # JSON string
    submitted_at = Column(DateTime, nullable=False)
    # Relationships
    user = relationship("User", back_populates="responses")
    activity = relationship("Activity", back_populates="responses")
EOF