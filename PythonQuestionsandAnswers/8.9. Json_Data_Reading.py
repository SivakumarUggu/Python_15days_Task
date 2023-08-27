import json
def extract_json_data():
    with open('/Python_In_15days_ Q&A/8.8. Json_Data', 'r') as f1:
        data=json.load(f1)
        employee_data=data.get('employee',{})
        extract_info={
            'name':employee_data.get('name',None),
            'salary':employee_data.get('salary',None)
        }
    return extract_info

result=extract_json_data()
print(result)