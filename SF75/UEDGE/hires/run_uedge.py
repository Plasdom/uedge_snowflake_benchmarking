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
from uedge_dcp.gridue_manip import interpolate_save, UESave
import time
import numpy as np

"""============  Apply settings  ==============="""
us.set_geometry(
    gridfile="../../gridfiles/gridue_SF75_R0_10000_hires",
    geometry="snowflake75     ",
    isudsym=0,
    nxpt=2,
)
us.set_apdirs()
us.set_fd_algos()
us.set_bcs(
    iflcore=1,
    tcore=50,
    pcore=10000 * 0.5e6,
    lyni=0.02,
    lyt=0.04,
    ncore=2.0e19,
    recycw=0.98,
    recycp=0.98,
)
us.set_flux_limits()
us.set_solver()
us.set_h_gas(fluid_neuts=True)
us.set_div_gas_puff_h()
us.set_initial_conditions()
bbb.b0 = -1
bbb.isphion = 1
bbb.isnewpot = 1
bbb.newbcl = 1
bbb.newbcr = 1
bbb.iphibcc = 2
bbb.rsigpl = 1e-8
us.initial_short_run(update_jac=False)
bbb.difni = 1
bbb.kye = 5
bbb.kyi = 5
"""============  ================  ==============="""

hdf5_restore("restart.hdf5")
bbb.exmain()
