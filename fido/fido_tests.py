import unittest, re

from fido import Fido


mime_types = []
def handle_matches(fullname, matches, delta_t, matchtype):
    while mime_types: del mime_types[0]
    for f,s in matches:
        mime_element = f.find("mime")
        mimetype = mime_element.text if mime_element != None else ""
        puid_element = f.find("puid")
        puid = puid_element.text if puid_element != None else ""

        if mimetype not in mime_types:
            mime_types.append((mimetype, matchtype, puid))

# This Class contains tests for the conversion of PRONOM regexs to pyhhon re's
class convert_to_regex(unittest.TestCase):
    def setUp(self):
        self.fidoObj = Fido(handle_matches=handle_matches)

    def tearDown(self):
        pass

    def test_file_1(self):
        self.fidoObj.identify_file("test_files/application/vnd.ms-excel/1.xls")
        self.assertEqual(mime_types, [('', 'signature', 'fmt/111')])

    def test_file_2(self):
        self.fidoObj.identify_file("test_files/application/msword/1.doc")
        self.assertEqual(mime_types, [('', 'signature', 'fmt/111')])

    def test_file_3(self):
        self.fidoObj.identify_file("test_files/application/x-executable/1")
        self.assertEqual(mime_types, [])

    def test_file_4(self):
        self.fidoObj.identify_file("test_files/application/x-gzip/1.gz")
        self.assertEqual(mime_types, [('application/x-gzip', 'signature', 'x-fmt/266')])

    def test_file_5(self):
        self.fidoObj.identify_file("test_files/application/vnd.oasis.opendocument.spreadsheet/1.ods")
        self.assertEqual(mime_types, [('', 'signature', 'fmt/295')])

    def test_file_6(self):
        self.fidoObj.identify_file("test_files/application/rss+xml/1.rss")
        self.assertEqual(mime_types, [('text/xml', 'signature', 'fmt/101')])

    def test_file_7(self):
        self.fidoObj.identify_file("test_files/application/x-tar/1.tar")
        self.assertEqual(mime_types, [('application/x-tar', 'signature', 'x-fmt/265')])

    def test_file_8(self):
        self.fidoObj.identify_file("test_files/application/pdf/1.pdf")
        self.assertEqual(mime_types, [('application/pdf', 'signature', 'fmt/18')])

    def test_file_9(self):
        self.fidoObj.identify_file("test_files/application/vnd.oasis.opendocument.text/1.odt")
        self.assertEqual(mime_types, [('', 'signature', 'fmt/291')])

    def test_file_10(self):
        self.fidoObj.identify_file("test_files/application/zip/1.zip")
        self.assertEqual(mime_types, [('application/zip', 'signature', 'x-fmt/263')])

    def test_file_11(self):
        self.fidoObj.identify_file("test_files/audio/x-wav/1.wav")
        self.assertEqual(mime_types, [('audio/x-wav', 'signature', 'fmt/6')])

    def test_file_12(self):
        self.fidoObj.identify_file("test_files/text/css/1.css")
        self.assertEqual(mime_types, [('', 'extension', 'x-fmt/145'), ('text/css', 'extension', 'x-fmt/224')])

    def test_file_13(self):
        self.fidoObj.identify_file("test_files/text/css/1.css")
        self.assertEqual(mime_types, [('', 'extension', 'x-fmt/145'), ('text/css', 'extension', 'x-fmt/224')])

    def test_file_14(self):
        self.fidoObj.identify_file("test_files/text/html/1.html")
        self.assertEqual(mime_types, [('text/html', 'signature', 'fmt/96')])

    def test_file_15(self):
        self.fidoObj.identify_file("test_files/text/csv/1.csv")
        self.assertEqual(mime_types, [('text/csv', 'extension', 'x-fmt/18')])

    def test_file_16(self):
        self.fidoObj.identify_file("test_files/text/plain/1.txt")
        self.assertEqual(mime_types, [('text/plain', 'extension', 'x-fmt/111')])

    def test_file_17(self):
        self.fidoObj.identify_file("test_files/image/tiff/1.tiff")
        self.assertEqual(mime_types, [('image/tiff', 'signature', 'fmt/10'), ('image/tiff', 'signature', 'fmt/7'), ('image/tiff', 'signature', 'fmt/8'), ('image/tiff', 'signature', 'fmt/9')])

    def test_file_18(self):
        self.fidoObj.identify_file("test_files/image/png/1.png")
        self.assertEqual(mime_types, [('image/png', 'signature', 'fmt/12')])

    def test_file_19(self):
        self.fidoObj.identify_file("test_files/image/jpeg/1.jpg")
        self.assertEqual(mime_types, [('image/jpeg', 'signature', 'fmt/43')])

    def test_file_20(self):
        self.fidoObj.identify_file("test_files/image/gif/1.gif")
        self.assertEqual(mime_types, [('image/gif', 'signature', 'fmt/4')])

    def test_file_21(self):
        self.fidoObj.identify_file("test_files/xml/2.xml")
        self.assertEqual(mime_types, [('text/xml', 'signature', 'fmt/101')])

    def test_file_22(self):
        self.fidoObj.identify_file("test_files/xml/1.xml")
        self.assertEqual(mime_types, [('text/xml', 'extension', 'fmt/120'), ('text/xml', 'extension', 'fmt/121')])

    def test_file_23(self):
        self.fidoObj.identify_file("test_files/xml/1.xml")
        self.assertEqual(mime_types, [('text/xml', 'extension', 'fmt/120'), ('text/xml', 'extension', 'fmt/121')])
 
if __name__ == '__main__':
    unittest.main()

