#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


# TODO: Définissez vos fonction ici
def vol_et_masse(x=1,y=2,z=3,masse_volumique=4):
    volume = 4/3 * x * y * z * math.pi
    masse = masse_volumique * volume
    return volume, masse

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(vol_et_masse())

    pass
