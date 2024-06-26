from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.linkedin.com/jobs/search/?keywords=angular")


soup = BeautifulSoup(response.text, "html.parser")
article_jobs = soup.find_all(name="a", attrs={"class":"base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]"})
for link in article_jobs:
  print(link.getText().strip())
  print(link.get('href'),"\n")
