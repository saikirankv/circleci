import unittest

class SampleTests(unittest.TestCase):
    
    x=10
    
    @classmethod
    def setUpClass(cls):
        super(SampleTests, cls).setUpClass()
        print 'x value in setup->',cls.x
        cls.x=25

    @classmethod
    def test_s1(self):
        print 'x value in 1->',self.x
        self.x=20
        
    def test_s2(self):
        d={"asdf":7890,"v":90}
        f={"v":90,"asdf":7890}
        s='f'
        f='g'
#         self.assertItemsEqual(['j','v'],['v','j','l'],"false")
#         self.assertDictEqual(d,f)
        self.assertEqual(s,f)
        print 'x value in 2->',self.x
