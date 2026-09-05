"""Small standard-library server for the Meme Coin FOMO Simulator."""

from __future__ import annotations

import gzip
import json
import mimetypes
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8000


class SimulatorHandler(BaseHTTPRequestHandler):
    server_version = "FomoPractice/1.0"

    def _headers(self, content_type: str, length: int, compressed: bool = False) -> None:
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(length))
        self.send_header("Cache-Control", "no-cache" if content_type.startswith("text/html") else "public, max-age=3600")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        if compressed:
            self.send_header("Content-Encoding", "gzip")

    def _send_bytes(self, body: bytes, content_type: str, status: HTTPStatus = HTTPStatus.OK) -> None:
        accepts_gzip = "gzip" in self.headers.get("Accept-Encoding", "")
        payload = gzip.compress(body, compresslevel=6) if accepts_gzip and len(body) > 700 else body
        self.send_response(status)
        self._headers(content_type, len(payload), payload is not body)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(payload)

    def do_GET(self) -> None:  # noqa: N802
        route = urlparse(self.path).path
        if route == "/api/health":
            body = json.dumps({"status": "ok", "mode": "practice", "realFunds": False}).encode()
            self._send_bytes(body, "application/json; charset=utf-8")
            return

        relative = "index.html" if route in ("/", "") else route.lstrip("/")
        target = (ROOT / relative).resolve()
        if ROOT not in target.parents and target != ROOT:
            self._send_bytes(b"Not found", "text/plain; charset=utf-8", HTTPStatus.NOT_FOUND)
            return
        if not target.is_file():
            self._send_bytes(b"Not found", "text/plain; charset=utf-8", HTTPStatus.NOT_FOUND)
            return
        content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        self._send_bytes(target.read_bytes(), f"{content_type}; charset=utf-8" if content_type.startswith("text/") else content_type)

    def do_HEAD(self) -> None:  # noqa: N802
        self.do_GET()

    def log_message(self, format_string: str, *args: object) -> None:
        print(f"{self.address_string()} - {format_string % args}")


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), SimulatorHandler)
    print(f"Meme Coin FOMO Simulator: http://{HOST}:{PORT}")
    print("Practice only: no wallet connection and no real funds.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()