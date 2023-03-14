import csv
import json

with open('onerepcopy_potential2.html') as f:
    data = json.load(f)


print(data.keys())



item_list = data['data']
# for item in item_list:
#     print(item['data_broker'])
with open('links_for_check.csv', 'a', newline='') as csvF:
    writer = csv.writer(csvF)
    for item in item_list:
        writer.writerow([item['data_broker']])
        print(item['data_broker'])