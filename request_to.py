import requests
from web_app import get_ids

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 8080

    token = "123"
    list_of_id = get_ids()

    responses = [requests.post(f"http://{HOST}:{PORT}/create", params={"token": token, "text": "SSSHHHEEESSSHHH"}),
                 requests.delete(f"http://{HOST}:{PORT}/delete", params={"token": token, "ID": list_of_id[-1]}),
                 requests.get(f"http://{HOST}:{PORT}/getList", params={"token": token}),
                 requests.get(f"http://{HOST}:{PORT}/getInfo", params={"token": token, "ID": list_of_id[0]}),
                 requests.patch(f"http://{HOST}:{PORT}/update", params={"token": token, "ID": list_of_id[0],
                                                                        "text": "new text"}),
                 requests.get(f"http://{HOST}:{PORT}/getText", params={"token": token, "ID": list_of_id[0]})]

    for i in responses:
        print(f"Request: {i.request}")
        print(f"Status code: {i.status_code}")
        print(f"Response body: {i.text}")
        print(20 * "------")
