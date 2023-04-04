from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_book():
    response = client.get('/get/book/1')
    assert response.status_code ==200
    
def get_staff_book():
    response = client.get('get/book/introduction to computer networks')
    assert response.status_code == 200
    
    
def get_allbook():
    response = client.get('/get/book/ram')
    assert response.status_code == 200
    
def getbook():
    response = client.get('/book/')
    assert response.status_code == 200