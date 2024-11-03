import json
with open('documents.json', 'rt') as f_in:
    docs_raw = json.load(f_in)
documents = []

for course_dict in docs_raw:
    for doc in course_dict['documents']:
        doc['course'] = course_dict['course']
        documents.append(doc)    
documents[0]        
# {'text': "The purpose of this document is to capture frequently asked technical questions\nThe exact day and hour of the course will be 15th Jan 2024 at 17h00. The course will start with the first  “Office Hours'' live.1\nSubscribe to course public Google Calendar (it works from Desktop only).\nRegister before the course starts using this link.\nJoin the course Telegram channel with announcements.\nDon’t forget to register in DataTalks.Club's Slack and join the channel.",
#  'section': 'General course-related questions',
#  'question': 'Course - When will the course start?',
#  'course': 'data-engineering-zoomcamp'}

I'm following this course using nested json for data. the code above is just for extracting the document for the search engine(that what the video said, I'm not sure)

but now I have dataset like this translated_luat_giao_duc.txt so how to skip and change the way to imput the translated_luat_giao_duc.txt in?

National Assembly

-------



Socialist Republic of Vietnam

Independence - Freedom - Happiness

---------------



Law No. 43/2019/QH14



Hanoi, June 14, 2019
