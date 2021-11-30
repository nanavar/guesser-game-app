import os
import pytest

#   nujno da je to pred importom da gre iz memorija
os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from main import app, db

@pytest.fixture
def client():
    client = app.test_client()

    cleanup()

    db.create_all()

    yield client

def cleanup():
    db.drop_all()

#   do tuki je v usakem projektu ENAKO!


#   PRVI TEST

def test_index_not_logged_in(client):
    response = client.get("/")
    assert b"Enter your name" in response.data

def test_index_logged_in(client):
    client.post("/login", data={"user-name": "Dohyun", "user-email": "kim@gmail.com", "user-password": "1234"}, follow_redirects=True)
    response = client.get("/")
    assert b"Enter your guess" in response.data