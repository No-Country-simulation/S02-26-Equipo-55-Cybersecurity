import requests
import sys

if len(sys.argv) != 2:
    print("Uso: python header_check.py https://example.com")
    sys.exit(1)

url = sys.argv[1]
response = requests.get(url)

security_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "X-XSS-Protection"
]

print(f"\nAnalizando headers para {url}\n")

for header in security_headers:
    if header in response.headers:
        print(f"[OK] {header} presente")
    else:
        print(f"[WARNING] {header} NO presente")
