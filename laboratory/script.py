import sys
import time
import requests

# Set program bounds safely under the 5 RPS limit (4 RPS = 0.25s delay)
RATE_LIMIT_DELAY = 0.25  

# Benign testing strings to check for structural anomalies safely
TEST_PAYLOADS = [
    "'\"",        # Check database string escaping constraints
    "../../",     # Check path evaluation constraints
    "{{7*7}}",    # Check template compilation logic
]

def analyze_endpoint(url):
    """Safely audits query parameters for unexpected server handling behavior."""
    if "?" not in url:
        return

    print(f"\n[*] Evaluating asset path: {url.split('?')[0]}")
    base_url, query_string = url.split("?", 1)
    params = dict(item.split("=", 1) for item in query_string.split("&") if "=" in item)

    for param_key in params.keys():
        for payload in TEST_PAYLOADS:
            # Clone baseline parameters and insert the testing string safely
            modified_params = params.copy()
            modified_params[param_key] = f"{params[param_key]}{payload}"
            
            try:
                # Maintain safe platform pacing
                time.sleep(RATE_LIMIT_DELAY)
                
                response = requests.get(base_url, params=modified_params, timeout=5, allow_redirects=False)
                
                # Highlight structural differences or backend error codes (e.g., 500 Internal Server Error)
                if response.status_code == 500:
                    print(f" [!] Potentially unhandled input behavior discovered!")
                    print(f"     -> Parameter: '{param_key}'")
                    print(f"     -> Payload Context: {payload}")
                    print(f"     -> Trigger Link: {response.url}")
                    
            except requests.exceptions.RequestException as error:
                print(f" [!] Connection exception on parameter '{param_key}': {error}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[!] Error: Please specify an endpoints list file.")
        print("Usage: python3 verify_endpoints.py <filename.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        with open(input_file, "r") as file:
            urls = [line.strip() for line in file if line.strip()]
            
        print(f"[+] Loaded {len(urls)} target points from {input_file}. Starting safe validation...")
        for target_url in urls:
            analyze_endpoint(target_url)
            
    except FileNotFoundError:
        print(f"[!] Error: File '{input_file}' not found.")
