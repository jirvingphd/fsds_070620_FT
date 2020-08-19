## Look for outliers
from scipy import stats
def find_outliers_z(data):
    zFP = np.abs(stats.zscore(data))
    
    zFP = pd.Series(zFP, index=data.index)
    idx_outliers = zFP > 3
    return idx_outliers