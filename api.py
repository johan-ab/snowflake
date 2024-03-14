import requests

def send_api_request():
    url = 'https://jsonplaceholder.typicode.com/albums'
    
    # Definer eventuelle nødvendige parametre eller headers


    # Sendeanmodning
    response = requests.get(url)
    
    # Hvis du vil sende en POST-anmodning, kan du bruge følgende linje i stedet:
    # response = requests.post(url, json=payload, headers=headers)

    # Håndter svar
    if response.status_code == 200:
        # Succes, behandle data
        data = response.json()
        print("Svar fra API'en:", data)
    else:
        # Hvis der opstod en fejl, udskriv fejlmeddelelse
        print("Fejl ved anmodning til API'en. Statuskode:", response.status_code)

if __name__ == "__main__":
    send_api_request()
