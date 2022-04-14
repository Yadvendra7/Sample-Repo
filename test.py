import requests
import json
import csv

access_token = "RuMe6KhKDnQ7PrNJc5f20EoHINFOUIfhNd2WcT8T"

headers = {
    'authorization': 'Bearer ' + access_token,
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'

}

course_dict = {}
counter = 1
while(1):
  params = (
    ('ordering', '-last_accessed'),
    ('page', str(counter)),
    ('page_size', '100'),
  )

  response = requests.get('https://www.udemy.com/api-2.0/users/me/subscribed-courses/', headers=headers, params=params)
  json_data = json.loads(response.text)

  if "results" in json_data:
      for data in json_data['results']:
        course_dict.update({data['title']:"https://www.udemy.com"+data['url']}) 

  counter+=1  
  if not "results" in json_data:
   break



with open('Courses.csv', 'w',encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Coures Title", "Course Url"])
    for courseName, courseUrl in course_dict.items(): 
      writer.writerow([courseName, courseUrl])
