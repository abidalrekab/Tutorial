

''' Tutorial of today is Dictionaries '''

# create a dictionary
student = {'name': 'John', 'Age': 25, 'courses': ['Math', 'Science']}

# add a new item
student['phone'] = '555-506-30322'
print(student)

# add or modify an exsitance item using dic.update
student.update({'Origin': 'Libya', 'GPA': 4.0})
print(student)

# how to delete an item "key"
del(student['Age'])

# how to loop over keys and values in a dictionary
for key, values in student.items():
    print('{} = {}'.format(key, values))
