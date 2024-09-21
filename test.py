import requests

def get_location_by_ip(ip_address):
    try:
        # Отправляем запрос на ip-api.com для получения информации о местоположении
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        
        if data['status'] == 'success':
            # Получаем местоположение
            location_info = {
                'IP': data['query'],
                'Country': data['country'],
                'Region': data['regionName'],
                'City': data['city'],
                'ISP': data['isp'],
                'Latitude': data['lat'],
                'Longitude': data['lon'],
                'Timezone': data['timezone']
            }
            return location_info
        else:
            return f"Ошибка: {data['message']}"
    
    except Exception as e:
        return f"Произошла ошибка: {e}"

if __name__ == "__main__":
    # Получаем IP-адрес от пользователя
    ip_address = input("Введите IP-адрес: ")
    location = get_location_by_ip(ip_address)
    
    # Выводим результат
    if isinstance(location, dict):
        print("Местоположение по IP:")
        for key, value in location.items():
            print(f"{key}: {value}")
    else:
        print(location)
