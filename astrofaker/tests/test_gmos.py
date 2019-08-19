#!/usr/bin/env python

import astropy.io.fits as fits
import numpy as np
import pytest

import astrodata
import astrofaker

from astrofaker import gmos


def test_can_create_dataset():

    ad = astrofaker.create('GMOS-S')

    assert isinstance(ad, astrodata.AstroData)
    assert isinstance(ad, astrodata.AstroDataFits)
    assert isinstance(ad, astrofaker.AstroFaker)
    assert isinstance(ad, gmos.AstroFakerGmos)
    assert len(ad) == 0


def test_can_add_image_extension():

    hdu = fits.ImageHDU()
    hdu.data = np.random.random((100, 100))

    ad = astrofaker.create('GMOS-S')

    # ToDo: The line below raises a TypeError if `pixel_scale` is not provided.
    # We need either to provide a better error message to the programmer or
    # set `pixel_scale` with a default value and raise a warning.
    ad.add_extension(hdu, pixel_scale=1.0)

    assert len(ad) == 1


def test_can_update_descriptor_dispersion_axis_of_astrodata():

    hdu = fits.ImageHDU()
    hdu.data = np.random.random((100, 100))

    ad = astrofaker.create('GMOS-S')
    ad.add_extension(hdu, pixel_scale=1.0)

    # ToDo: how are descriptor assignments handled?
    # I suspect they should be something like Python Properties. This would
    # allow some variable validation with a comprehensive error message.
    ad.dispersion_axis = [1]
    assert ad.dispersion_axis() == [1]


def test_can_update_descriptor_dispersion_axis_of_astrodata_extensions():

    hdu = fits.ImageHDU()
    hdu.data = np.random.random((100, 100))

    ad = astrofaker.create('GMOS-S')
    ad.add_extension(hdu, pixel_scale=1.0)
    ad.add_extension(hdu, pixel_scale=1.0)

    # ToDo: how are descriptor assignments handled?
    # I suspect they should be something like Python Properties. This would
    # allow some variable validation with a comprehensive error message.
    for ext in ad:
        ext.dispersion_axis = 1

    for ext in ad:
        assert ext.dispersion_axis == 1


if __name__ == '__main__':
    pytest.main()
