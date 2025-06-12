import requests
from bs4 import BeautifulSoup
import time  # 시간 측정을 위한 모듈 추가

visited_links = set()
collected_links = []

def get_links(url):
    # link 목록을 list 로 전달.
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith('http'):
                title = link.text.strip() or href
                links.append((title, href))
        return links
    except:
        return []

def crawl(url, current_depth, max_depth, max_links):
    if current_depth > max_depth or len(collected_links) >= max_links or url in visited_links:
        return

    visited_links.add(url)
    print(f"[Depth {current_depth}] Crawling: {url}")

    links = get_links(url)
    for title, link in links:
        if len(collected_links) >= max_links:
            break
        print(f"Title: {title}, Link: {link}")
        collected_links.append((title, link))
        crawl(link, current_depth + 1, max_depth, max_links)

def save_links(filename="titles.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for title, link in collected_links:
            f.write(f"{title}\t{link}\n")

def main():
    start_url = input("Enter starting URL: ")
    max_depth = int(input("Enter max depth (0 for only start page): "))
    max_links = int(input("Enter max links to collect: "))

    start_time = time.time()  # 시작 시간 기록

    crawl(start_url, 0, max_depth, max_links)
    save_links()

    end_time = time.time()  # 종료 시간 기록
    elapsed_time = end_time - start_time  # 실행 시간 계산

    print(f"\nFinished crawling. Saved {len(collected_links)} links to titles.txt")
    print(f"Execution time: {elapsed_time:.2f} seconds")  # 실행 시간 출력

if __name__ == "__main__":
    main()
