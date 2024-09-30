import time
from linearmodels import IV2SLS
from linearmodels.datasets import meps
from statsmodels.api import OLS, add_constant
from collections import OrderedDict
from linearmodels.iv.results import compare

# This script runs examples of IV regression methods
# https://bashtage.github.io/linearmodels/iv/examples/advanced-examples.html#2SLS-as-OLS

def run_iv_regression():
    # Record the start and end times
    start = time.time()

    # Import data and define variables
    data = meps.load()
    data = data.dropna()
    controls = ["totchr", "female", "age", "linc", "blhisp"]
    instruments = ["ssiratio", "lowincome", "multlc", "firmsz"]
    data["const"] = 1
    controls = ["const"] + controls

    # Run Models
    ivolsmod = IV2SLS(data.ldrugexp, data[["hi_empunion"] + controls], None, None)
    res_ols = ivolsmod.fit()
    ivmod = IV2SLS(data.ldrugexp, data[controls], data.hi_empunion, data.ssiratio)
    res_2sls = ivmod.fit()
    ivmod = IV2SLS(
        data.ldrugexp, data[controls], data.hi_empunion, data[["ssiratio", "multlc"]]
    )
    res_2sls_robust = ivmod.fit()
    ivmod = IV2SLS(
        data.ldrugexp, data[controls], data.hi_empunion, data[["ssiratio", "multlc"]]
    )
    res_2sls_std = ivmod.fit(cov_type="unadjusted")
    ivmod = IVGMM(
        data.ldrugexp, data[controls], data.hi_empunion, data[["ssiratio", "multlc"]]
    )
    res_gmm = ivmod.fit()
    ivmod = IVGMM(
        data.ldrugexp,
        data[controls],
        data.hi_empunion,
        data[["ssiratio", "multlc"]],
        weight_type="clustered",
        clusters=data.age,
    )
    res_gmm_clustered = ivmod.fit(cov_type="clustered", clusters=data.age)
    ivmod = IVGMMCUE(
        data.ldrugexp, data[controls], data.hi_empunion, data[["ssiratio", "multlc"]]
    )
    res_gmm_cue = ivmod.fit(cov_type="robust", display=True)

    # Print results
    res = OrderedDict()
    res["OLS"] = res_ols
    res["2SLS"] = res_2sls
    res["2SLS-Homo"] = res_2sls_std
    res["2SLS-Hetero"] = res_2sls_robust
    res["GMM"] = res_gmm
    res["GMM Cluster(Age)"] = res_gmm_clustered
    res["GMM-CUE"] = res_gmm_cue
    print(compare(res))

    # End time
    end = time.time()
    print("Elapsed time", end-start)

if __name__ == "__main__":
    run_iv_regression()
