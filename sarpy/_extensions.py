__classification__ = "UNCLASSIFIED"



def entry_points( **_3to2kwargs):
    group = _3to2kwargs['group']; del _3to2kwargs['group']
    """
    Simple wrapper around entry_points.

    Parameters
    ----------
    group : str
        entry point group name

    Returns
    -------
    list of entry points belonging to group
    """
    try:
        # Python >= 3.8 (but API changed in 3.10)
        import importlib.metadata as metadata
    except ImportError:
        # Python 2.7 / 3.7 and lower: use the backport
        import importlib_metadata as metadata

    eps = metadata.entry_points()
    if hasattr(eps, 'select'):
        # Python >= 3.10
        return eps.select(group=group)
    else:
        # Python < 3.10 (including backport)
        return eps.get(group, [])