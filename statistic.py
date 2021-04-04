import json
from scipy import stats
import numpy as np
from  scipy.stats import ttest_rel


baseline_spice=json.load(open('./data/baseline2_spice.json','r'))
DATR_spice=json.load(open('./data/baseline2_spice.json','r'))

for k in baseline_spice.keys():
    baseline_spice[k]=np.array(baseline_spice[k]).astype("float")
    DATR_spice[k]=np.array(DATR_spice[k]).astype("float")
    

    ttest=stats.ttest_rel(baseline_spice[k],DATR_spice[k])
    print(k,'baseline spice mean',np.array(baseline_spice[k]).mean())
    print(k,'our spice mean',np.array(DATR_spice[k]).mean())
    print(k,'ttest p_value--',ttest.pvalue)
