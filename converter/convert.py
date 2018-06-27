import csv
import json
import yaml
import xmltodict
import openpyxl
import zipfile
import os
import collections


file_formats = ('.csv', '.tsv', '.json', '.yml', '.xml')


def create_csv(file_name, content, folder_path):
    with open(folder_path + file_name + '.csv', 'w', encoding='utf-8') as csv_file:
        csv_file.write(content)


def create_tsv(file_name, content, folder_path):
    with open(folder_path + file_name + '.tsv', 'w', encoding='utf-8') as tsv_file:
        tsv_file.write(content.replace(',', '   '))


def create_json(file_name, folder_path):
    result = []
    dict = {'id': file_name}
    with open(folder_path + file_name + '.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        for line in reader:
            result.append(line)
        dict["datas"] = result
        json_file = open(folder_path + file_name + '.json', 'w', encoding='utf-8')
        json.dump(dict, json_file, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
        json_file.close()


def represent_odict(dumper, instance):
    return dumper.represent_mapping('tag:yaml.org,2002:map', instance.datas())


def create_yaml(file_name, folder_path):
    result = []
    dict = {'id': file_name}
    with open(folder_path + file_name + '.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        yaml.add_representer(collections.OrderedDict, represent_odict)
        for line in reader:
            result.append(line)
        dict["datas"] = result
        yaml_file = open(folder_path + file_name + '.yml', 'w', encoding='utf-8')
        yaml.dump(dict, yaml_file, allow_unicode=True, default_flow_style=False)


def create_xml(file_name, folder_path):
    result = []
    with open(folder_path + file_name + '.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        for line in reader:
            result.append(line)

        dict = {
            'root': {
                'id': file_name,
                'datas': result
            }
        }

        xml_file = open(folder_path + file_name + '.xml', 'w', encoding='utf-8')
        xmltodict.unparse(dict, xml_file, pretty=True)


def create_zip(file_name, folder_path):
    with zipfile.ZipFile(folder_path + file_name + '.zip', 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
        for file_format in file_formats:
            new_zip.write(folder_path + file_name + file_format, arcname=file_name + file_format)
            os.remove(folder_path + file_name + file_format)


def remove_files(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))


# if __name__ == '__main__':
#     id = 'firstTest'
#     str = 'ad,japanese_calendar,theater,sports_acilities,other,golf_course,mahjong,pachinko\n2011,H23,20,6,44,33,215,212\n2012,H24,18,6,43,34,209,208\n2013,H25,19,6,43,33,185,204\n2014,H26,20,6,43,32,191,199\n2015,H27,18,6,43,32,146,189'
#     create_tsv(id, str, '..')
