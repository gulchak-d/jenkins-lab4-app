import unittest
import app as tested_app
import xmlrunner

class TestApp(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(tested_app.hello_world(), 'Hello new day')

if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
