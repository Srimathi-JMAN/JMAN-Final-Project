import requests
import time

# URL to request
urls = [
        # 'https://www.priem.be',
        'https://aquilae.be',
        'https://www.declercq-verstichel.be',
        'https://www.hillewaere-verzekeringen.be/',
        # 'https://www.deridderkris.be',
        'https://www.invicta-art.com',
        'https://www.invicta-insurance.be/'
        ]  # Replace with your target URL

# Function to send requests and check responses
def send_requests_for_duration(duration):
    start_time = time.time()
    end_time = start_time + duration
    valid_responses = 0
    invalid_responses = 0

    while time.time() < end_time:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                valid_responses += 1
            else:
                invalid_responses += 1
        except requests.exceptions.RequestException:
            invalid_responses += 1

    return valid_responses, invalid_responses

for url in urls:
    print(f"url: {url}")
    # Run the request sending function for 5 minutes
    duration_in_seconds = 10 * 60  # 5 minutes
    valid_count, invalid_count = send_requests_for_duration(duration_in_seconds)
    print(f"Total valid responses (status 200): {valid_count}")
    print(f"Total invalid responses (status other than 200): {invalid_count}")
