from numpy import pi as _pi


def cylinder(target, throat_diameter='throat.diameter'):
    r"""
    Calculate throat cross-sectional area for a cylindrical throat

    Parameters
    ----------
    geometry : OpenPNM Geometry Object
        The Geometry object which this model is associated with. This controls
        the length of the calculated array, and also provides access to other
        necessary geometric properties.

    throat_diameter : string
        Dictionary key of the throat diameter values

    """
    diams = target[throat_diameter]
    value = _pi/4*(diams)**2
    return value


def cuboid(target, throat_diameter='throat.diameter'):
    r"""
    Calculate throat cross-sectional area for a cuboid throat

    Parameters
    ----------
    geometry : OpenPNM Geometry Object
        The Geometry object which this model is associated with. This controls
        the length of the calculated array, and also provides access to other
        necessary geometric properties.

    throat_diameter : string
        Dictionary key of the throat diameter values

    """
    diams = target[throat_diameter]
    value = (diams)**2
    return value