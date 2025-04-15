from playwright.sync_api import sync_playwright
import time

# URL to request
url = 'https://example.com'  # Replace with your target URL

# Function to send requests and check responses
def send_requests_for_duration(duration):
    start_time = time.time()
    end_time = start_time + duration
    valid_responses = 0
    invalid_responses = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True for headless mode
        context = browser.new_context()
        page = context.new_page()

        while time.time() < end_time:
            response = page.goto(url)  # Send request
            if response.status == 200:
                valid_responses += 1
            else:
                invalid_responses += 1

        # Close the browser
        browser.close()

    return valid_responses, invalid_responses

# Run the request sending function for 5 minutes
duration_in_seconds = 5 * 60  # 5 minutes
valid_count, invalid_count = send_requests_for_duration(duration_in_seconds)

print(f"Total valid responses (status 200): {valid_count}")
print(f"Total invalid responses (status other than 200): {invalid_count}")