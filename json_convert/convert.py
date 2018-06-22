import csv
import json

indent = 2


def get_indent():
    return " " * indent


def creat_csv(id, content):
    with open('../testSheets/' + id + '.csv', 'w') as csv_file:
        csv_file.write(content)


def create_json(id):
    result = []
    dict = {'id': id}
    with open('../testSheets/' + id + '.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for line in reader:
            result.append(line)
        dict["items"] = result
        json_file = open('../testSheets/' + id + '.json', 'w')
        json.dump(dict, json_file, indent=4, sort_keys=True, separators=(',', ': '))
        json_file.close()


if __name__ == '__main__':
    id = 'firstTest'
    str = 'ad,japanese_calendar,theater,sports_acilities,other,golf_course,mahjong,pachinko\n2011,H23,20,6,44,33,215,212\n2012,H24,18,6,43,34,209,208\n2013,H25,19,6,43,33,185,204\n2014,H26,20,6,43,32,191,199\n2015,H27,18,6,43,32,146,189'
    creat_csv(id, str)
    create_json(id)

    # json_file = open('../testSheets/test.json', 'r')
    # dict = json.load(json_file)
    # for item in dict["items"]:
    #     print(item["ad"])
    # print(dict["items"])
