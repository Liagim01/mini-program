'''
This file contains the test cases for xmltodict library.
'''
import unittest
import xmltodict
class TestXmlToDict(unittest.TestCase):
    def test_parse(self):
        xml_content = '<root><key>value</key></root>'
        expected_dict = {'root': {'key': 'value'}}
        result_dict = xmltodict.parse(xml_content)
        self.assertEqual(result_dict, expected_dict)
if __name__ == '__main__':
    unittest.main()