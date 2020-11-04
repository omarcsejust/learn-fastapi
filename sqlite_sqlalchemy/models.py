from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship

from .database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    salary = Column(Numeric(10, 2))
    dept_id = Column(Integer, ForeignKey('departments.id'), nullable=False)

    department = relationship("Department", back_populates="owner")


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    dept_name = Column(String, unique=True, index=True)

    owner = relationship("Employee", back_populates="department")



