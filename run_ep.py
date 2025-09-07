# import uvicorn
#
# if __name__ == "__main__":
#     uvicorn.run(
#         "app.main:app",  # module:variable
#         host="127.0.0.1",
#         port=8000,
#         reload=True
#     )

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def guts_print(title: str, response: requests.Response):
    print("=" * 60)
    print(f"[] {title}")
    print(f"=>  URL: {response.url}")
    print(f"¨° Status: {response.status_code}")
    try:
        data = response.json()
        print("|_| Response JSON:")
        print(json.dumps(data, indent=4, ensure_ascii=False))
    except Exception:
        print("|| Response Text:")
        print(response.text)
    print("=" * 60, "\n")


def test_health():
    r = requests.get(f"{BASE_URL}/health")
    guts_print("Health Check", r)

def test_stations():
    r = requests.get(f"{BASE_URL}/stations")
    guts_print("Stations List", r)

def test_sessions():
    r = requests.get(f"{BASE_URL}/sessions?limit=2")
    guts_print("Charging Sessions (limit=2)", r)


if __name__ == "__main__":
    print("\n Testing EV Charging Dashboard API Endpoints\n")
    test_health()
    test_stations()
    test_sessions()
    print("** End of endpoints.\n")