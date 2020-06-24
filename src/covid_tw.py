import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import pandas as pd
import twint

import nest_asyncio
nest_asyncio.apply()

c = twint.Config()
c.Username = None
c.Search = 'covid-19'
c.Limit = 20
c.Since = '2020-06-21 0:0:0'
c.Geo = "25.7617,80.1918,1km"
c.Store_csv = True
c.Output = "covid.csv"
c.Lang = "en"

# run
twint.run.Search(c)
