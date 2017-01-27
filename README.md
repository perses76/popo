### Plain Old Python Object (POPO)

Analog of [POJO](https://www.martinfowler.com/bliki/POJO.html) in Python

Basic validation (if property exists, type of property) is implemented. You can create custom class of popo.Field if more validation required.

### Examples

#### Simple use
```python
class A(popo.Popo):
    first_name = popo.Field()
    last_name = popo.Field()
a = A(first_name='first_name', last_name='last_name')
assert a.first_name == 'first_name'
assert a.last_name == 'last_name'
```

#### Validate if field exists
```python
class A(popo.Popo):
    name = popo.Field()

try:
  A(age=45)
except ValueError:
    print('field age does not exists in class A')
```

#### Type validation
```python
class A1(popo.Popo):
    name = popo.Field()
    
class B1(popo.Popo):
    a = popo.Field(field_type=A1)
try:
  B1(a=45)
except ValueError:
    print('Property "a" accepts only type "A1"')
```


