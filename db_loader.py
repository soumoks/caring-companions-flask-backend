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
post_1 = {
    'name': 'Sourabh',
    'descr': 'PyMongo is fun, you guys',
    'home': 'A',
    'interests' : ['biking','hiking'],
    'timeslots' : ['2-4','4-6']
}
post_2 = {
    'name': 'Vaibhav',
    'descr': 'Frontend guy',
    'home': 'B',
    'interests' : ['eating','sleeping'],
    'timeslots' : ['2-4','4-6']
}
post_3 = {
    'name': 'Than',
    'descr': 'Coder girl',
    'home': 'B',
    'interests' : ['singing','dancing'],
    'timeslots' : ['2-4','4-6','7-9']
}
post_4 = {
    'name': 'Arsalan',
    'descr': 'Cool dude',
    'home': 'C',
    'interests' : ['playing','sleeping'],
    'timeslots' : ['7-9','4-6']
}
post_5 = {
    'name': 'Yves',
    'descr': 'Frontend guy',
    'home': 'B',
    'interests' : ['eating','sleeping'],
    'timeslots' : ['2-4','4-6']
}
post_6 = {
    'name': 'Mussavi',
    'descr': 'Frontend guy',
    'home': 'B',
    'interests' : ['eating','sleeping'],
    'timeslots' : ['2-4','4-6']
}
post_7 = {
    'name': 'Mohammad',
    'descr': 'Frontend guy',
    'home': 'B',
    'interests' : ['eating','sleeping'],
    'timeslots' : ['2-4','4-6']
}
post_8 = {
    'name': 'Biker',
    'descr': 'Frontend guy',
    'home': 'B',
    'interests' : ['eating','sleeping'],
    'timeslots' : ['2-4','4-6']
}
post_9 = {
    'name': 'Player',
    'descr': 'Frontend guy',
    'home': 'B',
    'interests' : ['eating','sleeping'],
    'timeslots' : ['2-4','4-6']
}
post_10 = {
    'name': 'Hiker',
    'descr': 'Frontend guy',
    'home': 'B',
    'interests' : ['eating','sleeping'],
    'timeslots' : ['2-4','4-6']
}

#new_result = posts.insert_many([post_1, post_2, post_3,post_4,post_5,post_6,post_7,post_8,post_9,post_10])

#print('Multiple posts: {0}'.format(new_result.inserted_ids))

for post in posts.find():
    print(post)

new_list = [post for post in posts.find()]

#Find one 
print(posts.find_one({'name':'Sourabh'}))