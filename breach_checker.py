import requests
from urllib.parse import quote


def check_breaches(email, api_key):

    encoded_email = quote(email, safe="")

    url = (
        f"https://haveibeenpwned.com/api/v3/breachedAccount/{encoded_email}")

    headers = {

        "hibp-api-key": str(api_key),
        "User-Agent": "BreachWatch/1.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 404:
            return []

        response.raise_for_status()  # raises http error

        return response.json()

    except requests.exceptions.Timeout:
        print("Error: The request Timeout")
        return None

    except requests.exceptions.HTTPError as error:
        status_code = (
            error.response.status_code if error.response is not None else None)

        if status_code == 401:
            print(
                "Error: HIBP authentication failed. Check your API key and access permissions.")

        elif status_code == 403:
            print("Error: The request was forbidden. Check your API permissions.")

        elif status_code == 429:
            print("Error: Rate limit exceeded. Please try again later.")

        else:
            print(
                f"Error: HTTP request failed with status code {status_code}.")
        return None

    except requests.exceptions.RequestException:
        print("Error: The API request failed due to a network or request issue.")
        return None
