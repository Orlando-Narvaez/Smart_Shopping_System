from sqlalchemy import Column, Integer, ForeignKey, String, TIMESTAMP, text
from app.database.base import Base

# Modelo de miembro de familia
class FamilyMember(Base):
    __tablename__ = "family_members"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    family_id = Column(Integer, ForeignKey("families.id"))
    role = Column(String(20))
    joined_at = Column(TIMESTAMP, server_default=text("NOW()"))