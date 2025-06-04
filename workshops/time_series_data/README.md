# Working with Time Series Datasets in Python 
June 2025 

## What is Time Series Data?
There are two types of datasets I would consider common "in the wild". 

The first is more characteristic data, where you are trying to identify something. This could be a picture, an event, an anomaly, anything. You essentially have a group of features and an outcome, but the structure of the features is maybe less important than the collection of them. 

The second type is time series data, where you have a group of features, maybe an outcome, with specific values **at given points in time**. This is a very common type of dataset, although it can be hard to collect. The values of the features matter, but so do the times at which the values occur. 

Time series data is very common when looking at things in a more process-like way rather than looking at some individual thing. Weather data is usually time series. Manufacturing operations also also often time series. 

However, time series data can be notoriously difficult to curate, especially when you are looking at several different sources. This workshop is meant to go through some of things to consider and look out for when looking at time series data, as well as how to put disparate sources together. We are going to be using python and pandas, like we did for the data manipulation workshop, because pandas has some robust tools we can use. 

Let's talk about a quick example before we get into the processing aspects of time series data. 

## Example - Jurassic Park. 

Let's say you have a dataset where you are trying to identify the dinosaurs in Jurassic Park. In this case, we are only looking at dinosaur characteristic data. What features might we look at?

- Size 
- Color 
- Diet
- Sound
- Etc

Our data would probably have a given row as a type of dinosaur, and these characteristics would be the columns. 

We can probably get a pretty good idea of what the dinosaur is from these characteristics. What if, instead, we looked at this identification from a time series standpoint?

