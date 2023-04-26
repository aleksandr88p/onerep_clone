import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, proxy={
            "server": "http://45.155.201.162:8000",
            "username": "4UsLX7",
            "password": "tCDbq9"})

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }

        context = await browser.new_context()
        await stealth_async(context)
        page = await context.new_page()
        await page.set_extra_http_headers(headers)
        # await page.goto("https://www.google.com/")
        await page.goto('https://www.usa-people-search.com/name/billie-bones/new-york')
        # await page.goto('https://www.peoplesearchnow.com/person/john-smith_new-york_ny')
        await asyncio.sleep(1200000)  # пауза на 2 минуты
        await browser.close()

asyncio.run(main())