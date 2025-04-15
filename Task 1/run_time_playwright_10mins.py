from playwright.sync_api import sync_playwright
import time

# List of URLs to test
urls = [
    # 'https://www.priem.be',
    # 'https://aquilae.be',
    # 'https://www.declercq-verstichel.be',
    # 'https://www.hillewaere-verzekeringen.be/',
    'https://www.deridderkris.be',
    # 'https://www.invicta-art.com',
    # 'https://www.invicta-insurance.be/'
]

# Function to send requests and check responses
def send_requests_for_duration(url, duration):
    start_time = time.time()
    end_time = start_time + duration
    valid_responses = 0
    invalid_responses = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        while time.time() < end_time:
            try:
                response = page.goto(url, timeout=60000, wait_until="domcontentloaded")
                if response and response.status == 200:
                    valid_responses += 1
                else:
                    invalid_responses += 1
            except Exception as e:
                print(f"Error visiting {url}: {e}")
                invalid_responses += 1

        browser.close()

    return valid_responses, invalid_responses

# Loop through each URL
for url in urls:
    print(f"\nTesting URL: {url}")
    duration_in_seconds = 10 * 60  # 10 minutes
    valid_count, invalid_count = send_requests_for_duration(url, duration_in_seconds)

    print(f"Total valid responses (status 200): {valid_count}")
    print(f"Total invalid responses (errors or non-200): {invalid_count}")


# from playwright.sync_api import sync_playwright
# import time

# # URL to request
# # URL to request
# urls = [
#         # 'https://www.priem.be',
#         # 'https://aquilae.be',
#         # 'https://www.declercq-verstichel.be',
#         # 'https://www.hillewaere-verzekeringen.be/',
#         'https://www.deridderkris.be',
#         # 'https://www.invicta-art.com',
#         # 'https://www.invicta-insurance.be/'
#         ]  # Replace with your target URL

# # Function to send requests and check responses
# def send_requests_for_duration(duration):
#     start_time = time.time()
#     end_time = start_time + duration
#     valid_responses = 0
#     invalid_responses = 0

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)  # Set headless=True for headless mode
#         context = browser.new_context()
#         page = context.new_page()

#         while time.time() < end_time:
#             response = page.goto(url)  # Send request
#             if response.status == 200:
#                 valid_responses += 1
#             else:
#                 invalid_responses += 1

#         # Close the browser
#         browser.close()

#     return valid_responses, invalid_responses

# for url in urls:
#     print(f"url: {url}")
#     # Run the request sending function for 5 minutes
#     duration_in_seconds = 10 * 60  # 5 minutes
#     valid_count, invalid_count = send_requests_for_duration(duration_in_seconds)

#     print(f"Total valid responses (status 200): {valid_count}")
#     print(f"Total invalid responses (status other than 200): {invalid_count}")