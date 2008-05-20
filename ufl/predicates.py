"""Functions to check properties of forms and integrals."""

__authors__ = "Martin Sandve Alnes"
__date__ = "2008-03-14 -- 2008-05-20"

from output import *
from all import *
from traversal import *
from analysis import *


#--- Utilities for checking properties of forms ---

def is_multilinear(a):
    """Checks if a form is multilinear. Returns True/False."""
    ufl_assert(isinstance(o, Form), "Assuming a Form.")
    ufl_warning("is_multilinear is not implemented.")
    return True

