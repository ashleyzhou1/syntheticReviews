import numpy as np
from scipy import stats

def perform_t_test(data, hypothesized_mean=0):
    #convert data to a NumPy array if it's not already
    data = np.array(data)
    
    #perform one-sample t-test
    t_statistic, p_value = stats.ttest_1samp(data, hypothesized_mean)
    
    return t_statistic, p_value
