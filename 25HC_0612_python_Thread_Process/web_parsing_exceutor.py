import time, random
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

URLS = [
'https://www.naver.com',
'https://www.daum.net',
'https://www.google.com',
]

def printStatus(statusCode):
    """Print detailed HTTP status message based on status code"""
    status_messages = {
        200: "OK - Request succeeded",301: "Moved Permanently",
        302: "Found (Moved Temporarily)",400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable"
        }
    message = status_messages.get(statusCode, f"Unknown status code{statusCode}")
    print(f"HTTP Status {statusCode}: {message}")

def checkStatus(url):
    print(f"attempt to crawl URL : {url}")
    req = Request(url, headers={'User-Agents' : 'Mozilla/5.0'})
    response = urlopen(req)
    printStatus(response.getcode())
    return response.getcode(), URLS

def main():
    with ThreadPoolExecutor(max_workers=3) as excutor:
        tasks = []
        for url in URLS:
            task = excutor.submit(checkStatus,(url))
            tasks.append(task)
            
        for result in as_completed(tasks):
            printStatus(result)
            
if __name__ == '__main__':
    main()