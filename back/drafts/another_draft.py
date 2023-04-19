import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    url = 'https://www.kidslivesafe.com/personalinfocheck/search'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://www.kidslivesafe.com/personalinfocheck/search',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.kidslivesafe.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Cookie': 'AWSALB=CEEfw9hbjIbshlmLsGU74m6B+Iyvy9rC08wk+NCDVSG9I9Ftm0yvQ072LKlyKmCV0aiOIfyGvxWbmddlN+mZ6TJw47qlr5KLtfY6FmfJMDwgHYuxVAKpCpjNBlAZ; AWSALBCORS=CEEfw9hbjIbshlmLsGU74m6B+Iyvy9rC08wk+NCDVSG9I9Ftm0yvQ072LKlyKmCV0aiOIfyGvxWbmddlN+mZ6TJw47qlr5KLtfY6FmfJMDwgHYuxVAKpCpjNBlAZ; koa.sid=gsy2Yszry_mU3nCeizZABX8CGI8Ad9R6; koa.sid.sig=DbquZgrZzUu9-BDqepwxVmdjy1c; _gcl_au=1.1.704266776.1681510906'
    }

    data = {
        'state[long]': 'Indiana',
        'state[short]': 'IN',
        'minAge': '18',
        'maxAge': '100',
        'city': '',
        'firstName': 'john',
        'lastName': 'smith'
    }

    async with playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_context().new_page()

        # Make the POST request
        await page.goto(url, {'method': 'POST', 'headers': headers, 'body': data})

        # Wait for the page to load
        await page.wait_for_selector('.result-details')

        # Get the HTML content of the page
        content = await page.content()

        # Close the browser
        await browser.close()

    print(content)


async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())