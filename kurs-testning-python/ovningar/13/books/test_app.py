#
# Här skriver du dina tester för appen i app.py
#

def test_empty_list_returns_200(client):
    response = client.get("/api/books")
    assert response.status_code == 200
    assert response.get_json() == []
