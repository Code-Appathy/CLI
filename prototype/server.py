#!/usr/bin/env python3
"""UbuntuCLIApp capability prototype.

Standard-library-only HTTP server intended for a trusted LAN during prototyping.
It exposes a phone-friendly web UI and a deliberately small allow-list of
development commands. It does NOT provide an arbitrary shell.
"""

from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse
import json
import subprocess
import os

ROOT = Path(__file__).resolve().parent
WEB = ROOT / "web"
HOST = os.environ.get("UCLI_HOST", "0.0.0.0")
PORT = int(os.environ.get("UCLI_PORT", "8765"))

COMMANDS = {
    "system": ["uname", "-a"],
    "git_version": ["git", "--version"],
    "python_version": ["python3", "--version"],
    "node_version": ["node", "--version"],
    "codex_version": ["codex", "--version"],
    "git_status": ["git", "status", "--short", "--branch"],
}


def run_command(name: str):
    command = COMMANDS.get(name)
    if not command:
        return {"ok": False, "error": "Command is not allowed."}
    try:
        result = subprocess.run(
            command,
            cwd=os.environ.get("UCLI_PROJECT_DIR", str(ROOT.parent)),
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )
        output = (result.stdout + result.stderr).strip()
        return {"ok": result.returncode == 0, "code": result.returncode, "output": output}
    except FileNotFoundError:
        return {"ok": False, "error": f"{command[0]} is not installed or not in PATH."}
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "Command timed out."}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB), **kwargs)

    def _json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/health":
            return self._json({"ok": True, "service": "UbuntuCLIApp prototype"})
        if path == "/api/capabilities":
            return self._json({"ok": True, "commands": list(COMMANDS)})
        if path.startswith("/api/run/"):
            return self._json(run_command(path.removeprefix("/api/run/")))
        return super().do_GET()


if __name__ == "__main__":
    print(f"UbuntuCLIApp prototype: http://{HOST}:{PORT}")
    print("Prototype only: use on a trusted network. No authentication is implemented yet.")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
