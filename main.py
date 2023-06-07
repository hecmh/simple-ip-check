import requests
import folium as fl


def getInfo(ip = '127.0.0.1'):
    try:
        response = requests.get(url = f'http://ip-api.com/json/{ip}').json()
        # print(response)
        
        data = {
            '[IP]': response.get('query'),
            '[INT PROV]': response.get('isp'),
            '[ORG]': response.get('org'),
            '[Country]': response.get('country'),
            '[Country code]': response.get('countryCode'),
            '[Region]': response.get('region'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Time zone]': response.get('timezone'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon')
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        area = fl.Map(location = [response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print("[!] check ur connection.")


def main():
    ip = input ('input ip: ')
 
    getInfo(ip = ip)


if __name__ == '__main__':
    main()
