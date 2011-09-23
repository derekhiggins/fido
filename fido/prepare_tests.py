import unittest, re

import prepare


# This Class contains tests for the conversion of PRONOM regexs to pyhhon re's
class convert_to_regex(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    #Originally Taken from  fmt/100
    def test_convert_to_regex_0(self):
        self.assertEqual(prepare.convert_to_regex('3C21(444F4354595045|646F6374797065)20(48544D4C|68746D6C)20(5055424C4943|7075626C6963)20222D2F2F{1-16}2F2F(445444|647464)20{0-64}(48544D4C|68746D6C)20342E3031', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}<!(?:DOCTYPE|doctype) (?:HTML|html) (?:PUBLIC|public) "-//.{1,16}//(?:DTD|dtd) .{0,64}(?:HTML|html) 4\\.01')

    #Originally Taken from  fmt/101
    def test_convert_to_regex_1(self):
        self.assertEqual(prepare.convert_to_regex('3C3F786D6C2076657273696F6E3D(22|27)312E30(22|27)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A<\\?xml version=(?:"|\')1\\.0(?:"|\')')

    #Originally Taken from  fmt/102
    def test_convert_to_regex_2(self):
        self.assertEqual(prepare.convert_to_regex('3C21444F43545950452068746D6C205055424C494320222D2F2F5733432F2F445444205848544D4C20312E30', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1\\.0')

    #Originally Taken from  fmt/102
    def test_convert_to_regex_3(self):
        self.assertEqual(prepare.convert_to_regex('3C68746D6C20786D6C6E733D22687474703A2F2F7777772E77332E6F72672F313939392F7868746D6C22*3C7469746C653E*3C2F7469746C653E', 'Little', 'VAR', '0', ''), 
            '(?s)<html xmlns="http://www\\.w3\\.org/1999/xhtml".*<title>.*</title>')

    #Originally Taken from  fmt/103
    def test_convert_to_regex_4(self):
        self.assertEqual(prepare.convert_to_regex('3C21444F43545950452068746D6C205055424C494320222D2F2F5733432F2F445444205848544D4C20312E31', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1\\.1')

    #Originally Taken from  fmt/103
    def test_convert_to_regex_5(self):
        self.assertEqual(prepare.convert_to_regex('3C68746D6C20786D6C6E733D22687474703A2F2F7777772E77332E6F72672F313939392F7868746D6C22*3C7469746C653E*3C2F7469746C653E', 'Little', 'VAR', '0', ''), 
            '(?s)<html xmlns="http://www\\.w3\\.org/1999/xhtml".*<title>.*</title>')

    #Originally Taken from  fmt/104
    def test_convert_to_regex_6(self):
        self.assertEqual(prepare.convert_to_regex('(43|46)575301', 'Little', 'BOF', '0', ''), 
            '(?s)\\A(?:C|F)WS\\x01')

    #Originally Taken from  fmt/104
    def test_convert_to_regex_7(self):
        self.assertEqual(prepare.convert_to_regex('0000', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00\\Z')

    #Originally Taken from  fmt/105
    def test_convert_to_regex_8(self):
        self.assertEqual(prepare.convert_to_regex('(43|46)575302', 'Little', 'BOF', '0', ''), 
            '(?s)\\A(?:C|F)WS\\x02')

    #Originally Taken from  fmt/105
    def test_convert_to_regex_9(self):
        self.assertEqual(prepare.convert_to_regex('0000', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00\\Z')

    #Originally Taken from  fmt/106
    def test_convert_to_regex_10(self):
        self.assertEqual(prepare.convert_to_regex('(43|46)575303', 'Little', 'BOF', '0', ''), 
            '(?s)\\A(?:C|F)WS\\x03')

    #Originally Taken from  fmt/106
    def test_convert_to_regex_11(self):
        self.assertEqual(prepare.convert_to_regex('0000', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00\\Z')

    #Originally Taken from  fmt/107
    def test_convert_to_regex_12(self):
        self.assertEqual(prepare.convert_to_regex('(43|46)575304', 'Little', 'BOF', '0', ''), 
            '(?s)\\A(?:C|F)WS\\x04')

    #Originally Taken from  fmt/107
    def test_convert_to_regex_13(self):
        self.assertEqual(prepare.convert_to_regex('0000', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00\\Z')

    #Originally Taken from  fmt/108
    def test_convert_to_regex_14(self):
        self.assertEqual(prepare.convert_to_regex('(43|46)575305', 'Little', 'BOF', '0', ''), 
            '(?s)\\A(?:C|F)WS\\x05')

    #Originally Taken from  fmt/108
    def test_convert_to_regex_15(self):
        self.assertEqual(prepare.convert_to_regex('0000', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00\\Z')

    #Originally Taken from  fmt/109
    def test_convert_to_regex_16(self):
        self.assertEqual(prepare.convert_to_regex('(43|46)575306', 'Little', 'BOF', '0', ''), 
            '(?s)\\A(?:C|F)WS\\x06')

    #Originally Taken from  fmt/109
    def test_convert_to_regex_17(self):
        self.assertEqual(prepare.convert_to_regex('0000', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00\\Z')

    #Originally Taken from  fmt/110
    def test_convert_to_regex_18(self):
        self.assertEqual(prepare.convert_to_regex('(43|46)575307', 'Little', 'BOF', '0', ''), 
            '(?s)\\A(?:C|F)WS\\x07')

    #Originally Taken from  fmt/110
    def test_convert_to_regex_19(self):
        self.assertEqual(prepare.convert_to_regex('0000', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00\\Z')

    #Originally Taken from  fmt/111
    def test_convert_to_regex_20(self):
        self.assertEqual(prepare.convert_to_regex('D0CF11E0A1B11AE1{20}FEFF', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xd0\\xcf\\x11\\xe0\\xa1\\xb1\\x1a\\xe1.{20}\\xfe\\xff')

    #Originally Taken from  fmt/112
    def test_convert_to_regex_21(self):
        self.assertEqual(prepare.convert_to_regex('FFD8FFE800205350494646000100(00|01|02|03|04){11}(00|01|02|03|04|05){9}FFE8', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xd8\\xff\\xe8\\x00 SPIFF\\x00\\x01\\x00(?:\\x00|\\x01|\\x02|\\x03|\\x04).{11}(?:\\x00|\\x01|\\x02|\\x03|\\x04|\\x05).{9}\\xff\\xe8')

    #Originally Taken from  fmt/114
    def test_convert_to_regex_22(self):
        self.assertEqual(prepare.convert_to_regex('0000{6}01(01|04|08)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00.{6}\\x01(?:\\x01|\\x04|\\x08)')

    #Originally Taken from  fmt/115
    def test_convert_to_regex_23(self):
        self.assertEqual(prepare.convert_to_regex('424D{4}00000000{4}0C000000{4}0100(01|04|08|18)00', 'Little', 'BOF', '0', ''), 
            '(?s)\\ABM.{4}\\x00\\x00\\x00\\x00.{4}\\x0c\\x00\\x00\\x00.{4}\\x01\\x00(?:\\x01|\\x04|\\x08|\\x18)\\x00')

    #Originally Taken from  fmt/116
    def test_convert_to_regex_24(self):
        self.assertEqual(prepare.convert_to_regex('424D{4}00000000{4}28000000{8}0100(01|04|08|18)00(00|01|02)000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\ABM.{4}\\x00\\x00\\x00\\x00.{4}\\(\\x00\\x00\\x00.{8}\\x01\\x00(?:\\x01|\\x04|\\x08|\\x18)\\x00(?:\\x00|\\x01|\\x02)\\x00\\x00\\x00')

    #Originally Taken from  fmt/117
    def test_convert_to_regex_25(self):
        self.assertEqual(prepare.convert_to_regex('424D{4}00000000{4}28000000{8}0100(10|20)0003000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\ABM.{4}\\x00\\x00\\x00\\x00.{4}\\(\\x00\\x00\\x00.{8}\\x01\\x00(?:\\x10| )\\x00\\x03\\x00\\x00\\x00')

    #Originally Taken from  fmt/118
    def test_convert_to_regex_26(self):
        self.assertEqual(prepare.convert_to_regex('424D{4}00000000{4}6C000000{8}0100(01|04|08|10|18|20)00(00|01|02|03)00000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\ABM.{4}\\x00\\x00\\x00\\x00.{4}l\\x00\\x00\\x00.{8}\\x01\\x00(?:\\x01|\\x04|\\x08|\\x10|\\x18| )\\x00(?:\\x00|\\x01|\\x02|\\x03)\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/119
    def test_convert_to_regex_27(self):
        self.assertEqual(prepare.convert_to_regex('424D{4}00000000{4}7C000000{8}0100(01|04|08|10|18|20)00(00|01|02|03|04|05)00000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\ABM.{4}\\x00\\x00\\x00\\x00.{4}\\|\\x00\\x00\\x00.{8}\\x01\\x00(?:\\x01|\\x04|\\x08|\\x10|\\x18| )\\x00(?:\\x00|\\x01|\\x02|\\x03|\\x04|\\x05)\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/11
    def test_convert_to_regex_28(self):
        self.assertEqual(prepare.convert_to_regex('89504E470D0A1A0A0000000D49484452', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x89PNG\\r\\n\\x1a\\n\\x00\\x00\\x00\\rIHDR')

    #Originally Taken from  fmt/11
    def test_convert_to_regex_29(self):
        self.assertEqual(prepare.convert_to_regex('0000000049454E44AE426082', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00\\x00\\x00IEND\\xaeB`\\x82\\Z')

    #Originally Taken from  fmt/120
    def test_convert_to_regex_30(self):
        self.assertEqual(prepare.convert_to_regex('{0-50}3C46696C65436F6C6C656374696F6E20{0-100}3C44524F494456657273696F6E3E{1-10}3C2F44524F494456657273696F6E3E', 'Little', 'BOF', '0', ''), 
            '(?s)\\A.{0,50}<FileCollection .{0,100}<DROIDVersion>.{1,10}</DROIDVersion>')

    #Originally Taken from  fmt/121
    def test_convert_to_regex_31(self):
        self.assertEqual(prepare.convert_to_regex('{0-50}3C46465369676E617475726546696C6520{0-100}56657273696F6E3D', 'Little', 'BOF', '0', ''), 
            '(?s)\\A.{0,50}<FFSignatureFile .{0,100}Version=')

    #Originally Taken from  fmt/122
    def test_convert_to_regex_32(self):
        self.assertEqual(prepare.convert_to_regex('252150532D41646F62652D322E3020455053462D312E32(0D|0A|0D0A|0A0D)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A%!PS-Adobe-2\\.0 EPSF-1\\.2(?:\\r|\\n|\\r\\n|\\n\\r)')

    #Originally Taken from  fmt/122
    def test_convert_to_regex_33(self):
        self.assertEqual(prepare.convert_to_regex('C5D0D3C6', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xc5\\xd0\\xd3\\xc6')

    #Originally Taken from  fmt/122
    def test_convert_to_regex_34(self):
        self.assertEqual(prepare.convert_to_regex('252150532D41646F62652D322E3020455053462D312E32(0D|0A|0D0A|0A0D)', 'Little', 'VAR', '0', ''), 
            '(?s)%!PS-Adobe-2\\.0 EPSF-1\\.2(?:\\r|\\n|\\r\\n|\\n\\r)')

    #Originally Taken from  fmt/123
    def test_convert_to_regex_35(self):
        self.assertEqual(prepare.convert_to_regex('252150532D41646F62652D322E3020455053462D322E30(0D|0A|0D0A|0A0D)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A%!PS-Adobe-2\\.0 EPSF-2\\.0(?:\\r|\\n|\\r\\n|\\n\\r)')

    #Originally Taken from  fmt/123
    def test_convert_to_regex_36(self):
        self.assertEqual(prepare.convert_to_regex('C5D0D3C6', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xc5\\xd0\\xd3\\xc6')

    #Originally Taken from  fmt/123
    def test_convert_to_regex_37(self):
        self.assertEqual(prepare.convert_to_regex('252150532D41646F62652D322E3020455053462D322E30(0D|0A|0D0A|0A0D)', 'Little', 'VAR', '0', ''), 
            '(?s)%!PS-Adobe-2\\.0 EPSF-2\\.0(?:\\r|\\n|\\r\\n|\\n\\r)')

    #Originally Taken from  fmt/124
    def test_convert_to_regex_38(self):
        self.assertEqual(prepare.convert_to_regex('252150532D41646F62652D332E3020455053462D332E30(0D|0A|0D0A|0A0D)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A%!PS-Adobe-3\\.0 EPSF-3\\.0(?:\\r|\\n|\\r\\n|\\n\\r)')

    #Originally Taken from  fmt/124
    def test_convert_to_regex_39(self):
        self.assertEqual(prepare.convert_to_regex('C5D0D3C6', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xc5\\xd0\\xd3\\xc6')

    #Originally Taken from  fmt/124
    def test_convert_to_regex_40(self):
        self.assertEqual(prepare.convert_to_regex('252150532D41646F62652D332E3020455053462D332E30(0D|0A|0D0A|0A0D)', 'Little', 'VAR', '0', ''), 
            '(?s)%!PS-Adobe-3\\.0 EPSF-3\\.0(?:\\r|\\n|\\r\\n|\\n\\r)')

    #Originally Taken from  fmt/124
    def test_convert_to_regex_41(self):
        self.assertEqual(prepare.convert_to_regex('252150532D41646F62652D332E3120455053462D332E30(0D|0A|0D0A|0A0D)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A%!PS-Adobe-3\\.1 EPSF-3\\.0(?:\\r|\\n|\\r\\n|\\n\\r)')

    #Originally Taken from  fmt/125
    def test_convert_to_regex_42(self):
        self.assertEqual(prepare.convert_to_regex('D0CF11E0A1B11AE1{20}FEFF', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xd0\\xcf\\x11\\xe0\\xa1\\xb1\\x1a\\xe1.{20}\\xfe\\xff')

    #Originally Taken from  fmt/125
    def test_convert_to_regex_43(self):
        self.assertEqual(prepare.convert_to_regex('50006F0077006500720050006F0069006E007400200044006F00630075006D0065006E007400', 'Little', 'VAR', '0', ''), 
            '(?s)P\\x00o\\x00w\\x00e\\x00r\\x00P\\x00o\\x00i\\x00n\\x00t\\x00 \\x00D\\x00o\\x00c\\x00u\\x00m\\x00e\\x00n\\x00t\\x00')

    #Originally Taken from  fmt/125
    def test_convert_to_regex_44(self):
        self.assertEqual(prepare.convert_to_regex('4D6963726F736F66742028522920506F776572506F696E74202852292057696E646F777320200007(00|01)0000F00300005F', 'Little', 'VAR', '0', ''), 
            '(?s)Microsoft \\(R\\) PowerPoint \\(R\\) Windows  \\x00\\x07(?:\\x00|\\x01)\\x00\\x00\\xf0\\x03\\x00\\x00_')

    #Originally Taken from  fmt/126
    def test_convert_to_regex_45(self):
        self.assertEqual(prepare.convert_to_regex('D0CF11E0A1B11AE1{20}FEFF', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xd0\\xcf\\x11\\xe0\\xa1\\xb1\\x1a\\xe1.{20}\\xfe\\xff')

    #Originally Taken from  fmt/126
    def test_convert_to_regex_46(self):
        self.assertEqual(prepare.convert_to_regex('50006F0077006500720050006F0069006E007400200044006F00630075006D0065006E007400', 'Little', 'VAR', '0', ''), 
            '(?s)P\\x00o\\x00w\\x00e\\x00r\\x00P\\x00o\\x00i\\x00n\\x00t\\x00 \\x00D\\x00o\\x00c\\x00u\\x00m\\x00e\\x00n\\x00t\\x00')

    #Originally Taken from  fmt/127
    def test_convert_to_regex_47(self):
        self.assertEqual(prepare.convert_to_regex('504B0304140000000000{20}6D696D65747970656170706C69636174696F6E2F766E642E73756E2E786D6C2E64726177*504B0304140000000000{20}6D6574612E786D6C3C3F786D6C2076657273696F6E3D22312E3022{383}6F66666963653A76657273696F6E3D22312E30223E', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04\\x14\\x00\\x00\\x00\\x00\\x00.{20}mimetypeapplication/vnd\\.sun\\.xml\\.draw.*PK\\x03\\x04\\x14\\x00\\x00\\x00\\x00\\x00.{20}meta\\.xml<\\?xml version="1\\.0".{383}office:version="1\\.0">')

    #Originally Taken from  fmt/128
    def test_convert_to_regex_48(self):
        self.assertEqual(prepare.convert_to_regex('504B0304140000000000{20}6D696D65747970656170706C69636174696F6E2F766E642E73756E2E786D6C2E777269746572*504B0304140000000000{20}6D6574612E786D6C3C3F786D6C2076657273696F6E3D22312E3022{322}6F66666963653A76657273696F6E3D22312E30223E', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04\\x14\\x00\\x00\\x00\\x00\\x00.{20}mimetypeapplication/vnd\\.sun\\.xml\\.writer.*PK\\x03\\x04\\x14\\x00\\x00\\x00\\x00\\x00.{20}meta\\.xml<\\?xml version="1\\.0".{322}office:version="1\\.0">')

    #Originally Taken from  fmt/129
    def test_convert_to_regex_49(self):
        self.assertEqual(prepare.convert_to_regex('504B0304140000000000{20}6D696D65747970656170706C69636174696F6E2F766E642E73756E2E786D6C2E63616C63*504B0304140000000000{20}6D6574612E786D6C3C3F786D6C2076657273696F6E3D22312E3022{322}6F66666963653A76657273696F6E3D22312E30223E', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04\\x14\\x00\\x00\\x00\\x00\\x00.{20}mimetypeapplication/vnd\\.sun\\.xml\\.calc.*PK\\x03\\x04\\x14\\x00\\x00\\x00\\x00\\x00.{20}meta\\.xml<\\?xml version="1\\.0".{322}office:version="1\\.0">')

    #Originally Taken from  fmt/12
    def test_convert_to_regex_50(self):
        self.assertEqual(prepare.convert_to_regex('89504E470D0A1A0A0000000D49484452*69434350', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x89PNG\\r\\n\\x1a\\n\\x00\\x00\\x00\\rIHDR.*iCCP')

    #Originally Taken from  fmt/12
    def test_convert_to_regex_51(self):
        self.assertEqual(prepare.convert_to_regex('0000000049454E44AE426082', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00\\x00\\x00IEND\\xaeB`\\x82\\Z')

    #Originally Taken from  fmt/12
    def test_convert_to_regex_52(self):
        self.assertEqual(prepare.convert_to_regex('89504E470D0A1A0A0000000D49484452*73504C54', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x89PNG\\r\\n\\x1a\\n\\x00\\x00\\x00\\rIHDR.*sPLT')

    #Originally Taken from  fmt/12
    def test_convert_to_regex_53(self):
        self.assertEqual(prepare.convert_to_regex('0000000049454E44AE426082', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00\\x00\\x00IEND\\xaeB`\\x82\\Z')

    #Originally Taken from  fmt/12
    def test_convert_to_regex_54(self):
        self.assertEqual(prepare.convert_to_regex('89504E470D0A1A0A0000000D49484452*73524742', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x89PNG\\r\\n\\x1a\\n\\x00\\x00\\x00\\rIHDR.*sRGB')

    #Originally Taken from  fmt/12
    def test_convert_to_regex_55(self):
        self.assertEqual(prepare.convert_to_regex('0000000049454E44AE426082', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00\\x00\\x00IEND\\xaeB`\\x82\\Z')

    #Originally Taken from  fmt/130
    def test_convert_to_regex_56(self):
        self.assertEqual(prepare.convert_to_regex('504B0304140000000000{20}6D696D65747970656170706C69636174696F6E2F766E642E73756E2E786D6C2E696D7072657373*504B0304140000000000{20}6D6574612E786D6C3C3F786D6C2076657273696F6E3D22312E3022{383}6F66666963653A76657273696F6E3D22312E30223E', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04\\x14\\x00\\x00\\x00\\x00\\x00.{20}mimetypeapplication/vnd\\.sun\\.xml\\.impress.*PK\\x03\\x04\\x14\\x00\\x00\\x00\\x00\\x00.{20}meta\\.xml<\\?xml version="1\\.0".{383}office:version="1\\.0">')

    #Originally Taken from  fmt/131
    def test_convert_to_regex_57(self):
        self.assertEqual(prepare.convert_to_regex('3026B2758E66CF11A6D900AA0062CE6C{12}0102', 'Little', 'BOF', '0', ''), 
            '(?s)\\A0&\\xb2u\\x8ef\\xcf\\x11\\xa6\\xd9\\x00\\xaa\\x00b\\xcel.{12}\\x01\\x02')

    #Originally Taken from  fmt/132
    def test_convert_to_regex_58(self):
        self.assertEqual(prepare.convert_to_regex('3026B2758E66CF11A6D900AA0062CE6C{12}0102', 'Little', 'BOF', '0', ''), 
            '(?s)\\A0&\\xb2u\\x8ef\\xcf\\x11\\xa6\\xd9\\x00\\xaa\\x00b\\xcel.{12}\\x01\\x02')

    #Originally Taken from  fmt/132
    def test_convert_to_regex_59(self):
        self.assertEqual(prepare.convert_to_regex('{30}9107DCB7B7A9CF118EE600C00C205365{8}409E69F84D5BCF11A8FD00805F5C442B{38}(6101|6201|6301)', 'Little', 'VAR', '0', ''), 
            '(?s).{30}\\x91\\x07\\xdc\\xb7\\xb7\\xa9\\xcf\\x11\\x8e\\xe6\\x00\\xc0\\x0c Se.{8}@\\x9ei\\xf8M\\[\\xcf\\x11\\xa8\\xfd\\x00\\x80_\\\\D\\+.{38}(?:a\\x01|b\\x01|c\\x01)')

    #Originally Taken from  fmt/133
    def test_convert_to_regex_60(self):
        self.assertEqual(prepare.convert_to_regex('3026B2758E66CF11A6D900AA0062CE6C{12}0102', 'Little', 'BOF', '0', ''), 
            '(?s)\\A0&\\xb2u\\x8ef\\xcf\\x11\\xa6\\xd9\\x00\\xaa\\x00b\\xcel.{12}\\x01\\x02')

    #Originally Taken from  fmt/133
    def test_convert_to_regex_61(self):
        self.assertEqual(prepare.convert_to_regex('{30}9107DCB7B7A9CF118EE600C00C205365{8}C0EF19BC4D5BCF11A8FD00805F5C442B{65}574D56(31|32|33)', 'Little', 'VAR', '0', ''), 
            '(?s).{30}\\x91\\x07\\xdc\\xb7\\xb7\\xa9\\xcf\\x11\\x8e\\xe6\\x00\\xc0\\x0c Se.{8}\\xc0\\xef\\x19\\xbcM\\[\\xcf\\x11\\xa8\\xfd\\x00\\x80_\\\\D\\+.{65}WMV(?:1|2|3)')

    #Originally Taken from  fmt/134
    def test_convert_to_regex_62(self):
        self.assertEqual(prepare.convert_to_regex('FFFB[10:EB]{46-1439}FFFB[10:EB]{46-1439}FFFB[10:EB]{46-1439}FFFB[10:EB]{46-1439}FFFB[10:EB]{7-500}000000{36-1426}', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xfb[\\x10-\\xeb].{46,1439}\\xff\\xfb[\\x10-\\xeb].{46,1439}\\xff\\xfb[\\x10-\\xeb].{46,1439}\\xff\\xfb[\\x10-\\xeb].{46,1439}\\xff\\xfb[\\x10-\\xeb].{7,500}\\x00\\x00\\x00.{36,1426}\\Z')

    #Originally Taken from  fmt/134
    def test_convert_to_regex_63(self):
        self.assertEqual(prepare.convert_to_regex('494433', 'Little', 'BOF', '0', ''), 
            '(?s)\\AID3')

    #Originally Taken from  fmt/134
    def test_convert_to_regex_64(self):
        self.assertEqual(prepare.convert_to_regex('FFF3[10:EB]{46-1439}FFF3[10:EB]{46-1439}FFF3[10:EB]{46-1439}FFF3[10:EB]{46-1439}FFF3[10:EB]{7-500}000000{36-1426}', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xf3[\\x10-\\xeb].{46,1439}\\xff\\xf3[\\x10-\\xeb].{46,1439}\\xff\\xf3[\\x10-\\xeb].{46,1439}\\xff\\xf3[\\x10-\\xeb].{46,1439}\\xff\\xf3[\\x10-\\xeb].{7,500}\\x00\\x00\\x00.{36,1426}\\Z')

    #Originally Taken from  fmt/134
    def test_convert_to_regex_65(self):
        self.assertEqual(prepare.convert_to_regex('494433', 'Little', 'BOF', '0', ''), 
            '(?s)\\AID3')

    #Originally Taken from  fmt/134
    def test_convert_to_regex_66(self):
        self.assertEqual(prepare.convert_to_regex('FFFA[10:EB]{46-1439}FFFA[10:EB]{46-1439}FFFA[10:EB]{46-1439}FFFA[10:EB]{46-1439}FFFA[10:EB]{7-500}000000{36-1426}', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xfa[\\x10-\\xeb].{46,1439}\\xff\\xfa[\\x10-\\xeb].{46,1439}\\xff\\xfa[\\x10-\\xeb].{46,1439}\\xff\\xfa[\\x10-\\xeb].{46,1439}\\xff\\xfa[\\x10-\\xeb].{7,500}\\x00\\x00\\x00.{36,1426}\\Z')

    #Originally Taken from  fmt/134
    def test_convert_to_regex_67(self):
        self.assertEqual(prepare.convert_to_regex('494433', 'Little', 'BOF', '0', ''), 
            '(?s)\\AID3')

    #Originally Taken from  fmt/134
    def test_convert_to_regex_68(self):
        self.assertEqual(prepare.convert_to_regex('FFF2[10:EB]{46-1439}FFF2[10:EB]{46-1439}FFF2[10:EB]{46-1439}FFF2[10:EB]{46-1439}FFF2[10:EB]{7-500}000000{36-1426}', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xf2[\\x10-\\xeb].{46,1439}\\xff\\xf2[\\x10-\\xeb].{46,1439}\\xff\\xf2[\\x10-\\xeb].{46,1439}\\xff\\xf2[\\x10-\\xeb].{46,1439}\\xff\\xf2[\\x10-\\xeb].{7,500}\\x00\\x00\\x00.{36,1426}\\Z')

    #Originally Taken from  fmt/134
    def test_convert_to_regex_69(self):
        self.assertEqual(prepare.convert_to_regex('494433', 'Little', 'BOF', '0', ''), 
            '(?s)\\AID3')

    #Originally Taken from  fmt/134
    def test_convert_to_regex_70(self):
        self.assertEqual(prepare.convert_to_regex('FFFB[10:EB]{46-1439}FFFB[10:EB]{46-1439}FFFB[10:EB]{46-1439}FFFB[10:EB]{46-1439}FFFB[10:EB]{46-1439}FFFB[10:EB]{46-1439}FFFB[10:EB]{46-1439}FFFB[10:EB]{46-1439}', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xfb[\\x10-\\xeb].{46,1439}\\xff\\xfb[\\x10-\\xeb].{46,1439}\\xff\\xfb[\\x10-\\xeb].{46,1439}\\xff\\xfb[\\x10-\\xeb].{46,1439}\\xff\\xfb[\\x10-\\xeb].{46,1439}\\xff\\xfb[\\x10-\\xeb].{46,1439}\\xff\\xfb[\\x10-\\xeb].{46,1439}\\xff\\xfb[\\x10-\\xeb].{46,1439}')

    #Originally Taken from  fmt/134
    def test_convert_to_regex_71(self):
        self.assertEqual(prepare.convert_to_regex('FFF3[10:EB]{46-1439}FFF3[10:EB]{46-1439}FFF3[10:EB]{46-1439}FFF3[10:EB]{46-1439}FFF3[10:EB]{46-1439}FFF3[10:EB]{46-1439}FFF3[10:EB]{46-1439}FFF3[10:EB]{46-1439}', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xf3[\\x10-\\xeb].{46,1439}\\xff\\xf3[\\x10-\\xeb].{46,1439}\\xff\\xf3[\\x10-\\xeb].{46,1439}\\xff\\xf3[\\x10-\\xeb].{46,1439}\\xff\\xf3[\\x10-\\xeb].{46,1439}\\xff\\xf3[\\x10-\\xeb].{46,1439}\\xff\\xf3[\\x10-\\xeb].{46,1439}\\xff\\xf3[\\x10-\\xeb].{46,1439}')

    #Originally Taken from  fmt/134
    def test_convert_to_regex_72(self):
        self.assertEqual(prepare.convert_to_regex('FFFA[10:EB]{46-1439}FFFA[10:EB]{46-1439}FFFA[10:EB]{46-1439}FFFA[10:EB]{46-1439}FFFA[10:EB]{46-1439}FFFA[10:EB]{46-1439}FFFA[10:EB]{46-1439}FFFA[10:EB]{46-1439}', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xfa[\\x10-\\xeb].{46,1439}\\xff\\xfa[\\x10-\\xeb].{46,1439}\\xff\\xfa[\\x10-\\xeb].{46,1439}\\xff\\xfa[\\x10-\\xeb].{46,1439}\\xff\\xfa[\\x10-\\xeb].{46,1439}\\xff\\xfa[\\x10-\\xeb].{46,1439}\\xff\\xfa[\\x10-\\xeb].{46,1439}\\xff\\xfa[\\x10-\\xeb].{46,1439}')

    #Originally Taken from  fmt/134
    def test_convert_to_regex_73(self):
        self.assertEqual(prepare.convert_to_regex('FFF2[10:EB]{46-1439}FFF2[10:EB]{46-1439}FFF2[10:EB]{46-1439}FFF2[10:EB]{46-1439}FFF2[10:EB]{46-1439}FFF2[10:EB]{46-1439}FFF2[10:EB]{46-1439}FFF2[10:EB]{46-1439}', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xf2[\\x10-\\xeb].{46,1439}\\xff\\xf2[\\x10-\\xeb].{46,1439}\\xff\\xf2[\\x10-\\xeb].{46,1439}\\xff\\xf2[\\x10-\\xeb].{46,1439}\\xff\\xf2[\\x10-\\xeb].{46,1439}\\xff\\xf2[\\x10-\\xeb].{46,1439}\\xff\\xf2[\\x10-\\xeb].{46,1439}\\xff\\xf2[\\x10-\\xeb].{46,1439}')

    #Originally Taken from  fmt/135
    def test_convert_to_regex_74(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E*6F66666963653A76657273696F6E3D22312E30', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\..*office:version="1\\.0')

    #Originally Taken from  fmt/136
    def test_convert_to_regex_75(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E74657874*6F66666963653A76657273696F6E3D22312E30', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.text.*office:version="1\\.0')

    #Originally Taken from  fmt/137
    def test_convert_to_regex_76(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E7370726561647368656574*6F66666963653A76657273696F6E3D22312E30', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.spreadsheet.*office:version="1\\.0')

    #Originally Taken from  fmt/138
    def test_convert_to_regex_77(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E70726573656E746174696F6E*6F66666963653A76657273696F6E3D22312E30', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.presentation.*office:version="1\\.0')

    #Originally Taken from  fmt/139
    def test_convert_to_regex_78(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E6772617068696373*6F66666963653A76657273696F6E3D22312E30', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.graphics.*office:version="1\\.0')

    #Originally Taken from  fmt/13
    def test_convert_to_regex_79(self):
        self.assertEqual(prepare.convert_to_regex('89504E470D0A1A0A0000000D49484452*69545874', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x89PNG\\r\\n\\x1a\\n\\x00\\x00\\x00\\rIHDR.*iTXt')

    #Originally Taken from  fmt/13
    def test_convert_to_regex_80(self):
        self.assertEqual(prepare.convert_to_regex('0000000049454E44AE426082', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00\\x00\\x00IEND\\xaeB`\\x82\\Z')

    #Originally Taken from  fmt/140
    def test_convert_to_regex_81(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E73756E2E786D6C2E62617365*6F66666963653A76657273696F6E3D22312E30', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.sun\\.xml\\.base.*office:version="1\\.0')

    #Originally Taken from  fmt/14
    def test_convert_to_regex_82(self):
        self.assertEqual(prepare.convert_to_regex('255044462D312E30', 'Little', 'BOF', '0', '144'), 
            '(?s)\\A.{0,144}%PDF-1\\.0')

    #Originally Taken from  fmt/14
    def test_convert_to_regex_83(self):
        self.assertEqual(prepare.convert_to_regex('2525454F(46|460A|460D|460D0A|460D00)', 'Little', 'EOF', '0', '64'), 
            '(?s)%%EO(?:F|F\\n|F\\r|F\\r\\n|F\\r\\x00).{0,64}\\Z')

    #Originally Taken from  fmt/15
    def test_convert_to_regex_84(self):
        self.assertEqual(prepare.convert_to_regex('255044462D312E31', 'Little', 'BOF', '0', '144'), 
            '(?s)\\A.{0,144}%PDF-1\\.1')

    #Originally Taken from  fmt/15
    def test_convert_to_regex_85(self):
        self.assertEqual(prepare.convert_to_regex('2525454F(46|460A|460D|460D0A|460D00)', 'Little', 'EOF', '0', '64'), 
            '(?s)%%EO(?:F|F\\n|F\\r|F\\r\\n|F\\r\\x00).{0,64}\\Z')

    #Originally Taken from  fmt/161
    def test_convert_to_regex_86(self):
        self.assertEqual(prepare.convert_to_regex('504B0304', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04')

    #Originally Taken from  fmt/161
    def test_convert_to_regex_87(self):
        self.assertEqual(prepare.convert_to_regex('504B01{43-65531}504B0506{18-65531}', 'Little', 'EOF', '0', ''), 
            '(?s)PK\\x01.{43,65531}PK\\x05\\x06.{18,65531}\\Z')

    #Originally Taken from  fmt/161
    def test_convert_to_regex_88(self):
        self.assertEqual(prepare.convert_to_regex('786D6C6E733D22687474703A2F2F7777772E6261722E61646D696E2E63682F786D6C6E732F73696172642F312E302F6D657461646174612E78736422', 'Little', 'VAR', '1024', ''), 
            '(?s)xmlns="http://www\\.bar\\.admin\\.ch/xmlns/siard/1\\.0/metadata\\.xsd"')

    #Originally Taken from  fmt/16
    def test_convert_to_regex_89(self):
        self.assertEqual(prepare.convert_to_regex('255044462D312E32', 'Little', 'BOF', '0', '144'), 
            '(?s)\\A.{0,144}%PDF-1\\.2')

    #Originally Taken from  fmt/16
    def test_convert_to_regex_90(self):
        self.assertEqual(prepare.convert_to_regex('2525454F(46|460A|460D|460D0A|460D00)', 'Little', 'EOF', '0', '64'), 
            '(?s)%%EO(?:F|F\\n|F\\r|F\\r\\n|F\\r\\x00).{0,64}\\Z')

    #Originally Taken from  fmt/17
    def test_convert_to_regex_91(self):
        self.assertEqual(prepare.convert_to_regex('255044462D312E33', 'Little', 'BOF', '0', '144'), 
            '(?s)\\A.{0,144}%PDF-1\\.3')

    #Originally Taken from  fmt/17
    def test_convert_to_regex_92(self):
        self.assertEqual(prepare.convert_to_regex('2525454F(46|460A|460D|460D0A|460D00)', 'Little', 'EOF', '0', '64'), 
            '(?s)%%EO(?:F|F\\n|F\\r|F\\r\\n|F\\r\\x00).{0,64}\\Z')

    #Originally Taken from  fmt/183
    def test_convert_to_regex_93(self):
        self.assertEqual(prepare.convert_to_regex('3330302C??2C{3}2C', 'Little', 'BOF', '0', ''), 
            '(?s)\\A300,.?,.{3},')

    #Originally Taken from  fmt/184
    def test_convert_to_regex_94(self):
        self.assertEqual(prepare.convert_to_regex('3338302C??2C{3}2C', 'Little', 'BOF', '0', ''), 
            '(?s)\\A380,.?,.{3},')

    #Originally Taken from  fmt/185
    def test_convert_to_regex_95(self):
        self.assertEqual(prepare.convert_to_regex('3339302C??2C{3}2C', 'Little', 'BOF', '0', ''), 
            '(?s)\\A390,.?,.{3},')

    #Originally Taken from  fmt/186
    def test_convert_to_regex_96(self):
        self.assertEqual(prepare.convert_to_regex('3430302C??2C{3}2C', 'Little', 'BOF', '0', ''), 
            '(?s)\\A400,.?,.{3},')

    #Originally Taken from  fmt/187
    def test_convert_to_regex_97(self):
        self.assertEqual(prepare.convert_to_regex('3432302C??2C{3}2C', 'Little', 'BOF', '0', ''), 
            '(?s)\\A420,.?,.{3},')

    #Originally Taken from  fmt/188
    def test_convert_to_regex_98(self):
        self.assertEqual(prepare.convert_to_regex('3433302C??2C{3}2C', 'Little', 'BOF', '0', ''), 
            '(?s)\\A430,.?,.{3},')

    #Originally Taken from  fmt/189
    def test_convert_to_regex_99(self):
        self.assertEqual(prepare.convert_to_regex('5B436F6E74656E745F54797065735D2E786D6C20A2', 'Little', 'BOF', '30', ''), 
            '(?s)\\A.{30}\\[Content_Types\\]\\.xml \\xa2')

    #Originally Taken from  fmt/189
    def test_convert_to_regex_100(self):
        self.assertEqual(prepare.convert_to_regex('504B0304*504B0102*504B0506', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.*PK\\x01\\x02.*PK\\x05\\x06')

    #Originally Taken from  fmt/18
    def test_convert_to_regex_101(self):
        self.assertEqual(prepare.convert_to_regex('255044462D312E34', 'Little', 'BOF', '0', '144'), 
            '(?s)\\A.{0,144}%PDF-1\\.4')

    #Originally Taken from  fmt/18
    def test_convert_to_regex_102(self):
        self.assertEqual(prepare.convert_to_regex('2525454F(46|460A|460D|460D0A|460D00)', 'Little', 'EOF', '0', '64'), 
            '(?s)%%EO(?:F|F\\n|F\\r|F\\r\\n|F\\r\\x00).{0,64}\\Z')

    #Originally Taken from  fmt/198
    def test_convert_to_regex_103(self):
        self.assertEqual(prepare.convert_to_regex('FFFC[10:EB]{45-1726}FFFC[10:EB]{45-1726}FFFC[10:EB]{45-1726}FFFC[10:EB]{45-1726}', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xfc[\\x10-\\xeb].{45,1726}\\xff\\xfc[\\x10-\\xeb].{45,1726}\\xff\\xfc[\\x10-\\xeb].{45,1726}\\xff\\xfc[\\x10-\\xeb].{45,1726}')

    #Originally Taken from  fmt/198
    def test_convert_to_regex_104(self):
        self.assertEqual(prepare.convert_to_regex('FFFD[10:EB]{45-1726}FFFD[10:EB]{45-1726}FFFD[10:EB]{45-1726}FFFD[10:EB]{45-1726}', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xfd[\\x10-\\xeb].{45,1726}\\xff\\xfd[\\x10-\\xeb].{45,1726}\\xff\\xfd[\\x10-\\xeb].{45,1726}\\xff\\xfd[\\x10-\\xeb].{45,1726}')

    #Originally Taken from  fmt/198
    def test_convert_to_regex_105(self):
        self.assertEqual(prepare.convert_to_regex('FFF4[10:EB]{45-1726}FFF4[10:EB]{45-1726}FFF4[10:EB]{45-1726}FFF4[10:EB]{45-1726}', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xf4[\\x10-\\xeb].{45,1726}\\xff\\xf4[\\x10-\\xeb].{45,1726}\\xff\\xf4[\\x10-\\xeb].{45,1726}\\xff\\xf4[\\x10-\\xeb].{45,1726}')

    #Originally Taken from  fmt/198
    def test_convert_to_regex_106(self):
        self.assertEqual(prepare.convert_to_regex('FFF5[10:EB]{45-1726}FFF5[10:EB]{45-1726}FFF5[10:EB]{45-1726}FFF5[10:EB]{45-1726}', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xf5[\\x10-\\xeb].{45,1726}\\xff\\xf5[\\x10-\\xeb].{45,1726}\\xff\\xf5[\\x10-\\xeb].{45,1726}\\xff\\xf5[\\x10-\\xeb].{45,1726}')

    #Originally Taken from  fmt/198
    def test_convert_to_regex_107(self):
        self.assertEqual(prepare.convert_to_regex('494433', 'Little', 'BOF', '0', ''), 
            '(?s)\\AID3')

    #Originally Taken from  fmt/198
    def test_convert_to_regex_108(self):
        self.assertEqual(prepare.convert_to_regex('FFFC[10:EB]{45-1726}FFFC[10:EB]{45-1726}FFFC[10:EB]{45-1726}FFFC[10:EB]{45-1726}FFFC[10:EB]{7-500}000000{36-1426}', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xfc[\\x10-\\xeb].{45,1726}\\xff\\xfc[\\x10-\\xeb].{45,1726}\\xff\\xfc[\\x10-\\xeb].{45,1726}\\xff\\xfc[\\x10-\\xeb].{45,1726}\\xff\\xfc[\\x10-\\xeb].{7,500}\\x00\\x00\\x00.{36,1426}\\Z')

    #Originally Taken from  fmt/198
    def test_convert_to_regex_109(self):
        self.assertEqual(prepare.convert_to_regex('494433', 'Little', 'BOF', '0', ''), 
            '(?s)\\AID3')

    #Originally Taken from  fmt/198
    def test_convert_to_regex_110(self):
        self.assertEqual(prepare.convert_to_regex('FFFD[10:EB]{45-1726}FFFD[10:EB]{45-1726}FFFD[10:EB]{45-1726}FFFD[10:EB]{45-1726}FFFD[10:EB]{7-500}000000{36-1426}', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xfd[\\x10-\\xeb].{45,1726}\\xff\\xfd[\\x10-\\xeb].{45,1726}\\xff\\xfd[\\x10-\\xeb].{45,1726}\\xff\\xfd[\\x10-\\xeb].{45,1726}\\xff\\xfd[\\x10-\\xeb].{7,500}\\x00\\x00\\x00.{36,1426}\\Z')

    #Originally Taken from  fmt/198
    def test_convert_to_regex_111(self):
        self.assertEqual(prepare.convert_to_regex('494433', 'Little', 'BOF', '0', ''), 
            '(?s)\\AID3')

    #Originally Taken from  fmt/198
    def test_convert_to_regex_112(self):
        self.assertEqual(prepare.convert_to_regex('FFF4[10:EB]{45-1726}FFF4[10:EB]{45-1726}FFF4[10:EB]{45-1726}FFF4[10:EB]{45-1726}FFF4[10:EB]{7-500}000000{36-1426}', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xf4[\\x10-\\xeb].{45,1726}\\xff\\xf4[\\x10-\\xeb].{45,1726}\\xff\\xf4[\\x10-\\xeb].{45,1726}\\xff\\xf4[\\x10-\\xeb].{45,1726}\\xff\\xf4[\\x10-\\xeb].{7,500}\\x00\\x00\\x00.{36,1426}\\Z')

    #Originally Taken from  fmt/198
    def test_convert_to_regex_113(self):
        self.assertEqual(prepare.convert_to_regex('494433', 'Little', 'BOF', '0', ''), 
            '(?s)\\AID3')

    #Originally Taken from  fmt/198
    def test_convert_to_regex_114(self):
        self.assertEqual(prepare.convert_to_regex('FFF5[10:EB]{45-1726}FFF5[10:EB]{45-1726}FFF5[10:EB]{45-1726}FFF5[10:EB]{45-1726}FFF5[10:EB]{7-500}000000{36-1426}', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xf5[\\x10-\\xeb].{45,1726}\\xff\\xf5[\\x10-\\xeb].{45,1726}\\xff\\xf5[\\x10-\\xeb].{45,1726}\\xff\\xf5[\\x10-\\xeb].{45,1726}\\xff\\xf5[\\x10-\\xeb].{7,500}\\x00\\x00\\x00.{36,1426}\\Z')

    #Originally Taken from  fmt/199
    def test_convert_to_regex_115(self):
        self.assertEqual(prepare.convert_to_regex('66747970{0-64}(6D703432|6D703431|69736F6D|69736F32){4-64}(6D6F6F76|6D646174|636D6F76)', 'Little', 'BOF', '4', ''), 
            '(?s)\\A.{4}ftyp.{0,64}(?:mp42|mp41|isom|iso2).{4,64}(?:moov|mdat|cmov)')

    #Originally Taken from  fmt/19
    def test_convert_to_regex_116(self):
        self.assertEqual(prepare.convert_to_regex('255044462D312E35', 'Little', 'BOF', '0', '144'), 
            '(?s)\\A.{0,144}%PDF-1\\.5')

    #Originally Taken from  fmt/19
    def test_convert_to_regex_117(self):
        self.assertEqual(prepare.convert_to_regex('2525454F(46|460A|460D|460D0A|460D00)', 'Little', 'EOF', '0', '64'), 
            '(?s)%%EO(?:F|F\\n|F\\r|F\\r\\n|F\\r\\x00).{0,64}\\Z')

    #Originally Taken from  fmt/1
    def test_convert_to_regex_118(self):
        self.assertEqual(prepare.convert_to_regex('52494646{4}57415645*62657874{350}0000{254-*}666D7420100000000100{14-*}64617461', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIFF.{4}WAVE.*bext.{350}\\x00\\x00.{254,}fmt \\x10\\x00\\x00\\x00\\x01\\x00.{14,}data')

    #Originally Taken from  fmt/1
    def test_convert_to_regex_119(self):
        self.assertEqual(prepare.convert_to_regex('52494646{4}57415645*62657874{350}0000{254-*}666D7420280000005000{38}6661637404000000{4}6D6578740C000000{12}64617461', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIFF.{4}WAVE.*bext.{350}\\x00\\x00.{254,}fmt \\(\\x00\\x00\\x00P\\x00.{38}fact\\x04\\x00\\x00\\x00.{4}mext\\x0c\\x00\\x00\\x00.{12}data')

    #Originally Taken from  fmt/203
    def test_convert_to_regex_120(self):
        self.assertEqual(prepare.convert_to_regex('4F6767530002{23}766F7262697300000000{19}4F676753', 'Little', 'BOF', '0', ''), 
            '(?s)\\AOggS\\x00\\x02.{23}vorbis\\x00\\x00\\x00\\x00.{19}OggS')

    #Originally Taken from  fmt/20
    def test_convert_to_regex_121(self):
        self.assertEqual(prepare.convert_to_regex('255044462D312E36', 'Little', 'BOF', '0', '144'), 
            '(?s)\\A.{0,144}%PDF-1\\.6')

    #Originally Taken from  fmt/20
    def test_convert_to_regex_122(self):
        self.assertEqual(prepare.convert_to_regex('2525454F(46|460A|460D|460D0A|460D00)', 'Little', 'EOF', '0', '64'), 
            '(?s)%%EO(?:F|F\\n|F\\r|F\\r\\n|F\\r\\x00).{0,64}\\Z')

    #Originally Taken from  fmt/217
    def test_convert_to_regex_123(self):
        self.assertEqual(prepare.convert_to_regex('4A4153432042524F57532046494C4500', 'Little', 'BOF', '0', ''), 
            '(?s)\\AJASC BROWS FILE\\x00')

    #Originally Taken from  fmt/21
    def test_convert_to_regex_124(self):
        self.assertEqual(prepare.convert_to_regex('4D43302E30', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMC0\\.0')

    #Originally Taken from  fmt/22
    def test_convert_to_regex_125(self):
        self.assertEqual(prepare.convert_to_regex('4143312E32', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1\\.2')

    #Originally Taken from  fmt/23
    def test_convert_to_regex_126(self):
        self.assertEqual(prepare.convert_to_regex('4143312E33', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1\\.3')

    #Originally Taken from  fmt/24
    def test_convert_to_regex_127(self):
        self.assertEqual(prepare.convert_to_regex('4143312E3430', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1\\.40')

    #Originally Taken from  fmt/255
    def test_convert_to_regex_128(self):
        self.assertEqual(prepare.convert_to_regex('41542654464F524D{4}(444A564D4449524D|444A5655494E464F)', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAT&TFORM.{4}(?:DJVMDIRM|DJVUINFO)')

    #Originally Taken from  fmt/25
    def test_convert_to_regex_129(self):
        self.assertEqual(prepare.convert_to_regex('4143312E3530', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1\\.50')

    #Originally Taken from  fmt/26
    def test_convert_to_regex_130(self):
        self.assertEqual(prepare.convert_to_regex('4143322E3130', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC2\\.10')

    #Originally Taken from  fmt/275
    def test_convert_to_regex_131(self):
        self.assertEqual(prepare.convert_to_regex('000100005374616E64617264204143452044420002000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x01\\x00\\x00Standard ACE DB\\x00\\x02\\x00\\x00\\x00')

    #Originally Taken from  fmt/275
    def test_convert_to_regex_132(self):
        self.assertEqual(prepare.convert_to_regex('410063006300650073007300560065007200730069006F006E{0-2048}300039002E00[30:39]00[30:39]', 'Little', 'VAR', '0', ''), 
            '(?s)A\\x00c\\x00c\\x00e\\x00s\\x00s\\x00V\\x00e\\x00r\\x00s\\x00i\\x00o\\x00n.{0,2048}0\\x009\\x00\\.\\x00[0-9]\\x00[0-9]')

    #Originally Taken from  fmt/276
    def test_convert_to_regex_133(self):
        self.assertEqual(prepare.convert_to_regex('255044462D312E37', 'Little', 'BOF', '0', '144'), 
            '(?s)\\A.{0,144}%PDF-1\\.7')

    #Originally Taken from  fmt/276
    def test_convert_to_regex_134(self):
        self.assertEqual(prepare.convert_to_regex('2525454F(46|460A|460D|460D0A|460D00)', 'Little', 'EOF', '0', '64'), 
            '(?s)%%EO(?:F|F\\n|F\\r|F\\r\\n|F\\r\\x00).{0,64}\\Z')

    #Originally Taken from  fmt/277
    def test_convert_to_regex_135(self):
        self.assertEqual(prepare.convert_to_regex('0000270A0000000000000000000000000000000000000000{4}E8030000{68}00000032', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\'\\n\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00.{4}\\xe8\\x03\\x00\\x00.{68}\\x00\\x00\\x002')

    #Originally Taken from  fmt/278
    def test_convert_to_regex_136(self):
        self.assertEqual(prepare.convert_to_regex('0D0A582D4D696D654F4C453A2050726F6475636564204279204D6963726F736F6674204D696D654F4C452056362E30302E{4}2E{4}0D0A', 'Little', 'VAR', '0', '1024'), 
            '(?s)\\r\\nX-MimeOLE: Produced By Microsoft MimeOLE V6\\.00\\..{4}\\..{4}\\r\\n')

    #Originally Taken from  fmt/278
    def test_convert_to_regex_137(self):
        self.assertEqual(prepare.convert_to_regex('0D0A582D436F6E7665727465642D42793A20456D61696C6368656D7920??2E', 'Little', 'BOF', '0', '4096'), 
            '(?s)\\A.{0,4096}\\r\\nX-Converted-By: Emailchemy .?\\.')

    #Originally Taken from  fmt/279
    def test_convert_to_regex_138(self):
        self.assertEqual(prepare.convert_to_regex('664C6143', 'Little', 'BOF', '0', '4'), 
            '(?s)\\A.{0,4}fLaC')

    #Originally Taken from  fmt/27
    def test_convert_to_regex_139(self):
        self.assertEqual(prepare.convert_to_regex('4143(322E3231|322E3232|31303031)', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC(?:2\\.21|2\\.22|1001)')

    #Originally Taken from  fmt/280
    def test_convert_to_regex_140(self):
        self.assertEqual(prepare.convert_to_regex('5C646F63756D656E74636C617373', 'Little', 'BOF', '0', '4096'), 
            '(?s)\\A.{0,4096}\\\\documentclass')

    #Originally Taken from  fmt/281
    def test_convert_to_regex_141(self):
        self.assertEqual(prepare.convert_to_regex('5C(7573657061636B6167657B|636861707465727B|73656374696F6E7B|73756273656374696F6E7B|626567696E7B)', 'Little', 'BOF', '0', '4096'), 
            '(?s)\\A.{0,4096}\\\\(?:usepackage\\{|chapter\\{|section\\{|subsection\\{|begin\\{)')

    #Originally Taken from  fmt/282
    def test_convert_to_regex_142(self):
        self.assertEqual(prepare.convert_to_regex('43444601', 'Little', 'BOF', '0', ''), 
            '(?s)\\ACDF\\x01')

    #Originally Taken from  fmt/283
    def test_convert_to_regex_143(self):
        self.assertEqual(prepare.convert_to_regex('43444602', 'Little', 'BOF', '0', ''), 
            '(?s)\\ACDF\\x02')

    #Originally Taken from  fmt/284
    def test_convert_to_regex_144(self):
        self.assertEqual(prepare.convert_to_regex('47524942{3}01', 'Little', 'BOF', '0', ''), 
            '(?s)\\AGRIB.{3}\\x01')

    #Originally Taken from  fmt/284
    def test_convert_to_regex_145(self):
        self.assertEqual(prepare.convert_to_regex('37373737', 'Little', 'EOF', '0', ''), 
            '(?s)7777\\Z')

    #Originally Taken from  fmt/285
    def test_convert_to_regex_146(self):
        self.assertEqual(prepare.convert_to_regex('47524942{3}02', 'Little', 'BOF', '0', ''), 
            '(?s)\\AGRIB.{3}\\x02')

    #Originally Taken from  fmt/285
    def test_convert_to_regex_147(self):
        self.assertEqual(prepare.convert_to_regex('37373737', 'Little', 'EOF', '0', ''), 
            '(?s)7777\\Z')

    #Originally Taken from  fmt/286
    def test_convert_to_regex_148(self):
        self.assertEqual(prepare.convert_to_regex('894844460D0A1A0A01', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x89HDF\\r\\n\\x1a\\n\\x01')

    #Originally Taken from  fmt/287
    def test_convert_to_regex_149(self):
        self.assertEqual(prepare.convert_to_regex('894844460D0A1A0A02', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x89HDF\\r\\n\\x1a\\n\\x02')

    #Originally Taken from  fmt/288
    def test_convert_to_regex_150(self):
        self.assertEqual(prepare.convert_to_regex('7674695F656E636F64696E673A53527C757466382D6E6C0D0A', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}vti_encoding:SR\\|utf8-nl\\r\\n')

    #Originally Taken from  fmt/289
    def test_convert_to_regex_151(self):
        self.assertEqual(prepare.convert_to_regex('574152432F{3-4}0D0A574152432D547970653A{0-13}0D0A{0-512}574152432D446174653A{0-1}{4}2D{2}2D{2}54{2}3A{2}3A{2}5A0D0A{0-512}0D0A0D0A', 'Little', 'VAR', '0', '4096'), 
            '(?s)WARC/.{3,4}\\r\\nWARC-Type:.{0,13}\\r\\n.{0,512}WARC-Date:.{0,1}.{4}-.{2}-.{2}T.{2}:.{2}:.{2}Z\\r\\n.{0,512}\\r\\n\\r\\n')

    #Originally Taken from  fmt/28
    def test_convert_to_regex_152(self):
        self.assertEqual(prepare.convert_to_regex('414331303032', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1002')

    #Originally Taken from  fmt/290
    def test_convert_to_regex_153(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E74657874*6F66666963653A76657273696F6E3D22312E3122', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.text.*office:version="1\\.1"')

    #Originally Taken from  fmt/290
    def test_convert_to_regex_154(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E74657874', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.text')

    #Originally Taken from  fmt/291
    def test_convert_to_regex_155(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E74657874*6F66666963653A76657273696F6E3D22312E3222', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.text.*office:version="1\\.2"')

    #Originally Taken from  fmt/292
    def test_convert_to_regex_156(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E70726573656E746174696F6E*6F66666963653A76657273696F6E3D22312E3122', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.presentation.*office:version="1\\.1"')

    #Originally Taken from  fmt/292
    def test_convert_to_regex_157(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E70726573656E746174696F6E', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.presentation')

    #Originally Taken from  fmt/293
    def test_convert_to_regex_158(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E70726573656E746174696F6E*6F66666963653A76657273696F6E3D22312E3222', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.presentation.*office:version="1\\.2"')

    #Originally Taken from  fmt/294
    def test_convert_to_regex_159(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E7370726561647368656574504B030414*6F66666963653A76657273696F6E3D22312E3122', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.spreadsheetPK\\x03\\x04\\x14.*office:version="1\\.1"')

    #Originally Taken from  fmt/294
    def test_convert_to_regex_160(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E7370726561647368656574504B030414', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.spreadsheetPK\\x03\\x04\\x14')

    #Originally Taken from  fmt/295
    def test_convert_to_regex_161(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E7370726561647368656574504B030414*6F66666963653A76657273696F6E3D22312E3222', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.spreadsheetPK\\x03\\x04\\x14.*office:version="1\\.2"')

    #Originally Taken from  fmt/296
    def test_convert_to_regex_162(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E6772617068696373*6F66666963653A76657273696F6E3D22312E3122', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.graphics.*office:version="1\\.1"')

    #Originally Taken from  fmt/296
    def test_convert_to_regex_163(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E6772617068696373', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.graphics')

    #Originally Taken from  fmt/297
    def test_convert_to_regex_164(self):
        self.assertEqual(prepare.convert_to_regex('504B0304{26}6D696D65747970656170706C69636174696F6E2F766E642E6F617369732E6F70656E646F63756D656E742E6772617068696373*6F66666963653A76657273696F6E3D22312E3222', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.{26}mimetypeapplication/vnd\\.oasis\\.opendocument\\.graphics.*office:version="1\\.2"')

    #Originally Taken from  fmt/298
    def test_convert_to_regex_165(self):
        self.assertEqual(prepare.convert_to_regex('12AF{6}08{120}F1', 'Little', 'BOF', '4', ''), 
            '(?s)\\A.{4}\\x12\\xaf.{6}\\x08.{120}\\xf1')

    #Originally Taken from  fmt/299
    def test_convert_to_regex_166(self):
        self.assertEqual(prepare.convert_to_regex('464C49420200{2}00{3}0000{2}00{5}0000{2}0000', 'Little', 'BOF', '0', ''), 
            '(?s)\\AFLIB\\x02\\x00.{2}\\x00.{3}\\x00\\x00.{2}\\x00.{5}\\x00\\x00.{2}\\x00\\x00')

    #Originally Taken from  fmt/29
    def test_convert_to_regex_167(self):
        self.assertEqual(prepare.convert_to_regex('414331303033', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1003')

    #Originally Taken from  fmt/2
    def test_convert_to_regex_168(self):
        self.assertEqual(prepare.convert_to_regex('52494646{4}57415645*62657874{350}0100{254-*}666D7420100000000100{14-*}64617461', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIFF.{4}WAVE.*bext.{350}\\x01\\x00.{254,}fmt \\x10\\x00\\x00\\x00\\x01\\x00.{14,}data')

    #Originally Taken from  fmt/2
    def test_convert_to_regex_169(self):
        self.assertEqual(prepare.convert_to_regex('52494646{4}57415645*62657874{350}0100{254-*}666D7420280000005000{38}6661637404000000{4}6D6578740C000000{12}64617461', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIFF.{4}WAVE.*bext.{350}\\x01\\x00.{254,}fmt \\(\\x00\\x00\\x00P\\x00.{38}fact\\x04\\x00\\x00\\x00.{4}mext\\x0c\\x00\\x00\\x00.{12}data')

    #Originally Taken from  fmt/300
    def test_convert_to_regex_170(self):
        self.assertEqual(prepare.convert_to_regex('2843484957524954455220342E', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\(CHIWRITER 4\\.')

    #Originally Taken from  fmt/301
    def test_convert_to_regex_171(self):
        self.assertEqual(prepare.convert_to_regex('42(45|65)(47|67)(4D|6D)(46|66)*(4D|6D)(46|66)(56|76)(65|45)(52|72)(53|73)(49|69)(4F|6F)(4E|6E){1}33', 'Little', 'BOF', '0', ''), 
            '(?s)\\AB(?:E|e)(?:G|g)(?:M|m)(?:F|f).*(?:M|m)(?:F|f)(?:V|v)(?:e|E)(?:R|r)(?:S|s)(?:I|i)(?:O|o)(?:N|n).{1}3')

    #Originally Taken from  fmt/301
    def test_convert_to_regex_172(self):
        self.assertEqual(prepare.convert_to_regex('45(4E|6E)(44|64)(4D|6D)(46|66){0-1}3B', 'Little', 'EOF', '0', '2048'), 
            '(?s)E(?:N|n)(?:D|d)(?:M|m)(?:F|f).{0,1};.{0,2048}\\Z')

    #Originally Taken from  fmt/301
    def test_convert_to_regex_173(self):
        self.assertEqual(prepare.convert_to_regex('42(45|65)(47|67)(4D|6D)(46|66)*(4D|6D)(46|66)(56|76)(65|45)(52|72)(53|73)(49|69)(4F|6F)(4E|6E){1}33', 'Little', 'BOF', '0', ''), 
            '(?s)\\AB(?:E|e)(?:G|g)(?:M|m)(?:F|f).*(?:M|m)(?:F|f)(?:V|v)(?:e|E)(?:R|r)(?:S|s)(?:I|i)(?:O|o)(?:N|n).{1}3')

    #Originally Taken from  fmt/301
    def test_convert_to_regex_174(self):
        self.assertEqual(prepare.convert_to_regex('65(4E|6E)(44|64)(4D|6D)(46|66){0-1}3B', 'Little', 'EOF', '0', '2048'), 
            '(?s)e(?:N|n)(?:D|d)(?:M|m)(?:F|f).{0,1};.{0,2048}\\Z')

    #Originally Taken from  fmt/301
    def test_convert_to_regex_175(self):
        self.assertEqual(prepare.convert_to_regex('62(45|65)(47|67)(4D|6D)(46|66)*(4D|6D)(46|66)(56|76)(65|45)(52|72)(53|73)(49|69)(4F|6F)(4E|6E){1}33', 'Little', 'BOF', '0', ''), 
            '(?s)\\Ab(?:E|e)(?:G|g)(?:M|m)(?:F|f).*(?:M|m)(?:F|f)(?:V|v)(?:e|E)(?:R|r)(?:S|s)(?:I|i)(?:O|o)(?:N|n).{1}3')

    #Originally Taken from  fmt/301
    def test_convert_to_regex_176(self):
        self.assertEqual(prepare.convert_to_regex('45(4E|6E)(44|64)(4D|6D)(46|66){0-1}3B', 'Little', 'EOF', '0', '2048'), 
            '(?s)E(?:N|n)(?:D|d)(?:M|m)(?:F|f).{0,1};.{0,2048}\\Z')

    #Originally Taken from  fmt/301
    def test_convert_to_regex_177(self):
        self.assertEqual(prepare.convert_to_regex('62(45|65)(47|67)(4D|6D)(46|66)*(4D|6D)(46|66)(56|76)(65|45)(52|72)(53|73)(49|69)(4F|6F)(4E|6E){1}33', 'Little', 'BOF', '0', ''), 
            '(?s)\\Ab(?:E|e)(?:G|g)(?:M|m)(?:F|f).*(?:M|m)(?:F|f)(?:V|v)(?:e|E)(?:R|r)(?:S|s)(?:I|i)(?:O|o)(?:N|n).{1}3')

    #Originally Taken from  fmt/301
    def test_convert_to_regex_178(self):
        self.assertEqual(prepare.convert_to_regex('65(4E|6E)(44|64)(4D|6D)(46|66){0-1}3B', 'Little', 'EOF', '0', '2048'), 
            '(?s)e(?:N|n)(?:D|d)(?:M|m)(?:F|f).{0,1};.{0,2048}\\Z')

    #Originally Taken from  fmt/302
    def test_convert_to_regex_179(self):
        self.assertEqual(prepare.convert_to_regex('42(45|65)(47|67)(4D|6D)(46|66)*(4D|6D)(46|66)(56|76)(65|45)(52|72)(53|73)(49|69)(4F|6F)(4E|6E){1}34', 'Little', 'BOF', '0', ''), 
            '(?s)\\AB(?:E|e)(?:G|g)(?:M|m)(?:F|f).*(?:M|m)(?:F|f)(?:V|v)(?:e|E)(?:R|r)(?:S|s)(?:I|i)(?:O|o)(?:N|n).{1}4')

    #Originally Taken from  fmt/302
    def test_convert_to_regex_180(self):
        self.assertEqual(prepare.convert_to_regex('45(4E|6E)(44|64)(4D|6D)(46|66){0-1}3B', 'Little', 'EOF', '0', '2048'), 
            '(?s)E(?:N|n)(?:D|d)(?:M|m)(?:F|f).{0,1};.{0,2048}\\Z')

    #Originally Taken from  fmt/302
    def test_convert_to_regex_181(self):
        self.assertEqual(prepare.convert_to_regex('42(45|65)(47|67)(4D|6D)(46|66)*(4D|6D)(46|66)(56|76)(65|45)(52|72)(53|73)(49|69)(4F|6F)(4E|6E){1}34', 'Little', 'BOF', '0', ''), 
            '(?s)\\AB(?:E|e)(?:G|g)(?:M|m)(?:F|f).*(?:M|m)(?:F|f)(?:V|v)(?:e|E)(?:R|r)(?:S|s)(?:I|i)(?:O|o)(?:N|n).{1}4')

    #Originally Taken from  fmt/302
    def test_convert_to_regex_182(self):
        self.assertEqual(prepare.convert_to_regex('65(4E|6E)(44|64)(4D|6D)(46|66){0-1}3B', 'Little', 'EOF', '0', '2048'), 
            '(?s)e(?:N|n)(?:D|d)(?:M|m)(?:F|f).{0,1};.{0,2048}\\Z')

    #Originally Taken from  fmt/302
    def test_convert_to_regex_183(self):
        self.assertEqual(prepare.convert_to_regex('62(45|65)(47|67)(4D|6D)(46|66)*(4D|6D)(46|66)(56|76)(65|45)(52|72)(53|73)(49|69)(4F|6F)(4E|6E){1}34', 'Little', 'BOF', '0', ''), 
            '(?s)\\Ab(?:E|e)(?:G|g)(?:M|m)(?:F|f).*(?:M|m)(?:F|f)(?:V|v)(?:e|E)(?:R|r)(?:S|s)(?:I|i)(?:O|o)(?:N|n).{1}4')

    #Originally Taken from  fmt/302
    def test_convert_to_regex_184(self):
        self.assertEqual(prepare.convert_to_regex('45(4E|6E)(44|64)(4D|6D)(46|66){0-1}3B', 'Little', 'EOF', '0', '2048'), 
            '(?s)E(?:N|n)(?:D|d)(?:M|m)(?:F|f).{0,1};.{0,2048}\\Z')

    #Originally Taken from  fmt/302
    def test_convert_to_regex_185(self):
        self.assertEqual(prepare.convert_to_regex('62(45|65)(47|67)(4D|6D)(46|66)*(4D|6D)(46|66)(56|76)(65|45)(52|72)(53|73)(49|69)(4F|6F)(4E|6E){1}34', 'Little', 'BOF', '0', ''), 
            '(?s)\\Ab(?:E|e)(?:G|g)(?:M|m)(?:F|f).*(?:M|m)(?:F|f)(?:V|v)(?:e|E)(?:R|r)(?:S|s)(?:I|i)(?:O|o)(?:N|n).{1}4')

    #Originally Taken from  fmt/302
    def test_convert_to_regex_186(self):
        self.assertEqual(prepare.convert_to_regex('65(4E|6E)(44|64)(4D|6D)(46|66){0-1}3B', 'Little', 'EOF', '0', '2048'), 
            '(?s)e(?:N|n)(?:D|d)(?:M|m)(?:F|f).{0,1};.{0,2048}\\Z')

    #Originally Taken from  fmt/303
    def test_convert_to_regex_187(self):
        self.assertEqual(prepare.convert_to_regex('00[20:3F]*10220001', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00[ -\\?].*\\x10"\\x00\\x01')

    #Originally Taken from  fmt/303
    def test_convert_to_regex_188(self):
        self.assertEqual(prepare.convert_to_regex('0040', 'Little', 'EOF', '0', '1024'), 
            '(?s)\\x00@.{0,1024}\\Z')

    #Originally Taken from  fmt/304
    def test_convert_to_regex_189(self):
        self.assertEqual(prepare.convert_to_regex('00[20:3F]*10220002', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00[ -\\?].*\\x10"\\x00\\x02')

    #Originally Taken from  fmt/304
    def test_convert_to_regex_190(self):
        self.assertEqual(prepare.convert_to_regex('0040', 'Little', 'EOF', '0', '1024'), 
            '(?s)\\x00@.{0,1024}\\Z')

    #Originally Taken from  fmt/305
    def test_convert_to_regex_191(self):
        self.assertEqual(prepare.convert_to_regex('00[20:3F]*10220003', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00[ -\\?].*\\x10"\\x00\\x03')

    #Originally Taken from  fmt/305
    def test_convert_to_regex_192(self):
        self.assertEqual(prepare.convert_to_regex('0040', 'Little', 'EOF', '0', '1024'), 
            '(?s)\\x00@.{0,1024}\\Z')

    #Originally Taken from  fmt/306
    def test_convert_to_regex_193(self):
        self.assertEqual(prepare.convert_to_regex('00[20:3F]*10220004', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00[ -\\?].*\\x10"\\x00\\x04')

    #Originally Taken from  fmt/306
    def test_convert_to_regex_194(self):
        self.assertEqual(prepare.convert_to_regex('0040', 'Little', 'EOF', '0', '1024'), 
            '(?s)\\x00@.{0,1024}\\Z')

    #Originally Taken from  fmt/307
    def test_convert_to_regex_195(self):
        self.assertEqual(prepare.convert_to_regex('21547970653A*5E', 'Little', 'BOF', '0', '64'), 
            '(?s)\\A.{0,64}!Type:.*\\^')

    #Originally Taken from  fmt/308
    def test_convert_to_regex_196(self):
        self.assertEqual(prepare.convert_to_regex('AC9EBD8F0000??00', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xac\\x9e\\xbd\\x8f\\x00\\x00.?\\x00')

    #Originally Taken from  fmt/309
    def test_convert_to_regex_197(self):
        self.assertEqual(prepare.convert_to_regex('4F46584845414445523A313030{0-2}444154413A*56455253494F4E3A313032{0-2}53454355524954593A*454E434F44494E473A*434841525345543A*434F4D5052455353494F4E3A*4F4C4446494C455549443A*4E455746494C455549443A', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}OFXHEADER:100.{0,2}DATA:.*VERSION:102.{0,2}SECURITY:.*ENCODING:.*CHARSET:.*COMPRESSION:.*OLDFILEUID:.*NEWFILEUID:')

    #Originally Taken from  fmt/30
    def test_convert_to_regex_198(self):
        self.assertEqual(prepare.convert_to_regex('414331303034', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1004')

    #Originally Taken from  fmt/310
    def test_convert_to_regex_199(self):
        self.assertEqual(prepare.convert_to_regex('4F46584845414445523A313030{0-2}444154413A*56455253494F4E3A313033{0-2}53454355524954593A*454E434F44494E473A*434841525345543A*434F4D5052455353494F4E3A*4F4C4446494C455549443A*4E455746494C455549443A', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}OFXHEADER:100.{0,2}DATA:.*VERSION:103.{0,2}SECURITY:.*ENCODING:.*CHARSET:.*COMPRESSION:.*OLDFILEUID:.*NEWFILEUID:')

    #Originally Taken from  fmt/311
    def test_convert_to_regex_200(self):
        self.assertEqual(prepare.convert_to_regex('4F46584845414445523A3130300D0A444154413A*0D0A56455253494F4E3A3136300D0A53454355524954593A*0D0A454E434F44494E473A*0D0A434841525345543A*0D0A434F4D5052455353494F4E3A*0D0A4F4C4446494C455549443A*0D0A4E455746494C455549443A', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}OFXHEADER:100\\r\\nDATA:.*\\r\\nVERSION:160\\r\\nSECURITY:.*\\r\\nENCODING:.*\\r\\nCHARSET:.*\\r\\nCOMPRESSION:.*\\r\\nOLDFILEUID:.*\\r\\nNEWFILEUID:')

    #Originally Taken from  fmt/312
    def test_convert_to_regex_201(self):
        self.assertEqual(prepare.convert_to_regex('4F46584845414445523D(22|27)323030(22|27)0D0A56455253494F4E3D(22|27)323033(22|27)0D0A53454355524954593D(22|27)*(22|27)0D0A4F4C4446494C455549443D(22|27)*(22|27)0D0A4E455746494C455549443D', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}OFXHEADER=(?:"|\')200(?:"|\')\\r\\nVERSION=(?:"|\')203(?:"|\')\\r\\nSECURITY=(?:"|\').*(?:"|\')\\r\\nOLDFILEUID=(?:"|\').*(?:"|\')\\r\\nNEWFILEUID=')

    #Originally Taken from  fmt/313
    def test_convert_to_regex_202(self):
        self.assertEqual(prepare.convert_to_regex('4F46584845414445523D(22|27)323030(22|27)0D0A56455253494F4E3D(22|27)323131(22|27)0D0A53454355524954593D(22|27)*(22|27)0D0A4F4C4446494C455549443D(22|27)*(22|27)0D0A4E455746494C455549443D', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}OFXHEADER=(?:"|\')200(?:"|\')\\r\\nVERSION=(?:"|\')211(?:"|\')\\r\\nSECURITY=(?:"|\').*(?:"|\')\\r\\nOLDFILEUID=(?:"|\').*(?:"|\')\\r\\nNEWFILEUID=')

    #Originally Taken from  fmt/314
    def test_convert_to_regex_203(self):
        self.assertEqual(prepare.convert_to_regex('5053494400010076', 'Little', 'BOF', '0', ''), 
            '(?s)\\APSID\\x00\\x01\\x00v')

    #Originally Taken from  fmt/315
    def test_convert_to_regex_204(self):
        self.assertEqual(prepare.convert_to_regex('5053494400(01|02)007C', 'Little', 'BOF', '0', ''), 
            '(?s)\\APSID\\x00(?:\\x01|\\x02)\\x00\\|')

    #Originally Taken from  fmt/316
    def test_convert_to_regex_205(self):
        self.assertEqual(prepare.convert_to_regex('525349440002007C{4}0000', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARSID\\x00\\x02\\x00\\|.{4}\\x00\\x00')

    #Originally Taken from  fmt/317
    def test_convert_to_regex_206(self):
        self.assertEqual(prepare.convert_to_regex('58464952{4}3339564D70616D6918000000010000002C', 'Little', 'BOF', '0', ''), 
            '(?s)\\AXFIR.{4}39VMpami\\x18\\x00\\x00\\x00\\x01\\x00\\x00\\x00,')

    #Originally Taken from  fmt/318
    def test_convert_to_regex_207(self):
        self.assertEqual(prepare.convert_to_regex('53444A56', 'Little', 'BOF', '0', ''), 
            '(?s)\\ASDJV')

    #Originally Taken from  fmt/319
    def test_convert_to_regex_208(self):
        self.assertEqual(prepare.convert_to_regex('0000270AFFFFFE70000000000000000000000000000000000000{2}0000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\'\\n\\xff\\xff\\xfep\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00.{2}\\x00\\x00')

    #Originally Taken from  fmt/31
    def test_convert_to_regex_209(self):
        self.assertEqual(prepare.convert_to_regex('414331303036', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1006')

    #Originally Taken from  fmt/320
    def test_convert_to_regex_210(self):
        self.assertEqual(prepare.convert_to_regex('47454F474353*444154554D*53504845524F4944*5052494D454D*554E4954', 'Little', 'BOF', '0', '152'), 
            '(?s)\\A.{0,152}GEOGCS.*DATUM.*SPHEROID.*PRIMEM.*UNIT')

    #Originally Taken from  fmt/320
    def test_convert_to_regex_211(self):
        self.assertEqual(prepare.convert_to_regex('5D5D', 'Little', 'EOF', '0', ''), 
            '(?s)\\]\\]\\Z')

    #Originally Taken from  fmt/321
    def test_convert_to_regex_212(self):
        self.assertEqual(prepare.convert_to_regex('0000000001{35}2E{34}01', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x00\\x00\\x01.{35}\\..{34}\\x01')

    #Originally Taken from  fmt/322
    def test_convert_to_regex_213(self):
        self.assertEqual(prepare.convert_to_regex('5046460007020006', 'Little', 'BOF', '0', ''), 
            '(?s)\\APFF\\x00\\x07\\x02\\x00\\x06')

    #Originally Taken from  fmt/323
    def test_convert_to_regex_214(self):
        self.assertEqual(prepare.convert_to_regex('457874656E646564204D6F64756C653A20{20}1A', 'Little', 'BOF', '0', ''), 
            '(?s)\\AExtended Module: .{20}\\x1a')

    #Originally Taken from  fmt/324
    def test_convert_to_regex_215(self):
        self.assertEqual(prepare.convert_to_regex('0008(00|FF)(FF|00)0000(00|10)(10|00)525346545354594C(00100100|10000001)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x08(?:\\x00|\\xff)(?:\\xff|\\x00)\\x00\\x00(?:\\x00|\\x10)(?:\\x10|\\x00)RSFTSTYL(?:\\x00\\x10\\x01\\x00|\\x10\\x00\\x00\\x01)')

    #Originally Taken from  fmt/324
    def test_convert_to_regex_216(self):
        self.assertEqual(prepare.convert_to_regex('0008(00|FF)(FF|00)0000(00|10)(10|00)454E444E454E4654(00100100|10000001)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x08(?:\\x00|\\xff)(?:\\xff|\\x00)\\x00\\x00(?:\\x00|\\x10)(?:\\x10|\\x00)ENDNENFT(?:\\x00\\x10\\x01\\x00|\\x10\\x00\\x00\\x01)')

    #Originally Taken from  fmt/325
    def test_convert_to_regex_217(self):
        self.assertEqual(prepare.convert_to_regex('(01|03){2}[00:0F]{4}FE{0-1}3F{1}00{1}00{1}00', 'Little', 'BOF', '0', ''), 
            '(?s)\\A(?:\\x01|\\x03).{2}[\\x00-\\x0f].{4}\\xfe.{0,1}\\?.{1}\\x00.{1}\\x00.{1}\\x00')

    #Originally Taken from  fmt/325
    def test_convert_to_regex_218(self):
        self.assertEqual(prepare.convert_to_regex('(01|03){2}[00:0F]{4}FF{0-1}3F{1}00{1}00{1}00', 'Little', 'BOF', '0', ''), 
            '(?s)\\A(?:\\x01|\\x03).{2}[\\x00-\\x0f].{4}\\xff.{0,1}\\?.{1}\\x00.{1}\\x00.{1}\\x00')

    #Originally Taken from  fmt/325
    def test_convert_to_regex_219(self):
        self.assertEqual(prepare.convert_to_regex('0000{2}00{7}0000{2}0000{2}0002{8}202040404020000040404040', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00.{2}\\x00.{7}\\x00\\x00.{2}\\x00\\x00.{2}\\x00\\x02.{8}  @@@ \\x00\\x00@@@@')

    #Originally Taken from  fmt/326
    def test_convert_to_regex_220(self):
        self.assertEqual(prepare.convert_to_regex('454E444E454E5A33000000{5}000000260005{2}0000FFFFFFFF', 'Little', 'BOF', '0', ''), 
            '(?s)\\AENDNENZ3\\x00\\x00\\x00.{5}\\x00\\x00\\x00&\\x00\\x05.{2}\\x00\\x00\\xff\\xff\\xff\\xff')

    #Originally Taken from  fmt/327
    def test_convert_to_regex_221(self):
        self.assertEqual(prepare.convert_to_regex('454E444E454C3273000000{5}000000260003{2}0000FFFFFFFF', 'Little', 'BOF', '0', ''), 
            '(?s)\\AENDNEL2s\\x00\\x00\\x00.{5}\\x00\\x00\\x00&\\x00\\x03.{2}\\x00\\x00\\xff\\xff\\xff\\xff')

    #Originally Taken from  fmt/329
    def test_convert_to_regex_222(self):
        self.assertEqual(prepare.convert_to_regex('2321{0-1}2F62696E2F73680A2320546869732069732061207368656C6C2061726368697665', 'Little', 'VAR', '0', '1936'), 
            '(?s)#!.{0,1}/bin/sh\\n# This is a shell archive')

    #Originally Taken from  fmt/329
    def test_convert_to_regex_223(self):
        self.assertEqual(prepare.convert_to_regex('2320546869732069732061207368656C6C2061726368697665', 'Little', 'BOF', '0', ''), 
            '(?s)\\A# This is a shell archive')

    #Originally Taken from  fmt/32
    def test_convert_to_regex_224(self):
        self.assertEqual(prepare.convert_to_regex('414331303039', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1009')

    #Originally Taken from  fmt/330
    def test_convert_to_regex_225(self):
        self.assertEqual(prepare.convert_to_regex('F106000000[01:02]0000{3}00{3}0000000000{4}FFFFFFFF00000000', 'Little', 'BOF', '0', '0'), 
            '(?s)\\A.{0,0}\\xf1\\x06\\x00\\x00\\x00[\\x01-\\x02]\\x00\\x00.{3}\\x00.{3}\\x00\\x00\\x00\\x00\\x00.{4}\\xff\\xff\\xff\\xff\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/331
    def test_convert_to_regex_226(self):
        self.assertEqual(prepare.convert_to_regex('5B6175746F72756E5D{2-4}(4F50454E|6F70656E|49434F4E|69636F6E){0-1}3D', 'Little', 'BOF', '0', '0'), 
            '(?s)\\A.{0,0}\\[autorun\\].{2,4}(?:OPEN|open|ICON|icon).{0,1}=')

    #Originally Taken from  fmt/332
    def test_convert_to_regex_227(self):
        self.assertEqual(prepare.convert_to_regex('2F332E[30:33]0D0A284F44422E31', 'Little', 'BOF', '0', ''), 
            '(?s)\\A/3\\.[0-3]\\r\\n\\(ODB\\.1')

    #Originally Taken from  fmt/333
    def test_convert_to_regex_228(self):
        self.assertEqual(prepare.convert_to_regex('786D6C6E733D22687474703A2F2F7777772E786D6C2D636D6C2E6F72672F736368656D6122', 'Little', 'BOF', '0', '65536'), 
            '(?s)\\A.{0,65536}xmlns="http://www\\.xml-cml\\.org/schema"')

    #Originally Taken from  fmt/334
    def test_convert_to_regex_229(self):
        self.assertEqual(prepare.convert_to_regex('205F61746F6D5F747970655F736361745F64697370657273696F6E5F7265616C', 'Little', 'BOF', '0', '65536'), 
            '(?s)\\A.{0,65536} _atom_type_scat_dispersion_real')

    #Originally Taken from  fmt/335
    def test_convert_to_regex_230(self):
        self.assertEqual(prepare.convert_to_regex('7C7C{1-100}40{1-253}2E', 'Little', 'BOF', '0', '64'), 
            '(?s)\\A.{0,64}\\|\\|.{1,100}@.{1,253}\\.')

    #Originally Taken from  fmt/336
    def test_convert_to_regex_231(self):
        self.assertEqual(prepare.convert_to_regex('54484E4C', 'Little', 'BOF', '0', ''), 
            '(?s)\\ATHNL')

    #Originally Taken from  fmt/338
    def test_convert_to_regex_232(self):
        self.assertEqual(prepare.convert_to_regex('464F524D{4}494C424D424D4844', 'Little', 'BOF', '0', ''), 
            '(?s)\\AFORM.{4}ILBMBMHD')

    #Originally Taken from  fmt/339
    def test_convert_to_regex_233(self):
        self.assertEqual(prepare.convert_to_regex('464F524D{4}3853565856484452', 'Little', 'BOF', '0', ''), 
            '(?s)\\AFORM.{4}8SVXVHDR')

    #Originally Taken from  fmt/33
    def test_convert_to_regex_234(self):
        self.assertEqual(prepare.convert_to_regex('414331303132', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1012')

    #Originally Taken from  fmt/340
    def test_convert_to_regex_235(self):
        self.assertEqual(prepare.convert_to_regex('576F726450726F0000000000000000004C5750370000000000000000000000000000FFFFFFFF000000002E', 'Little', 'BOF', '0', ''), 
            '(?s)\\AWordPro\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00LWP7\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\xff\\xff\\xff\\xff\\x00\\x00\\x00\\x00\\.')

    #Originally Taken from  fmt/341
    def test_convert_to_regex_236(self):
        self.assertEqual(prepare.convert_to_regex('001102FF0C00', 'Little', 'BOF', '522', ''), 
            '(?s)\\A.{522}\\x00\\x11\\x02\\xff\\x0c\\x00')

    #Originally Taken from  fmt/342
    def test_convert_to_regex_237(self):
        self.assertEqual(prepare.convert_to_regex('4D5058(2C|3B){1-50}(2C|3B)34(2C|2E)30', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMPX(?:,|;).{1,50}(?:,|;)4(?:,|\\.)0')

    #Originally Taken from  fmt/343
    def test_convert_to_regex_238(self):
        self.assertEqual(prepare.convert_to_regex('4D5058(2C|3B){1-50}(2C|3B)332E30', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMPX(?:,|;).{1,50}(?:,|;)3\\.0')

    #Originally Taken from  fmt/344
    def test_convert_to_regex_239(self):
        self.assertEqual(prepare.convert_to_regex('0100000064000000{32}20454D4600000100{12}00000000{28}00000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x01\\x00\\x00\\x00d\\x00\\x00\\x00.{32} EMF\\x00\\x00\\x01\\x00.{12}\\x00\\x00\\x00\\x00.{28}\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/344
    def test_convert_to_regex_240(self):
        self.assertEqual(prepare.convert_to_regex('01000000{36}20454D4600000100{16}64000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x01\\x00\\x00\\x00.{36} EMF\\x00\\x00\\x01\\x00.{16}d\\x00\\x00\\x00')

    #Originally Taken from  fmt/344
    def test_convert_to_regex_241(self):
        self.assertEqual(prepare.convert_to_regex('01000000{36}20454D4600000100{44}64000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x01\\x00\\x00\\x00.{36} EMF\\x00\\x00\\x01\\x00.{44}d\\x00\\x00\\x00')

    #Originally Taken from  fmt/345
    def test_convert_to_regex_242(self):
        self.assertEqual(prepare.convert_to_regex('010000006C000000{32}20454D4600000100{12}00000000{28}00000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x01\\x00\\x00\\x00l\\x00\\x00\\x00.{32} EMF\\x00\\x00\\x01\\x00.{12}\\x00\\x00\\x00\\x00.{28}\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/345
    def test_convert_to_regex_243(self):
        self.assertEqual(prepare.convert_to_regex('01000000{36}20454D4600000100{16}6C000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x01\\x00\\x00\\x00.{36} EMF\\x00\\x00\\x01\\x00.{16}l\\x00\\x00\\x00')

    #Originally Taken from  fmt/345
    def test_convert_to_regex_244(self):
        self.assertEqual(prepare.convert_to_regex('01000000{36}20454D4600000100{44}6C000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x01\\x00\\x00\\x00.{36} EMF\\x00\\x00\\x01\\x00.{44}l\\x00\\x00\\x00')

    #Originally Taken from  fmt/346
    def test_convert_to_regex_245(self):
        self.assertEqual(prepare.convert_to_regex('FE3200C1', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xfe2\\x00\\xc1')

    #Originally Taken from  fmt/347
    def test_convert_to_regex_246(self):
        self.assertEqual(prepare.convert_to_regex('FFF6[10:EB]{29-769}FFF6[10:EB]{29-769}FFF6[10:EB]{29-769}FFF6[10:EB]{29-769}', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xf6[\\x10-\\xeb].{29,769}\\xff\\xf6[\\x10-\\xeb].{29,769}\\xff\\xf6[\\x10-\\xeb].{29,769}\\xff\\xf6[\\x10-\\xeb].{29,769}')

    #Originally Taken from  fmt/347
    def test_convert_to_regex_247(self):
        self.assertEqual(prepare.convert_to_regex('FFF7[10:EB]{29-769}FFF7[10:EB]{29-769}FFF7[10:EB]{29-769}FFF7[10:EB]{29-769}', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xf7[\\x10-\\xeb].{29,769}\\xff\\xf7[\\x10-\\xeb].{29,769}\\xff\\xf7[\\x10-\\xeb].{29,769}\\xff\\xf7[\\x10-\\xeb].{29,769}')

    #Originally Taken from  fmt/347
    def test_convert_to_regex_248(self):
        self.assertEqual(prepare.convert_to_regex('FFFE[10:EB]{29-769}FFFE[10:EB]{29-769}FFFE[10:EB]{29-769}FFFE[10:EB]{29-769}', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xfe[\\x10-\\xeb].{29,769}\\xff\\xfe[\\x10-\\xeb].{29,769}\\xff\\xfe[\\x10-\\xeb].{29,769}\\xff\\xfe[\\x10-\\xeb].{29,769}')

    #Originally Taken from  fmt/347
    def test_convert_to_regex_249(self):
        self.assertEqual(prepare.convert_to_regex('FFFF[10:EB]{29-769}FFFF[10:EB]{29-769}FFFF[10:EB]{29-769}FFFF[10:EB]{29-769}', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xff[\\x10-\\xeb].{29,769}\\xff\\xff[\\x10-\\xeb].{29,769}\\xff\\xff[\\x10-\\xeb].{29,769}\\xff\\xff[\\x10-\\xeb].{29,769}')

    #Originally Taken from  fmt/348
    def test_convert_to_regex_250(self):
        self.assertEqual(prepare.convert_to_regex('5061696E742053686F702050726F20496D6167652046696C650A1A00000000000900', 'Little', 'BOF', '0', ''), 
            '(?s)\\APaint Shop Pro Image File\\n\\x1a\\x00\\x00\\x00\\x00\\x00\\x09\\x00')

    #Originally Taken from  fmt/349
    def test_convert_to_regex_251(self):
        self.assertEqual(prepare.convert_to_regex('5061696E742053686F702050726F20496D6167652046696C650A1A00000000000A00', 'Little', 'BOF', '0', ''), 
            '(?s)\\APaint Shop Pro Image File\\n\\x1a\\x00\\x00\\x00\\x00\\x00\\n\\x00')

    #Originally Taken from  fmt/34
    def test_convert_to_regex_252(self):
        self.assertEqual(prepare.convert_to_regex('414331303134', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1014')

    #Originally Taken from  fmt/350
    def test_convert_to_regex_253(self):
        self.assertEqual(prepare.convert_to_regex('0008(00|02)[01:04]{31}00000000{16}[03:04]', 'Little', 'BOF', '2', ''), 
            '(?s)\\A.{2}\\x00\\x08(?:\\x00|\\x02)[\\x01-\\x04].{31}\\x00\\x00\\x00\\x00.{16}[\\x03-\\x04]')

    #Originally Taken from  fmt/351
    def test_convert_to_regex_254(self):
        self.assertEqual(prepare.convert_to_regex('0008(00|02)[01:04]{51}[05:09]{34}00000000', 'Little', 'BOF', '2', ''), 
            '(?s)\\A.{2}\\x00\\x08(?:\\x00|\\x02)[\\x01-\\x04].{51}[\\x05-\\x09].{34}\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/352
    def test_convert_to_regex_255(self):
        self.assertEqual(prepare.convert_to_regex('0008(00|02)[01:20]{51}(0A|0B){34}00000000', 'Little', 'BOF', '2', ''), 
            '(?s)\\A.{2}\\x00\\x08(?:\\x00|\\x02)[\\x01- ].{51}(?:\\n|\\x0b).{34}\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/353
    def test_convert_to_regex_256(self):
        self.assertEqual(prepare.convert_to_regex('49492A00', 'Little', 'BOF', '0', ''), 
            '(?s)\\AII\\*\\x00')

    #Originally Taken from  fmt/353
    def test_convert_to_regex_257(self):
        self.assertEqual(prepare.convert_to_regex('4D4D002A', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMM\\x00\\*')

    #Originally Taken from  fmt/354
    def test_convert_to_regex_258(self):
        self.assertEqual(prepare.convert_to_regex('255044462D312E(33|34|35|36|37)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A%PDF-1\\.(?:3|4|5|6|7)')

    #Originally Taken from  fmt/354
    def test_convert_to_regex_259(self):
        self.assertEqual(prepare.convert_to_regex('786D6C6E733A7064666169643D(22|27)687474703A2F2F7777772E6169696D2E6F72672F706466612F6E732F6964{0-20}7064666169643A70617274(3D22|3D27|3E)31(22|27|3C2F7064666169643A706172743E){0-11}7064666169643A636F6E666F726D616E6365(3E|3D22|3D27)42(22|27|3C2F7064666169643A636F6E666F726D616E63653E)', 'Little', 'VAR', '0', ''), 
            '(?s)xmlns:pdfaid=(?:"|\')http://www\\.aiim\\.org/pdfa/ns/id.{0,20}pdfaid:part(?:="|=\'|>)1(?:"|\'|</pdfaid:part>).{0,11}pdfaid:conformance(?:>|="|=\')B(?:"|\'|</pdfaid:conformance>)')

    #Originally Taken from  fmt/355
    def test_convert_to_regex_260(self):
        self.assertEqual(prepare.convert_to_regex('7B5C7274(66|6631){0-15}(616E7369|6D6163|7063|706361)5C616E7369637067{3-*}5C737473686664626368{1-5}5C73747368666C6F6368{1-5}5C737473686668696368{1-5}5C73747368666269{0-64000}(7B5C2A5C636F6C6F72736368656D656D617070696E67|5C6166656C6576|7B5C2A5C6461746173746F7265|7B5C2A5C646566636870)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\{\\\\rt(?:f|f1).{0,15}(?:ansi|mac|pc|pca)\\\\ansicpg.{3,}\\\\stshfdbch.{1,5}\\\\stshfloch.{1,5}\\\\stshfhich.{1,5}\\\\stshfbi.{0,64000}(?:\\{\\\\\\*\\\\colorschememapping|\\\\afelev|\\{\\\\\\*\\\\datastore|\\{\\\\\\*\\\\defchp)')

    #Originally Taken from  fmt/356
    def test_convert_to_regex_261(self):
        self.assertEqual(prepare.convert_to_regex('2321414D520A', 'Little', 'BOF', '0', ''), 
            '(?s)\\A#!AMR\\n')

    #Originally Taken from  fmt/357
    def test_convert_to_regex_262(self):
        self.assertEqual(prepare.convert_to_regex('667479703367(65|67|68|70|72|73|74)[34:39]0000[00:03]00', 'Little', 'BOF', '4', ''), 
            '(?s)\\A.{4}ftyp3g(?:e|g|h|p|r|s|t)[4-9]\\x00\\x00[\\x00-\\x03]\\x00')

    #Originally Taken from  fmt/358
    def test_convert_to_regex_263(self):
        self.assertEqual(prepare.convert_to_regex('5B51756572795D*(43|63)69(53|73)636F70653D', 'Little', 'BOF', '0', '3424'), 
            '(?s)\\A.{0,3424}\\[Query\\].*(?:C|c)i(?:S|s)cope=')

    #Originally Taken from  fmt/358
    def test_convert_to_regex_264(self):
        self.assertEqual(prepare.convert_to_regex('5B51756572795D*(43|63)69(43|63)6F6C756D6E733D', 'Little', 'BOF', '0', '3424'), 
            '(?s)\\A.{0,3424}\\[Query\\].*(?:C|c)i(?:C|c)olumns=')

    #Originally Taken from  fmt/358
    def test_convert_to_regex_265(self):
        self.assertEqual(prepare.convert_to_regex('5B51756572795D*(43|63)69(54|74)656D706C6174653D2F', 'Little', 'BOF', '0', '3424'), 
            '(?s)\\A.{0,3424}\\[Query\\].*(?:C|c)i(?:T|t)emplate=/')

    #Originally Taken from  fmt/358
    def test_convert_to_regex_266(self):
        self.assertEqual(prepare.convert_to_regex('5B51756572795D*(43|63)69(52|72)65737472696374696F6E3D{0-1}25', 'Little', 'BOF', '0', '3424'), 
            '(?s)\\A.{0,3424}\\[Query\\].*(?:C|c)i(?:R|r)estriction=.{0,1}%')

    #Originally Taken from  fmt/359
    def test_convert_to_regex_267(self):
        self.assertEqual(prepare.convert_to_regex('1C010000{272}0C0000002C000000{4}FFFFFFFF0002', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x1c\\x01\\x00\\x00.{272}\\x0c\\x00\\x00\\x00,\\x00\\x00\\x00.{4}\\xff\\xff\\xff\\xff\\x00\\x02')

    #Originally Taken from  fmt/35
    def test_convert_to_regex_268(self):
        self.assertEqual(prepare.convert_to_regex('414331303135', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1015')

    #Originally Taken from  fmt/360
    def test_convert_to_regex_269(self):
        self.assertEqual(prepare.convert_to_regex('0000803F{12}00000000{4}0000{2}0000{1}[41:42]{8}0000000000000000000000000000000000000000{28}00000000{3}[40:49]', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x80\\?.{12}\\x00\\x00\\x00\\x00.{4}\\x00\\x00.{2}\\x00\\x00.{1}[A-B].{8}\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00.{28}\\x00\\x00\\x00\\x00.{3}[@-I]')

    #Originally Taken from  fmt/361
    def test_convert_to_regex_270(self):
        self.assertEqual(prepare.convert_to_regex('4E554D424552204F46205452414345532020203D20[30:39]{3-*}4E554D424552204F46205054532F54524320203D20[30:39]', 'Little', 'BOF', '0', '100'), 
            '(?s)\\A.{0,100}NUMBER OF TRACES   = [0-9].{3,}NUMBER OF PTS/TRC  = [0-9]')

    #Originally Taken from  fmt/361
    def test_convert_to_regex_271(self):
        self.assertEqual(prepare.convert_to_regex('535552564559204D4F444520202020202020203D20', 'Little', 'EOF', '0', '150'), 
            '(?s)SURVEY MODE        = .{0,150}\\Z')

    #Originally Taken from  fmt/362
    def test_convert_to_regex_272(self):
        self.assertEqual(prepare.convert_to_regex('(FF00|0007)000400(02|04)100000(00|80)0000(00|80)[41:42]{84}[31:39][30:39][30:39]{13}(46494C45|434C4153){906}(0000|FFFF)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A(?:\\xff\\x00|\\x00\\x07)\\x00\\x04\\x00(?:\\x02|\\x04)\\x10\\x00\\x00(?:\\x00|\\x80)\\x00\\x00(?:\\x00|\\x80)[A-B].{84}[1-9][0-9][0-9].{13}(?:FILE|CLAS).{906}(?:\\x00\\x00|\\xff\\xff)')

    #Originally Taken from  fmt/364
    def test_convert_to_regex_273(self):
        self.assertEqual(prepare.convert_to_regex('4E49544630312E3130{16}[30:33][30:39][30:32][30:39][30:35][30:39][30:35][30:39]5A{3}[30:39][30:39]{80}(43|52|53|54|55)', 'Little', 'BOF', '0', ''), 
            '(?s)\\ANITF01\\.10.{16}[0-3][0-9][0-2][0-9][0-5][0-9][0-5][0-9]Z.{3}[0-9][0-9].{80}(?:C|R|S|T|U)')

    #Originally Taken from  fmt/365
    def test_convert_to_regex_274(self):
        self.assertEqual(prepare.convert_to_regex('4E49544630322E3030[30:39][31:39]20202020{10}[30:33][30:39][30:32][30:39][30:35][30:39][30:35][30:39]5A{3}[30:39][30:39]{80}(43|52|53|54|55)', 'Little', 'BOF', '0', ''), 
            '(?s)\\ANITF02\\.00[0-9][1-9]    .{10}[0-3][0-9][0-2][0-9][0-5][0-9][0-5][0-9]Z.{3}[0-9][0-9].{80}(?:C|R|S|T|U)')

    #Originally Taken from  fmt/366
    def test_convert_to_regex_275(self):
        self.assertEqual(prepare.convert_to_regex('4E49544630322E3130[30:39][31:39]{14}(31|32)[30:39][30:39][30:39](30|31)[30:39][30:33][30:39][30:32][30:39][30:35][30:39][30:35][30:39]{80}(43|52|53|54|55)', 'Little', 'BOF', '0', ''), 
            '(?s)\\ANITF02\\.10[0-9][1-9].{14}(?:1|2)[0-9][0-9][0-9](?:0|1)[0-9][0-3][0-9][0-2][0-9][0-5][0-9][0-5][0-9].{80}(?:C|R|S|T|U)')

    #Originally Taken from  fmt/36
    def test_convert_to_regex_276(self):
        self.assertEqual(prepare.convert_to_regex('414331303138', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1018')

    #Originally Taken from  fmt/37
    def test_convert_to_regex_277(self):
        self.assertEqual(prepare.convert_to_regex('9BA5{16}00000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x9b\\xa5.{16}\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/38
    def test_convert_to_regex_278(self):
        self.assertEqual(prepare.convert_to_regex('DBA5{16}00000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xdb\\xa5.{16}\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/39
    def test_convert_to_regex_279(self):
        self.assertEqual(prepare.convert_to_regex('D0CF11E0A1B11AE1{20}FEFF', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xd0\\xcf\\x11\\xe0\\xa1\\xb1\\x1a\\xe1.{20}\\xfe\\xff')

    #Originally Taken from  fmt/39
    def test_convert_to_regex_280(self):
        self.assertEqual(prepare.convert_to_regex('57006F007200640044006F00630075006D0065006E007400{42}02(00|01)', 'Little', 'VAR', '0', ''), 
            '(?s)W\\x00o\\x00r\\x00d\\x00D\\x00o\\x00c\\x00u\\x00m\\x00e\\x00n\\x00t\\x00.{42}\\x02(?:\\x00|\\x01)')

    #Originally Taken from  fmt/39
    def test_convert_to_regex_281(self):
        self.assertEqual(prepare.convert_to_regex('4D6963726F736F667420576F726420(362E30|666F722057696E646F7773203935|362E302D446F6B756D656E74)', 'Little', 'VAR', '0', ''), 
            '(?s)Microsoft Word (?:6\\.0|for Windows 95|6\\.0-Dokument)')

    #Originally Taken from  fmt/3
    def test_convert_to_regex_282(self):
        self.assertEqual(prepare.convert_to_regex('474946383761', 'Little', 'BOF', '0', ''), 
            '(?s)\\AGIF87a')

    #Originally Taken from  fmt/3
    def test_convert_to_regex_283(self):
        self.assertEqual(prepare.convert_to_regex('3B', 'Little', 'EOF', '0', ''), 
            '(?s);\\Z')

    #Originally Taken from  fmt/40
    def test_convert_to_regex_284(self):
        self.assertEqual(prepare.convert_to_regex('D0CF11E0A1B11AE1{20}FEFF', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xd0\\xcf\\x11\\xe0\\xa1\\xb1\\x1a\\xe1.{20}\\xfe\\xff')

    #Originally Taken from  fmt/40
    def test_convert_to_regex_285(self):
        self.assertEqual(prepare.convert_to_regex('57006F007200640044006F00630075006D0065006E007400{42}02(00|01)', 'Little', 'VAR', '0', ''), 
            '(?s)W\\x00o\\x00r\\x00d\\x00D\\x00o\\x00c\\x00u\\x00m\\x00e\\x00n\\x00t\\x00.{42}\\x02(?:\\x00|\\x01)')

    #Originally Taken from  fmt/40
    def test_convert_to_regex_286(self):
        self.assertEqual(prepare.convert_to_regex('4D6963726F736F667420576F7264(20382E30|20392E30|2031302E30|2D446F6B756D656E74)', 'Little', 'VAR', '0', ''), 
            '(?s)Microsoft Word(?: 8\\.0| 9\\.0| 10\\.0|-Dokument)')

    #Originally Taken from  fmt/41
    def test_convert_to_regex_287(self):
        self.assertEqual(prepare.convert_to_regex('FFD8FF', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xd8\\xff')

    #Originally Taken from  fmt/41
    def test_convert_to_regex_288(self):
        self.assertEqual(prepare.convert_to_regex('FFD9', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xd9\\Z')

    #Originally Taken from  fmt/42
    def test_convert_to_regex_289(self):
        self.assertEqual(prepare.convert_to_regex('FFD8FFE0{2}4A464946000100(00|01|02)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xd8\\xff\\xe0.{2}JFIF\\x00\\x01\\x00(?:\\x00|\\x01|\\x02)')

    #Originally Taken from  fmt/42
    def test_convert_to_regex_290(self):
        self.assertEqual(prepare.convert_to_regex('FFD9', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xd9\\Z')

    #Originally Taken from  fmt/43
    def test_convert_to_regex_291(self):
        self.assertEqual(prepare.convert_to_regex('FFD8FFE0{2}4A464946000101(00|01|02)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xd8\\xff\\xe0.{2}JFIF\\x00\\x01\\x01(?:\\x00|\\x01|\\x02)')

    #Originally Taken from  fmt/43
    def test_convert_to_regex_292(self):
        self.assertEqual(prepare.convert_to_regex('FFD9', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xd9\\Z')

    #Originally Taken from  fmt/44
    def test_convert_to_regex_293(self):
        self.assertEqual(prepare.convert_to_regex('FFD8FFE0{2}4A464946000102(00|01|02)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xd8\\xff\\xe0.{2}JFIF\\x00\\x01\\x02(?:\\x00|\\x01|\\x02)')

    #Originally Taken from  fmt/44
    def test_convert_to_regex_294(self):
        self.assertEqual(prepare.convert_to_regex('FFD9', 'Little', 'EOF', '0', '1'), 
            '(?s)\\xff\\xd9.{0,1}\\Z')

    #Originally Taken from  fmt/45
    def test_convert_to_regex_295(self):
        self.assertEqual(prepare.convert_to_regex('7B5C7274(66|6631)5C(616E7369|6D6163|7063|706361)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\{\\\\rt(?:f|f1)\\\\(?:ansi|mac|pc|pca)')

    #Originally Taken from  fmt/46
    def test_convert_to_regex_296(self):
        self.assertEqual(prepare.convert_to_regex('7B5C7274(66|6631)5C(616E7369|6D6163|7063|706361)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\{\\\\rt(?:f|f1)\\\\(?:ansi|mac|pc|pca)')

    #Originally Taken from  fmt/47
    def test_convert_to_regex_297(self):
        self.assertEqual(prepare.convert_to_regex('7B5C7274(66|6631)5C(616E7369|6D6163|7063|706361)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\{\\\\rt(?:f|f1)\\\\(?:ansi|mac|pc|pca)')

    #Originally Taken from  fmt/48
    def test_convert_to_regex_298(self):
        self.assertEqual(prepare.convert_to_regex('7B5C7274(66|6631)5C(616E7369|6D6163|7063|706361)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\{\\\\rt(?:f|f1)\\\\(?:ansi|mac|pc|pca)')

    #Originally Taken from  fmt/49
    def test_convert_to_regex_299(self):
        self.assertEqual(prepare.convert_to_regex('7B5C7274(66|6631)5C(616E7369|6D6163|7063|706361)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\{\\\\rt(?:f|f1)\\\\(?:ansi|mac|pc|pca)')

    #Originally Taken from  fmt/4
    def test_convert_to_regex_300(self):
        self.assertEqual(prepare.convert_to_regex('474946383961', 'Little', 'BOF', '0', ''), 
            '(?s)\\AGIF89a')

    #Originally Taken from  fmt/4
    def test_convert_to_regex_301(self):
        self.assertEqual(prepare.convert_to_regex('3B', 'Little', 'EOF', '0', ''), 
            '(?s);\\Z')

    #Originally Taken from  fmt/50
    def test_convert_to_regex_302(self):
        self.assertEqual(prepare.convert_to_regex('7B5C7274(66|6631)5C(616E7369|6D6163|7063|706361)5C616E7369637067', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\{\\\\rt(?:f|f1)\\\\(?:ansi|mac|pc|pca)\\\\ansicpg')

    #Originally Taken from  fmt/51
    def test_convert_to_regex_303(self):
        self.assertEqual(prepare.convert_to_regex('7B5C7274(66|6631)5C(616E7369|6D6163|7063|706361)5C616E7369637067', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\{\\\\rt(?:f|f1)\\\\(?:ansi|mac|pc|pca)\\\\ansicpg')

    #Originally Taken from  fmt/52
    def test_convert_to_regex_304(self):
        self.assertEqual(prepare.convert_to_regex('7B5C7274(66|6631)5C(616E7369|6D6163|7063|706361)5C616E7369637067{3-*}5C737473686664626368{1-4}5C73747368666C6F6368{1-4}5C737473686668696368{1-4}5C73747368666269', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\{\\\\rt(?:f|f1)\\\\(?:ansi|mac|pc|pca)\\\\ansicpg.{3,}\\\\stshfdbch.{1,4}\\\\stshfloch.{1,4}\\\\stshfhich.{1,4}\\\\stshfbi')

    #Originally Taken from  fmt/53
    def test_convert_to_regex_305(self):
        self.assertEqual(prepare.convert_to_regex('7B5C7274(66|6631){0-15}(616E7369|6D6163|7063|706361)5C616E7369637067{3-*}5C737473686664626368{1-4}5C73747368666C6F6368{1-4}5C737473686668696368{1-4}5C73747368666269*5C6C73647374696D6178', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\{\\\\rt(?:f|f1).{0,15}(?:ansi|mac|pc|pca)\\\\ansicpg.{3,}\\\\stshfdbch.{1,4}\\\\stshfloch.{1,4}\\\\stshfhich.{1,4}\\\\stshfbi.*\\\\lsdstimax')

    #Originally Taken from  fmt/54
    def test_convert_to_regex_306(self):
        self.assertEqual(prepare.convert_to_regex('00', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\Z')

    #Originally Taken from  fmt/54
    def test_convert_to_regex_307(self):
        self.assertEqual(prepare.convert_to_regex('4175746F4341442044584220312E300D0A1A00', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAutoCAD DXB 1\\.0\\r\\n\\x1a\\x00')

    #Originally Taken from  fmt/55
    def test_convert_to_regex_308(self):
        self.assertEqual(prepare.convert_to_regex('0900{2}07001000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x09\\x00.{2}\\x07\\x00\\x10\\x00')

    #Originally Taken from  fmt/56
    def test_convert_to_regex_309(self):
        self.assertEqual(prepare.convert_to_regex('0902{2}00001000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x09\\x02.{2}\\x00\\x00\\x10\\x00')

    #Originally Taken from  fmt/57
    def test_convert_to_regex_310(self):
        self.assertEqual(prepare.convert_to_regex('0904{2}00001000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x09\\x04.{2}\\x00\\x00\\x10\\x00')

    #Originally Taken from  fmt/58
    def test_convert_to_regex_311(self):
        self.assertEqual(prepare.convert_to_regex('0904{2}00040001', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x09\\x04.{2}\\x00\\x04\\x00\\x01')

    #Originally Taken from  fmt/59
    def test_convert_to_regex_312(self):
        self.assertEqual(prepare.convert_to_regex('0908{2}00050500(9C35|6C92|920C|F90C)', 'Little', 'BOF', '512', ''), 
            '(?s)\\A.{512}\\x09\\x08.{2}\\x00\\x05\\x05\\x00(?:\\x9c5|l\\x92|\\x92\\x0c|\\xf9\\x0c)')

    #Originally Taken from  fmt/5
    def test_convert_to_regex_313(self):
        self.assertEqual(prepare.convert_to_regex('52494646{4}41564920*4C495354{4}6864726C61766968*4C495354{4}6D6F7669', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIFF.{4}AVI .*LIST.{4}hdrlavih.*LIST.{4}movi')

    #Originally Taken from  fmt/60
    def test_convert_to_regex_314(self):
        self.assertEqual(prepare.convert_to_regex('0908{2}00050500(9C35|6C92|920C|F90C)', 'Little', 'BOF', '512', ''), 
            '(?s)\\A.{512}\\x09\\x08.{2}\\x00\\x05\\x05\\x00(?:\\x9c5|l\\x92|\\x92\\x0c|\\xf9\\x0c)')

    #Originally Taken from  fmt/61
    def test_convert_to_regex_315(self):
        self.assertEqual(prepare.convert_to_regex('0908{2}00060500EC30CD07', 'Little', 'BOF', '512', ''), 
            '(?s)\\A.{512}\\x09\\x08.{2}\\x00\\x06\\x05\\x00\\xec0\\xcd\\x07')

    #Originally Taken from  fmt/62
    def test_convert_to_regex_316(self):
        self.assertEqual(prepare.convert_to_regex('0908{2}00060500EC30CD07', 'Little', 'BOF', '512', ''), 
            '(?s)\\A.{512}\\x09\\x08.{2}\\x00\\x06\\x05\\x00\\xec0\\xcd\\x07')

    #Originally Taken from  fmt/63
    def test_convert_to_regex_317(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A{0-2}320D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n.{0,2}2\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/63
    def test_convert_to_regex_318(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', '1'), 
            '(?s)0\\r\\nEOF\\r\\n.{0,1}\\Z')

    #Originally Taken from  fmt/64
    def test_convert_to_regex_319(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4D43302E300D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nMC0\\.0\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/64
    def test_convert_to_regex_320(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/65
    def test_convert_to_regex_321(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143312E320D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC1\\.2\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/65
    def test_convert_to_regex_322(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/66
    def test_convert_to_regex_323(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143312E330D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC1\\.3\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/66
    def test_convert_to_regex_324(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/67
    def test_convert_to_regex_325(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143312E34300D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC1\\.40\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/67
    def test_convert_to_regex_326(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/68
    def test_convert_to_regex_327(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143312E35300D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC1\\.50\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/68
    def test_convert_to_regex_328(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/69
    def test_convert_to_regex_329(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143322E31300D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC2\\.10\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/69
    def test_convert_to_regex_330(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/6
    def test_convert_to_regex_331(self):
        self.assertEqual(prepare.convert_to_regex('52494646{4}57415645*666D7420{18-*}64617461', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIFF.{4}WAVE.*fmt .{18,}data')

    #Originally Taken from  fmt/70
    def test_convert_to_regex_332(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143(322E3231|322E3232|31303031)0D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC(?:2\\.21|2\\.22|1001)\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/70
    def test_convert_to_regex_333(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/71
    def test_convert_to_regex_334(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143313030320D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC1002\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/71
    def test_convert_to_regex_335(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/72
    def test_convert_to_regex_336(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143313030330D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC1003\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/72
    def test_convert_to_regex_337(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/73
    def test_convert_to_regex_338(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143313030340D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC1004\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/73
    def test_convert_to_regex_339(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/74
    def test_convert_to_regex_340(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143313030360D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC1006\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/74
    def test_convert_to_regex_341(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/75
    def test_convert_to_regex_342(self):
        self.assertEqual(prepare.convert_to_regex('30(0D0A|0A)53454354494F4E(0D0A|0A)202032(0D0A|0A)484541444552(0D0A|0A)*39(0D0A|0A)2441434144564552(0D0A|0A)202031(0D0A|0A)414331303039(0D0A|0A)*30(0D0A|0A)454E44534543(0D0A|0A)', 'Little', 'VAR', '0', ''), 
            '(?s)0(?:\\r\\n|\\n)SECTION(?:\\r\\n|\\n)  2(?:\\r\\n|\\n)HEADER(?:\\r\\n|\\n).*9(?:\\r\\n|\\n)\\$ACADVER(?:\\r\\n|\\n)  1(?:\\r\\n|\\n)AC1009(?:\\r\\n|\\n).*0(?:\\r\\n|\\n)ENDSEC(?:\\r\\n|\\n)')

    #Originally Taken from  fmt/75
    def test_convert_to_regex_343(self):
        self.assertEqual(prepare.convert_to_regex('30(0D0A|0A)454F46(0D0A|0A)', 'Little', 'EOF', '0', ''), 
            '(?s)0(?:\\r\\n|\\n)EOF(?:\\r\\n|\\n)\\Z')

    #Originally Taken from  fmt/76
    def test_convert_to_regex_344(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143313031320D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC1012\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/76
    def test_convert_to_regex_345(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/77
    def test_convert_to_regex_346(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143313031340D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC1014\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/77
    def test_convert_to_regex_347(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/78
    def test_convert_to_regex_348(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143313031350D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC1015\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/78
    def test_convert_to_regex_349(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/79
    def test_convert_to_regex_350(self):
        self.assertEqual(prepare.convert_to_regex('300D0A53454354494F4E0D0A2020320D0A4845414445520D0A*390D0A24414341445645520D0A2020310D0A4143313031380D0A*300D0A454E445345430D0A', 'Little', 'VAR', '0', ''), 
            '(?s)0\\r\\nSECTION\\r\\n  2\\r\\nHEADER\\r\\n.*9\\r\\n\\$ACADVER\\r\\n  1\\r\\nAC1018\\r\\n.*0\\r\\nENDSEC\\r\\n')

    #Originally Taken from  fmt/79
    def test_convert_to_regex_351(self):
        self.assertEqual(prepare.convert_to_regex('300D0A454F460D0A', 'Little', 'EOF', '0', ''), 
            '(?s)0\\r\\nEOF\\r\\n\\Z')

    #Originally Taken from  fmt/80
    def test_convert_to_regex_352(self):
        self.assertEqual(prepare.convert_to_regex('4175746F4341442042696E617279204458460D0A1A00*0053454354494F4E000248454144455200*092441434144564552000141433130303600*00454E4453454300', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAutoCAD Binary DXF\\r\\n\\x1a\\x00.*\\x00SECTION\\x00\\x02HEADER\\x00.*\\x09\\$ACADVER\\x00\\x01AC1006\\x00.*\\x00ENDSEC\\x00')

    #Originally Taken from  fmt/80
    def test_convert_to_regex_353(self):
        self.assertEqual(prepare.convert_to_regex('00454F4600', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00EOF\\x00\\Z')

    #Originally Taken from  fmt/81
    def test_convert_to_regex_354(self):
        self.assertEqual(prepare.convert_to_regex('4175746F4341442042696E617279204458460D0A1A00*0053454354494F4E000248454144455200*092441434144564552000141433130303900*00454E4453454300', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAutoCAD Binary DXF\\r\\n\\x1a\\x00.*\\x00SECTION\\x00\\x02HEADER\\x00.*\\x09\\$ACADVER\\x00\\x01AC1009\\x00.*\\x00ENDSEC\\x00')

    #Originally Taken from  fmt/81
    def test_convert_to_regex_355(self):
        self.assertEqual(prepare.convert_to_regex('00454F4600', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00EOF\\x00\\Z')

    #Originally Taken from  fmt/82
    def test_convert_to_regex_356(self):
        self.assertEqual(prepare.convert_to_regex('4175746F4341442042696E617279204458460D0A1A00*0053454354494F4E000248454144455200*092441434144564552000141433130313200*00454E4453454300', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAutoCAD Binary DXF\\r\\n\\x1a\\x00.*\\x00SECTION\\x00\\x02HEADER\\x00.*\\x09\\$ACADVER\\x00\\x01AC1012\\x00.*\\x00ENDSEC\\x00')

    #Originally Taken from  fmt/82
    def test_convert_to_regex_357(self):
        self.assertEqual(prepare.convert_to_regex('00454F4600', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00EOF\\x00\\Z')

    #Originally Taken from  fmt/83
    def test_convert_to_regex_358(self):
        self.assertEqual(prepare.convert_to_regex('4175746F4341442042696E617279204458460D0A1A00*000053454354494F4E00020048454144455200*0900244143414456455200010041433130313400*0000454E4453454300', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAutoCAD Binary DXF\\r\\n\\x1a\\x00.*\\x00\\x00SECTION\\x00\\x02\\x00HEADER\\x00.*\\x09\\x00\\$ACADVER\\x00\\x01\\x00AC1014\\x00.*\\x00\\x00ENDSEC\\x00')

    #Originally Taken from  fmt/83
    def test_convert_to_regex_359(self):
        self.assertEqual(prepare.convert_to_regex('0000454F4600', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00EOF\\x00\\Z')

    #Originally Taken from  fmt/84
    def test_convert_to_regex_360(self):
        self.assertEqual(prepare.convert_to_regex('4175746F4341442042696E617279204458460D0A1A00*000053454354494F4E00020048454144455200*0900244143414456455200010041433130313500*0000454E4453454300', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAutoCAD Binary DXF\\r\\n\\x1a\\x00.*\\x00\\x00SECTION\\x00\\x02\\x00HEADER\\x00.*\\x09\\x00\\$ACADVER\\x00\\x01\\x00AC1015\\x00.*\\x00\\x00ENDSEC\\x00')

    #Originally Taken from  fmt/84
    def test_convert_to_regex_361(self):
        self.assertEqual(prepare.convert_to_regex('0000454F4600', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00EOF\\x00\\Z')

    #Originally Taken from  fmt/85
    def test_convert_to_regex_362(self):
        self.assertEqual(prepare.convert_to_regex('4175746F4341442042696E617279204458460D0A1A00*000053454354494F4E00020048454144455200*0900244143414456455200010041433130313800*0000454E4453454300', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAutoCAD Binary DXF\\r\\n\\x1a\\x00.*\\x00\\x00SECTION\\x00\\x02\\x00HEADER\\x00.*\\x09\\x00\\$ACADVER\\x00\\x01\\x00AC1018\\x00.*\\x00\\x00ENDSEC\\x00')

    #Originally Taken from  fmt/85
    def test_convert_to_regex_363(self):
        self.assertEqual(prepare.convert_to_regex('0000454F4600', 'Little', 'EOF', '0', ''), 
            '(?s)\\x00\\x00EOF\\x00\\Z')

    #Originally Taken from  fmt/86
    def test_convert_to_regex_364(self):
        self.assertEqual(prepare.convert_to_regex('0A0001(01|02|04|08){60}00{3}(01|02)00{4}000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\n\\x00\\x01(?:\\x01|\\x02|\\x04|\\x08).{60}\\x00.{3}(?:\\x01|\\x02)\\x00.{4}\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/87
    def test_convert_to_regex_365(self):
        self.assertEqual(prepare.convert_to_regex('0A0201(01|02|04|08){60}00{3}(01|02)00{4}000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\n\\x02\\x01(?:\\x01|\\x02|\\x04|\\x08).{60}\\x00.{3}(?:\\x01|\\x02)\\x00.{4}\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/88
    def test_convert_to_regex_366(self):
        self.assertEqual(prepare.convert_to_regex('0A0301(01|02|04|08){60}00{3}(01|02)00{4}000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\n\\x03\\x01(?:\\x01|\\x02|\\x04|\\x08).{60}\\x00.{3}(?:\\x01|\\x02)\\x00.{4}\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/89
    def test_convert_to_regex_367(self):
        self.assertEqual(prepare.convert_to_regex('0A0401(01|02|04|08){60}00{3}(01|02)00{4}000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\n\\x04\\x01(?:\\x01|\\x02|\\x04|\\x08).{60}\\x00.{3}(?:\\x01|\\x02)\\x00.{4}\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/90
    def test_convert_to_regex_368(self):
        self.assertEqual(prepare.convert_to_regex('0A0501(01|02|04|08){60}00{3}(01|02)00{4}000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\n\\x05\\x01(?:\\x01|\\x02|\\x04|\\x08).{60}\\x00.{3}(?:\\x01|\\x02)\\x00.{4}\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/91
    def test_convert_to_regex_369(self):
        self.assertEqual(prepare.convert_to_regex('3C3F786D6C2076657273696F6E3D22312E3022*3C737667*7376673E', 'Little', 'BOF', '0', ''), 
            '(?s)\\A<\\?xml version="1\\.0".*<svg.*svg>')

    #Originally Taken from  fmt/92
    def test_convert_to_regex_370(self):
        self.assertEqual(prepare.convert_to_regex('3C3F786D6C2076657273696F6E3D22312E3022*3C737667*76657273696F6E3D22312E3122*7376673E', 'Little', 'BOF', '0', ''), 
            '(?s)\\A<\\?xml version="1\\.0".*<svg.*version="1\\.1".*svg>')

    #Originally Taken from  fmt/93
    def test_convert_to_regex_371(self):
        self.assertEqual(prepare.convert_to_regex('2356524D4C2056312E30206173636969', 'Little', 'BOF', '0', ''), 
            '(?s)\\A#VRML V1\\.0 ascii')

    #Originally Taken from  fmt/94
    def test_convert_to_regex_372(self):
        self.assertEqual(prepare.convert_to_regex('2356524D4C2056322E302075746638', 'Little', 'BOF', '0', ''), 
            '(?s)\\A#VRML V2\\.0 utf8')

    #Originally Taken from  fmt/95
    def test_convert_to_regex_373(self):
        self.assertEqual(prepare.convert_to_regex('255044462D312E34', 'Little', 'BOF', '0', ''), 
            '(?s)\\A%PDF-1\\.4')

    #Originally Taken from  fmt/95
    def test_convert_to_regex_374(self):
        self.assertEqual(prepare.convert_to_regex('786D6C6E733A7064666169643D(22|27)687474703A2F2F7777772E6169696D2E6F72672F706466612F6E732F6964{0-20}7064666169643A70617274(3D22|3D27|3E)31(22|27|3C2F7064666169643A706172743E){0-11}7064666169643A636F6E666F726D616E6365(3E|3D22|3D27)41(22|27|3C2F7064666169643A636F6E666F726D616E63653E)', 'Little', 'VAR', '0', ''), 
            '(?s)xmlns:pdfaid=(?:"|\')http://www\\.aiim\\.org/pdfa/ns/id.{0,20}pdfaid:part(?:="|=\'|>)1(?:"|\'|</pdfaid:part>).{0,11}pdfaid:conformance(?:>|="|=\')A(?:"|\'|</pdfaid:conformance>)')

    #Originally Taken from  fmt/96
    def test_convert_to_regex_375(self):
        self.assertEqual(prepare.convert_to_regex('3C(48544D4C|68746D6C)', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}<(?:HTML|html)')

    #Originally Taken from  fmt/96
    def test_convert_to_regex_376(self):
        self.assertEqual(prepare.convert_to_regex('3C2F(48544D4C|68746D6C|424F4459|626F6479)3E', 'Little', 'EOF', '0', '1024'), 
            '(?s)</(?:HTML|html|BODY|body)>.{0,1024}\\Z')

    #Originally Taken from  fmt/97
    def test_convert_to_regex_377(self):
        self.assertEqual(prepare.convert_to_regex('3C21(444F4354595045|646F6374797065)20(48544D4C|68746D6C)20(5055424C4943|7075626C6963)20222D2F2F{1-16}2F2F(445444|647464)20{0-64}(48544D4C|68746D6C)20322E30', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}<!(?:DOCTYPE|doctype) (?:HTML|html) (?:PUBLIC|public) "-//.{1,16}//(?:DTD|dtd) .{0,64}(?:HTML|html) 2\\.0')

    #Originally Taken from  fmt/98
    def test_convert_to_regex_378(self):
        self.assertEqual(prepare.convert_to_regex('3C21(444F4354595045|646F6374797065)20(48544D4C|68746D6C)20(5055424C4943|7075626C6963)20222D2F2F{1-16}2F2F(445444|647464)20{0-64}(48544D4C|68746D6C)20332E32', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}<!(?:DOCTYPE|doctype) (?:HTML|html) (?:PUBLIC|public) "-//.{1,16}//(?:DTD|dtd) .{0,64}(?:HTML|html) 3\\.2')

    #Originally Taken from  fmt/99
    def test_convert_to_regex_379(self):
        self.assertEqual(prepare.convert_to_regex('3C21(444F4354595045|646F6374797065)20(48544D4C|68746D6C)20(5055424C4943|7075626C6963)20222D2F2F{1-16}2F2F(445444|647464)20{0-64}(48544D4C|68746D6C)20342E(3020|302F)', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}<!(?:DOCTYPE|doctype) (?:HTML|html) (?:PUBLIC|public) "-//.{1,16}//(?:DTD|dtd) .{0,64}(?:HTML|html) 4\\.(?:0 |0/)')

    #Originally Taken from  x-fmt/101
    def test_convert_to_regex_380(self):
        self.assertEqual(prepare.convert_to_regex('48474231', 'Little', 'BOF', '0', ''), 
            '(?s)\\AHGB1')

    #Originally Taken from  x-fmt/103
    def test_convert_to_regex_381(self):
        self.assertEqual(prepare.convert_to_regex('4175746F4341442D383620(736861706573|756E69666F6E74|626967666F6E74)20312E', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAutoCAD-86 (?:shapes|unifont|bigfont) 1\\.')

    #Originally Taken from  x-fmt/104
    def test_convert_to_regex_382(self):
        self.assertEqual(prepare.convert_to_regex('4175746F43414420536C696465204C69627261727920', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAutoCAD Slide Library ')

    #Originally Taken from  x-fmt/105
    def test_convert_to_regex_383(self):
        self.assertEqual(prepare.convert_to_regex('4175746F43414420536C6964650D0A1A00', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAutoCAD Slide\\r\\n\\x1a\\x00')

    #Originally Taken from  x-fmt/107
    def test_convert_to_regex_384(self):
        self.assertEqual(prepare.convert_to_regex('50494146494C4556455253494F4E5F322E302C535442564552312C636F6D70726573730D0A706D7A6C6962636F646563', 'Little', 'BOF', '0', ''), 
            '(?s)\\APIAFILEVERSION_2\\.0,STBVER1,compress\\r\\npmzlibcodec')

    #Originally Taken from  x-fmt/114
    def test_convert_to_regex_385(self):
        self.assertEqual(prepare.convert_to_regex('00000200060406000800', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x02\\x00\\x06\\x04\\x06\\x00\\x08\\x00')

    #Originally Taken from  x-fmt/115
    def test_convert_to_regex_386(self):
        self.assertEqual(prepare.convert_to_regex('00001A0000100400', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x1a\\x00\\x00\\x10\\x04\\x00')

    #Originally Taken from  x-fmt/116
    def test_convert_to_regex_387(self):
        self.assertEqual(prepare.convert_to_regex('00001A0002100400', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x1a\\x00\\x02\\x10\\x04\\x00')

    #Originally Taken from  x-fmt/117
    def test_convert_to_regex_388(self):
        self.assertEqual(prepare.convert_to_regex('000002000404', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x02\\x00\\x04\\x04')

    #Originally Taken from  x-fmt/135
    def test_convert_to_regex_389(self):
        self.assertEqual(prepare.convert_to_regex('464F524D{4}41494646', 'Little', 'BOF', '0', ''), 
            '(?s)\\AFORM.{4}AIFF')

    #Originally Taken from  x-fmt/136
    def test_convert_to_regex_390(self):
        self.assertEqual(prepare.convert_to_regex('464F524D{4}41494643', 'Little', 'BOF', '0', ''), 
            '(?s)\\AFORM.{4}AIFC')

    #Originally Taken from  x-fmt/142
    def test_convert_to_regex_391(self):
        self.assertEqual(prepare.convert_to_regex('42(45|65)(47|67)(4D|6D)(46|66)*(4D|6D)(46|66)(56|76)(65|45)(52|72)(53|73)(49|69)(4F|6F)(4E|6E){1}31', 'Little', 'BOF', '0', ''), 
            '(?s)\\AB(?:E|e)(?:G|g)(?:M|m)(?:F|f).*(?:M|m)(?:F|f)(?:V|v)(?:e|E)(?:R|r)(?:S|s)(?:I|i)(?:O|o)(?:N|n).{1}1')

    #Originally Taken from  x-fmt/142
    def test_convert_to_regex_392(self):
        self.assertEqual(prepare.convert_to_regex('45(4E|6E)(44|64)(4D|6D)(46|66){0-1}3B', 'Little', 'EOF', '0', '2048'), 
            '(?s)E(?:N|n)(?:D|d)(?:M|m)(?:F|f).{0,1};.{0,2048}\\Z')

    #Originally Taken from  x-fmt/142
    def test_convert_to_regex_393(self):
        self.assertEqual(prepare.convert_to_regex('42(45|65)(47|67)(4D|6D)(46|66)*(4D|6D)(46|66)(56|76)(65|45)(52|72)(53|73)(49|69)(4F|6F)(4E|6E){1}31', 'Little', 'BOF', '0', ''), 
            '(?s)\\AB(?:E|e)(?:G|g)(?:M|m)(?:F|f).*(?:M|m)(?:F|f)(?:V|v)(?:e|E)(?:R|r)(?:S|s)(?:I|i)(?:O|o)(?:N|n).{1}1')

    #Originally Taken from  x-fmt/142
    def test_convert_to_regex_394(self):
        self.assertEqual(prepare.convert_to_regex('65(4E|6E)(44|64)(4D|6D)(46|66){0-1}3B', 'Little', 'EOF', '0', '2048'), 
            '(?s)e(?:N|n)(?:D|d)(?:M|m)(?:F|f).{0,1};.{0,2048}\\Z')

    #Originally Taken from  x-fmt/142
    def test_convert_to_regex_395(self):
        self.assertEqual(prepare.convert_to_regex('62(45|65)(47|67)(4D|6D)(46|66)*(4D|6D)(46|66)(56|76)(65|45)(52|72)(53|73)(49|69)(4F|6F)(4E|6E){1}31', 'Little', 'BOF', '0', ''), 
            '(?s)\\Ab(?:E|e)(?:G|g)(?:M|m)(?:F|f).*(?:M|m)(?:F|f)(?:V|v)(?:e|E)(?:R|r)(?:S|s)(?:I|i)(?:O|o)(?:N|n).{1}1')

    #Originally Taken from  x-fmt/142
    def test_convert_to_regex_396(self):
        self.assertEqual(prepare.convert_to_regex('45(4E|6E)(44|64)(4D|6D)(46|66){0-1}3B', 'Little', 'EOF', '0', '2048'), 
            '(?s)E(?:N|n)(?:D|d)(?:M|m)(?:F|f).{0,1};.{0,2048}\\Z')

    #Originally Taken from  x-fmt/142
    def test_convert_to_regex_397(self):
        self.assertEqual(prepare.convert_to_regex('62(45|65)(47|67)(4D|6D)(46|66)*(4D|6D)(46|66)(56|76)(65|45)(52|72)(53|73)(49|69)(4F|6F)(4E|6E){1}31', 'Little', 'BOF', '0', ''), 
            '(?s)\\Ab(?:E|e)(?:G|g)(?:M|m)(?:F|f).*(?:M|m)(?:F|f)(?:V|v)(?:e|E)(?:R|r)(?:S|s)(?:I|i)(?:O|o)(?:N|n).{1}1')

    #Originally Taken from  x-fmt/142
    def test_convert_to_regex_398(self):
        self.assertEqual(prepare.convert_to_regex('65(4E|6E)(44|64)(4D|6D)(46|66){0-1}3B', 'Little', 'EOF', '0', '2048'), 
            '(?s)e(?:N|n)(?:D|d)(?:M|m)(?:F|f).{0,1};.{0,2048}\\Z')

    #Originally Taken from  x-fmt/147
    def test_convert_to_regex_399(self):
        self.assertEqual(prepare.convert_to_regex('0008(00|02)[01:20]{51}0C{34}00000000', 'Little', 'BOF', '2', ''), 
            '(?s)\\A.{2}\\x00\\x08(?:\\x00|\\x02)[\\x01- ].{51}\\x0c.{34}\\x00\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/153
    def test_convert_to_regex_400(self):
        self.assertEqual(prepare.convert_to_regex('0100000058000000{32}20454D4600000100{16}00000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x01\\x00\\x00\\x00X\\x00\\x00\\x00.{32} EMF\\x00\\x00\\x01\\x00.{16}\\x00\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/153
    def test_convert_to_regex_401(self):
        self.assertEqual(prepare.convert_to_regex('01000000{36}20454D4600000100{16}58000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x01\\x00\\x00\\x00.{36} EMF\\x00\\x00\\x01\\x00.{16}X\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/154
    def test_convert_to_regex_402(self):
        self.assertEqual(prepare.convert_to_regex('11AF{6}08{24}00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000{4}FAF1{2}0000000000000000', 'Little', 'BOF', '4', ''), 
            '(?s)\\A.{4}\\x11\\xaf.{6}\\x08.{24}\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00.{4}\\xfa\\xf1.{2}\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/157
    def test_convert_to_regex_403(self):
        self.assertEqual(prepare.convert_to_regex('(464F524D|4C495354|43415420)00', 'Little', 'BOF', '0', ''), 
            '(?s)\\A(?:FORM|LIST|CAT )\\x00')

    #Originally Taken from  x-fmt/159
    def test_convert_to_regex_404(self):
        self.assertEqual(prepare.convert_to_regex('0001000800(01|04)0002', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x01\\x00\\x08\\x00(?:\\x01|\\x04)\\x00\\x02')

    #Originally Taken from  x-fmt/162
    def test_convert_to_regex_405(self):
        self.assertEqual(prepare.convert_to_regex('3C4D494646696C6520{4}3E2023', 'Little', 'BOF', '0', ''), 
            '(?s)\\A<MIFFile .{4}> #')

    #Originally Taken from  x-fmt/183
    def test_convert_to_regex_406(self):
        self.assertEqual(prepare.convert_to_regex('727473703A2F2F', 'Little', 'BOF', '0', ''), 
            '(?s)\\Artsp://')

    #Originally Taken from  x-fmt/190
    def test_convert_to_regex_407(self):
        self.assertEqual(prepare.convert_to_regex('2E524D4600000012', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\.RMF\\x00\\x00\\x00\\x12')

    #Originally Taken from  x-fmt/191
    def test_convert_to_regex_408(self):
        self.assertEqual(prepare.convert_to_regex('5B7665725D{6}5B7374795D*5B65646F635D', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\[ver\\].{6}\\[sty\\].*\\[edoc\\]')

    #Originally Taken from  x-fmt/19
    def test_convert_to_regex_409(self):
        self.assertEqual(prepare.convert_to_regex('4D4D{4}02000A000000(03|04){3}3D3D', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMM.{4}\\x02\\x00\\n\\x00\\x00\\x00(?:\\x03|\\x04).{3}==')

    #Originally Taken from  x-fmt/1
    def test_convert_to_regex_410(self):
        self.assertEqual(prepare.convert_to_regex('FE3400(C1|00)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xfe4\\x00(?:\\xc1|\\x00)')

    #Originally Taken from  x-fmt/212
    def test_convert_to_regex_411(self):
        self.assertEqual(prepare.convert_to_regex('00001A0002100400', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x1a\\x00\\x02\\x10\\x04\\x00')

    #Originally Taken from  x-fmt/218
    def test_convert_to_regex_412(self):
        self.assertEqual(prepare.convert_to_regex('0000270AFFFF(FC14|FBF8)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\'\\n\\xff\\xff(?:\\xfc\\x14|\\xfb\\xf8)')

    #Originally Taken from  x-fmt/219
    def test_convert_to_regex_413(self):
        self.assertEqual(prepare.convert_to_regex('66696C65646573633A2F2F{34-300}55524C2049502D6164647265737320417263686976652D6461746520436F6E74656E742D7479706520417263686976652D6C656E677468', 'Little', 'BOF', '0', ''), 
            '(?s)\\Afiledesc://.{34,300}URL IP-address Archive-date Content-type Archive-length')

    #Originally Taken from  x-fmt/220
    def test_convert_to_regex_414(self):
        self.assertEqual(prepare.convert_to_regex('2A424547494E205350524541445348454554532056455253494F4E3D', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\*BEGIN SPREADSHEETS VERSION=')

    #Originally Taken from  x-fmt/220
    def test_convert_to_regex_415(self):
        self.assertEqual(prepare.convert_to_regex('2A454E44205350524541445348454554530A', 'Little', 'EOF', '0', ''), 
            '(?s)\\*END SPREADSHEETS\\n\\Z')

    #Originally Taken from  x-fmt/221
    def test_convert_to_regex_416(self):
        self.assertEqual(prepare.convert_to_regex('2077000240', 'Little', 'BOF', '0', ''), 
            '(?s)\\A w\\x00\\x02@')

    #Originally Taken from  x-fmt/221
    def test_convert_to_regex_417(self):
        self.assertEqual(prepare.convert_to_regex('20770033', 'Little', 'BOF', '0', ''), 
            '(?s)\\A w\\x003')

    #Originally Taken from  x-fmt/223
    def test_convert_to_regex_418(self):
        self.assertEqual(prepare.convert_to_regex('1991[!4001C80000000000]', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x19\\x91(!@\\x01\\xc8\\x00\\x00\\x00\\x00\\x00)')

    #Originally Taken from  x-fmt/226
    def test_convert_to_regex_419(self):
        self.assertEqual(prepare.convert_to_regex('4558502020[30:31]', 'Little', 'BOF', '0', ''), 
            '(?s)\\AEXP  [0-1]')

    #Originally Taken from  x-fmt/226
    def test_convert_to_regex_420(self):
        self.assertEqual(prepare.convert_to_regex('454F49{0-2}454F53{0-2}0A', 'Little', 'EOF', '0', ''), 
            '(?s)EOI.{0,2}EOS.{0,2}\\n\\Z')

    #Originally Taken from  x-fmt/228
    def test_convert_to_regex_421(self):
        self.assertEqual(prepare.convert_to_regex('2A(424547494E|5354415254)205241535445522056455253494F4E3D', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\*(?:BEGIN|START) RASTER VERSION=')

    #Originally Taken from  x-fmt/228
    def test_convert_to_regex_422(self):
        self.assertEqual(prepare.convert_to_regex('2A454E44205241535445520A', 'Little', 'EOF', '0', ''), 
            '(?s)\\*END RASTER\\n\\Z')

    #Originally Taken from  x-fmt/230
    def test_convert_to_regex_423(self):
        self.assertEqual(prepare.convert_to_regex('4D5468640000000600[00:02]{4}4D54726B', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMThd\\x00\\x00\\x00\\x06\\x00[\\x00-\\x02].{4}MTrk')

    #Originally Taken from  x-fmt/231
    def test_convert_to_regex_424(self):
        self.assertEqual(prepare.convert_to_regex('56(45|65)(52|72)(53|73)(49|69)??(4E|6E){5-6}(43|63)(48|68)(41|61)(52|72)(53|73)(45|65)(54|74)*43(4F|6F)(4C|6C)(55|75)(4D|6D)(4E|6E)(53|73)', 'Little', 'BOF', '0', '10'), 
            '(?s)\\A.{0,10}V(?:E|e)(?:R|r)(?:S|s)(?:I|i).?(?:N|n).{5,6}(?:C|c)(?:H|h)(?:A|a)(?:R|r)(?:S|s)(?:E|e)(?:T|t).*C(?:O|o)(?:L|l)(?:U|u)(?:M|m)(?:N|n)(?:S|s)')

    #Originally Taken from  x-fmt/231
    def test_convert_to_regex_425(self):
        self.assertEqual(prepare.convert_to_regex('56(45|65)(52|72)(53|73)(49|69)??(4E|6E){5-6}(43|63)(48|68)(41|61)(52|72)(53|73)(45|65)(54|74)*63(4F|6F)(4C|6C)(55|75)(4D|6D)(4E|6E)(53|73)', 'Little', 'BOF', '0', ''), 
            '(?s)\\AV(?:E|e)(?:R|r)(?:S|s)(?:I|i).?(?:N|n).{5,6}(?:C|c)(?:H|h)(?:A|a)(?:R|r)(?:S|s)(?:E|e)(?:T|t).*c(?:O|o)(?:L|l)(?:U|u)(?:M|m)(?:N|n)(?:S|s)')

    #Originally Taken from  x-fmt/231
    def test_convert_to_regex_426(self):
        self.assertEqual(prepare.convert_to_regex('76(45|65)(52|72)(53|73)(49|69)??(4E|6E){5-6}(43|63)(48|68)(41|61)(52|72)(53|73)(45|65)(54|74)*43(4F|6F)(4C|6C)(55|75)(4D|6D)(4E|6E)(53|73)', 'Little', 'BOF', '0', ''), 
            '(?s)\\Av(?:E|e)(?:R|r)(?:S|s)(?:I|i).?(?:N|n).{5,6}(?:C|c)(?:H|h)(?:A|a)(?:R|r)(?:S|s)(?:E|e)(?:T|t).*C(?:O|o)(?:L|l)(?:U|u)(?:M|m)(?:N|n)(?:S|s)')

    #Originally Taken from  x-fmt/231
    def test_convert_to_regex_427(self):
        self.assertEqual(prepare.convert_to_regex('76(45|65)(52|72)(53|73)(49|69)??(4E|6E){5-6}(43|63)(48|68)(41|61)(52|72)(53|73)(45|65)(54|74)*63(4F|6F)(4C|6C)(55|75)(4D|6D)(4E|6E)(53|73)', 'Little', 'BOF', '0', ''), 
            '(?s)\\Av(?:E|e)(?:R|r)(?:S|s)(?:I|i).?(?:N|n).{5,6}(?:C|c)(?:H|h)(?:A|a)(?:R|r)(?:S|s)(?:E|e)(?:T|t).*c(?:O|o)(?:L|l)(?:U|u)(?:M|m)(?:N|n)(?:S|s)')

    #Originally Taken from  x-fmt/232
    def test_convert_to_regex_428(self):
        self.assertEqual(prepare.convert_to_regex('4D5058(2C|3B){1-50}(2C|3B)312E30', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMPX(?:,|;).{1,50}(?:,|;)1\\.0')

    #Originally Taken from  x-fmt/233
    def test_convert_to_regex_429(self):
        self.assertEqual(prepare.convert_to_regex('5061696E742053686F702050726F20496D6167652046696C650A1A00000000000300', 'Little', 'BOF', '0', ''), 
            '(?s)\\APaint Shop Pro Image File\\n\\x1a\\x00\\x00\\x00\\x00\\x00\\x03\\x00')

    #Originally Taken from  x-fmt/234
    def test_convert_to_regex_430(self):
        self.assertEqual(prepare.convert_to_regex('5061696E742053686F702050726F20496D6167652046696C650A1A00000000000500', 'Little', 'BOF', '0', ''), 
            '(?s)\\APaint Shop Pro Image File\\n\\x1a\\x00\\x00\\x00\\x00\\x00\\x05\\x00')

    #Originally Taken from  x-fmt/235
    def test_convert_to_regex_431(self):
        self.assertEqual(prepare.convert_to_regex('0000270A0000000000000000000000000000000000000000{4}E8030000{68}00000001', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\'\\n\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00.{4}\\xe8\\x03\\x00\\x00.{68}\\x00\\x00\\x00\\x01')

    #Originally Taken from  x-fmt/238
    def test_convert_to_regex_432(self):
        self.assertEqual(prepare.convert_to_regex('000100005374616E64617264204A65742044420000000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x01\\x00\\x00Standard Jet DB\\x00\\x00\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/238
    def test_convert_to_regex_433(self):
        self.assertEqual(prepare.convert_to_regex('41636365737356657273696F6E{0-1024}30362E[30:39][30:39]', 'Little', 'VAR', '0', ''), 
            '(?s)AccessVersion.{0,1024}06\\.[0-9][0-9]')

    #Originally Taken from  x-fmt/239
    def test_convert_to_regex_434(self):
        self.assertEqual(prepare.convert_to_regex('000100005374616e64617264204a65742044420000000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x01\\x00\\x00Standard Jet DB\\x00\\x00\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/239
    def test_convert_to_regex_435(self):
        self.assertEqual(prepare.convert_to_regex('41636365737356657273696f6e{0-1024}30372e[30:39][30:39]', 'Little', 'VAR', '0', ''), 
            '(?s)AccessVersion.{0,1024}07\\.[0-9][0-9]')

    #Originally Taken from  x-fmt/240
    def test_convert_to_regex_436(self):
        self.assertEqual(prepare.convert_to_regex('000100005374616E64617264204A65742044420001000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x01\\x00\\x00Standard Jet DB\\x00\\x01\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/240
    def test_convert_to_regex_437(self):
        self.assertEqual(prepare.convert_to_regex('410063006300650073007300560065007200730069006F006E{0-2048}300038002E00[30:39]00[30:39]', 'Little', 'VAR', '0', ''), 
            '(?s)A\\x00c\\x00c\\x00e\\x00s\\x00s\\x00V\\x00e\\x00r\\x00s\\x00i\\x00o\\x00n.{0,2048}0\\x008\\x00\\.\\x00[0-9]\\x00[0-9]')

    #Originally Taken from  x-fmt/241
    def test_convert_to_regex_438(self):
        self.assertEqual(prepare.convert_to_regex('000100005374616E64617264204A65742044420001000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x01\\x00\\x00Standard Jet DB\\x00\\x01\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/241
    def test_convert_to_regex_439(self):
        self.assertEqual(prepare.convert_to_regex('410063006300650073007300560065007200730069006F006E{0-2048}300039002E00[30:39]00[30:39]', 'Little', 'VAR', '0', ''), 
            '(?s)A\\x00c\\x00c\\x00e\\x00s\\x00s\\x00V\\x00e\\x00r\\x00s\\x00i\\x00o\\x00n.{0,2048}0\\x009\\x00\\.\\x00[0-9]\\x00[0-9]')

    #Originally Taken from  x-fmt/248
    def test_convert_to_regex_440(self):
        self.assertEqual(prepare.convert_to_regex('2142444E{4}534D(0E00|0F00)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A!BDN.{4}SM(?:\\x0e\\x00|\\x0f\\x00)')

    #Originally Taken from  x-fmt/249
    def test_convert_to_regex_441(self):
        self.assertEqual(prepare.convert_to_regex('2142444E{4}534D1700', 'Little', 'BOF', '0', ''), 
            '(?s)\\A!BDN.{4}SM\\x17\\x00')

    #Originally Taken from  x-fmt/263
    def test_convert_to_regex_442(self):
        self.assertEqual(prepare.convert_to_regex('504B0304', 'Little', 'BOF', '0', '4'), 
            '(?s)\\A.{0,4}PK\\x03\\x04')

    #Originally Taken from  x-fmt/263
    def test_convert_to_regex_443(self):
        self.assertEqual(prepare.convert_to_regex('504B01{43-65531}504B0506{18-65531}', 'Little', 'EOF', '0', ''), 
            '(?s)PK\\x01.{43,65531}PK\\x05\\x06.{18,65531}\\Z')

    #Originally Taken from  x-fmt/265
    def test_convert_to_regex_444(self):
        self.assertEqual(prepare.convert_to_regex('[21:EF]{104}[30:37][20:37]00{5}[30:37][20:37]00{5}[30:37][20:37]00{10}[30:37](00|20){10}[30:37](00|20){5}[30:37][00:37](00|20)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A[!-\\xef].{104}[0-7][ -7]\\x00.{5}[0-7][ -7]\\x00.{5}[0-7][ -7]\\x00.{10}[0-7](?:\\x00| ).{10}[0-7](?:\\x00| ).{5}[0-7][\\x00-7](?:\\x00| )')

    #Originally Taken from  x-fmt/266
    def test_convert_to_regex_445(self):
        self.assertEqual(prepare.convert_to_regex('1F8B08', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x1f\\x8b\\x08')

    #Originally Taken from  x-fmt/267
    def test_convert_to_regex_446(self):
        self.assertEqual(prepare.convert_to_regex('425A30', 'Little', 'BOF', '0', ''), 
            '(?s)\\ABZ0')

    #Originally Taken from  x-fmt/268
    def test_convert_to_regex_447(self):
        self.assertEqual(prepare.convert_to_regex('425A68??314159265359', 'Little', 'BOF', '0', ''), 
            '(?s)\\ABZh.?1AY&SY')

    #Originally Taken from  x-fmt/270
    def test_convert_to_regex_448(self):
        self.assertEqual(prepare.convert_to_regex('424D{12}(10|30|40)000000{8}0100', 'Little', 'BOF', '0', ''), 
            '(?s)\\ABM.{12}(?:\\x10|0|@)\\x00\\x00\\x00.{8}\\x01\\x00')

    #Originally Taken from  x-fmt/270
    def test_convert_to_regex_449(self):
        self.assertEqual(prepare.convert_to_regex('424D{12}28000000{8}0100180004000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\ABM.{12}\\(\\x00\\x00\\x00.{8}\\x01\\x00\\x18\\x00\\x04\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/270
    def test_convert_to_regex_450(self):
        self.assertEqual(prepare.convert_to_regex('424D{12}28000000{8}0100010003000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\ABM.{12}\\(\\x00\\x00\\x00.{8}\\x01\\x00\\x01\\x00\\x03\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/274
    def test_convert_to_regex_451(self):
        self.assertEqual(prepare.convert_to_regex('31BE000000AB{110}00', 'Little', 'BOF', '0', ''), 
            '(?s)\\A1\\xbe\\x00\\x00\\x00\\xab.{110}\\x00')

    #Originally Taken from  x-fmt/275
    def test_convert_to_regex_452(self):
        self.assertEqual(prepare.convert_to_regex('31BE000000AB{110}04', 'Little', 'BOF', '0', ''), 
            '(?s)\\A1\\xbe\\x00\\x00\\x00\\xab.{110}\\x04')

    #Originally Taken from  x-fmt/276
    def test_convert_to_regex_453(self):
        self.assertEqual(prepare.convert_to_regex('31BE000000AB{110}07', 'Little', 'BOF', '0', ''), 
            '(?s)\\A1\\xbe\\x00\\x00\\x00\\xab.{110}\\x07')

    #Originally Taken from  x-fmt/28
    def test_convert_to_regex_454(self):
        self.assertEqual(prepare.convert_to_regex('737263646F6369643A', 'Little', 'BOF', '0', ''), 
            '(?s)\\Asrcdocid:')

    #Originally Taken from  x-fmt/290
    def test_convert_to_regex_455(self):
        self.assertEqual(prepare.convert_to_regex('414D495F4D45544146494C455F464F524D41542056455253494F4E', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAMI_METAFILE_FORMAT VERSION')

    #Originally Taken from  x-fmt/291
    def test_convert_to_regex_456(self):
        self.assertEqual(prepare.convert_to_regex('524946(46|58){4}434452377672736E', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIF(?:F|X).{4}CDR7vrsn')

    #Originally Taken from  x-fmt/292
    def test_convert_to_regex_457(self):
        self.assertEqual(prepare.convert_to_regex('524946(46|58){4}434452387672736E', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIF(?:F|X).{4}CDR8vrsn')

    #Originally Taken from  x-fmt/297
    def test_convert_to_regex_458(self):
        self.assertEqual(prepare.convert_to_regex('5061696E742053686F702050726F20496D6167652046696C650A1A00000000000600', 'Little', 'BOF', '0', ''), 
            '(?s)\\APaint Shop Pro Image File\\n\\x1a\\x00\\x00\\x00\\x00\\x00\\x06\\x00')

    #Originally Taken from  x-fmt/298
    def test_convert_to_regex_459(self):
        self.assertEqual(prepare.convert_to_regex('5061696E742053686F702050726F20496D6167652046696C650A1A00000000000700', 'Little', 'BOF', '0', ''), 
            '(?s)\\APaint Shop Pro Image File\\n\\x1a\\x00\\x00\\x00\\x00\\x00\\x07\\x00')

    #Originally Taken from  x-fmt/29
    def test_convert_to_regex_460(self):
        self.assertEqual(prepare.convert_to_regex('524946(46|58){4}434452367672736E', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIF(?:F|X).{4}CDR6vrsn')

    #Originally Taken from  x-fmt/302
    def test_convert_to_regex_461(self):
        self.assertEqual(prepare.convert_to_regex('3C4D616B657246696C6520382E30483E', 'Little', 'BOF', '0', ''), 
            '(?s)\\A<MakerFile 8\\.0H>')

    #Originally Taken from  x-fmt/303
    def test_convert_to_regex_462(self):
        self.assertEqual(prepare.convert_to_regex('46483331', 'Little', 'BOF', '0', ''), 
            '(?s)\\AFH31')

    #Originally Taken from  x-fmt/307
    def test_convert_to_regex_463(self):
        self.assertEqual(prepare.convert_to_regex('000100{8}00100010{1}1040000008', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x01\\x00.{8}\\x00\\x10\\x00\\x10.{1}\\x10@\\x00\\x00\\x08')

    #Originally Taken from  x-fmt/309
    def test_convert_to_regex_464(self):
        self.assertEqual(prepare.convert_to_regex('5C31637720332E', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\\\1cw 3\\.')

    #Originally Taken from  x-fmt/314
    def test_convert_to_regex_465(self):
        self.assertEqual(prepare.convert_to_regex('55484C31{7}(57|45){7}(4E|53){60}445349', 'Little', 'BOF', '0', ''), 
            '(?s)\\AUHL1.{7}(?:W|E).{7}(?:N|S).{60}DSI')

    #Originally Taken from  x-fmt/317
    def test_convert_to_regex_466(self):
        self.assertEqual(prepare.convert_to_regex('2F322E[30:33](0D0A|0A)2850726F6A6563742E31(0D0A|0A)094E616D653A0922', 'Little', 'BOF', '0', ''), 
            '(?s)\\A/2\\.[0-3](?:\\r\\n|\\n)\\(Project\\.1(?:\\r\\n|\\n)\\x09Name:\\x09"')

    #Originally Taken from  x-fmt/320
    def test_convert_to_regex_467(self):
        self.assertEqual(prepare.convert_to_regex('464946', 'Little', 'BOF', '0', ''), 
            '(?s)\\AFIF')

    #Originally Taken from  x-fmt/324
    def test_convert_to_regex_468(self):
        self.assertEqual(prepare.convert_to_regex('53484F57', 'Little', 'BOF', '0', ''), 
            '(?s)\\ASHOW')

    #Originally Taken from  x-fmt/325
    def test_convert_to_regex_469(self):
        self.assertEqual(prepare.convert_to_regex('46616C63', 'Little', 'BOF', '0', ''), 
            '(?s)\\AFalc')

    #Originally Taken from  x-fmt/32
    def test_convert_to_regex_470(self):
        self.assertEqual(prepare.convert_to_regex('48474233', 'Little', 'BOF', '0', ''), 
            '(?s)\\AHGB3')

    #Originally Taken from  x-fmt/331
    def test_convert_to_regex_471(self):
        self.assertEqual(prepare.convert_to_regex('000002000680(02|96)00', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x02\\x00\\x06\\x80(?:\\x02|\\x96)\\x00')

    #Originally Taken from  x-fmt/340
    def test_convert_to_regex_472(self):
        self.assertEqual(prepare.convert_to_regex('576F726450726F0DFB000000000000000005985C8172030040CCC1BFFFBDF950', 'Little', 'BOF', '0', ''), 
            '(?s)\\AWordPro\\r\\xfb\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x05\\x98\\\\\\x81r\\x03\\x00@\\xcc\\xc1\\xbf\\xff\\xbd\\xf9P')

    #Originally Taken from  x-fmt/341
    def test_convert_to_regex_473(self):
        self.assertEqual(prepare.convert_to_regex('52494658{4}4D563933696D617000000018000000010000002C', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIFX.{4}MV93imap\\x00\\x00\\x00\\x18\\x00\\x00\\x00\\x01\\x00\\x00\\x00,')

    #Originally Taken from  x-fmt/348
    def test_convert_to_regex_474(self):
        self.assertEqual(prepare.convert_to_regex('B168DE3A', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xb1h\\xde:')

    #Originally Taken from  x-fmt/34
    def test_convert_to_regex_475(self):
        self.assertEqual(prepare.convert_to_regex('524946(46|58){4}434D5831', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIF(?:F|X).{4}CMX1')

    #Originally Taken from  x-fmt/35
    def test_convert_to_regex_476(self):
        self.assertEqual(prepare.convert_to_regex('524946(46|58){4}434D5831', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIF(?:F|X).{4}CMX1')

    #Originally Taken from  x-fmt/374
    def test_convert_to_regex_477(self):
        self.assertEqual(prepare.convert_to_regex('524946(46|58){4}434452397672736E', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIF(?:F|X).{4}CDR9vrsn')

    #Originally Taken from  x-fmt/375
    def test_convert_to_regex_478(self):
        self.assertEqual(prepare.convert_to_regex('524946(46|58){4}434452417672736E', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIF(?:F|X).{4}CDRAvrsn')

    #Originally Taken from  x-fmt/376
    def test_convert_to_regex_479(self):
        self.assertEqual(prepare.convert_to_regex('5061696E742053686F702050726F20496D6167652046696C650A1A00000000000800', 'Little', 'BOF', '0', ''), 
            '(?s)\\APaint Shop Pro Image File\\n\\x1a\\x00\\x00\\x00\\x00\\x00\\x08\\x00')

    #Originally Taken from  x-fmt/377
    def test_convert_to_regex_480(self):
        self.assertEqual(prepare.convert_to_regex('5061696E742053686F702050726F20496D6167652046696C650A1A00000000000400', 'Little', 'BOF', '0', ''), 
            '(?s)\\APaint Shop Pro Image File\\n\\x1a\\x00\\x00\\x00\\x00\\x00\\x04\\x00')

    #Originally Taken from  x-fmt/378
    def test_convert_to_regex_481(self):
        self.assertEqual(prepare.convert_to_regex('524946(46|58){4}434452427672736E', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIF(?:F|X).{4}CDRBvrsn')

    #Originally Taken from  x-fmt/37
    def test_convert_to_regex_482(self):
        self.assertEqual(prepare.convert_to_regex('50494146494C4556455253494F4E5F322E302C435442564552312C636F6D70726573730D0A706D7A6C6962636F646563', 'Little', 'BOF', '0', ''), 
            '(?s)\\APIAFILEVERSION_2\\.0,CTBVER1,compress\\r\\npmzlibcodec')

    #Originally Taken from  x-fmt/382
    def test_convert_to_regex_483(self):
        self.assertEqual(prepare.convert_to_regex('464C5601', 'Little', 'BOF', '0', ''), 
            '(?s)\\AFLV\\x01')

    #Originally Taken from  x-fmt/383
    def test_convert_to_regex_484(self):
        self.assertEqual(prepare.convert_to_regex('53494D504C4520203D202020202020202020202020202020202020202054{50}42495450495820203D{19}(2038|2B38|3038|3136|3332|3634){50}4E415849532020203D', 'Little', 'BOF', '0', ''), 
            '(?s)\\ASIMPLE  =                    T.{50}BITPIX  =.{19}(?: 8|\\+8|08|16|32|64).{50}NAXIS   =')

    #Originally Taken from  x-fmt/384
    def test_convert_to_regex_485(self):
        self.assertEqual(prepare.convert_to_regex('6D6F6F76{4}6D766864', 'Little', 'BOF', '4', ''), 
            '(?s)\\A.{4}moov.{4}mvhd')

    #Originally Taken from  x-fmt/384
    def test_convert_to_regex_486(self):
        self.assertEqual(prepare.convert_to_regex('6D646174*6D6F6F76{4}6D766864', 'Little', 'BOF', '4', ''), 
            '(?s)\\A.{4}mdat.*moov.{4}mvhd')

    #Originally Taken from  x-fmt/384
    def test_convert_to_regex_487(self):
        self.assertEqual(prepare.convert_to_regex('6D6F6F76{4}636D6F76{4}64636F6D', 'Little', 'BOF', '4', ''), 
            '(?s)\\A.{4}moov.{4}cmov.{4}dcom')

    #Originally Taken from  x-fmt/384
    def test_convert_to_regex_488(self):
        self.assertEqual(prepare.convert_to_regex('6D646174*6D6F6F76{4}636D6F76{4}64636F6D', 'Little', 'BOF', '4', ''), 
            '(?s)\\A.{4}mdat.*moov.{4}cmov.{4}dcom')

    #Originally Taken from  x-fmt/384
    def test_convert_to_regex_489(self):
        self.assertEqual(prepare.convert_to_regex('0000000877696465{4}6D646174*6D6F6F76{4}6D766864', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x00\\x08wide.{4}mdat.*moov.{4}mvhd')

    #Originally Taken from  x-fmt/384
    def test_convert_to_regex_490(self):
        self.assertEqual(prepare.convert_to_regex('0000000877696465{4}6D646174*6D6F6F76{4}636D6F76{4}64636F6D', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x00\\x08wide.{4}mdat.*moov.{4}cmov.{4}dcom')

    #Originally Taken from  x-fmt/384
    def test_convert_to_regex_491(self):
        self.assertEqual(prepare.convert_to_regex('6D646174', 'Little', 'BOF', '4', ''), 
            '(?s)\\A.{4}mdat')

    #Originally Taken from  x-fmt/385
    def test_convert_to_regex_492(self):
        self.assertEqual(prepare.convert_to_regex('000001BA{8-11}000001BB', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x01\\xba.{8,11}\\x00\\x00\\x01\\xbb')

    #Originally Taken from  x-fmt/386
    def test_convert_to_regex_493(self):
        self.assertEqual(prepare.convert_to_regex('000001BA{8-11}000001BB', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x01\\xba.{8,11}\\x00\\x00\\x01\\xbb')

    #Originally Taken from  x-fmt/387
    def test_convert_to_regex_494(self):
        self.assertEqual(prepare.convert_to_regex('4D4D002A', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMM\\x00\\*')

    #Originally Taken from  x-fmt/387
    def test_convert_to_regex_495(self):
        self.assertEqual(prepare.convert_to_regex('900000070000000430323230', 'Little', 'EOF', '0', '65535'), 
            '(?s)\\x90\\x00\\x00\\x07\\x00\\x00\\x00\\x040220.{0,65535}\\Z')

    #Originally Taken from  x-fmt/387
    def test_convert_to_regex_496(self):
        self.assertEqual(prepare.convert_to_regex('49492A00', 'Little', 'BOF', '0', ''), 
            '(?s)\\AII\\*\\x00')

    #Originally Taken from  x-fmt/387
    def test_convert_to_regex_497(self):
        self.assertEqual(prepare.convert_to_regex('009007000400000030323230', 'Little', 'EOF', '0', '65535'), 
            '(?s)\\x00\\x90\\x07\\x00\\x04\\x00\\x00\\x000220.{0,65535}\\Z')

    #Originally Taken from  x-fmt/387
    def test_convert_to_regex_498(self):
        self.assertEqual(prepare.convert_to_regex('4D4D002A', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMM\\x00\\*')

    #Originally Taken from  x-fmt/387
    def test_convert_to_regex_499(self):
        self.assertEqual(prepare.convert_to_regex('900000070000000430323230', 'Little', 'BOF', '10', '65535'), 
            '(?s)\\A.{10,65535}\\x90\\x00\\x00\\x07\\x00\\x00\\x00\\x040220')

    #Originally Taken from  x-fmt/387
    def test_convert_to_regex_500(self):
        self.assertEqual(prepare.convert_to_regex('49492A00', 'Little', 'BOF', '0', ''), 
            '(?s)\\AII\\*\\x00')

    #Originally Taken from  x-fmt/387
    def test_convert_to_regex_501(self):
        self.assertEqual(prepare.convert_to_regex('009007000400000030323230', 'Little', 'BOF', '10', '65535'), 
            '(?s)\\A.{10,65535}\\x00\\x90\\x07\\x00\\x04\\x00\\x00\\x000220')

    #Originally Taken from  x-fmt/388
    def test_convert_to_regex_502(self):
        self.assertEqual(prepare.convert_to_regex('4D4D002A', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMM\\x00\\*')

    #Originally Taken from  x-fmt/388
    def test_convert_to_regex_503(self):
        self.assertEqual(prepare.convert_to_regex('900000070000000430323130', 'Little', 'EOF', '0', '65535'), 
            '(?s)\\x90\\x00\\x00\\x07\\x00\\x00\\x00\\x040210.{0,65535}\\Z')

    #Originally Taken from  x-fmt/388
    def test_convert_to_regex_504(self):
        self.assertEqual(prepare.convert_to_regex('49492A00', 'Little', 'BOF', '0', ''), 
            '(?s)\\AII\\*\\x00')

    #Originally Taken from  x-fmt/388
    def test_convert_to_regex_505(self):
        self.assertEqual(prepare.convert_to_regex('009007000400000030323130', 'Little', 'EOF', '0', '65535'), 
            '(?s)\\x00\\x90\\x07\\x00\\x04\\x00\\x00\\x000210.{0,65535}\\Z')

    #Originally Taken from  x-fmt/388
    def test_convert_to_regex_506(self):
        self.assertEqual(prepare.convert_to_regex('4D4D002A', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMM\\x00\\*')

    #Originally Taken from  x-fmt/388
    def test_convert_to_regex_507(self):
        self.assertEqual(prepare.convert_to_regex('{10-65535}900000070000000430323130', 'Little', 'BOF', '0', ''), 
            '(?s)\\A.{10,65535}\\x90\\x00\\x00\\x07\\x00\\x00\\x00\\x040210')

    #Originally Taken from  x-fmt/388
    def test_convert_to_regex_508(self):
        self.assertEqual(prepare.convert_to_regex('49492A00', 'Little', 'BOF', '0', ''), 
            '(?s)\\AII\\*\\x00')

    #Originally Taken from  x-fmt/388
    def test_convert_to_regex_509(self):
        self.assertEqual(prepare.convert_to_regex('009007000400000030323130', 'Little', 'BOF', '10', '65535'), 
            '(?s)\\A.{10,65535}\\x00\\x90\\x07\\x00\\x04\\x00\\x00\\x000210')

    #Originally Taken from  x-fmt/389
    def test_convert_to_regex_510(self):
        self.assertEqual(prepare.convert_to_regex('52494646{4}57415645*666D7420{4}(01|07|11)00*4C495354{4}6578696665766572{4}30323130*64617461', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIFF.{4}WAVE.*fmt .{4}(?:\\x01|\\x07|\\x11)\\x00.*LIST.{4}exifever.{4}0210.*data')

    #Originally Taken from  x-fmt/390
    def test_convert_to_regex_511(self):
        self.assertEqual(prepare.convert_to_regex('FFD8FFE1{2}4578696600004D4D002A*900000070000000430323130', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xd8\\xff\\xe1.{2}Exif\\x00\\x00MM\\x00\\*.*\\x90\\x00\\x00\\x07\\x00\\x00\\x00\\x040210')

    #Originally Taken from  x-fmt/390
    def test_convert_to_regex_512(self):
        self.assertEqual(prepare.convert_to_regex('FFD9', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xd9\\Z')

    #Originally Taken from  x-fmt/390
    def test_convert_to_regex_513(self):
        self.assertEqual(prepare.convert_to_regex('FFD8FFE1{2}45786966000049492A00*009007000400000030323130', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xd8\\xff\\xe1.{2}Exif\\x00\\x00II\\*\\x00.*\\x00\\x90\\x07\\x00\\x04\\x00\\x00\\x000210')

    #Originally Taken from  x-fmt/390
    def test_convert_to_regex_514(self):
        self.assertEqual(prepare.convert_to_regex('FFD9', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xd9\\Z')

    #Originally Taken from  x-fmt/391
    def test_convert_to_regex_515(self):
        self.assertEqual(prepare.convert_to_regex('FFD8FFE1{2}4578696600004D4D002A*900000070000000430323230', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xd8\\xff\\xe1.{2}Exif\\x00\\x00MM\\x00\\*.*\\x90\\x00\\x00\\x07\\x00\\x00\\x00\\x040220')

    #Originally Taken from  x-fmt/391
    def test_convert_to_regex_516(self):
        self.assertEqual(prepare.convert_to_regex('FFD9', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xd9\\Z')

    #Originally Taken from  x-fmt/391
    def test_convert_to_regex_517(self):
        self.assertEqual(prepare.convert_to_regex('FFD8FFE1{2}45786966000049492A00*009007000400000030323230', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xd8\\xff\\xe1.{2}Exif\\x00\\x00II\\*\\x00.*\\x00\\x90\\x07\\x00\\x04\\x00\\x00\\x000220')

    #Originally Taken from  x-fmt/391
    def test_convert_to_regex_518(self):
        self.assertEqual(prepare.convert_to_regex('FFD9', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xd9\\Z')

    #Originally Taken from  x-fmt/392
    def test_convert_to_regex_519(self):
        self.assertEqual(prepare.convert_to_regex('0000000C6A5020200D0A870A', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x00\\x0cjP  \\r\\n\\x87\\n')

    #Originally Taken from  x-fmt/393
    def test_convert_to_regex_520(self):
        self.assertEqual(prepare.convert_to_regex('FF575043{5}0A0000{2}0000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xffWPC.{5}\\n\\x00\\x00.{2}\\x00\\x00')

    #Originally Taken from  x-fmt/394
    def test_convert_to_regex_521(self):
        self.assertEqual(prepare.convert_to_regex('FF575043{5}0A0001{2}0000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xffWPC.{5}\\n\\x00\\x01.{2}\\x00\\x00')

    #Originally Taken from  x-fmt/395
    def test_convert_to_regex_522(self):
        self.assertEqual(prepare.convert_to_regex('FF5750431000000001160100{2}0000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xffWPC\\x10\\x00\\x00\\x00\\x01\\x16\\x01\\x00.{2}\\x00\\x00')

    #Originally Taken from  x-fmt/396
    def test_convert_to_regex_523(self):
        self.assertEqual(prepare.convert_to_regex('52494646{4}57415645*666D7420{4}(01|07|11)00*4C495354{4}6578696665766572{4}30323230*64617461', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIFF.{4}WAVE.*fmt .{4}(?:\\x01|\\x07|\\x11)\\x00.*LIST.{4}exifever.{4}0220.*data')

    #Originally Taken from  x-fmt/397
    def test_convert_to_regex_524(self):
        self.assertEqual(prepare.convert_to_regex('52494646{4}57415645*666D7420{4}(01|07|11)00*4C495354{4}6578696665766572{4}30323030*64617461', 'Little', 'BOF', '0', ''), 
            '(?s)\\ARIFF.{4}WAVE.*fmt .{4}(?:\\x01|\\x07|\\x11)\\x00.*LIST.{4}exifever.{4}0200.*data')

    #Originally Taken from  x-fmt/398
    def test_convert_to_regex_525(self):
        self.assertEqual(prepare.convert_to_regex('FFD8FFE1{2}4578696600004D4D002A*900000070000000430323030', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xd8\\xff\\xe1.{2}Exif\\x00\\x00MM\\x00\\*.*\\x90\\x00\\x00\\x07\\x00\\x00\\x00\\x040200')

    #Originally Taken from  x-fmt/398
    def test_convert_to_regex_526(self):
        self.assertEqual(prepare.convert_to_regex('FFD9', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xd9\\Z')

    #Originally Taken from  x-fmt/398
    def test_convert_to_regex_527(self):
        self.assertEqual(prepare.convert_to_regex('FFD8FFE1{2}45786966000049492A00*009007000400000030323030', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xd8\\xff\\xe1.{2}Exif\\x00\\x00II\\*\\x00.*\\x00\\x90\\x07\\x00\\x04\\x00\\x00\\x000200')

    #Originally Taken from  x-fmt/398
    def test_convert_to_regex_528(self):
        self.assertEqual(prepare.convert_to_regex('FFD9', 'Little', 'EOF', '0', ''), 
            '(?s)\\xff\\xd9\\Z')

    #Originally Taken from  x-fmt/399
    def test_convert_to_regex_529(self):
        self.assertEqual(prepare.convert_to_regex('49492A00', 'Little', 'BOF', '0', ''), 
            '(?s)\\AII\\*\\x00')

    #Originally Taken from  x-fmt/399
    def test_convert_to_regex_530(self):
        self.assertEqual(prepare.convert_to_regex('009007000400000030323030', 'Little', 'EOF', '0', '65535'), 
            '(?s)\\x00\\x90\\x07\\x00\\x04\\x00\\x00\\x000200.{0,65535}\\Z')

    #Originally Taken from  x-fmt/399
    def test_convert_to_regex_531(self):
        self.assertEqual(prepare.convert_to_regex('4D4D002A', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMM\\x00\\*')

    #Originally Taken from  x-fmt/399
    def test_convert_to_regex_532(self):
        self.assertEqual(prepare.convert_to_regex('900000070000000430323030', 'Little', 'EOF', '0', '65535'), 
            '(?s)\\x90\\x00\\x00\\x07\\x00\\x00\\x00\\x040200.{0,65535}\\Z')

    #Originally Taken from  x-fmt/399
    def test_convert_to_regex_533(self):
        self.assertEqual(prepare.convert_to_regex('49492A00', 'Little', 'BOF', '0', ''), 
            '(?s)\\AII\\*\\x00')

    #Originally Taken from  x-fmt/399
    def test_convert_to_regex_534(self):
        self.assertEqual(prepare.convert_to_regex('009007000400000030323030', 'Little', 'BOF', '10', '65535'), 
            '(?s)\\A.{10,65535}\\x00\\x90\\x07\\x00\\x04\\x00\\x00\\x000200')

    #Originally Taken from  x-fmt/399
    def test_convert_to_regex_535(self):
        self.assertEqual(prepare.convert_to_regex('4D4D002A', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMM\\x00\\*')

    #Originally Taken from  x-fmt/399
    def test_convert_to_regex_536(self):
        self.assertEqual(prepare.convert_to_regex('900000070000000430323030', 'Little', 'BOF', '10', '65535'), 
            '(?s)\\A.{10,65535}\\x90\\x00\\x00\\x07\\x00\\x00\\x00\\x040200')

    #Originally Taken from  x-fmt/406
    def test_convert_to_regex_537(self):
        self.assertEqual(prepare.convert_to_regex('252150532D41646F62652D322E30', 'Little', 'BOF', '0', ''), 
            '(?s)\\A%!PS-Adobe-2\\.0')

    #Originally Taken from  x-fmt/407
    def test_convert_to_regex_538(self):
        self.assertEqual(prepare.convert_to_regex('252150532D41646F62652D322E31', 'Little', 'BOF', '0', ''), 
            '(?s)\\A%!PS-Adobe-2\\.1')

    #Originally Taken from  x-fmt/408
    def test_convert_to_regex_539(self):
        self.assertEqual(prepare.convert_to_regex('252150532D41646F62652D332E30', 'Little', 'BOF', '0', ''), 
            '(?s)\\A%!PS-Adobe-3\\.0')

    #Originally Taken from  x-fmt/409
    def test_convert_to_regex_540(self):
        self.assertEqual(prepare.convert_to_regex('4D5A', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMZ')

    #Originally Taken from  x-fmt/410
    def test_convert_to_regex_541(self):
        self.assertEqual(prepare.convert_to_regex('4D5A*4E45', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMZ.*NE')

    #Originally Taken from  x-fmt/411
    def test_convert_to_regex_542(self):
        self.assertEqual(prepare.convert_to_regex('4D5A*50450000', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMZ.*PE\\x00\\x00')

    #Originally Taken from  x-fmt/412
    def test_convert_to_regex_543(self):
        self.assertEqual(prepare.convert_to_regex('504B0304*4D4554412D494E462F4D414E49464553542E4D46', 'Little', 'BOF', '0', ''), 
            '(?s)\\APK\\x03\\x04.*META-INF/MANIFEST\\.MF')

    #Originally Taken from  x-fmt/412
    def test_convert_to_regex_544(self):
        self.assertEqual(prepare.convert_to_regex('504B0506{18-65531}', 'Little', 'EOF', '0', ''), 
            '(?s)PK\\x05\\x06.{18,65531}\\Z')

    #Originally Taken from  x-fmt/414
    def test_convert_to_regex_545(self):
        self.assertEqual(prepare.convert_to_regex('4D534346{20}0301', 'Little', 'BOF', '0', ''), 
            '(?s)\\AMSCF.{20}\\x03\\x01')

    #Originally Taken from  x-fmt/415
    def test_convert_to_regex_546(self):
        self.assertEqual(prepare.convert_to_regex('CAFEBABE', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xca\\xfe\\xba\\xbe')

    #Originally Taken from  x-fmt/416
    def test_convert_to_regex_547(self):
        self.assertEqual(prepare.convert_to_regex('28546869732066696C65206D75737420626520636F6E76657274656420776974682042696E486578', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\(This file must be converted with BinHex')

    #Originally Taken from  x-fmt/418
    def test_convert_to_regex_548(self):
        self.assertEqual(prepare.convert_to_regex('00000100[01:09]00{3}00[00:01]00{1}00{3}00', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x00\\x01\\x00[\\x01-\\x09]\\x00.{3}\\x00[\\x00-\\x01]\\x00.{1}\\x00.{3}\\x00')

    #Originally Taken from  x-fmt/418
    def test_convert_to_regex_549(self):
        self.assertEqual(prepare.convert_to_regex('000028000000{2}0000{2}00000100[01:20]0000000000', 'Little', 'VAR', '18', '1024'), 
            '(?s)\\x00\\x00\\(\\x00\\x00\\x00.{2}\\x00\\x00.{2}\\x00\\x00\\x01\\x00[\\x01- ]\\x00\\x00\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/41
    def test_convert_to_regex_550(self):
        self.assertEqual(prepare.convert_to_regex('5441424C450D0A302C310D0A22{1-100}220D0A564543544F52530D0A', 'Little', 'BOF', '0', ''), 
            '(?s)\\ATABLE\\r\\n0,1\\r\\n".{1,100}"\\r\\nVECTORS\\r\\n')

    #Originally Taken from  x-fmt/420
    def test_convert_to_regex_551(self):
        self.assertEqual(prepare.convert_to_regex('5B(56|76)657273696F6E5D0D0A(53|73)69676E6174757265{0-1}3D{0-2}24(4368696361676F|4348494341474F)24{0-1}0D0A', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}\\[(?:V|v)ersion\\]\\r\\n(?:S|s)ignature.{0,1}=.{0,2}\\$(?:Chicago|CHICAGO)\\$.{0,1}\\r\\n')

    #Originally Taken from  x-fmt/420
    def test_convert_to_regex_552(self):
        self.assertEqual(prepare.convert_to_regex('5B(56|76)657273696F6E5D0D0A(53|73)69676E6174757265{0-3}3D{0-1}2224(57494E444F5753|57696E646F7773)204E5424220D0A', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}\\[(?:V|v)ersion\\]\\r\\n(?:S|s)ignature.{0,3}=.{0,1}"\\$(?:WINDOWS|Windows) NT\\$"\\r\\n')

    #Originally Taken from  x-fmt/420
    def test_convert_to_regex_553(self):
        self.assertEqual(prepare.convert_to_regex('5B(56|76)657273696F6E5D0D0A(53|73)69676E6174757265{0-3}3D{0-1}2224(57494E444F5753|57696E646F7773)20393524220D0A', 'Little', 'BOF', '0', '1024'), 
            '(?s)\\A.{0,1024}\\[(?:V|v)ersion\\]\\r\\n(?:S|s)ignature.{0,3}=.{0,1}"\\$(?:WINDOWS|Windows) 95\\$"\\r\\n')

    #Originally Taken from  x-fmt/428
    def test_convert_to_regex_554(self):
        self.assertEqual(prepare.convert_to_regex('4C0000000114020000000000C000000000000046', 'Little', 'BOF', '0', ''), 
            '(?s)\\AL\\x00\\x00\\x00\\x01\\x14\\x02\\x00\\x00\\x00\\x00\\x00\\xc0\\x00\\x00\\x00\\x00\\x00\\x00F')

    #Originally Taken from  x-fmt/430
    def test_convert_to_regex_555(self):
        self.assertEqual(prepare.convert_to_regex('D0CF11E0A1B11AE1{20}FEFF', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xd0\\xcf\\x11\\xe0\\xa1\\xb1\\x1a\\xe1.{20}\\xfe\\xff')

    #Originally Taken from  x-fmt/430
    def test_convert_to_regex_556(self):
        self.assertEqual(prepare.convert_to_regex('49504D2E4E6F7465', 'Little', 'VAR', '0', ''), 
            '(?s)IPM\\.Note')

    #Originally Taken from  x-fmt/430
    def test_convert_to_regex_557(self):
        self.assertEqual(prepare.convert_to_regex('720065006300690070005F00760065007200730069006F006E00', 'Little', 'VAR', '0', ''), 
            '(?s)r\\x00e\\x00c\\x00i\\x00p\\x00_\\x00v\\x00e\\x00r\\x00s\\x00i\\x00o\\x00n\\x00')

    #Originally Taken from  x-fmt/432
    def test_convert_to_regex_558(self):
        self.assertEqual(prepare.convert_to_regex('33442047656F6D657472792046696C6520466F726D617420202020202020203401000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A3D Geometry File Format        4\\x01\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/433
    def test_convert_to_regex_559(self):
        self.assertEqual(prepare.convert_to_regex('33442047656F6D657472792046696C6520466F726D617420202020202020203101000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A3D Geometry File Format        1\\x01\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/434
    def test_convert_to_regex_560(self):
        self.assertEqual(prepare.convert_to_regex('33442047656F6D657472792046696C6520466F726D617420202020202020203201000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A3D Geometry File Format        2\\x01\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/435
    def test_convert_to_regex_561(self):
        self.assertEqual(prepare.convert_to_regex('33442047656F6D657472792046696C6520466F726D617420202020202020203301000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A3D Geometry File Format        3\\x01\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/436
    def test_convert_to_regex_562(self):
        self.assertEqual(prepare.convert_to_regex('4341544941202020{2024}434154494120534F4C5554494F4E53205634{6}52454C4541534520', 'Little', 'BOF', '80', ''), 
            '(?s)\\A.{80}CATIA   .{2024}CATIA SOLUTIONS V4.{6}RELEASE ')

    #Originally Taken from  x-fmt/438
    def test_convert_to_regex_563(self):
        self.assertEqual(prepare.convert_to_regex('56355F434656320000*2E4341544D6174657269616C', 'Little', 'BOF', '0', ''), 
            '(?s)\\AV5_CFV2\\x00\\x00.*\\.CATMaterial')

    #Originally Taken from  x-fmt/439
    def test_convert_to_regex_564(self):
        self.assertEqual(prepare.convert_to_regex('56355F434656320000*2E43415450617274', 'Little', 'BOF', '0', ''), 
            '(?s)\\AV5_CFV2\\x00\\x00.*\\.CATPart')

    #Originally Taken from  x-fmt/440
    def test_convert_to_regex_565(self):
        self.assertEqual(prepare.convert_to_regex('56355F434656320000*2E43415450726F64756374', 'Little', 'BOF', '0', ''), 
            '(?s)\\AV5_CFV2\\x00\\x00.*\\.CATProduct')

    #Originally Taken from  x-fmt/44
    def test_convert_to_regex_566(self):
        self.assertEqual(prepare.convert_to_regex('FF575043{4}010A0201', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xffWPC.{4}\\x01\\n\\x02\\x01')

    #Originally Taken from  x-fmt/450
    def test_convert_to_regex_567(self):
        self.assertEqual(prepare.convert_to_regex('0606EDF5D81D46E5BD31EFE7FE74B71D444F43554D454E54', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x06\\x06\\xed\\xf5\\xd8\\x1dF\\xe5\\xbd1\\xef\\xe7\\xfet\\xb7\\x1dDOCUMENT')

    #Originally Taken from  x-fmt/451
    def test_convert_to_regex_568(self):
        self.assertEqual(prepare.convert_to_regex('FFFEFF0E53006B0065007400630068005500700020004D006F00640065006C00', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xfe\\xff\\x0eS\\x00k\\x00e\\x00t\\x00c\\x00h\\x00U\\x00p\\x00 \\x00M\\x00o\\x00d\\x00e\\x00l\\x00')

    #Originally Taken from  x-fmt/452
    def test_convert_to_regex_569(self):
        self.assertEqual(prepare.convert_to_regex('FFFEFF0E53006B0065007400630068005500700020004D006F00640065006C00', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xff\\xfe\\xff\\x0eS\\x00k\\x00e\\x00t\\x00c\\x00h\\x00U\\x00p\\x00 \\x00M\\x00o\\x00d\\x00e\\x00l\\x00')

    #Originally Taken from  x-fmt/453
    def test_convert_to_regex_570(self):
        self.assertEqual(prepare.convert_to_regex('0001000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x00\\x01\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/454
    def test_convert_to_regex_571(self):
        self.assertEqual(prepare.convert_to_regex('5B496E7465726E657453686F72746375745D', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\[InternetShortcut\\]')

    #Originally Taken from  x-fmt/455
    def test_convert_to_regex_572(self):
        self.assertEqual(prepare.convert_to_regex('4143313032310000', 'Little', 'BOF', '0', ''), 
            '(?s)\\AAC1021\\x00\\x00')

    #Originally Taken from  x-fmt/49
    def test_convert_to_regex_573(self):
        self.assertEqual(prepare.convert_to_regex('28445746205630??2E????29', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\(DWF V0.?\\..?.?\\)')

    #Originally Taken from  x-fmt/64
    def test_convert_to_regex_574(self):
        self.assertEqual(prepare.convert_to_regex('FE37001C', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xfe7\\x00\\x1c')

    #Originally Taken from  x-fmt/65
    def test_convert_to_regex_575(self):
        self.assertEqual(prepare.convert_to_regex('FE370023', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xfe7\\x00#')

    #Originally Taken from  x-fmt/66
    def test_convert_to_regex_576(self):
        self.assertEqual(prepare.convert_to_regex('01000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x01\\x00\\x00\\x00')

    #Originally Taken from  x-fmt/66
    def test_convert_to_regex_577(self):
        self.assertEqual(prepare.convert_to_regex('41636365737356657273696F6E{0-32}30322E[30:39][30:39]', 'Little', 'VAR', '0', ''), 
            '(?s)AccessVersion.{0,32}02\\.[0-9][0-9]')

    #Originally Taken from  x-fmt/75
    def test_convert_to_regex_578(self):
        self.assertEqual(prepare.convert_to_regex('2142444E{4}4142', 'Little', 'BOF', '0', ''), 
            '(?s)\\A!BDN.{4}AB')

    #Originally Taken from  x-fmt/78
    def test_convert_to_regex_579(self):
        self.assertEqual(prepare.convert_to_regex('50494146494C4556455253494F4E5F322E302C504333564552312C636F6D70726573730D0A706D7A6C6962636F646563', 'Little', 'BOF', '0', ''), 
            '(?s)\\APIAFILEVERSION_2\\.0,PC3VER1,compress\\r\\npmzlibcodec')

    #Originally Taken from  x-fmt/80
    def test_convert_to_regex_580(self):
        self.assertEqual(prepare.convert_to_regex('1101', 'Little', 'BOF', '522', ''), 
            '(?s)\\A.{522}\\x11\\x01')

    #Originally Taken from  x-fmt/82
    def test_convert_to_regex_581(self):
        self.assertEqual(prepare.convert_to_regex('010000000100080044000000000C7F0906', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x01\\x00\\x00\\x00\\x01\\x00\\x08\\x00D\\x00\\x00\\x00\\x00\\x0c\\x7f\\x09\\x06')

    #Originally Taken from  x-fmt/88
    def test_convert_to_regex_582(self):
        self.assertEqual(prepare.convert_to_regex('D0CF11E0A1B11AE1{20}FEFF', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\xd0\\xcf\\x11\\xe0\\xa1\\xb1\\x1a\\xe1.{20}\\xfe\\xff')

    #Originally Taken from  x-fmt/88
    def test_convert_to_regex_583(self):
        self.assertEqual(prepare.convert_to_regex('5000500034003000', 'Little', 'VAR', '0', ''), 
            '(?s)P\\x00P\\x004\\x000\\x00')

    #Originally Taken from  x-fmt/88
    def test_convert_to_regex_584(self):
        self.assertEqual(prepare.convert_to_regex('4D6963726F736F667420506F776572506F696E74', 'Little', 'VAR', '0', ''), 
            '(?s)Microsoft PowerPoint')

    #Originally Taken from  x-fmt/91
    def test_convert_to_regex_585(self):
        self.assertEqual(prepare.convert_to_regex('252150532D41646F62652D312E30', 'Little', 'BOF', '0', ''), 
            '(?s)\\A%!PS-Adobe-1\\.0')

    #Originally Taken from  x-fmt/91
    def test_convert_to_regex_586(self):
        self.assertEqual(prepare.convert_to_regex('2525454F46(0D|0A|0D0A)', 'Little', 'EOF', '0', ''), 
            '(?s)%%EOF(?:\\r|\\n|\\r\\n)\\Z')

    #Originally Taken from  x-fmt/92
    def test_convert_to_regex_587(self):
        self.assertEqual(prepare.convert_to_regex('38425053000100000000000000', 'Little', 'BOF', '0', ''), 
            '(?s)\\A8BPS\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00')

    #Originally Taken from  fmt/328
    def test_convert_to_regex_588(self):
        self.assertEqual(prepare.convert_to_regex('254120[41:5A]*(0A|0A0D)25(44|54)20([30:39]|[41:5A])', 'Little', 'BOF', '0', '154'), 
            '(?s)\\A.{0,154}%A [A-Z].*(?:\\n|\\n\\r)%(?:D|T) (?:[0-9]|[A-Z])')

    #Originally Taken from  fmt/328
    def test_convert_to_regex_589(self):
        self.assertEqual(prepare.convert_to_regex('2541[41:5A]*(0A|0A0D)25(44|54)([30:39]|[41:5A])', 'Little', 'BOF', '0', '154'), 
            '(?s)\\A.{0,154}%A[A-Z].*(?:\\n|\\n\\r)%(?:D|T)(?:[0-9]|[A-Z])')

    #Originally Taken from  fmt/363
    def test_convert_to_regex_590(self):
        self.assertEqual(prepare.convert_to_regex('40404040404040404040404040404040404040404040', 'Little', 'BOF', '0', '320'), 
            '(?s)\\A.{0,320}@@@@@@@@@@@@@@@@@@@@@@')

    #Originally Taken from  fmt/363
    def test_convert_to_regex_591(self):
        self.assertEqual(prepare.convert_to_regex('0000{15}[!00]{3}[!00]{2}(0100|00[01:08])', 'Little', 'BOF', '3200', ''), 
            '(?s)\\A.{3200}\\x00\\x00.{15}(!\\x00).{3}(!\\x00).{2}(?:\\x01\\x00|\\x00[\\x01-\\x08])')

    #Originally Taken from  fmt/363
    def test_convert_to_regex_592(self):
        self.assertEqual(prepare.convert_to_regex('40404040404040404040404040404040404040404040', 'Little', 'BOF', '0', '320'), 
            '(?s)\\A.{0,320}@@@@@@@@@@@@@@@@@@@@@@')

    #Originally Taken from  fmt/363
    def test_convert_to_regex_593(self):
        self.assertEqual(prepare.convert_to_regex('0000{15}[!00]{3}[!00]{2}(0100|00[01:08])', 'Little', 'BOF', '3600', ''), 
            '(?s)\\A.{3600}\\x00\\x00.{15}(!\\x00).{3}(!\\x00).{2}(?:\\x01\\x00|\\x00[\\x01-\\x08])')

    #Originally Taken from  x-fmt/158
    def test_convert_to_regex_594(self):
        self.assertEqual(prepare.convert_to_regex('53(202020202020|303030303030)31(0D0A|0A){72}(5320202020202032|5330303030303032|4720202020202031|4730303030303031)', 'Little', 'IBOF', '72', ''), 
            #'(?s)S(?:      |000000)1(?:\\r\\n|\\n).{72}(?:S      2|S0000002|G      1|G0000001)')
            'TODO : IBOF needs to be handled (New position type)')

    #Originally Taken from  x-fmt/271
    def test_convert_to_regex_595(self):
        self.assertEqual(prepare.convert_to_regex('83??[01:0C][01:1F]{28}([41:5A]|[61:7A]){10}(43|44|4C|4D|4E)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x83.?[\\x01-\\x0c][\\x01-\\x1f].{28}(?:[A-Z]|[a-z]).{10}(?:C|D|L|M|N)')

    #Originally Taken from  x-fmt/429
    def test_convert_to_regex_596(self):
        self.assertEqual(prepare.convert_to_regex('46726F6D3A', 'Little', 'BOF', '0', ''), 
            '(?s)\\AFrom:')

    #Originally Taken from  x-fmt/429
    def test_convert_to_regex_597(self):
        self.assertEqual(prepare.convert_to_regex('5375626A6563743A{1-100}446174653A{1-100}4D494D452D56657273696F6E3A{1-100}436F6E74656E742D547970653A206D756C7469706172742F72656C617465643B', 'Little', 'IBOF', '0', '105'), 
            #'(?s)Subject:.{1,100}Date:.{1,100}MIME-Version:.{1,100}Content-Type: multipart/related;')
            'TODO : IBOF needs to be handled (New position type)')

    #Originally Taken from  x-fmt/8
    def test_convert_to_regex_598(self):
        self.assertEqual(prepare.convert_to_regex('02{2}[01:1C][01:1F]????[00:03]([41:5A]|[61:7A]){10}(43|4E|4C)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x02.{2}[\\x01-\\x1c][\\x01-\\x1f].?.?[\\x00-\\x03](?:[A-Z]|[a-z]).{10}(?:C|N|L)')

    #Originally Taken from  x-fmt/8
    def test_convert_to_regex_599(self):
        self.assertEqual(prepare.convert_to_regex('02{2}000000??[00:03]([41:5A]|[61:7A]){10}(43|4E|4C)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x02.{2}\\x00\\x00\\x00.?[\\x00-\\x03](?:[A-Z]|[a-z]).{10}(?:C|N|L)')

    #Originally Taken from  x-fmt/9
    def test_convert_to_regex_600(self):
        self.assertEqual(prepare.convert_to_regex('03??[01:0C][01:1F]{28}([41:5A]|[61:7A]){10}(43|44|4C|4D|4E)', 'Little', 'BOF', '0', ''), 
            '(?s)\\A\\x03.?[\\x01-\\x0c][\\x01-\\x1f].{28}(?:[A-Z]|[a-z]).{10}(?:C|D|L|M|N)')

if __name__ == '__main__':
    unittest.main()
