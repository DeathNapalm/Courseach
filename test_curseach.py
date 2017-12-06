from . import courseach
from . import convert_to_scr
import unittest


class CourseTest(unittest.TestCase):
    def test_seidel(self):
        self.assertEqual(courseach.seidel([[3.6, 1.8, 4.7],
                                           [2.7, 3.6, 1.9],
                                           [1.5, 4.5, 3.3]], [3.8, 0.4, -1.6], 0.001), [0.4, -0.0946, -0.54])


if __name__ == '__main__':
    unittest.main()