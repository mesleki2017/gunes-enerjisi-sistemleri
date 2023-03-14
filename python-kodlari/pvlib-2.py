#pv sepha arasi mesafe belirleme
# 21 aralikta saat 12 deki gunes acisi eigimi ve enlem kullaniliyor

from pvlib import solarposition
from pvlib.location import Location
import pandas as pd
import numpy as np
import math

tz = 'Turkey'
#lat, lon = 40.06436260453357, 42.16731892278434
lat, lon = 36.617151165641374, 32.097118528499216

times = pd.date_range('2022-12-21 12:00:00', '2022-12-21 12:00:00', freq='H', tz=tz)
solpos = solarposition.get_solarposition(times, lat, lon)


sepha_yukseklik=4
solar_panel_egim_acisi=lat
gunes_acisi=solpos['apparent_elevation']['2022-12-21 12:00:00']

#triangle math
hip1=math.sin(math.radians(solar_panel_egim_acisi))*sepha_yukseklik
aaa=math.cos(math.radians(solar_panel_egim_acisi))*sepha_yukseklik
bbb=hip1/math.tan(math.radians(gunes_acisi))

solar_sepha_aralik=aaa+bbb

print("solar_sepha_aralik = ",solar_sepha_aralik)
