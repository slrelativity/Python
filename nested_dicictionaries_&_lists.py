x = [ [5,2,3], [10,8,9] ] 
x [1][0]=15
print(x)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name' ]='Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0]= 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)




students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(some_list):
    for dictionary in some_list: 
        arr =[]
        for key, value in dictionary.items():
            arr.append(f"{key} - {value}, ")
        for x in arr:
            print(x)

iterate_dictionary(students)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary2(key_name, students):
    for dictionary in students: 
        arr =[]
        if key_name in dictionary:
            print (dictionary[key_name])
            
    
iterate_dictionary2('first_name',students)
iterate_dictionary2('last_name',students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(some_dict):
    for key, value_count in some_dict.items():
        print(f"({len(value_count)}) {key.upper()}")
        for item in value_count:
            print(item)

print_info(dojo)


