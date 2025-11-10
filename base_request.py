import requests
import pprint

class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        max_attempts = 3  # Добавляем ограничение попыток
        attempts = 0
        
        while not stop_flag and attempts < max_attempts:
            attempts += 1
            try:
                if request_type == 'GET':
                    response = requests.get(url, timeout=10)  # Добавляем timeout
                elif request_type == 'POST':
                    response = requests.post(url, json=data, timeout=10)  # Исправляем на json
                else:
                    response = requests.delete(url, timeout=10)

                # Условие выхода из цикла
                if not expected_error and response.status_code == 200:
                    stop_flag = True
                elif expected_error:
                    stop_flag = True
                else:
                    # Если не ожидаем ошибку, но статус не 200, выходим
                    stop_flag = True

            except requests.exceptions.RequestException as e:
                print(f"Request error: {e}")
                stop_flag = True  # Выходим при ошибке

        # log part
        pprint.pprint(f'{request_type} example')
        pprint.pprint(f'URL: {url}')
        pprint.pprint(f'Status Code: {response.status_code}')
        pprint.pprint(f'Reason: {response.reason}')
        pprint.pprint(f'Response Text: {response.text}')
        if response.text:
            try:
                pprint.pprint(f'Response JSON: {response.json()}')
            except:
                pass
        pprint.pprint('**********')
        return response

    def get(self, endpoint, endpoint_id, expected_error=False):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.json() if response.text else {}

    def post(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'POST', data=body)
        return response.json() if response.text else {}

    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.json() if response.text else {}