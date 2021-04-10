import requests

class Pixela:

    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.url = "https://pixe.la/v1/users"
        self.headers = {"X-USER-TOKEN": self.token}

    def create_user(self):
        params = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }

        response = requests.post(url=self.url, json=params)
        print(response.text)

    def create_graph(self, graph_id, name, unit, data_type, color):
        graph_endpoint = f"{self.url}/{self.username}/graphs"

        graph_config = {
            "id": graph_id,                     # don't start with a number
            "name": name,                       # graph name
            "unit": unit,                       # unit measured
            "type": data_type,                  # int or float
            "color": color,                     # shibafu (green), momiji (red), sora (blue),
            "timezone": "America/Sao_Paulo"     # ichou (yellow), ajisai (purple) or kuro (black)
        }

        response = requests.post(url=graph_endpoint, json=graph_config, headers=self.headers)
        print(response.text)

    def post_pixel(self, graph_id, pixel_date, quantity, optional=None):  # date format: yyyyMMdd
        graph_endpoint = f"{self.url}/{self.username}/graphs/{graph_id}"

        body = {
            "date": pixel_date,
            "quantity": quantity,
            "optionalData": optional   # json
        }

        response = requests.post(url=graph_endpoint, json=body, headers=self.headers)
        print(response.text)

    def update_pixel(self, graph_id, pixel_date, quantity, optional=None):  # date format: yyyyMMdd
        graph_endpoint = f"{self.url}/{self.username}/graphs/{graph_id}/{pixel_date}"

        body = {
            "quantity": quantity,
            "optionalData": optional   # json
        }

        response = requests.put(url=graph_endpoint, json=body, headers=self.headers)
        print(response.text)

    def delete_pixel(self, graph_id, pixel_date):  # date format: yyyyMMdd
        graph_endpoint = f"{self.url}/{self.username}/graphs/{graph_id}/{pixel_date}"

        response = requests.delete(url=graph_endpoint, headers=self.headers)
        print(response.text)
