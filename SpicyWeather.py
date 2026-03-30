import requests

def get_spicy_weather():
    # '0' gives current weather only, 'A' forces ANSI (colors), 
    # 'Q' makes it quiet (removes 'Weather report' header)
    url = "https://wttr.in"
    
    try:
        # We 'fake' a curl user-agent to get the formatted terminal version
        response = requests.get(url, headers={'User-Agent': 'curl'})
        
        if response.status_code == 200:
            print("\n" + "="*30)
            print(" 🔥 SPICY WEATHER UPDATE 🔥 ")
            print("="*30 + "\n")
            print(response.text)
        else:
            print("Couldn't reach the weather gods. Status:", response.status_code)
            
    except Exception as e:
        print(f"Error fetching weather: {e}")

if __name__ == "__main__":
    get_spicy_weather()
