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
                    "get": {
                        "parameters": [
                            {
                                "name": "limit",
                                "in": "query",
                                "type": "integer"
                            },
                            {
                                "name": "offset",
                                "in": "query",
                                "type": "integer"
                            }
                        ]
                    }
                }
            }
        }
        expected_output_without_params = {
            "GET /api/users"
        }
        routes_without_params = extract_routes(swagger_data, include_params=False)
        self.assertEqual(expected_output_without_params, routes_without_params)

        expected_output_with_params = {
            "GET /api/users?limit&offset"
        }
        routes_with_params = extract_routes(swagger_data, include_params=True)
        self.assertEqual(expected_output_with_params, routes_with_params)


if __name__ == "__main__":
    unittest.main()

