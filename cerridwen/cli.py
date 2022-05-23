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

def emit_csv(result, comma = True):
    sign, deg, min, sec = result['position'].rel_tuple
    out = ('%f,%s,%d\',%d"' % (result['position'].absolute_degrees[0],
      sign, min, sec))
    if comma: out+=",";
    return out

def emit_csv_moon(result, comma = True):
    sign, deg, min, sec = result['position'].rel_tuple
    # trend+shape = phase
    trend = result['phase'].trend
    shape = result['phase'].shape
    quarter = result['phase'].quarter_english
    diameter = result["diameter"]
    nextNewMoon = result["next_new_moon"]
    nextFullMoon = result["next_full_moon"]
    return('%f,%s,%d\',%d",%s,%s,%s,%f,%s,%s,'
           % (result['position'].absolute_degrees[0],
      sign, min, sec, trend, shape, quarter,diameter,nextNewMoon, nextFullMoon))

def main():
    import argparse
    parser = argparse.ArgumentParser(prog='Cerridwen')
    parser.add_argument('--version', action='version', version='%(prog)s ' + cerridwen.__VERSION__)
    args = parser.parse_args()

    #cerridwen.quicktest()


    # sun_data = cerridwen.compute_sun_data()
    #
    # # sun_data["jd"]=2459722.0
    # # print(sun_data["jd"])
    # emit_time_info(sun_data)
    # emit_sun_text(sun_data)
    #
    #
    # emit_moon_text(cerridwen.compute_moon_data(sun_data["jd"]), True)
    # emit_mercury_text(cerridwen.compute_mercury_data(sun_data["jd"]))
    # emit_venus_text(cerridwen.compute_venus_data(sun_data["jd"]))
    # emit_mars_text(cerridwen.compute_mars_data(sun_data["jd"]))
    # emit_jupiter_text(cerridwen.compute_jupiter_data(sun_data["jd"]))
    # emit_saturn_text(cerridwen.compute_saturn_data(sun_data["jd"]))
    # emit_uranus_text(cerridwen.compute_uranus_data(sun_data["jd"]))
    # emit_neptune_text(cerridwen.compute_neptune_data(sun_data["jd"]))
    # emit_pluto_text(cerridwen.compute_pluto_data(sun_data["jd"]))

    # JD = 2459722.0
    # sun_data = cerridwen.compute_sun_data(JD)
    # emit_time_info(sun_data)
    # emit_sun_text(sun_data)


    # emit_csv(cerridwen.compute_moon_data(sun_data["jd"]), True)

    file = open("planets.csv", "a");
    buffer = "JD,"
    buffer += "timestamp,"
    buffer += "sun,s_sign,s_min,s_sec,"
    buffer += "moon," \
              "moon_sign," \
              "moon_min," \
              "moon_sec," \
              "moon_trend," \
              "moon_shape," \
              "moon_quarter," \
              "moon_diameter," \
              "moon_nextNewMoon," \
              "moon_nextFullMoon,"
    buffer += "mercury,m_sign,m_min,m_sec,"
    buffer += "venus,v_sign,v_min,v_sec,"
    buffer += "mars,ma_sign,ma_min,ma_sec,"
    buffer += "jupiter,j_sign,j_min,j_sec,"
    buffer += "saturn,sa_sign,sa_min,sa_sec,"
    buffer += "uranus,ur_sign,ur_min,ur_sec,"
    buffer += "neptune,ne_sign,ne_min,ne_sec,"
    buffer += "pluto,p_sign,p_min,p_sec\n"

    file.write(buffer)


    # for i in range(365*5):
    for i in range(365*2):
        # JD = 2460487.10000001 + i
        JD = 2460723.1 + i
        sun_data = cerridwen.compute_sun_data(JD)
        # loop
        buffer = "";
        buffer += str(sun_data["jd"]) + ","
        buffer += str(sun_data["iso_date"]) + ","
        buffer += emit_csv(sun_data)
        print(emit_csv_moon(cerridwen.compute_moon_data(sun_data["jd"])))
        buffer += emit_csv_moon(cerridwen.compute_moon_data(sun_data["jd"]))
        buffer += emit_csv(cerridwen.compute_mercury_data(sun_data["jd"]))
        buffer += emit_csv(cerridwen.compute_venus_data(sun_data["jd"]))
        buffer += emit_csv(cerridwen.compute_mars_data(sun_data["jd"]))
        buffer += emit_csv(cerridwen.compute_jupiter_data(sun_data["jd"]))
        buffer += emit_csv(cerridwen.compute_saturn_data(sun_data["jd"]))
        buffer += emit_csv(cerridwen.compute_uranus_data(sun_data["jd"]))
        buffer += emit_csv(cerridwen.compute_neptune_data(sun_data["jd"]))
        buffer += emit_csv(cerridwen.compute_pluto_data(sun_data["jd"]),False)
        buffer += "\n"
        file.write(buffer);
        print(buffer, end="")


if __name__ == '__main__':
    main()

