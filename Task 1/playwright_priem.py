from playwright.sync_api import sync_playwright
import time

# Function to run the Playwright script
def run_playwright():
    with sync_playwright() as p:
        # Launch the browser with options
        browser = p.chromium.launch(headless=False)  # Set headless=True to run in headless mode
        context = browser.new_context(
            ignore_https_errors=True,  # Ignore SSL certificate errors
            no_viewport=True,  # Disable viewport for incognito-like behavior
            accept_downloads=True  # Accept downloads if needed
        )
        
        # Open a new page
        page = context.new_page()

        # Navigate to the target URL
        page.goto("https://www.priem.be")
        time.sleep(10)  # Wait for the page to load

        # Scroll and extract paragraphs
        scroll_pause_time = 2
        last_height = page.evaluate("document.body.scrollHeight")

        while True:
            page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)

            new_height = page.evaluate("document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Extract all paragraphs
        paragraphs = page.locator("span").all_text_contents()  # Get all paragraph texts
        paragraphs = [text for text in paragraphs if text.strip() != ""]  # Filter out empty texts

        print(paragraphs)
        print("ok")

        # Close the browser
        browser.close()

# Run the Playwright function
run_playwright()

# from playwright.sync_api import sync_playwright
# import time

# # Function to run the Playwright script
# def run_playwright():
#     with sync_playwright() as p:
#         # Launch the browser with options
#         browser = p.chromium.launch(headless=False)  # Set headless=True to run in headless mode
#         context = browser.new_context(
#             ignore_https_errors=True,  # Ignore SSL certificate errors
#             no_viewport=True,  # Disable viewport for incognito-like behavior
#             accept_downloads=True  # Accept downloads if needed
#         )
        
#         # Open a new page
#         page = context.new_page()

#         # Navigate to the target URL
#         page.goto("https://www.priem.be")
#         time.sleep(10)  # Wait for the page to load

#         # Scroll and extract content
#         scroll_pause_time = 2
#         last_height = page.evaluate("document.body.scrollHeight")

#         while True:
#             page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(scroll_pause_time)

#             new_height = page.evaluate("document.body.scrollHeight")
#             if new_height == last_height:
#                 break
#             last_height = new_height

#         # Extract all text from the page
#         all_text = page.locator("//*").all_text_contents()
#         all_text = [text for text in all_text if text.strip() != ""]

#         print(all_text)
#         print("ok")

#         # Close the browser
#         browser.close()

# # Run the Playwright function
# run_playwright()