import pandas as pd
import numpy as np
import scipy.stats as stats


def analyze_returns(net_returns):
    """
    Perform a t-test, with the null hypothesis being that the mean return is zero.

    Parameters
    ----------
    net_returns : Pandas Series
        A Pandas Series for each date

    Returns
    -------
    t_value
        t-statistic from t-test
    p_value
        Corresponding p-value
    """
    # TODO: Perform one-tailed t-test on net_returns
    # Hint: You can use stats.ttest_1samp() to perform the test.
    #       However, this performs a two-tailed t-test.
    #       You'll need to divde the p-value by 2 to get the results of a one-tailed p-value.
    null_hypothesis = 0.0
    # t_value = (sm - m) / np.sqrt(sv / float(n))  # t-statistic for mean
    # p_value = stats.t.sf(np.abs(tt), n - 1) * 2  # two-sided pvalue = Prob(abs(t)>tt)
    t_value, p_value = stats.ttest_1samp(net_returns, null_hypothesis)
    # convert 2-tailed p-value to 1-tailed
    p_value /= 2.
    return t_value, p_value


def test_run(filename=r'C:\Users\Vicky Huang\Documents\Udacity\ai-for-trading\term1_quantitative_trading\exercises\lesson8_momentum_trading\quiz11_test_returns_for_statistical_significance\net_returns.csv'):
    """Test run analyze_returns() with net strategy returns from a file."""
    net_returns = pd.read_csv(filename, index_col=0, header=0, parse_dates=True)['return']
    t, p = analyze_returns(net_returns)
    print("t-statistic: {:.3f}\np-value: {:.6f}".format(t, p))


if __name__ == '__main__':
    test_run()