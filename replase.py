import json
jsonstr = '[{"time": "["20170101070311", "20230101070311"]", "amount": "3088"}]'

translist = json.loads(str(jsonstr))
print(translist)
print(type(translist))


# json_loads = [{'time': '['20170101070311', '20230101070311']', 'amount': '3088'}]