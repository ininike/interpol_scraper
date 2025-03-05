from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

DOMAIN = "https://www.interpol.int"

class InterpolScraper:
    def __init__(self):
        """Initialize the Selenium WebDriver options"""
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--window-size=1920x1080")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        
    @staticmethod
    async def search(self, keyword: str) -> list:
        """Search Interpol site based on a keyword"""
        html = self._get_results(keyword)
        if html:
            results = self._extract_content(html)
            return results
        return []

    def _get_results(self, keyword) -> str | None:
        """Search for the results of the first page"""
        url = f"{DOMAIN}/en/Search-Page?search={keyword}&year=0&category=0&type=all&limit=100&page=1"
        try:
            self.driver.get(url)
            time.sleep(5)
            html = self.driver.page_source
            return html
        except Exception as e:
            print("Error:", e)
            return None

    def _extract_content(self, html) -> list:
        """Extract search results"""
        soup = BeautifulSoup(html, 'html.parser')
        results = [
            {
                "type": result.select_one(".search__resultItem--type").text.strip(),
                "title": result.select_one(".search__resultItem--mainTitle").text.strip(),
                "link": self._format_link(result.select_one("a").get("href"))
            }
            for result in soup.select(".search__resultsBlock--result")
        ]
        return results

    def _format_link(self, link) -> str:
        """Completing links by adding the domain if necessary"""
        if not link.startswith("https") and "youtube" not in link:
            return DOMAIN + link
        return link

    def __del__(self):
        """Ensure the WebDriver is properly closed when the object is deleted"""
        self.driver.quit()
