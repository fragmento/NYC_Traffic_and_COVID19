===================
### Social Distance and Covid_19
===================

by: Andres Chaves

This is the last project while at Flatiron School Data Science Immersive Program (on campus) in New York City.

============================================================================

    ├── Data                 <- The original, immutable data dump, graphs.
    |
    ├── Notebooks            <- Jupyter notebooks.
    |
    ├── Reports              <- Generated analysis as HTML, PDF, Slides, etc.
    |
    ├── README.md            <- The top-level README for developers using this project.



===========================================================================

# Hospitalizations as a function of traffic in NYC


In this project, I plan to explore the relationship between social distance and Covid-19 related hospitalizations in New York City during the last 4 months.
For this, I will try to quantify the amount of social distancing using tomtom's traffic index. Tomtom's traffic index is the percentage of extra time that it takes to travel any given day based on some baseline(no traffic).

I will use this to create a daily traffic social distance (TSD) index that will reflect the change in congestion with respect to a normal traffic day. I will use the first week of February as my baseline traffic congestion. I will divide each day of the daily traffic index by the corresponding day in the base week. To smooth the data I will use a 7-day moving average.

This will give me an index where 0 indicates maximum TSD (no traffic), 1 indicates no TSD (same traffic as baseline). TSD greater than 1 indicate more traffic than usual.

Hospitalization data comes from [New York's City health webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page). The dataset contains daily hospitalization numbers related to Covid_19 in NYC. To smooth the volatility of the hospitalization data I use a 7-day moving average. Then I find the day to day change to approximate the rate of hospital admissions.

## Hospitalization Data

I create a hospitalization index by finding the daily percentage of change in the 7-day rolling hospitalization numbers.

![hospitalization rate](/Data/hospitalization_rate_of_change.png)
