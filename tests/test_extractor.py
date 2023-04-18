import unittest
from swagroutes.extractor import extract_routes


class TestExtractor(unittest.TestCase):
    def test_extract_routes(self):
        swagger_data = {
            "basePath": "/api",
            "paths": {
                "/users": {
                    "get": {},
                    "post": {}
                },
                "/profile/{profile_id}": {
                    "put": {}
                }
            }
        }
        expected_output = {
            "GET /api/users",
            "POST /api/users",
            "PUT /api/profile/{profile_id}"
        }
        routes = extract_routes(swagger_data)
        self.assertEqual(expected_output, routes)

    def test_extract_routes_with_parameters(self):
        swagger_data = {
            "basePath": "/api",
            "paths": {
                "/users": {
                    "post": {},
                    "parameters": {}
                }
            }
        }
        expected_output = {
            "POST /api/users",
        }
        routes = extract_routes(swagger_data)
        self.assertEqual(expected_output, routes)

if __name__ == "__main__":
    unittest.main()

