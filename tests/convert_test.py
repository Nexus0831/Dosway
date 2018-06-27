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
    str = 'ad,japanese_calendar,theater,sports_acilities,other,golf_course,mahjong,pachinko\n2011,H23,,6,44,33,215,212\n2012,H24,18,6,43,34,209,208\n2013,H25,19,6,43,33,185,204\n2014,H26,20,6,43,32,191,199\n2015,H27,18,6,43,32,146,189'
    converter.convert.create_csv(file_name, str, '../testSheets/')
    converter.convert.create_yaml(file_name, '../testSheets/')
    # converter.convert.create_xml(file_name, '../testSheets/')
    # converter.convert.remove_files('../testSheets/')

    # print(xml_file.readlines())
    print('test end')