from bs4 import BeautifulSoup
import requests
import time


print("Please Insert a skill")
unfamiliar_skill = input('>')
print('Filtering Results')
# print(jobs)


def job_search():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        publish_date = job.find('span', class_='sim-posted').span.text

        if 'few' in publish_date:

            company_namr = job.find(
                'h3', class_="joblist-comp-name").text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text
            moreInfo = job.header.h2.a['href']

            # print(f'''

            # Company Name : {company_namr}
            # Skills : {skills}
            # Published : {publish_date}

            # ''')
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}') as f:
                    f.write(f"Company Name: {company_namr.strip()}")
                    f.write(f"Skills Needed: {skills.strip()}")
                    f.write(f"More Info: {moreInfo}")
                    f.write(f"Publish Date: {publish_date.strip()}")
                print(f"Company Name: {company_namr.strip()}")
                print(f"Skills Needed: {skills.strip()}")
                print(f"More Info: {moreInfo}")
                print(' ')
                print(f"Publish Date: {publish_date.strip()}")

                print(' ')


if __name__ == "__main__":
    while True:
        job_search()
        time_wait = 10
        print(f'Waiting for {time_wait} Minutes')
        time.sleep(time_wait*60)
