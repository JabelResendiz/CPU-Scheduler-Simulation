import numpy as np
import scipy.stats as stats

def confidence_interval(data, confidence=0.95):
    """Calcula intervalo de confianza."""
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)
    margin = std_err * stats.t.ppf((1 + confidence) / 2, n - 1)
    return (mean, margin)

def compare_algorithms(algorithm_A, algorithm_B, metric="waiting_times"):
    """Test t para comparar dos algoritmos."""
    t_stat, p_value = stats.ttest_ind(algorithm_A[metric], algorithm_B[metric])
    return {
        "p_value": p_value,
        "significant": p_value < 0.05
    }