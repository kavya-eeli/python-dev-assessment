import requests

def fetch_and_display_users(num_users):
    
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        # Make GET request
        response = requests.get(url, timeout=5)

        # Check for non-200 status codes
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return None

        # Parse JSON response
        try:
            users = response.json()
        except ValueError:
            print("Error: Response is not valid JSON.")
            return None

        # Validate structure and iterate
        if not isinstance(users, list):
            print("Error: Unexpected JSON structure.")
            return None

        for i, user in enumerate(users[:num_users]):
            try:
                name = user.get("name", "N/A")
                email = user.get("email", "N/A")
                city = user.get("address", {}).get("city", "N/A")
                print(f"{i+1}. Name: {name}, Email: {email}, City: {city}")
            except Exception as e:
                print(f"Error processing user data: {e}")
                return None

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


# Example calls
if __name__ == "__main__":
    print("Fetching 3 users:")
    fetch_and_display_users(3)

    print("\nFetching 15 users (out-of-bounds test):")
    fetch_and_display_users(15)