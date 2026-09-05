import asyncio
import random
import aiohttp

async def fetch_with_retry(session, url, retries=5):
    delay = 1

    for attempt in range(retries):
        try:
            async with session.get(url, timeout=30) as response:

                if response.status == 200:
                    return await response.json()

                elif response.status == 429:
                    wait = delay + random.uniform(0, 1)
                    print(f"429 received. Waiting {wait:.2f} sec...")
                    await asyncio.sleep(wait)
                    delay *= 2

                else:
                    print(f"Status {response.status} for {url}")
                    return None

        except Exception as e:
            print("Retrying because:", e)
            await asyncio.sleep(delay)
            delay *= 2

    print("Failed after retries:", url)
    return None