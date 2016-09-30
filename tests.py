import unittest
import popo


class PopoConstractorTest(unittest.TestCase):
    def test_success(self):
        class A(popo.Popo):
            first_name = popo.Field()
            last_name = popo.Field()
        a = A(first_name='first_name', last_name='last_name')
        self.assertEqual(a.first_name, 'first_name')
        self.assertEqual(a.last_name, 'last_name')


class A(popo.Popo):
    name = popo.Field()

class B(popo.Popo):
    foo = popo.Field()

class PopoMethodsTest(unittest.TestCase):

    def test_equal_simple(self):
        a = A(name='test')
        a1 = A(name='test')
        self.assertTrue(a == a1)

    def test_not_equal_simple(self):
        a = A(name='test')
        a1 = A(name='test1')
        self.assertFalse(a == a1)

    def test_equal_complex(self):
        c = B(foo=A(name='test'))
        c1 = B(foo=A(name='test'))
        self.assertTrue(c == c1)

    def test_not_equal_complex(self):
        c = B(foo=A(name='test'))
        c1 = B(foo=A(name='test1'))
        self.assertFalse(c == c1)

    def test_to_dict_simple(self):
        a = A(name='test')
        self.assertEqual(a.to_dict(), {'name': 'test'})

    def test_to_dict_complex(self):
        b = B(foo=A(name='test'))
        self.assertEqual(b.to_dict(), {'foo': {'name': 'test'}})

    def test_initialize_only_field_restriction(self):
        try:
            A(age=45)
            self.fail('Excepted value error')
        except ValueError:
            pass



class A1(popo.Popo):
    name = popo.Field()


class C1(popo.Popo):
    name = popo.Field()


class B1(popo.Popo):
    a = popo.Field(field_type=A1)



class PopoPropertyTestCase(unittest.TestCase):
    def test_success(self):
        b =  B1(a=A1(name='test'))
        self.assertEqual(b.a.name, 'test')

    def test_wrong_field_type(self):
        try:
            B1(a=C1(name='test'))
            self.fail('Expected value error as C1 is not A1')
        except ValueError:
            pass


unittest.main()
