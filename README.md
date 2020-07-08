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

AT the end I show that social distancing in New York really helped "flatten the curve" of new Covid-19 hospitalizations.  

Hospitalization data comes from [New York's City health webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page). The dataset contains daily hospitalization numbers related to Covid_19 in NYC. To smooth the volatility of the hospitalization data I use a 7-day moving average. Then I find the day to day change to approximate the rate of hospital admissions.

## Hospitalization Data

I create a hospitalization index by finding the daily percentage of change in the 7-day rolling hospitalization numbers.

![hospitalization rate](/Data/hospitalization_rate_of_change.png)


## Social distance - Traffic index

I use the first week of February as my baseline traffic congestion. I divide each day of the daily traffic index by the corresponding day in the base week.

![TSD](/Data/TSD_index.png)

The brown line indicates March 13 when the former employer of the author closed down. The red dashed line indicates March 20th when Gov. Cuomo put officially the state of New York in PAUSE.
As you can see Newyorkers started quarantining themselves much earlier than the officially mandated stay in place orders.   


## Linear regression model

I fit a simple linear model using the traffic social distance `'TSD_rolling'` as a predictor of Hospitalization's percentage growth `'hosp_change'` and test the $R^{2}$ at differest lags.

![optimal lag](/Data/optimal_lag.png)

The analysis produces a 13-day lag ($R^{2}$=0.815) as the best predictor of the current hospitalizations rate of growth.

![13 lat regression](/Data/OLS_regression_13_day_lag.png)

## AR and SARIMAX Model

As a base model, I try to fit an autoregressive model to the data. Using auto_arima I find the best parameters (3,1,0). The predicted values are not very good. I get an RMSE (0.0424) value almost equal to the mean value in the test set. 

![ar model](/Data/AR_prediction_full.png)

Then, I try to improve upon this by fitting a SARIMAX model. Using auto_arima I find the best parameters (1,1,1)X(1,0,07) with the 13-day lagged traffic index as an exogenous variable. I get a lower RMSE (0.0248). However, this result is still not very impressive given the mean value of the test set (-0.042).

![ar model](/Data/SARIMAX_prediction_full.png)
## Conlusion

The United States is in the mids of the Covid-19 pandemic. The disease has tested the preparedness of the government and the community to face the virus. It is very important to quantify the impact of Government policies and community actions to stop the spread of Covid-19.  This analysis tries to estimate transportation trends in the city of New York as they related to the number of Covid_19 patients hospitalize.

I show that social distancing in New York really helped to curve down the rate of new hospitalizations.  Further, the analysis revealed that the impact of social distance captured by the traffic in the city is not obvious for about 13 days after the change in behavior.

## Future work

This part of the project's purpose is to quantify the relationship between social distance and hospitalization growth rate. However, other mechanisms to curve the spread of Covid-19 are overlooked. It would be nice to find a way of quantifying the impact of different ways of containing the spread like wearing masks, or the use of hand sanitizer.
Secondly, I would like to look at different urban areas with different traffic patterns.
