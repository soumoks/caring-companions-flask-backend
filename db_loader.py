from pymongo import MongoClient
client = MongoClient('localhost', 27017)
print("Connected")
db = client.Citizens

"""
Citizen object fields
#     #     self.name = name
#     #     self.descr = descr
#     #     self.home = home
#     #     self.interests = interests
#     #     self.timeslots = timeslots
"""
posts = db.posts
#posts.drop()
post_1 = {
    'name': 'John',
    'descr': 'Retired army veteran',
    'home': 'A',
    'interests' : ['music','chess'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/179127-275x390-senior-man-wearing-sweater.jpg'
}
post_2 = {
    'name': 'Judy',
    'descr': 'Nurse',
    'home': 'B',
    'interests' : ['games','photography'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/354-mckinsey-35-ae.jpg'
}
post_3 = {
    'name': 'Than',
    'descr': 'Banker',
    'home': 'B',
    'interests' : ['watching TV','home building'],
    'timeslots' : ['2-4','4-6','7-9'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/4c1a491bc0aa66334a5e1f2166d38303.jpg'
}
post_4 = {
    'name': 'Steph',
    'descr': 'School Teacher',
    'home': 'C',
    'interests' : ['helping kids','sleeping'],
    'timeslots' : ['7-9','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/F16F988F-B16C-45D6-B6F6AD6734363BEA_source.jpg'
}
post_5 = {
    'name': 'Amanda',
    'descr': 'Geologist',
    'home': 'B',
    'interests' : ['science','reading'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/Sixty-and-Me_10-Ideas-for-Petite-Clothing-for-Women-Over-60.jpg'
}
post_6 = {
    'name': 'Mark',
    'descr': 'Architect',
    'home': 'B',
    'interests' : ['design','chess'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/happy-senior-man-looking-at-tablet.jpg'
}
post_7 = {
    'name': 'Mohammad',
    'descr': 'Frontend guy',
    'home': 'B',
    'interests' : ['eating','sleeping'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/istockphoto-889902628-612x612.jpg'
}
post_8 = {
    'name': 'Randall',
    'descr': 'State Senator',
    'home': 'B',
    'interests' : ['politics','cooking'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/lrs1485_1.jpg'
}
post_9 = {
    'name': 'Camille',
    'descr': 'Chef',
    'home': 'B',
    'interests' : ['knitting','long walks'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/senior_holidays_c4cb390619.jpg'
}
post_10 = {
    'name': 'Meghan',
    'descr': 'Doctor',
    'home': 'B',
    'interests' : ['reading','music'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/seniors-citizen-age-@1X.jpg'
}

#new_result = posts.insert_many([post_1, post_2, post_3,post_4,post_5,post_6,post_7,post_8,post_9,post_10])

# print('Multiple posts: {0}'.format(new_result.inserted_ids))

# for post in posts.find():
#     print(post)

# new_list = [post for post in posts.find()]

# #Find one 
# print(posts.find_one({'name':'Sourabh'}))

senior_list = [post['interests'] for post in posts.find()]
for senior in senior_list:
    print(senior)