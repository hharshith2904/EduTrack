import os
import unittest
from src.feedback_summary import get_top_scores, get_grade_wise_counts

class TestFeedbackSummary(unittest.TestCase):
    def setUp(self):
        """Create a test feedback file."""
        self.test_file = "test_feedback_summary.txt"
        with open(self.test_file, "w") as file:
            file.write("John,90,A\n")
            file.write("Jane,85,B\n")
            file.write("Doe,95,A\n")
            file.write("Alice,88,B\n")
            file.write("Bob,70,C\n")

    def tearDown(self):
        """Delete the test feedback file."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_get_top_scores(self):
        """Test extracting top scores."""
        top_scores = get_top_scores(self.test_file, top_n=3)
        self.assertEqual(top_scores, [95, 90, 88])

    def test_get_grade_wise_counts(self):
        """Test calculating grade-wise counts."""
        grade_counts = get_grade_wise_counts(self.test_file)
        self.assertEqual(grade_counts, {"A": 2, "B": 2, "C": 1})

if __name__ == "__main__":
    unittest.main()
