from typing import Optional,Dict
from pydantic import BaseModel, Field
class Book(BaseModel):
    Accessnumber:int
    Title:str
    Author:str
    Subject:str
    KeyWord:str
    #categoryid:int
    bookcategory:str
    
    
class ShowBook(BaseModel):
    Accessnumber:int
    Title:str
    Author:str
    Subject:str
    KeyWord:str
    #categoryid:int
    bookcategory:str
    
    
    class Config():
        orm_mode = True
        
        
class Category(BaseModel):
    id:int
    bookcategory:str
    book:list[ShowBook]
    
class ShowCategory(BaseModel):
    id:int
    bookcategory:str
    
    
    
    class Config():
        orm_mode = True
        
 