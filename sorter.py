# Sort packages based on dimensions and mass
def sort(width, height, length, mass):
    
    # verify the parameters are all numbers greater than 0
    if not (isinstance(width, (int, float)) and width > 0):
        return "ERROR"

    if not (isinstance(height, (int, float)) and height > 0):
        return "ERROR"

    if not (isinstance(length, (int, float)) and length > 0):
        return "ERROR"

    if not (isinstance(mass, (int, float)) and mass > 0):
        return "ERROR"
      
    sides = [width, height, length]
    
   #verify we do not get an overflow on calculating the area.
    try:
        result = width * height * length
        if result > (2**31 - 1) or result < (-2**31):
            return "ERROR"
    except OverflowError as e:
        return "ERROR"
    
    bulky = any(num >= 150 for num in sides) or (result) >= 1000000
    heavy = mass >= 150
    
    if bulky and heavy:
        return "REJECTED"

    if not bulky and not heavy:
        return "STANDARD"
    
    return "SPECIAL"

# Unit Test
import unittest

class TestCompareNumbers(unittest.TestCase):
    def test_compare_numbers(self):
        print("unit testing")
        self.assertEqual(sort(50, 50, 50, 50), "STANDARD")
        self.assertEqual(sort(200, 50, 50, 50), "SPECIAL")
        self.assertEqual(sort(50, 200, 50, 50), "SPECIAL")
        self.assertEqual(sort(50, 50, 200, 50), "SPECIAL")
        self.assertEqual(sort(50, 50, 50, 200), "SPECIAL")
        self.assertEqual(sort(200, 50, 50, 200), "REJECTED")
        self.assertEqual(sort(0, 0, 0, 0), "ERROR")
        self.assertEqual(sort("a", "b", "c", "d"), "ERROR")
        self.assertEqual(sort(-50, 50, 50, 50), "ERROR")
        self.assertEqual(sort(50, -50, 50, 50), "ERROR")
        self.assertEqual(sort(50, 50, -50, 50), "ERROR")
        self.assertEqual(sort(50, 50, 50, -50), "ERROR")
        self.assertEqual(sort(1000000000, 3000, 50, 50), "ERROR")

if __name__ == '__main__':
    unittest.main()
