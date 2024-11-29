import requests


def get_posts():
    # Define the API endpoint URL
    url = 'https://archive-api.open-meteo.com/v1/archive?latitude=40.7143&longitude=-74.006&start_date=2022-01-01&end_date=2022-12-31&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None 
    except:
        print("failed")

if __name__ == "__main__":
    post = get_posts()
    print(post)