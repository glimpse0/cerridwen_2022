#!/usr/bin/python3

import time, calendar, astropy.time
import collections
import sys

from .defs import dbfile
from .utils import jd_now, jd2iso, parse_jd_or_iso_date
from .planets import Moon, Sun, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto
from .planets import PlanetEvent, PlanetLongitude, Ascendant, MoonPhaseData
from .approximate import approximate_event_date
from .version import __VERSION__

# TODO use astropy.coordinates.EarthLocation instead, if it's available (v0.4)
class LatLong():
    def __init__(self, lat, long):
        if lat > 90 or lat < -90:
            raise ValueError("Latitude must be between -90 and 90")
        if long > 180 or long < -180:
            raise ValueError("Longitude must be between -180 and 180")
        self.lat = lat
        self.long = long

def compute_sun_data(jd=None, observer=None):
    """Collect data for the sun.

     :param jd: reference date as Julian day, defaults to :func:`jd_now`
     :type jd: float or None
     :param observer: pass the observer position to have the output
                      include rise and set times.
     :type observer: LatLong or None
     :returns: a collection of sun data
     :rtype: OrderedDict
     """
    if jd is None: jd = jd_now()

    result = collections.OrderedDict()

    result['jd'] = jd
    result['iso_date'] = jd2iso(jd)

    sun = Sun(jd, observer)

    result['position'] = sun.position()

    result['dignity'] = sun.dignity()

    if observer:
        result['next_rise'] = sun.next_rise()
        result['next_set'] = sun.next_set()
        result['last_rise'] = sun.last_rise()
        result['last_set'] = sun.last_set()

    return result

def compute_moon_data(jd=None, observer=None):
    """Collect data for the moon.

     :param jd: reference date as Julian day, defaults to :func:`jd_now`
     :type jd: float or None
     :param observer: pass the observer position to have the output
                      include rise and set times.
     :type observer: LatLong or None
     :returns: a collection of sun data
     :rtype: OrderedDict
     """
    if jd is None: jd = jd_now()

    result = collections.OrderedDict()

    result['jd'] = jd
    result['iso_date'] = jd2iso(jd)

    moon = Moon(jd, observer)

    result['position'] = moon.position()

    result['phase'] = moon.phase()
    result['illumination'] = moon.illumination()
    result['distance'] = moon.distance()
    result['diameter'] = moon.diameter()
    result['diameter_ratio'] = moon.diameter_ratio()
    result['speed'] = moon.speed()
    result['speed_ratio'] = moon.speed_ratio()
    result['age'] = moon.age()
    result['period_length'] = moon.period_length()
    result['dignity'] = moon.dignity()

    result['next_new_moon'] = moon.next_new_moon()
    result['next_full_moon'] = moon.next_full_moon()
    # result['next_new_or_full_moon'] = moon.next_new_or_full_moon()
    # result['last_new_moon'] = moon.last_new_moon()
    # result['last_full_moon'] = moon.last_full_moon()

    if observer:
        result['next_rise'] = moon.next_rise()
        result['next_set'] = moon.next_set()
        result['last_rise'] = moon.last_rise()
        result['last_set'] = moon.last_set()

    return result

def compute_mercury_data(jd=None, observer=None):

    """Collect data for mercury.

     :param jd: reference date as Julian day, defaults to :func:`jd_now`
     :type jd: float or None
     :param observer: pass the observer position to have the output
                      include rise and set times.
     :type observer: LatLong or None
     :returns: a collection of sun data
     :rtype: OrderedDict
     """
    if jd is None: jd = jd_now()

    result = collections.OrderedDict()

    result['jd'] = jd
    result['iso_date'] = jd2iso(jd)

    mercury = Mercury(jd, observer)

    result['position'] = mercury.position()

    result['dignity'] = mercury.dignity()

    if observer:
        result['next_rise'] = mercury.next_rise()
        result['next_set'] = mercury.next_set()
        result['last_rise'] = mercury.last_rise()
        result['last_set'] = mercury.last_set()

    return result

