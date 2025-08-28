import unittest
import utils

class TestPalindrome(unittest.TestCase):
    def test_palindrome_lower(self):
        self.assertTrue(utils.is_palindrome("racecar"))
        self.assertTrue(utils.is_palindrome("madam"))
        self.assertFalse(utils.is_palindrome("palindrome"))
    def test_palindrome_mixed(self):
        self.assertTrue(utils.is_palindrome("Civic"))
        self.assertTrue(utils.is_palindrome("ciViC"))
        self.assertFalse(utils.is_palindrome("Utils"))
    def test_palindrome_ignore_nonalphanumeric(self):
        self.assertTrue(utils.is_palindrome("No melon, no lemon"))
        self.assertFalse(utils.is_palindrome("1 2 3 1"))
        self.assertTrue(utils.is_palindrome("12, ...|3|2|1!!!!!!!!!"))
    def test_palindrome_non_string(self):
        with self.assertRaises(Exception):
            utils.is_palindrome(["m", "a", "d", "a", "m"])
    def test_empty(self):
        self.assertTrue(utils.is_palindrome(""))
    def test_long(self):
        self.assertTrue(utils.is_palindrome("a"*500))
    
class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(utils.factorial(1), 1)
        self.assertEqual(utils.factorial(5), 120)
        self.assertEqual(utils.factorial(10), 3628800)
        self.assertEqual(utils.factorial(20), 2432902008176640000)
    def test_invalid_factorial(self):
        with self.assertRaises(ValueError):
            utils.factorial(-5)
        with self.assertRaises(ValueError):
            utils.factorial(-0.1)
    def test_zero_factorial(self):
        self.assertEqual(utils.factorial(0), 1)
    def test_float(self):
        with self.assertRaises(TypeError):
            f = utils.factorial(5.0)
            print(f)

class TestPrime(unittest.TestCase):
    def test_prime(self):
        for x in [2, 3, 5, 7, 11]:
            self.assertTrue(utils.is_prime(x))
    def test_not_prime(self):
        for x in [0, 1, 4, 8, 16, 32, 64, 128, 256]:
            self.assertFalse(utils.is_prime(x))
    # I can ony use somewhat big primes because chatgpt 
    # didn't use miller's algorithm so it's super slow
    def test_prime_big(self):
        self.assertTrue(utils.is_prime(5241300769))
    def test_not_prime_big(self):
        # two primes multiplied together
        self.assertFalse(utils.is_prime(81001 * 46411))
    def test_invalid(self):
        with self.assertRaises(Exception):
            utils.is_prime("seven")
        with self.assertRaises(Exception):
            utils.is_prime(3.4)
    def test_negative(self):
        for x in [-1, -10, -6, -893, -2]:
            self.assertFalse(utils.is_prime(x))

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(10):
            self.assertEqual(utils.fibonacci(i), fib[i])
    def test_negative_fibonacci(self):
        for i in range(-1, -10, -1):
            with self.assertRaises(ValueError):
                utils.fibonacci(i)
    def test_invalid(self):
        with self.assertRaises(Exception):
            utils.fibonacci("one")
            
class TestReverseWords(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(utils.reverse_words("This sentence is in reverse"), "reverse in is sentence This")
        self.assertEqual(utils.reverse_words("this sentence is good"), "good is sentence this")
        self.assertEqual(utils.reverse_words("fall leaves after leaves fall"), "fall leaves after leaves fall")
    def test_whitespace(self):
        self.assertEqual(utils.reverse_words("    \t \n \t\t"), "")
        self.assertEqual(utils.reverse_words("\tHow  are you     doing today?"), "today? doing you are How")
    def test_not_reverse(self):
        self.assertNotEqual(utils.reverse_words("backwards sentence"), "backwards sentence")
    def test_invalid(self):
        with self.assertRaises(Exception):
            utils.reverse_words(["words", "to", "reverse"])


class TestGCD(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(utils.gcd(100, 350), 50)
    def test_factor(self):
        self.assertEqual(utils.gcd(250, 50), 50)
        self.assertEqual(utils.gcd(33, 11), 11)
        self.assertEqual(utils.gcd(33, 3), 3)
    def test_gcd_one(self):
        self.assertEqual(utils.gcd(25, 68), 1)
    def test_gcd_negative(self):
        self.assertEqual(utils.gcd(-33, -11), 11)
        self.assertEqual(utils.gcd(-250, 50), 50)
        self.assertEqual(utils.gcd(20, -30), 10)
    def test_invalid(self):
        with self.assertRaises(Exception):
            utils.gcd("twenty", "four")
    def test_float(self):
        self.assertAlmostEqual(utils.gcd(3, 4.5), 1.5)
    def test_same(self):
        self.assertEqual(utils.gcd(50, 50), 50)
        self.assertEqual(utils.gcd(6, 6), 6)
        self.assertEqual(utils.gcd(-5, 5), 5)
        
        

if __name__ == "__main__":
    unittest.main()
    