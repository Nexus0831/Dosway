import converter
import xmltodict
import unittest


def xml_load_test():
    with open('../testSheets/' + file_name + '.xml', 'r', encoding='utf-8') as xml_file:
        # print(xml_file.read())
        dict = xmltodict.parse(xml_file.read())
        dict2 = dict['root']

        for item in dict2['items']:
            print('item start')
            for key, value in item.items():
                print(key + ': ' + value)
            print('item end')


if __name__ == '__main__':
    print('test start')
    file_name = 'firstTest'
    # converter.convert.create_yaml(file_name, '../testSheets/')
    # converter.convert.create_xml(file_name, '../testSheets/')
    converter.convert.remove_files('../testSheets/')

    # print(xml_file.readlines())
    print('test end')