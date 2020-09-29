# %%
import os
os.chdir('..')

# %%
import pandas as pd

# %%
df = pd.read_csv('datasets/hackatrain_synthetic_charging_data.csv')


# %%
from OSMPythonTools.nominatim import Nominatim
nominatim = Nominatim()
areaId = nominatim.query('Vienna, Austria').areaId()

# %% Extract Geo features
# IDEA: Use the QUERY
# - Join Station Address with City
# - Query using nominatim and pick the first result (highest relevance)
# - Extract the lat, lon, class and type
nominatim.query('Spoorstraat 22, 3511 EN Utrecht').toJSON()

# BONUS: Whats the distance to things like closest train station / shopping mall?

# %% Extract Time features
# - Convert date and time into
# - Get week day
# - Mark work hours
# - Mark rush hours
# - Mark bank holidays
