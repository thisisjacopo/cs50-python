fruit = input('Item: ').lower()
fruitList = [{"name":'apple', "calories": 130}, 
             {"name":'avocado', "calories": 50},
             {"name":'kiwifruit', "calories": 90},
             {"name": 'banana', "calories": 110}, 
             {"name": 'grapes', "calories": 90}, 
             {"name": 'sweet cherries', "calories": 100}, 
             {"name": 'orange', "calories": 80}, 
             {"name": 'pear', "calories": 100}, 
             {"name": 'strawberries', "calories": 50}]

#check if fruit is in the list and print its calories value else do nothing
for item in fruitList:
    if item["name"].lower() == fruit:
        print("Calories:", item["calories"])
        break
