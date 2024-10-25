from fastapi import Request, HTTPException
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from src._exceptions.to_except import ForbiddenError, UnauthorizedError


async def proc_req(request: Request):
    if request.headers.get('Authorization'):
        url = 'http://app:8000/examination/'
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers={'Authorization': request.headers.get('Authorization')}) as response:
                soup = await response.json()
                if response.status != 200:
                    raise UnauthorizedError('No authorization')
                else:
                    print(soup)
                    return soup
    raise UnauthorizedError('Token missing')