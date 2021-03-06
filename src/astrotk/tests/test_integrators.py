import numpy as np
from astrotk.simulator.eom.test import point_mass_acceleration_3D

from astrotk.bodies.bodies import Earth
from astrotk.twobody.utils.transformation import classical2vector

# NUMERICAL EXAMPLE EULER TABLE
ex_a = 7378.137  # km
ex_e = 0.1  # -
ex_i = 0.  # rad
ex_raan = 0.  # rad
ex_argp = 0.  # rad
ex_thet = 0.  # rad
ex_step_siz = 10.  # s

ex_r, ex_v = classical2vector(a=ex_a,
                              e=ex_e,
                              inc=ex_i,
                              raan=ex_raan,
                              argp=ex_argp,
                              theta=ex_thet,
                              mu=Earth.mu.si.value)

ex_t = np.array([0, 10., 20.])

ex_arg = {
    "t": ex_t,
    "eom": point_mass_acceleration_3D,
    "y0": np.concatenate((ex_r, ex_v)),
    "args": Earth.mu.si.value
}
