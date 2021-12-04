from bs4 import BeautifulSoup

with open('index.html', 'r') as hmtl_file:
    content = hmtl_file.read()

    soup = BeautifulSoup(content, 'lxml')

    print(soup.prettify())

    tags = soup.find('h1')

    print(tags)
