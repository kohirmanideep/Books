from sqlalchemy import Column,Integer,String,VARCHAR,ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Book(Base):
    __tablename__ = "books"
    Accessnumber =Column(Integer, primary_key=True)
    Title = Column(VARCHAR(50), unique=True, index=True)
    Author = Column(VARCHAR(50))
    Subject = Column(VARCHAR(50))
    KeyWord = Column(VARCHAR(30))
    #categoryid=Column(Integer,ForeignKey("categories.id"))
    #category_info = relationship("Category", back_populates="book")
    bookcategory=Column(VARCHAR(50))
    

 


#class Category(Base):
   # __tablename__ = "categories"
  #  id = Column(Integer, primary_key=True, index=True)
    #bookcategory=Column(VARCHAR(50))
   # book = relationship("Book", back_populates="category_info")