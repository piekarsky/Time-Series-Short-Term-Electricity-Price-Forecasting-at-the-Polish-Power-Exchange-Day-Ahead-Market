# Short Term Electricity Price Forecasting at the Polish Day-Ahead-Market


## Table of Contents

+ [Overview](#overview)
+ [About the dataset](#dataset)
+ [Modeling electricity prices](#modeling_electricity_prices)
+ [Results](#results)
+ [Run the Codes](#run_the_codes)
+ [Development Environment](#development_environment)

## Overview <a name = "overview"></a>

This repository contains the experimental source code for short term (24 hour advance) electricity price forecasting at the Polish SPOT (Day-Ahead-Market) market including **RNN**, **LSTM**, **GRU**, **MLP** and **Prophet** models.</br> Models using both the delayed exogenous variable and the endogenous variables from the forecast period and their delayed values for forecasting.

## About the dataset <a name = "dataset"></a>

Data includes over 26200 hourly observations of electricity prices (PLN/MWh) from January 2018 to December 2020 at the Polish Day-Ahead-Market. Course of this modeled time series of electricity prices is shown in the figure below.
<img width="740" height="420" src = figures/fig_1.png/>


The analysis of the time series of electricity prices confirmed the one described in the literature auto-regressive nature of this process. The figure below
illustrates autocorrelation function of the modeled time series, on which it can be seen that the price of electricity at a given hour is significantly affected by the value of the electricity price from the past corresponding to a delay of multiples of **24 hours**.
<img width="850" height="350" src = figures/fig_2.png/>

A specific feature of electricity prices resulting from the daily, weekly
and annual rhythm is the variability of its level over time. The annual cycle follows
from differences in energy demand in different seasons of the year, which makes
that energy demand is higher in winter and lower in winter
summer months. Electricity prices within the weekly cycle varies with
energy demand on weekdays and weekends. The figure below illustrates the weekly course of electricity prices. There are visible differences in  the course of electricity prices on Saturdays and Sundays compared to other days of the week, where the course of electricity prices is similar.

<img width="740" height="420" src = figures/fig_3.png/>


The daily volatility of electricity prices is influenced by the increased demand for energy,
which occurs between 6 a.m. and 9 p.m. and translates into a higher price of electricity in
this time (figure below). Short-term fluctuations in electricity prices can
result from weather factors that determine the scale of energy production in wind energy sources.


<img width="740" height="420" src = figures/fig_4.png/>


## Modeling electricity prices <a name = "modeling_electricity_prices"></a>

Features used to generate forecasts include autocorrelated lagged electricity prices, energy demand, generation energy from wind sources, time of the day and the occurrence of a holiday. 
Data with energy demand and generation energy from wind sources are published once a day for the coming 24 hour period. The data for these factors are published sufficiently in advance to be used in the model. </br> </br> Minimum delay values can be known and used in the model represent the electricity price 24 hours ago. The model uses delayed electricity price lags ranging between 7 days (being multiples of 24 hours)  and 14 days, as well respective values ​​of energy demand and generation of energy from wind sources.
</br> </br>
For time of the day and holiday
binary dummy coding was used. For time of the day, the value of input 1 was set for the period between 6 a.m. and 9 p.m., where it is visible
are higher electricity prices, and the value 0 is set for the remaining hours of the day.
Due to the fact that the time series of electricity prices in the analyzed period did not show
annual seasonality, the variables defining the annual cycle were omitted. </br> </br>
The data from January 2018 to December 2020 have been splitted as follows: </br> 
– training set: data from January 2018 to June 2020 </br>
– validation set: data from July to September 2020 </br>
– test set: data from October to December 2020 </br>
Splitting the dataset in this way is close to the ratio of 85-7.5-7.5.

## Results <a name = "results"></a>
According to the table below, **RNN** outperformed the other models.

| Model | MAE [PLN/MWh] ↓ | RMSE [PLN/MWh] ↓ | MAPE [%] ↓ | R Squared [-] ↑ |
|:---:|:---:|:---:|:---:|:---:|
| Prophet | 16.9 | 21.8 | 7.54 | 0.86 |
| MLP | 16.61 | 21.23 | 7.32 | 0.87 |
| **RNN (Vanilla)** | **16.15** | **20.84** | **6.94** | **0.87** |
| LSTM | 17.15 | 22.5 | 7.26 | 0.85 | 
| GRU | 17 | 22.12 | 7.32 | 0.86 |


In the figures below shows the actual and predicted electricity price at the Day Ahead Market in the sample period from test set. Forecasts have been generated by the model based on the Vanilla RNN, which was characterized by
the highest accuracy of electricity price predictions in the test period.

The course of the actual and predicted electricity price generated by the Vanilla RNN in October 2020.
<img width="680" height="420" src = figures/fig_5.png/>

The course of the actual and predicted electricity price generated by the Vanilla RNN in November 2020.
<img width="680" height="420" src = figures/fig_6.png/>

The course of the actual and predicted electricity price generated by the Vanilla RNN in December 2020.
<img width="680" height="420" src = figures/fig_7.png/>

The course of the actual and predicted electricity price generated by the Vanilla RNN in the 48th week of 2020.
<img width="680" height="420" src = figures/fig_8.png/>


## Run the Codes <a name = "run_the_codes"></a>

If you want to train *RNN* 

```
python main.py --model 'rnn'
```

If you want to train *GRU* with 2 hidden layers and a learning rate of 0.05

```
python main.py --model 'gru' --num_layers 2 --lr 0.05
```


## Development Environment <a name = "development_environment"></a>
```
- Windows 10 Home
- Python 3.7.3
- torch 1.8.1
- NVIDIA GFORCE RTX 2060

