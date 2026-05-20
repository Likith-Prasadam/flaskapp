from app import app, notes

def setup_function():
    notes.clear()

def test_home_page():

    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200

def test_add_note():

    client = app.test_client()

    response = client.post('/add', data={
        'note': 'Test Note'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Test Note' in response.data

def test_empty_note():

    client = app.test_client()

    response = client.post('/add', data={
        'note': ''
    }, follow_redirects=True)

    assert response.status_code == 200
    assert len(notes) == 0