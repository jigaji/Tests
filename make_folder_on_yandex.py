import requests

url = 'https://cloud-api.yandex.net/v1/disk/resources'
token = input('Введите токен: ')

def create_folder():
    name = input('Введите название новой папки: ')
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    params = {"path": name}
    new_folder = requests.put(url, params=params, headers=headers)
    return new_folder.status_code

if __name__ == '__main__':
    create_folder()