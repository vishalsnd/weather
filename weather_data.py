import requests

Api = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    date = input("Enter the date (yyyy-mm-dd): ")
    response = requests.get(Api)
    if response.status_code == 200:
        data = response.json()
        for item in data['list']:
            if item['dt_txt'].startswith(date):
                print(f"Temperature on {item['dt_txt']}: {item['main']['temp']} K")
                break
        else:
            print("Date not found.")
    else:
        print("Failed to fetch data.")

def get_wind_speed_data():
    date = input("Enter the date (yyyy-mm-dd): ")
    response = requests.get(Api)
    if response.status_code == 200:
        data = response.json()
        for item in data['list']:
            if item['dt_txt'].startswith(date):
                print(f"Wind Speed on {item['dt_txt']}: {item['wind']['speed']} m/s")
                break
        else:
            print("Date not found.")
    else:
        print("Failed to fetch data.")

def get_pressure_data():
    date = input("Enter the date (yyyy-mm-dd): ")
    response = requests.get(Api)
    if response.status_code == 200:
        data = response.json()
        for item in data['list']:
            if item['dt_txt'].startswith(date):
                print(f"Pressure on {item['dt_txt']}: {item['main']['pressure']} hPa")
                break
        else:
            print("Date not found.")
    else:
        print("Failed to fetch data.")

while True:
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

    option = input("Enter your choice: ")

    if option == '1':
        get_weather_data()
    elif option == '2':
        get_wind_speed_data()
    elif option == '3':
        get_pressure_data()
    elif option == '0':
        break
    else:
        print("Invalid option. Please try again.")

print("Program terminated.")
