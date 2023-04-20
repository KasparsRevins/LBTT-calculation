import unittest
from calculate_lbtt import calculate_lbtt

class TestCalc(unittest.TestCase):
    
    def test_add(self):
    # Buyers are exempt from LBTT for properties up to £145,000.

        self.assertEqual(calculate_lbtt(100000),0)
        self.assertEqual(calculate_lbtt(175000),600)
        self.assertEqual(calculate_lbtt(250000),2100)
        self.assertEqual(calculate_lbtt(325000),5850)
        self.assertEqual(calculate_lbtt(750000),48350)
        self.assertEqual(calculate_lbtt(1000000),78350)
        self.assertEqual(calculate_lbtt(-1),0)

    # First-time buyers are exempt from LBTT for properties up to £175,000.

        self.assertEqual(calculate_lbtt(175000,is_first_time_buyer=True),0)
        self.assertEqual(calculate_lbtt(175001,is_first_time_buyer=True),0.02)
        self.assertEqual(calculate_lbtt(250000,is_first_time_buyer=True),1500)
        self.assertEqual(calculate_lbtt(325000,is_first_time_buyer=True),5250)
        self.assertEqual(calculate_lbtt(750000,is_first_time_buyer=True),47750)
        self.assertEqual(calculate_lbtt(1000000,is_first_time_buyer=True),77750)
        self.assertEqual(calculate_lbtt(-1,is_first_time_buyer=True),0)

    # Additional homes buyers are subject to 6%, 8%, 11%, 16% and 18% tax.

        self.assertEqual(calculate_lbtt(40000,is_additional_home=True),2400)
        self.assertEqual(calculate_lbtt(145000,is_additional_home=True),8700)
        self.assertEqual(calculate_lbtt(250000,is_additional_home=True),17100)
        self.assertEqual(calculate_lbtt(325000,is_additional_home=True),25350)
        self.assertEqual(calculate_lbtt(500000,is_additional_home=True),53350)
        self.assertEqual(calculate_lbtt(750000,is_additional_home=True),93350)
        self.assertEqual(calculate_lbtt(1000000,is_additional_home=True),138350)
        self.assertEqual(calculate_lbtt(-1,is_additional_home=True),0)

if __name__ == "__main__":
    unittest.main()