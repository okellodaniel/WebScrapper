from bs4 import BeautifulSoup

with open('index.html', 'r') as hmtl_file:
    content = hmtl_file.read()

    soup = BeautifulSoup(content, 'lxml')

    # print(soup.prettify())

    # tags = soup.find('h1')

    # print(tags)

    course_cards = soup.find_all('div', class_='card')

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(course_name)
        print("===============================")
        print(course_price)

        # Using the f-string

        print(f'{course_name} costs {course_price}')
