import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://www.greggs.co.uk',
    'priority': 'u=1, i',
    'referer': 'https://www.greggs.co.uk/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

params = {
    'latitude': '51.5072178',
    'longitude': '-0.1275862',
    'distanceInMeters': '48024',
}

response = requests.get('https://production-digital.greggs.co.uk/api/v1.0/shops', params=params, headers=headers)

print(response.text)
