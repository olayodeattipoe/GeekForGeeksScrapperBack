from bs4 import BeautifulSoup
from GeeksForGeeks import get_source_code


soup = get_source_code("https://www.geeksforgeeks.org/quizzes/file-handling-gq/")
lou = soup.find_all(name='link', rel="preconnect")

