#json creation

#Create a JSON file (employee.json) containing employee information of minimum 5 employees.
#Name, DOB, Height, City, State


import json

emp_list = {
    "employee": [
        {
            "Emp_Name":"Tom Riddle", 
            "DOB":"11/8/1943",
            "Height":"180cm",
            "City":"Bangalore",
            "State": "Karnataka"
        },
        {
            "Emp_Name":"Harry Potter", 
            "DOB":"11/8/1995", 
            "Height":"160cm", 
            "City":"Bangalore", 
            "State": "Karnataka"
        },
        {
            "Emp_Name":"Ron Weasley", 
            "DOB":"13/6/1995", 
            "Height":"181cm", 
            "City":"Bangalore", 
            "State": "Karnataka"
        },
        {
            "Emp_Name":"Hermoine Granger", 
            "DOB":"22/2/1995", 
            "Height":"153cm", 
            "City":"Bangalore", 
            "State": "Karnataka"
        },        
        {
            "Emp_Name":"Severus Snape", 
            "DOB":"22/2/1995", 
            "Height":"170cm", 
            "City":"Bangalore", 
            "State": "Karnataka"
        }
    ]
}


json_string = json.dumps(emp_list, indent = 2)
with open ("Employee.json", "w") as emp:
    emp.write(json_string)
print("Json Created")


with open('Employee.json', 'r') as emp:
    data = emp.read()
    json_object = json.loads(data)
print(type(json_object['employee']))

for i in json_object['employee']:
    print(i)
#----------------------------
#my reference
# import json
# with open ("Employee.json","r") as emp:
# #     x = emp.read()
# # file_data = json.load(x)

# print(type(file_data))
# print (file_data)

# import json
# final_data = json.load('Employee.json') #loadS method is to load the string so we do not use this 
# print(final_data)
# print(type(final_data))
# print(type(final_data['employee']))

# for i in final_data['employee']:
#     print (i)
#--------------------------------------------------------------------



# Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
import json
state_dict = {
    "Andhra Pradesh": "Amaravati",
    "Bihar": "Patna",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Uttar Pradesh": "Lucknow",
    "West Bengal": "Kolkata"
}

with open ("India State Capital.json", "w") as states:
    json.dump(state_dict, states)

    print ("Created Json")


