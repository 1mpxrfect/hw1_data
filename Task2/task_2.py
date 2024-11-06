import numpy as np
from typing import List, Dict


def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def calculate_aggregated_threat_score(departments: List[Dict[str, any]]) -> float:
    weighted_scores = [np.mean(dept['scores']) * dept['importance'] for dept in departments]
    total_importance = sum(dept['importance'] for dept in departments)
    aggregated_score = sum(weighted_scores) / total_importance if total_importance else 0
    return min(max(aggregated_score, 0), 90)
