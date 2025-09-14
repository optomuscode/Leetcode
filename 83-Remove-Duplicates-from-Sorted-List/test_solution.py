import unittest
from solution import Solution, ListNode

# Helper function to create a linked list from a list
def create_linked_list(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    return items

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        head = create_linked_list([1, 1, 2])
        result = self.solver.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1, 2])

    def test_example_2(self):
        head = create_linked_list([1, 1, 2, 3, 3])
        result = self.solver.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_no_duplicates(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        result = self.solver.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5])

    def test_all_duplicates(self):
        head = create_linked_list([1, 1, 1, 1, 1])
        result = self.solver.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_empty_list(self):
        head = create_linked_list([])
        result = self.solver.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [])

if __name__ == '__main__':
    unittest.main()