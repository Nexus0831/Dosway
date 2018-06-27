import csv
import json
import yaml
import xml
import zipfile
import os
import collections

indent = 2

file_formats = ('.csv', '.tsv', '.json', '.yml')


def get_indent():
    return " " * indent


def create_csv(title, content, root_path):
    with open(root_path + '/download/' + title + '.csv', 'w', encoding='utf-8') as csv_file:
        csv_file.write(content)


def create_tsv(title, content, root_path):
    with open(root_path + '/download/' + title + '.tsv', 'w', encoding='utf-8') as tsv_file:
        tsv_file.write(content.replace(',', '   '))


def create_json(title, root_path):
    result = []
    dict = {'id': title}
    with open(root_path + '/download/' + title + '.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        for line in reader:
            result.append(line)
        dict["items"] = result
        json_file = open(root_path + '/download/' + title + '.json', 'w', encoding='utf-8')
        json.dump(dict, json_file, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
        json_file.close()


def represent_odict(dumper, instance):
    return dumper.represent_mapping('tag:yaml.org,2002:map', instance.items())


def create_yaml(title, root_path):
    result = []
    dict = {'id': title}
    with open(root_path + '/download/' + title + '.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        yaml.add_representer(collections.OrderedDict, represent_odict)
        for line in reader:
            result.append(line)
        dict["items"] = result
        yaml_file = open(root_path + '/download/' + title + '.yml', 'w', encoding='utf-8')
        yaml.dump(dict, yaml_file, allow_unicode=True)


def create_zip(title, root_path):
    base_dir = root_path + '/download/' + title
    with zipfile.ZipFile(base_dir + '.zip', 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
        for file_format in file_formats:
            new_zip.write(base_dir + file_format, arcname=title + file_format)
            os.remove(base_dir + file_format)


# if __name__ == '__main__':
#     id = 'firstTest'
#     str = 'ad,japanese_calendar,theater,sports_acilities,other,golf_course,mahjong,pachinko\n2011,H23,20,6,44,33,215,212\n2012,H24,18,6,43,34,209,208\n2013,H25,19,6,43,33,185,204\n2014,H26,20,6,43,32,191,199\n2015,H27,18,6,43,32,146,189'
#     create_tsv(id, str, '..')
