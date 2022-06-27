# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()

import pytest

from Stack import Stack


class TestStack:
    def test_stack_push_pop_single_item(self):
        test_stack = Stack()
        test_stack.push("first object")
        assert test_stack.size() == 1
        assert test_stack.pop() == "first object"

    def test_stack_item_order(self):
        test_stack = Stack()
        items_input = [1, 2, 3, 4, 5]
        items_output = []
        for item in items_input:
            test_stack.push(item)

        while not test_stack.empty():
            items_output.append(test_stack.pop())

        assert len(items_input) == len(items_output)
        items_output.reverse()
        assert items_input == items_output

    def test_stack_empty(self):
        test_stack = Stack()
        assert test_stack.empty() is True

        test_stack.push("Single Item")
        assert test_stack.empty() is False

        test_stack.pop()
        assert test_stack.empty() is True

    def test_stack_pop_empty(self):
        test_stack = Stack()
        assert test_stack.empty() is True
        with pytest.raises(Exception):
            test_stack.pop()

    def test_stack_peak(self):
        test_stack = Stack()
        test_stack.push(23)
        assert test_stack.peak() == 23

        test_stack.push(18)
        assert test_stack.peak() == 18

        test_stack.push(44)
        assert test_stack.peak() == 44

        test_stack.pop()
        assert test_stack.peak() == 18

        test_stack.pop()
        assert test_stack.peak() == 23
