import requests
import time

# URL to request
urls = [
        'https://www.priem.be',
        'https://aquilae.be',
        'https://www.declercq-verstichel.be',
        'https://www.hillewaere-verzekeringen.be/',
        'https://www.deridderkris.be',
        'https://www.invicta-art.com',
        'https://www.invicta-insurance.be/'
        ]

# Function to measure request time
def one_request_time(url):
    start_time = time.time()  # Start the timer
    response = requests.get(url)  # Make the request
    end_time = time.time()  # End the timer
    duration = end_time - start_time  # Calculate the duration
    return response, duration

def multiple_request_time(count,url):
    # Measure time for 100 requests
    start_time = time.time()  # Start the timer for 100 hits
    for _ in range(count):
        response = requests.get(url)  # Make the request
    end_time = time.time()  # End the timer
    duration_multiple = end_time - start_time  # Calculate the total duration
    return response, duration_multiple

for url in urls:

    print(f"url: {url}")
    # Measure time for a single request
    response_single_hit, duration_single_hit = one_request_time(url)
    print(f"Single request to {url} took {duration_single_hit:.2f} seconds. Status Code: {response_single_hit.status_code}")

    # Measure time for 100 requests
    response_of_100_hits, duration_of_100_hits = multiple_request_time(100,url)
    print(f"100 requests to {url} took {duration_of_100_hits:.2f} seconds. Last Status Code: {response_of_100_hits.status_code}")