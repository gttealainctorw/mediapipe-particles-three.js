import http.server
import socketserver
import os
import sys

PORT = 8000


class WasmHandler(http.server.SimpleHTTPRequestHandler):

    def end_headers(self):
        # Necesario para WASM + MediaPipe
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def guess_type(self, path):
        if path.endswith(".wasm"):
            return "application/wasm"
        if path.endswith(".js"):
            return "application/javascript"
        return super().guess_type(path)

    def log_message(self, format, *args):
        # args[0] puede NO ser string (HTTPStatus), lo forzamos
        msg = str(args[0]) if args else ""

        # Silenciar logs de assets pesados
        if any(x in msg for x in [".wasm", ".data", ".js"]):
            return

        super().log_message(format, *args)


# Cambiar al directorio del script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("\n🚀 Servidor local iniciado")
print(f"   → Abre Chrome en: http://localhost:{PORT}")
print(f"   → Carpeta: {os.getcwd()}")
print("   → Presiona Ctrl+C para detener\n")

with socketserver.TCPServer(("", PORT), WasmHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido")
        sys.exit(0)