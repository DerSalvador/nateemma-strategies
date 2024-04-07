#pragma pylint: disable=W0105, C0103, C0301, W1203


"""
####################################################################################
TS_Coeff_WPT - use a Wavelet Packet Transform model

####################################################################################
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
sys.path.append(str(Path(__file__)))

import utils.Wavelets as Wavelets
from TS_Coeff import TS_Coeff

class TS_Coeff_WPT(TS_Coeff):

    wavelet_type = Wavelets.WaveletType.WPT

