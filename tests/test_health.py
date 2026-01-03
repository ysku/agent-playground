import pytest
from fastapi.testclient import TestClient
from app.main import app

# Create a test client
client = TestClient(app)


class TestHealthEndpoint:
    """Comprehensive test suite for the /health endpoint."""

    def test_health_check_returns_200(self):
        """Test that the health check endpoint returns a 200 status code."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_check_returns_json(self):
        """Test that the health check endpoint returns JSON content type."""
        response = client.get("/health")
        assert response.headers["content-type"] == "application/json"

    def test_health_check_returns_correct_structure(self):
        """Test that the health check endpoint returns the correct JSON structure."""
        response = client.get("/health")
        data = response.json()
        assert isinstance(data, dict)
        assert "status" in data

    def test_health_check_returns_ok_status(self):
        """Test that the health check endpoint returns status 'ok'."""
        response = client.get("/health")
        data = response.json()
        assert data["status"] == "ok"

    def test_health_check_full_response(self):
        """Test the complete response of the health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_health_check_idempotency(self):
        """Test that multiple calls to the health check return consistent results."""
        response1 = client.get("/health")
        response2 = client.get("/health")
        response3 = client.get("/health")
        
        assert response1.status_code == response2.status_code == response3.status_code == 200
        assert response1.json() == response2.json() == response3.json() == {"status": "ok"}

    def test_health_check_method_not_allowed(self):
        """Test that non-GET methods are not allowed on the health endpoint."""
        # POST should not be allowed
        response_post = client.post("/health")
        assert response_post.status_code == 405

        # PUT should not be allowed
        response_put = client.put("/health")
        assert response_put.status_code == 405

        # DELETE should not be allowed
        response_delete = client.delete("/health")
        assert response_delete.status_code == 405

    def test_health_check_no_query_params_needed(self):
        """Test that the health check works without any query parameters."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_health_check_ignores_query_params(self):
        """Test that the health check ignores any query parameters."""
        response = client.get("/health?foo=bar&baz=qux")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_health_check_response_contains_only_status(self):
        """Test that the response contains only the status field."""
        response = client.get("/health")
        data = response.json()
        assert len(data) == 1
        assert list(data.keys()) == ["status"]
