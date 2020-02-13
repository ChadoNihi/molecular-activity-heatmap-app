from main import app

def test_has_static_route():
	assert any(route.name == "static" for route in app.routes)
