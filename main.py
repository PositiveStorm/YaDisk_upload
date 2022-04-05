

import requests
import os


with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()
    print(token)

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        files_adress = 'E:/Screenshots'
        files_list = os.listdir(files_adress)
        for file in files_list:
            headers = {
                        'Content-Type': 'application/json',
                        'Authorization': '{}'.format(self.token)
                    }

            upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            params = {"path": file, "overwrite": "true"}
            response = requests.get(upload_url, headers=headers, params=params)
            href_json = response.json()
            href = href_json['href']
            response = requests.put(href, data=open(file_path, 'rb'))
            response.raise_for_status()
            if response.status_code == 201:
                print("Success")

if __name__ == '__main__':
    path_to_file = 'E:/Screenshots/1.txt'
    token = token
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
