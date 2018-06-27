import converter
import unittest


if __name__ == '__main__':
    print('test start')
    file_name = 'firstTest'
    converter.convert.create_yaml(file_name, '../testSheets/')
    print('test end')