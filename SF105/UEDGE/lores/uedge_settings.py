from uedge import *
import os
import numpy as np

bbb.GridFileName = "../../gridfiles/gridue_SF105_R0_10000_lores"
bbb.mhdgeo = 1
com.geometry[0] = "snowflake105    "
com.isudsym = 0
bbb.gengrid = 0
bbb.newgeo = 1
com.nxpt = 2
com.isnonog = 1

aph.aphdir = "../../../atomic_data"

bbb.methn = 33  # ion continuty eqn
bbb.methu = 33  # ion parallel momentum eqn
bbb.methe = 33  # electron energy eqn
bbb.methi = 33  # ion energy eqn
bbb.methg = 66  # neutral gas continuity eqn
bbb.allocate()  # allocates storage for arrays

bbb.isnicore[0] = 1  # =3 gives uniform density and I=curcore
bbb.ncore[0] = 2.0e19  # hydrogen ion density on core
bbb.isybdryog = 1  # =1 uses orthog diff at iy=0 and iy=ny bndry
bbb.iflcore = 1  # flag; =0, fixed Te,i; =1, fixed power on core
# bbb.tcoree = tcore  # core Te if iflcore=0
# bbb.tcorei = tcore  # core Ti if iflcore=0
bbb.pcoree = 10000 * 0.5e6  # core elec power if iflcore=1
bbb.pcorei = 10000 * 0.5e6  # core ion  power if iflcore=1
bbb.isnwcono = 3  # =3 for (1/n)dn/dy = 1/lyni
bbb.nwomin[0] = 1.0e13  # 1.e14 # 1.e12 #
bbb.nwimin[0] = 1.0e13  # 1.e14 # 1.e12 #
bbb.isnwconi = 3  # switch for private-flux wall
bbb.lyni[1] = 0.02  # iy=ny+1 density radial scale length (m)
bbb.lyni[0] = 0.02  # iy=0 density radial scale length
bbb.istepfc = 3  # =3 for (1/Te)dTe/dy=1/lyte on pf wall
bbb.istipfc = 3  # =3 ditto for Ti on pf wall
bbb.istewc = 3  # =3 ditto for Te on vessel wall
bbb.istiwc = 3  # =3 ditto for Ti on vessel wall
bbb.lyte = 0.04  # 0.02	# scale length for Te bc
bbb.lyti = 0.04  # 0.02	# scale length for Ti bc
bbb.tedge = 2.0  # fixed wall,pf Te,i if istewc=1, etc.
bbb.isupcore = 1  # =1 sets d(up)/dy=0
bbb.isupwo = 2  # =2 sets d(up)/dy=0
bbb.isupwi = 2  # =2 sets d(up)/dy=0
bbb.isplflxl = 0  # 1		#=0 for no flux limit (te & ti) at plate
bbb.isngcore[0] = 0  # set neutral density gradient at core bndry
bbb.matwso[0] = 1  # =1 --> make the outer wall recycling.
bbb.matwsi[0] = 1  # =1 --> make the inner wall recycling.
bbb.recycp = 1
bbb.recycw = 1
bbb.recycw[0] = 0.98  # recycling coeff. at wall
bbb.recycp[0] = 0.98  # hydrogen recycling coeff. at plates
bbb.recycm = -0.7  # mom BC at plates:up(,,2) = -recycm*up(,,1)

bbb.flalfe = 1.0  # electron parallel thermal conduct. coeff
bbb.flalfi = 1.0  # ion parallel thermal conduct. coeff
bbb.flalfv = 0.5  # ion parallel viscosity coeff
bbb.flalfgx = 1.0  # neut. gas in poloidal direction
bbb.flalfgy = 1.0  # neut. gas in radial direction
bbb.flalfgxy = 1.0
bbb.lgmax = 2e-1  # maximum scale-length for gas diffusion
bbb.lgtmax = 2e-1  # maximum scale-length for temperature
bbb.lgvmax = 2e-1  # maximum scale-length for viscosity
bbb.flalftgx = 1.0  # limit x thermal transport
bbb.flalftgy = 1.0  # limit y thermal transport
bbb.flalfvgx = 1.0  # limit x neut visc transport
bbb.flalfvgy = 1.0  # limit y neut visc transport
bbb.flalfvgxy = 1.0  # limit x-y nonorthog neut visc transport
bbb.isplflxlv = 1  # =0, flalfv not active at ix=0 & nx;=1 active all ix
bbb.isplflxlgx = 1  # =0, flalfgx not active at ix=0 & nx;=1 active all ix
bbb.isplflxlgxy = 1  # =0, flalfgxy not active at ix=0 & nx;=1 active all ixv
bbb.isplflxlvgx = 1  # =0, flalfvgx not active at ix=0 & nx;=1 active all ix
bbb.isplflxlvgxy = 1  # =0, flalfvgxy not active at ix=0 & nx;=1 active all ix
bbb.iswflxlvgy = 1  # =0, flalfvgy not active at iy=0 & ny;=1 active all iy
bbb.isplflxltgx = 1  # =0, flalfvgx not active at ix=0 & nx;=1 active all ix
bbb.isplflxltgxy = 1  # =0, flalfvgxy not active at ix=0 & nx;=1 active all ix
bbb.iswflxltgy = 1  # =0, flalfvgy not active at iy=0 & ny;=1 active all iy
bbb.islnlamcon = 1  # =1,  The Coulomb logarithm is set to a constant value
bbb.lnlam = 12  # Constant value used for the Coulomb logarythm
bbb.kxe = 1.0  # elec thermal conduc scale factor;now default
bbb.lmfplim = 1.0e3  # elec thermal conduc reduc 1/(1+mfp/lmfplim)

bbb.svrpkg = "nksol"  # Newton solver using Krylov method
bbb.premeth = "ilut"  # "banded"	#Solution method for precond. Jacobian matrix

com.istabon = 10  # 10=>Stotler tables
bbb.isrecmon = 1  # =1 for recombination
com.ngsp = 1
bbb.ineudif = 2  # pressure driven neutral diffusion
bbb.ngbackg = 1.0e13  # 1.e15 # 1.e12 #          # background gas level (1/m**3)
bbb.isupgon[0] = 1
bbb.isngon[0] = 0
com.nhsp = 2
bbb.ziin[com.nhsp - 1] = 0
bbb.gcfacgx = 1.0  # sets plate convective gas flux
bbb.gcfacgy = 1.0  # sets wall convective gas flux

bbb.restart = 1
bbb.isbcwdt = 1
bbb.allocate()
bbb.tes = 10 * bbb.ev
bbb.tis = 10 * bbb.ev
bbb.nis[:, :, 0] = 1e20
bbb.nis[:, :, 1:] = 1e16
bbb.ngs = 1e16
bbb.ups = 0
bbb.isbcwdt = 1

bbb.b0 = 1
bbb.isphion = 1
bbb.isnewpot = 1
bbb.newbcl = 1
bbb.newbcr = 1
bbb.iphibcc = 2
bbb.rsigpl = 1e-8

bbb.restart = 1
bbb.isbcwdt = 1
bbb.dtreal = 1e-12
bbb.icntnunk = 0
bbb.itermx = 30
bbb.issfon = 0
bbb.ftol = 1e20
bbb.exmain()
bbb.itermx = 7
bbb.issfon = 1
bbb.ftol = 1e-6

bbb.difni = 1
bbb.kye = 5
bbb.kyi = 5