def compute_venus_data(jd=None, observer=None):

    """Collect data for mercury.

     :param jd: reference date as Julian day, defaults to :func:`jd_now`
     :type jd: float or None
     :param observer: pass the observer position to have the output
                      include rise and set times.
     :type observer: LatLong or None
     :returns: a collection of sun data
     :rtype: OrderedDict
     """
    if jd is None: jd = jd_now()

    result = collections.OrderedDict()

    result['jd'] = jd
    result['iso_date'] = jd2iso(jd)

    venus = Venus(jd, observer)

    result['position'] = venus.position()

    result['dignity'] = venus.dignity()

    if observer:
        result['next_rise'] = venus.next_rise()
        result['next_set'] = venus.next_set()
        result['last_rise'] = venus.last_rise()
        result['last_set'] = venus.last_set()

    return result

def compute_mars_data(jd=None, observer=None):

    """Collect data for mercury.

     :param jd: reference date as Julian day, defaults to :func:`jd_now`
     :type jd: float or None
     :param observer: pass the observer position to have the output
                      include rise and set times.
     :type observer: LatLong or None
     :returns: a collection of sun data
     :rtype: OrderedDict
     """
    if jd is None: jd = jd_now()

    result = collections.OrderedDict()

    result['jd'] = jd
    result['iso_date'] = jd2iso(jd)

    mars = Mars(jd, observer)

    result['position'] = mars.position()

    result['dignity'] = mars.dignity()

    if observer:
        result['next_rise'] = mars.next_rise()
        result['next_set'] = mars.next_set()
        result['last_rise'] = mars.last_rise()
        result['last_set'] = mars.last_set()

    return result

def compute_jupiter_data(jd=None, observer=None):

    """Collect data for mercury.

     :param jd: reference date as Julian day, defaults to :func:`jd_now`
     :type jd: float or None
     :param observer: pass the observer position to have the output
                      include rise and set times.
     :type observer: LatLong or None
     :returns: a collection of sun data
     :rtype: OrderedDict
     """
    if jd is None: jd = jd_now()

    result = collections.OrderedDict()

    result['jd'] = jd
    result['iso_date'] = jd2iso(jd)

    jupiter = Jupiter(jd, observer)

    result['position'] = jupiter.position()

    result['dignity'] = jupiter.dignity()

    if observer:
        result['next_rise'] = jupiter.next_rise()
        result['next_set'] = jupiter.next_set()
        result['last_rise'] = jupiter.last_rise()
        result['last_set'] = jupiter.last_set()

    return result

def compute_saturn_data(jd=None, observer=None):

    """Collect data for mercury.

     :param jd: reference date as Julian day, defaults to :func:`jd_now`
     :type jd: float or None
     :param observer: pass the observer position to have the output
                      include rise and set times.
     :type observer: LatLong or None
     :returns: a collection of sun data
     :rtype: OrderedDict
     """
    if jd is None: jd = jd_now()

    result = collections.OrderedDict()

    result['jd'] = jd
    result['iso_date'] = jd2iso(jd)

    saturn = Saturn(jd, observer)

    result['position'] = saturn.position()

    result['dignity'] = saturn.dignity()

    if observer:
        result['next_rise'] = saturn.next_rise()
        result['next_set'] = saturn.next_set()
        result['last_rise'] = saturn.last_rise()
        result['last_set'] = saturn.last_set()

    return result

def compute_uranus_data(jd=None, observer=None):

    """Collect data for mercury.

     :param jd: reference date as Julian day, defaults to :func:`jd_now`
     :type jd: float or None
     :param observer: pass the observer position to have the output
                      include rise and set times.
     :type observer: LatLong or None
     :returns: a collection of sun data
     :rtype: OrderedDict
     """
    if jd is None: jd = jd_now()

    result = collections.OrderedDict()

    result['jd'] = jd
    result['iso_date'] = jd2iso(jd)

    uranus = Uranus(jd, observer)

    result['position'] = uranus.position()

    # result['dignity'] = uranus.dignity()

    if observer:
        result['next_rise'] = uranus.next_rise()
        result['next_set'] = uranus.next_set()
        result['last_rise'] = uranus.last_rise()
        result['last_set'] = uranus.last_set()

    return result

def compute_neptune_data(jd=None, observer=None):

    """Collect data for mercury.

     :param jd: reference date as Julian day, defaults to :func:`jd_now`
     :type jd: float or None
     :param observer: pass the observer position to have the output
                      include rise and set times.
     :type observer: LatLong or None
     :returns: a collection of sun data
     :rtype: OrderedDict
     """
    if jd is None: jd = jd_now()

    result = collections.OrderedDict()

    result['jd'] = jd
    result['iso_date'] = jd2iso(jd)

    neptune = Neptune(jd, observer)

    result['position'] = neptune.position()

    # result['dignity'] = uranus.dignity()

    if observer:
        result['next_rise'] = neptune.next_rise()
        result['next_set'] = neptune.next_set()
        result['last_rise'] = neptune.last_rise()
        result['last_set'] = neptune.last_set()

    return result

