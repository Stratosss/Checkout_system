import unittest
import checkoutSystem

class resultsVerification(unittest.TestCase):
    #testing inputs
    #testing for wrong item code
    def test_val_one(self):
        data = [{'code': 'A', 'quantity': 3}, {'code': 23, 'quantity': 3}, {'code': 'C', 'quantity': 1}, {'code': 'D', 'quantity': 2}]
        self.assertRaises(SystemExit, checkoutSystem.fileFiltering,data)
        
    #testing for wrong item code 
    def test_val_two(self):
        data = [{'code': 'g', 'quantity':1}, {'code': 'B', 'quantity': 3}, {'code': 'C', 'quantity': 1}, {'code': 'D', 'quantity': 2}]
        self.assertRaises(SystemExit, checkoutSystem.fileFiltering,data) 
    
    #testing for string value in quantity field
    def test_val_three(self):
        data = [{'code': 'A', 'quantity':'string'}, {'code': 'B', 'quantity': 3}, {'code': 'C', 'quantity': 1}, {'code': 'D', 'quantity': 2}]
        self.assertRaises(SystemExit, checkoutSystem.fileFiltering, data)
        
    #testing for negative number value in quantity field
    def test_val_four(self):
        data = [{'code': 'A', 'quantity': 4}, {'code': 'B', 'quantity': 2}, {'code': 'C', 'quantity': -1}, {'code': 'D', 'quantity': 2}]
        self.assertRaises(SystemExit, checkoutSystem.fileFiltering, data)
        
    #testing for decimal value in quantity field
    def test_val_five(self):
        data = [{'code': 'A', 'quantity': 4}, {'code': 'B', 'quantity': 2.2}, {'code': 'C', 'quantity': -1}, {'code': 'D', 'quantity': 2}]
        self.assertRaises(SystemExit, checkoutSystem.fileFiltering, data) 
        
    #testing calculations
    def test_calc_one(self):
        data = {"A":6,"B":2,"C":1,"D":4}
        result = checkoutSystem.calculator(data)
        self.assertEqual(result, 340)
    
    def test_calc_two(self):
        data = {"A":2,"B":15,"C":3,"D":8}
        result = checkoutSystem.calculator(data)
        self.assertEqual(result, 555)
        
    def test_calc_three(self):
        data = {"A":0,"B":0,"C":0,"D":0}
        result = checkoutSystem.calculator(data)
        self.assertEqual(result, 0)  
    
    def test_calc_four(self):
        data = {"A":13,"B":2,"C":4,"D":5}
        result = checkoutSystem.calculator(data)
        self.assertEqual(result, 670)  
    
    def test_calc_five(self):
        data = {"A":2,"B":1,"C":3,"D":4}
        result = checkoutSystem.calculator(data)
        self.assertEqual(result, 135) 
    
    def test_calc_six(self):
        data = {"A":122,"B":133,"C":1,"D":2}
        result = checkoutSystem.calculator(data)
        self.assertEqual(result, 9695)     
        
if __name__=="__main__":
    unittest.main()