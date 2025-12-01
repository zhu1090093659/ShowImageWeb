import json
import requests
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    """Vercel Serverless Function for proxying AI image generation API requests."""

    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()

    def do_POST(self):
        """Handle POST requests to generate images."""
        try:
            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body) if body else {}

            # Extract parameters
            api_url = data.get('api_url', '')
            api_key = data.get('api_key', '')
            prompt = data.get('prompt', '')
            seed = data.get('seed', 42)

            # Validate required fields
            if not api_url:
                self._send_error(400, 'API URL is required')
                return
            if not api_key:
                self._send_error(400, 'API Key is required')
                return
            if not prompt:
                self._send_error(400, 'Prompt is required')
                return

            # Prepare request to target API
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }
            payload = {
                'prompt': prompt,
                'seed': seed
            }

            # Make request to target API
            response = requests.post(
                api_url,
                headers=headers,
                json=payload,
                timeout=60
            )

            if response.status_code == 200:
                result = response.json()
                self._send_json(200, result)
            else:
                self._send_error(
                    response.status_code,
                    f'API Error: {response.text}'
                )

        except requests.exceptions.Timeout:
            self._send_error(504, 'Request timeout')
        except requests.exceptions.ConnectionError:
            self._send_error(502, 'Failed to connect to API server')
        except json.JSONDecodeError:
            self._send_error(400, 'Invalid JSON in request body')
        except Exception as e:
            self._send_error(500, str(e))

    def _set_cors_headers(self):
        """Set CORS headers for the response."""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def _send_json(self, status_code, data):
        """Send a JSON response."""
        self.send_response(status_code)
        self._set_cors_headers()
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _send_error(self, status_code, message):
        """Send an error response."""
        self.send_response(status_code)
        self._set_cors_headers()
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'error': message}).encode())