def compute_pluto_data(jd=None, observer=None):

    """Collect data for mercury.

     :param jd: reference date as Julian day, defaults to :func:`jd_now`
     :type jd: float or None
     :param observer: pass the observer position to have the output
                      include rise and set times.
     :type observer: LatLong or None
     :returns: a collection of sun data
     :rtype: OrderedDict
     """
    if jd is None: jd = jd_now()

    result = collections.OrderedDict()

    result['jd'] = jd
    result['iso_date'] = jd2iso(jd)

    pluto = Pluto(jd, observer)

    result['position'] = pluto.position()

    # result['dignity'] = uranus.dignity()

    if observer:
        result['next_rise'] = pluto.next_rise()
        result['next_set'] = pluto.next_set()
        result['last_rise'] = pluto.last_rise()
        result['last_set'] = pluto.last_set()

    return result



def get_events(jd_start, jd_end, limit=100, filter_fn=None):
    # TODO we only support AND of filters, not OR
    import sqlite3

    conn = sqlite3.connect(dbfile)
    conn.row_factory = sqlite3.Row
    if filter_fn is None:
        def filter_fn(type, subtype, planet, data):
            return True
    conn.create_function("filter_event", 4, filter_fn)

    c = conn.cursor()

    sql = """SELECT * FROM events
             WHERE jd BETWEEN ? AND ?
               AND filter_event(type, subtype, planet, data) = 1
             ORDER BY jd ASC
             LIMIT ?"""
    rows = c.execute(sql, (jd_start, jd_end, limit))

    result = []
    for row in rows:
        dict = collections.OrderedDict()
        for key in ['jd', 'type', 'subtype', 'planet', 'data']:
                dict[key] = row[key]
        dict['iso_date'] = jd2iso(row['jd'])
        dict['delta_days'] = row['jd'] - jd_start
        result.append(dict)

    return result

def print_moon_events():
    import sqlite3
    conn = sqlite3.connect('moon-events.db')

def quicktest():
    return # re-enable later when we have a quick sanity test suite.
    print('Cerridwen: running basic sanity tests.')
    import nose
    nose.run()

def main():
    quicktest()

    print('Now:', jd_now())

    print('AC (Berlin): ', Ascendant(13.3, 52.5).position())

    moon = Moon(observer=LatLong(52.5, 13.3))
    # TODO: rise/set tests
    print('moon pos:', moon.position())
    print('next rise:', moon.next_rise())
    print('next set:', moon.next_set())
    print('last rise:', moon.last_rise())
    print('last set:', moon.last_set())
    print(moon.next_new_moon().jd)
    print(moon.last_new_moon())
    print(moon.period_length())

    if debug_event_approximation:
        for i in range(1,100):
            moon = Moon()
            jd = jd_now()+i*30
            new = moon.next_new_moon(jd)
            full = moon.next_full_moon(jd)
            print(jd2iso(new[0]), new[2])
            print(jd2iso(full[0]), full[2])
        sys.exit(1)

# v1.1.0
# use new/full moon tables
# lunation_number
 
# LATER
# latitude: when within band of the sun (David)
# folk_names moon_in_year
# tidal acceleration

# for diameter ratio see the numbers here:
# http://en.wikipedia.org/wiki/Angular_diameter#Use_in_astronomy

# some more ideas:
# * monthly calendar (as widget and for printing)
# * upcoming event stream:
#    https://play.google.com/store/apps/details?id=uk.co.lunarium.iluna
#    http://www.lunarliving.org/

# http://starchild.gsfc.nasa.gov/docs/StarChild/questions/question5.html

# events to subscribe to:
# full, new, 1st quarter, 3rd quarter, sign change, void of course, aspect (one of subset X) to planet (one of subset Y)

# LATER:
# use astropy.time.Time everywhere
# use astropy.coordinates.EarthLocation (astropy 0.4)
#
# merge compute_*_data functions into one
#
# lunar standstills
# moon out of sun's declination band
