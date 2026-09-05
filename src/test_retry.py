import asyncio
import aiohttp
from retry_utils import fetch_with_retry

async def main():
    async with aiohttp.ClientSession() as session:
        data = await fetch_with_retry(
            session,
            "https://huggingface.co/api/models?limit=5"
        )

        if data:
            print("Success! Models fetched:", len(data))

asyncio.run(main())