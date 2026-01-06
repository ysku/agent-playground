from fastapi.testclient import TestClient
from app.main import app

# Create a test client
client = TestClient(app)


class TestReadyzEndpoint:
    """Comprehensive test suite for the /readyz endpoint."""

    def test_readyz_check_returns_200(self):
        """Test that the readyz check endpoint returns a 200 status code."""
        response = client.get("/readyz")
        assert response.status_code == 200

    def test_readyz_check_returns_json(self):
        """Test that the readyz check endpoint returns JSON content type."""
        response = client.get("/readyz")
        assert response.headers["content-type"] == "application/json"

    def test_readyz_check_returns_correct_structure(self):
        """Test that the readyz check endpoint returns the correct JSON structure."""
        response = client.get("/readyz")
        data = response.json()
        assert isinstance(data, dict)
        assert "status" in data

    def test_readyz_check_returns_ok_status(self):
        """Test that the readyz check endpoint returns status 'ok'."""
        response = client.get("/readyz")
        data = response.json()
        assert data["status"] == "ok"

    def test_readyz_check_full_response(self):
        """Test the complete response of the readyz check endpoint."""
        response = client.get("/readyz")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_readyz_check_idempotency(self):
        """Test that multiple calls to the readyz check return consistent results."""
        response1 = client.get("/readyz")
        response2 = client.get("/readyz")
        response3 = client.get("/readyz")
        
        assert response1.status_code == response2.status_code == response3.status_code == 200
        assert response1.json() == response2.json() == response3.json() == {"status": "ok"}

    def test_readyz_check_method_not_allowed(self):
        """Test that non-GET methods are not allowed on the readyz endpoint."""
        # POST should not be allowed
        response_post = client.post("/readyz")
        assert response_post.status_code == 405

        # PUT should not be allowed
        response_put = client.put("/readyz")
        assert response_put.status_code == 405

        # DELETE should not be allowed
        response_delete = client.delete("/readyz")
        assert response_delete.status_code == 405

    def test_readyz_check_ignores_query_params(self):
        """Test that the readyz check ignores any query parameters."""
        response = client.get("/readyz?foo=bar&baz=qux")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_readyz_check_response_contains_only_status(self):
        """Test that the response contains only the status field."""
        response = client.get("/readyz")
        data = response.json()
        assert len(data) == 1
        assert list(data.keys()) == ["status"]
