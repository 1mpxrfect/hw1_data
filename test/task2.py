import unittest
from Task2.task_2 import generate_random_data, calculate_aggregated_threat_score


class TestAggregatedThreatScore(unittest.TestCase):

    def test_zero_threat(self):
        departments = [
            {"name": "Engineering", "importance": 2, "scores": [0] * 50},
            {"name": "Marketing", "importance": 3, "scores": [0] * 50},
            {"name": "Finance", "importance": 4, "scores": [0] * 50},
            {"name": "HR", "importance": 1, "scores": [0] * 50},
            {"name": "Science", "importance": 5, "scores": [0] * 50}
        ]
        score = calculate_aggregated_threat_score(departments)
        self.assertEqual(score, 0)

    def test_max_threat(self):
        departments = [
            {"name": "Engineering", "importance": 1, "scores": [95] * 50},
            {"name": "Marketing", "importance": 2, "scores": [95] * 50},
            {"name": "Finance", "importance": 3, "scores": [95] * 50},
            {"name": "HR", "importance": 4, "scores": [95] * 50},
            {"name": "Science", "importance": 5, "scores": [95] * 50}
        ]
        score = calculate_aggregated_threat_score(departments)
        self.assertEqual(score, 95)

    def test_mixed_threat_and_importance(self):
        departments = [
            {"name": "Engineering", "importance": 1, "scores": generate_random_data(20, 10, 50)},
            {"name": "Marketing", "importance": 2, "scores": generate_random_data(30, 10, 50)},
            {"name": "Finance", "importance": 3, "scores": generate_random_data(40, 10, 50)},
            {"name": "HR", "importance": 4, "scores": generate_random_data(50, 10, 50)},
            {"name": "Science", "importance": 5, "scores": generate_random_data(60, 10, 50)}
        ]
        score = calculate_aggregated_threat_score(departments)
        self.assertTrue(40 <= score <= 60)


if __name__ == '__main__':
    unittest.main()