Lets say every minute of Jurassic park is a timestamp. Our dataset is now made of timesteps as rows, and the columns are broken out into **features at a timestep**. (Let's also assume, in this case, for sake of simplicity, that only one dinosaur is onscreen at a given minute. Obviously, that rule is broken many times in the actual movie)

| Time | Size | Diet | Sound | Color | Dinosaur | 
| ---- | ---- | ---- | ----  | ----  | ---- | 
| Minute 1 | medium | carnivore | barking | purple | raptor | 
| Minute 2 | medium | carnivore | silent | purple | raptor | 
| Minute 3 | N/A | N/A | N/A | N/A | None | 

Based on the movie, we could probably train some sort of model to learn the difference between the dinosaurs based on size, diet, sound, and color alone. But what if we only had the Diet and Sound feature? It might be hard to differentiate a velociraptor from a T-Rex if they aren't currenly making a sound. A mistake that is both embarrasing and deadly. 

Time essentially becomes another feature, and patterns through time can often help us differentiate parts of a process or events that are happening. It's especially helpful in our Jurassic Park example, since we know for most of the first and second act, if an animal is a carnivore, its the T-Rex, and for the third act, it's probably the velociraptor. 

Most of the time, when working with time series data, the data is formated where the row is the timestamp, and the columns are features measured or recorded **at that same timestamp**. There are a lot of considerations when putting this data together and analyzing it, though. For example, sometimes you may have a feature that is useful to know generally, but may be the same for all timestamps. For example, if you have time series data for a machine running something on your manufacturing line, it may be useful to know the machine's brand -- but that isn't going to change at any point of the process its running. Do you copy that feature for all values of the time stamp, or treat that differently? 

## Common Time Series Scenarios 
- Sensor readings at intervals during a process run: For example, a machine recording its internal temperature and pressue while soldering a part. 
- Periodic readings from multiple sensors in the same area: For example, we take 5 minute readings from two weather stations in the same Orchard in Sandpoint. The sensors do not report at exactly the same time. 
- One variable with list of readings at specified intervals: For example, if you have a setpoint for a process, you may get one "start" timestamp, and then a list of values of the setpoint each taken 10 minutes apart (aside: this kind of formatting is my personal kryptonite)

## Sampling Rates
There are different ways to sample sensor data. 

### Constant Sampling Rates 
- Sensor A samples every 5 minutes, starting at 12:00pm 
- Sensor B samples every 10 minutes, starting at 12:00pm
- Sensor C samples every 5 minutes starting at 12:02 pm 
- Sensor D samples every 5 minutes, starting at 12:00pm 
- Sensor E samples every 10 minutes, starting at 12:02pm 
- Sensor A, B, and C, D, and E's sampling rate is consistent within-sensor
- Sensor A and B's sampling rate  is not consistent across sensors (but is aligned)
- Sensor A and C's sampling rate is consistent across sensors, but not aligned 
- Sensor A and D's sampling rate is consistent across sensors, and aligned 
- Sensor B and E's sampling rate is consistent across sensors, but not aligned 
- A and E's sampling rate is not consistent across sensors, and is not aligned 

### Sampling on Change
- Common for setpoints in manufacturing 
- Sensors may not have consistent reporting sample rates, which may vary quite a bit across sensors 
- You may have other inconsistently sampled sensors for a variety of reasons 

### Episodes 
- Additionally, you may have different processes/etc. that involve the same type of process but may have taken place on different days 
- These episodes may also not be the same length of time
- Might have to treat them as separate sequences of samples, may have to calculate offsets and go from there 

## How to Process Time Series Data? 
- In a LOT of scenarios, you want timestamp as your row index, and input/output variables as your column headers 
    - Best case scenario – your data already looks like that
    - Worst case scenario - all your data is self-contained in a list of readings, within-sensor sampling has different rates, and between-sensor sampling has different rates 
- It can be very, very, very, VERY, annoying to try and get the data in this format (though many machine learning models will expect it in this way) 
- You may have to:
    - Resample
    - Interpolate
    - Determine Valid intervals for different streams 
    - Assign to closest time step  


## Tips and Tricks
### Formatting 
- This can be harder for exploratory research, but in general, try to figure out what specific input format your model will want to run and get the data there
- If you have no clue, I would recommend getting your data in row=timestep, variables = column headers format 

### Episodes
- Is your data episodic? Need to sort into episodes (most likely sequences)
    - Frost events
    - Flattening heart rate 
    - Event occurred, etc. 
- Check variables for significant periods of missing data 
    - Does a variable have significant coverage of a time period? Should we throw it out otherwise? For all episodes? 

### Missing Data 
Missing Data (but not enough missing to throw out)
- Copy from last value?
- Take the average? 
- Copy from first value? 
- Put in dummy value to indicate missing (often not great) - can work for NA values, like in genetic algorithms

### Resampling 
- Enforce highest resolution?
- Enforce lowest resolution? 
- Something else? 
- May have to create "bins" (decide on time slots relevant)
- Too little data – copy, interpolate, etc
- Too much data – resample, average, max/min, etc 
    - Could create new columns for each of these – not uncommon 
- Do all variables get kept? 
- How to handle missing values if interpolating

### Time Zones 
- Daylight Savings Time is a MAJOR PAIN
- If you can get away with collecting data in UTC time in the first place, do that
- If not, you will have to do some major conversion – might not be so straightforward in python pandas 
- Expect the possibility that different data might be in different time zones 
- Aligning data from disparate sources is often the trickiest part!

## Final Thoughts on Time Series Data Wrangling 
- Make sure you’re checking yourself periodically throughout the process – it is easy to make mistakes 
    - And often very difficult to catch them 
- Document your process! It will be easier to recreate later. You could find yourself recreating the process more often than you would like 
- On the output project, make sure you explain data transformations you conducted


## Time Series Data from the Black Lagoon 
You want to conduct a study synthesizing data from 4 different sensors

- Sensor 1 – hourly(ish), records setpoints with a variation of 1-4 hours between timestamps. Data formatted (timestamp, reading)
- Sensor 2 – sample rate 5 minutes, given start time of January 1, 2022, hr 1. Data formatted as a list of values 
- Sensor 3 – samples rate 5 minutes, given an end time of December 31st, at hr 23 and minute 8. Timezone PRC. Data formatted as a list of values 
- Sensor 4 – sample rate every 15 minutes. Data formatted as (timestamp, reading)

Code files and datasets are inside the "code" folder in this workshop folder on the repository. We will be going through the code file to make this happen. 

