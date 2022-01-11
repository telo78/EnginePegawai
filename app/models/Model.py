from sqlalchemy import Column, Integer, SmallInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, Float, String, Text
from ..db.database import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255))
    nip = Column(String(255))
    role = Column(String(25))
    username = Column(String(255))
    password = Column(String(255))
    emailConfirmationToken = Column(String(50))
    status = Column(SmallInteger)
    createdAt = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    savecourse = relationship("SaveCourse", back_populates="users")


class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    isActive = Column(SmallInteger)
    createdAt = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    courses = relationship("Course", back_populates="category")


class Course(Base):
    __tablename__ = 'Course'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))
    image = Column(String(255))
    duration = Column(Integer)
    price = Column(String(255))
    instructors = Column(String(255))
    url = Column(String(255))
    rating = Column(Float)
    categoryId = Column(Integer, ForeignKey('Category.id'))
    category = relationship("Category", back_populates="courses")
    providerId = Column(Integer, ForeignKey('Provider.id'))
    providers = relationship("Provider", back_populates="courses")
    createdAt = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    savecourse = relationship("SaveCourse", back_populates="courses")


class Provider(Base):
    __tablename__ = 'Provider'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(150))
    image = Column(String(100))
    description = Column(Text)
    createdAt = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    courses = relationship("Course", back_populates="providers")


class SaveCourse(Base):
    __tablename__ = 'SaveCourse'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    courseId = Column(Integer, ForeignKey('Course.id'))
    userId = Column(Integer, ForeignKey('User.id'))
    createdAt = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    users = relationship("User", back_populates="savecourse")
    courses = relationship("Course", back_populates="savecourse")
