'''
iterate = पुनरावर्ती करना
Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
The iterator object is initialized using the iter() method. It uses the next() method for iteration.

__iter(iterable)__ method that is called for the initialization of an iterator. This returns an iterator object
next ( __next__ in Python 3) The next method returns the next value for the iterable. When we use a for loop to traverse any iterable object,
 internally it uses the iter() method to get an iterator object which further uses next() method to iterate over.
 This method raises a StopIteration to signal the end of the iteration.

'''


nums = [7, 8, 9, 5]


it = iter(nums)

#print(it.__next__())
#print(it.__next__())

print(next(it))

for i in nums:
    print(i)


#creat own function
class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <=10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = TopTen()

for i in values:
    print(i)
