
from playwright.sync_api import sync_playwright

def verify(page):
    page.goto("http://localhost:8000/index.html")
    page.wait_for_selector(".img-comp-container")

    # Wait for the image to be loaded (since it is base64, it should be fast, but good to be safe)
    page.wait_for_selector(".img-comp-overlay img")

    # Take screenshot of initial state
    page.screenshot(path="final_fix_view.png")

    # Simulate drag to reveal more video
    slider = page.locator(".img-comp-slider")
    box = slider.bounding_box()
    if box:
        page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
        page.mouse.down()
        page.mouse.move(box["x"] - 100, box["y"] + box["height"] / 2)
        page.mouse.up()
        page.screenshot(path="final_fix_slide.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            verify(page)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()
