#!/usr/bin/python3

import cerridwen

import time

def emit_time_info(result):
    print('Julian day:', result['jd'])
    print('Universal time (UTC):', result['iso_date'])
    print('Local time:', time.asctime())

def emit_sun_text(result):
    sign, deg, min, sec = result['position'].rel_tuple
    print('Sun: %f / %d %s %d\' %d"' % (result['position'].absolute_degrees[0],
        deg, sign, min, sec))

def emit_moon_text(result, simple=False):
    if simple:
        sign, deg, min, sec = result['position'].rel_tuple
        print('Moon: %f / %d %s %d\' %d"' % (result['position'].absolute_degrees[0],
                                             deg, sign, min, sec))
    else:
        sign, deg, min, sec = result['position'].rel_tuple
        print('Moon: %f / %d %s %d\' %d"' % (result['position'].absolute_degrees[0],
            deg, sign, min, sec))


        trend, shape, quarter, quarter_english = result['phase']
        phase = trend + ' ' + shape
        print("phase: %s, quarter: %s, illum: %d%%" %
                (phase, quarter_english, result['illumination'] * 100))

        next_new_moon = result['next_new_moon']
        print("next new moon: %s: in %s (%s / %f)" %
                (next_new_moon.description,
                 cerridwen.utils.render_delta_days(next_new_moon.delta_days),
                 cerridwen.jd2iso(next_new_moon.jd), next_new_moon.jd))

        next_full_moon = result['next_full_moon']
        print("next full moon: %s: in %s (%s / %f)" %
                (next_full_moon.description,
                 cerridwen.utils.render_delta_days(next_full_moon.delta_days),
                 cerridwen.jd2iso(next_full_moon.jd), next_full_moon.jd))

def emit_mercury_text(result):
    sign, deg, min, sec = result['position'].rel_tuple
    print('Mercury: %f / %d %s %d\' %d"' % (result['position'].absolute_degrees[0],
        deg, sign, min, sec))

def emit_venus_text(result):
    sign, deg, min, sec = result['position'].rel_tuple
    print('Venus: %f / %d %s %d\' %d"' % (result['position'].absolute_degrees[0],
        deg, sign, min, sec))

def emit_mars_text(result):
    sign, deg, min, sec = result['position'].rel_tuple
    print('Mars: %f / %d %s %d\' %d"' % (result['position'].absolute_degrees[0],
        deg, sign, min, sec))

def emit_jupiter_text(result):
    sign, deg, min, sec = result['position'].rel_tuple
    print('Jupiter: %f / %d %s %d\' %d"' % (result['position'].absolute_degrees[0],
        deg, sign, min, sec))

def emit_saturn_text(result):
    sign, deg, min, sec = result['position'].rel_tuple
    print('Saturn: %f / %d %s %d\' %d"' % (result['position'].absolute_degrees[0],
        deg, sign, min, sec))

def emit_uranus_text(result):
    sign, deg, min, sec = result['position'].rel_tuple
    print('Uranus: %f / %d %s %d\' %d"' % (result['position'].absolute_degrees[0],
        deg, sign, min, sec))

def emit_neptune_text(result):
    sign, deg, min, sec = result['position'].rel_tuple
    print('Neptune: %f / %d %s %d\' %d"' % (result['position'].absolute_degrees[0],
        deg, sign, min, sec))

def emit_pluto_text(result):
    sign, deg, min, sec = result['position'].rel_tuple
    print('Pluto: %f / %d %s %d\' %d"' % (result['position'].absolute_degrees[0],
        deg, sign, min, sec))



def main():
    import argparse
    parser = argparse.ArgumentParser(prog='Cerridwen')
    parser.add_argument('--version', action='version', version='%(prog)s ' + cerridwen.__VERSION__)
    args = parser.parse_args()

    #cerridwen.quicktest()

    sun_data = cerridwen.compute_sun_data()
    emit_time_info(sun_data)
    emit_sun_text(sun_data)

    emit_moon_text(cerridwen.compute_moon_data(), True)
    emit_mercury_text(cerridwen.compute_mercury_data())
    emit_venus_text(cerridwen.compute_venus_data())
    emit_mars_text(cerridwen.compute_mars_data())
    emit_jupiter_text(cerridwen.compute_jupiter_data())
    emit_saturn_text(cerridwen.compute_saturn_data())
    emit_uranus_text(cerridwen.compute_uranus_data())
    emit_neptune_text(cerridwen.compute_neptune_data())
    emit_pluto_text(cerridwen.compute_pluto_data())




if __name__ == '__main__':
    main()

