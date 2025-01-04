import numpy as np
from scipy import stats

def perform_t_test(data, hypothesized_mean=0):
    """
    Perform a one-sample t-test comparing the mean of the data to a hypothesized mean.

    Parameters:
    - data (array-like): The input data array to test.
    - hypothesized_mean (float): The mean value to test against (default is 0).

    Returns:
    - t_statistic (float): The t-statistic of the test.
    - p_value (float): The p-value of the test.
    """
    #convert data to a NumPy array if it's not already
    data = np.array(data)
    
    #perform one-sample t-test
    t_statistic, p_value = stats.ttest_1samp(data, hypothesized_mean)
    
    return t_statistic, p_value

# abs value compound diff actual data
actual_data_1 = [0.12417, 0.23119, 0.12092, 0.25425, 0.23462,
        0.04657, 0.21027, 0.36272, 0.33218, 0.3712,
        0.36283, 0.28704, 0.43296, 0.37971, 0.34839,
        0.13452, 0.33761]

t_statistic, p_value = perform_t_test(actual_data_1)
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

actual_data_2 = np.array([0.39807, 0.15761, 0.10559, 0.42284, 0.53252,
                 0.26204, 0.09286, 0.09966, 0.36227, 0.27507,
                 0.39212, 0.31116, 0.33692, 0.24324, 0.40884,
                 0.31838, 0.01744])

t_statistic, p_value = perform_t_test(actual_data_2)
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

actual_data_3 = np.array([0.38484, 0.01911, 0.27329, 0.28822, 0.21898,
                 0.16151, 0.15122, 0.17801, 0.17386, 0.08506,
                 0.09505, 0.39714, 0.15756, 0.42274, 0.18006,
                 0.02649, 0.3182])

t_statistic, p_value = perform_t_test(actual_data_3)
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

syn_data_100 = data = np.array([0.087938, 0.109355, 0.119796, 0.192939, 0.046457,
                 0.206842, 0.13673, 0.166114, 0.009628, 0.02092])

t_statistic, p_value = perform_t_test(syn_data_100)
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

syn_data_500 = np.array([0.0489726, 0.2562742, 0.189489, 0.1281408, 0.020385,
                 0.0629078, 0.1111562, 0.186542, 0.0507506, 0.0620388])

t_statistic, p_value = perform_t_test(syn_data_500)
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

syn_data_1000 = np.array([0.3879242, 0.2031151, 0.3031563, 0.0298703, 0.0403368,
                 0.0746585, 0.003475, 0.0113922, 0.007013, 0.0968953])

t_statistic, p_value = perform_t_test(syn_data_1000)
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
