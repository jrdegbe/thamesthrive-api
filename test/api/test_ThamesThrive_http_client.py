from ThamesThrive.service.ThamesThrive_http_client import HttpClient
from test.utils import Endpoint
import asyncio

# Define a common async function for making HTTP requests
async def make_request(method, path, expected_status):
    async with HttpClient(5, 200, headers={"some-header": "1"}) as client:
        request_method = getattr(client, method)
        async with request_method(Endpoint.host(path), json={}) as response:
            assert response.status == expected_status
            if expected_status == 200:
                response_body = await response.json()
                assert "headers" in response_body
                assert response_body["headers"]["some-header"] == "1"

# Test functions for different HTTP methods
async def should_get():
    await make_request('get', '/healthcheck', 200)

async def should_post():
    await make_request('post', '/healthcheck', 200)

async def should_put():
    await make_request('put', '/healthcheck', 200)

async def should_delete():
    await make_request('delete', '/healthcheck', 200)

async def should_give_404():
    await make_request('get', '/this-endpoint-does-not-exist', 404)

# Main test function to run all tests
async def test_thames_thrive_http_client():
    await should_get()
    await should_post()
    await should_put()
    await should_delete()
    await should_give_404()

# Running the test suite
if __name__ == "__main__":
    asyncio.run(test_thames_thrive_http_client())
