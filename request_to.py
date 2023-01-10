import requests

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 8080

    response = requests.get(f"http://{HOST}:{PORT}/getList", params={"token": "abs"})
    print(f"Status code: {response.status_code}")
    print(f"Response body: {response.text}")
