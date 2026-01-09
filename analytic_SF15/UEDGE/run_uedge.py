from hmac import new
from uedge import *
from uedge.hdf5 import *
import uedge_mvu.plot as mp
import uedge_mvu.utils as mu
import uedge_mvu.tstep as mt
from uedge.rundt import rundt, UeRun
import uedge_dcp.mastu_uedge_settings as us
import uedge_dcp.plotting as dp
import uedge_dcp.post_processing as pp
from uedge.uedge_lists import *
from uedge_dcp.gridue_manip import interpolate_save
import time
import numpy as np
import matplotlib.pyplot as plt

"""============  Apply settings  ==============="""
us.set_geometry(
    # gridfile="/Users/power8/Documents/04_mastu_modelling/2024_MASTU_shots/cases/analytic_SF15/gridfiles/gridue_full_high_R0_b",
    gridfile="/Users/power8/Documents/04_mastu_modelling/2024_MASTU_shots/works_in_progress/analytic_SFs/analytic_SF15/gridfiles/gridue_full_b_R0_10000_c",
    geometry="snowflake15     ",
    isudsym=0,
    nxpt=2,
)
us.set_apdirs("/Users/power8/Documents/01_code/01_uedge/uedge")
us.set_fd_algos()
us.set_bcs(
    iflcore=1,
    tcore=100,
    # pcore=10000 * 2 * 0.5e6,
    pcore=10000 * 0.5e6,
    lyni=0.04,
    lyt=0.05,
    ncore=2.3e19,
    recycw=1,
    recycp=1,
)
us.set_flux_limits()
us.set_solver()
us.set_h_gas(fluid_neuts=True)
# us.set_div_gas_puff_h()
us.set_initial_conditions()
# us.set_drifts_maxim(-1000.0)
# bbb.cfybf = 0.0
# bbb.cf2bf = 0.0
# bbb.cfqybf = 0.0
# bbb.cfq2bf = 0.0
bbb.b0 = -1
bbb.isphion = 1
bbb.isnewpot = 1
bbb.newbcl = 1
bbb.newbcr = 1
bbb.iphibcc = 2
bbb.rsigpl = 1e-8
us.initial_short_run(update_jac=False)
# us.set_transport_coeffs_DM(
#     inplace=True,
#     k_x=[-0.025, -0.02, -0.0025, 0.0004],
#     k_v=[10.0, 10.0, 10.0, 10.0],
#     d_x=[-0.025, -0.01, 0.0004, 0.01],
#     d_v=[2.0, 0.15, 0.15, 0.5],
#     reverse_r_mp=True,
#     dif_div=1.0,
#     ky_div=10.0,
# )
bbb.difni = 0.5
bbb.kye = 5
bbb.kyi = 5
"""============  ================  ==============="""

# hdf5_restore("start_iflcore_1_R0_10000.hdf5")
hdf5_restore("wip_R0_10000_phionly.hdf5")
bbb.exmain()
# rundt()
