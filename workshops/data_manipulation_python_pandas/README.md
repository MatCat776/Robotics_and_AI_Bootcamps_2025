# Basics of Data Manipulation with Python and Pandas Bootcamp 

## Introduction 
For this bootcamp, you will want a python environment on your computer or on an online environment, like Google Colab. You will need the following packages installed:

- pandas
- matplotlib 
- seaborn 

## Installing the Required Packages 

If you are using an anaconda virtual environment, you will want to run:

```bash
conda install pandas
conda install matplotlib
conda install seaborn 
```

If you are using a native linux environment, you will instead want to run 

```bash
pip install pandas
pip install matplotlib
pip install seaborn
```

If you are using Google Colab, these packages are probably already installed. If not, you can run:

    %pip3 install pandas
    %pip3 install matplotlib
    %pip3 install seaborn 

On your top code cell. 

## Pandas
Pandas is a python library for working with tabular data, which pandas calls **dataframes**. You are probably more familiar with referring to these structures as spreadsheets or excel files. In most data science applications, rows of a spreadsheet are **observations** while columns on the spreadsheet are **features** of that observation. 

## Tabular Data 
Lets make an example dataframe with the class right now. We are going to go around the room, person by person. Each person will get a number, and that number will be how we identify that person as an observation. What we will be observing for each person will include the following features:

    - Favorite Color
    - Favorite Movie 
    - Height
    - Number of times you've visited another country 

We'll give everyone a couple of minutes to collect their answers, then start building the dataframe row by row. 

A couple of observations: 
There are different **types** of data within this dataframe. 

Favorite Color is a (somewhat closed-ended) category. We would enter it as a word, which in programming we would call a  "string". 

Favorite Movie is a (much more open-ended) category. We would enter the title as a word or collection or words, wich would also be a string. 

Height is a number, and a continuous one. It could be 60 inches or 72.5 inches 76.999999 inches. It could take basically any continuous value. 

Number of time you have visited another country is a number, but not a continuous value. It should only really take a whole number value, like 0, 1, 2, etc. It would be hard to conceptualize visiting another country 1 and a half times. 

Depending on the type of data, you may treat a feature column differently. You also may have to clean out data differently based on certain responses. For example, if this was a written survey, you might have to have a program know, at some level, that 'green', 'Green', and 'GREEN' are all the same color. 

There are also different ways of **filtering** this dataframe. We could look at, for example, just everyone's favorite movie. Or, we could look at:

- How many people's favorite color was red
- How many people are over 65 inches tall 
- The average amount of times someone has visited another country if their favorite color is green 

And then, we might start asking some scientific(-ish) questions like, 

- is there a stastically significant difference in the number of times people visisted a different country if their favorite color was blue vs red?
- Are people with the same favorite movie likely to be within 2 inches of the same height?

Most of the time, when we are investigating data like this, we are trying to either run some type of model or answer some type of question. Being able to filter and manipulate the data really comes in handy for this, as does being able to visualize different aspects of the data. For this reason, we are going to explore how to do this with the python library. 

## Dataset Information

We are going to be using a dataset on white wine quality. 

The Wine Quality dataset can be viewed here: https://archive.ics.uci.edu/dataset/186/wine+quality 

And the citation for the dataset is here: 

P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.Modeling wine preferences by data mining from physicochemical properties.In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236.

This 2009 dataset has 13 variables, one of which is a wine quality score (quality) between 0 and 10. We will use the winequality-white csv (comma separated value, a pretty common form for datasets) dataset, which has 4898 rows. A more complete description of the data can be found in the documentation for the dataset, especially the winequality.names file.

We can open the csv file and take a look at the attributes. 

There is an attached code file in the "code" section of this workshop in the github. I will be typing this code file out, and feel free to code along with me. However, the file itself is available if you get lost, want to check your work, or if I'm going too fast. 

Please feel free to slow me down if I am going too fast!! 


### Loading 
We are going to use the pandas library to manipulate our dataset. This is not the only optional, but pandas is quite full-featured. In some cases, pandas can be slower than other libraries to perform data operations. For our limited set of operations on this relatively small dataset, pandas will do just fine. 

First, you are going to import the pandas package. In python, we use the import statement to load in a package and its associated functionality. 

    import pandas as pd

The "as pd" part lets us locally re-name the package we are importing as "pd", so we can use "pd.<function>" to access the function name instead of the full pandas.<function>. Of course, we could have said "import pandas" and left it at that. But "pd" is a somewhat common nickname for pandas across example code out there in the wilderness, and it's convenient and short, so we'll keep it. 

By the way, matplotlib is one of those "big" packages. When we type 

    import matplolib.pyplot

we are telling python to only import the pyplot **sub-module** of the matplotlib packages, because its the only one we'll be using today. That creates a little less overhead when we actually run the program. 

Next, we want to load our csv file into a pandas dataframe. The dataframe object provided by the pandas library is a very convenient way to work with the data and use the library functionality.

    #Read the dataset into the "wine_df" variable
    wine_df = pd.read_csv("winequality-white.csv", sep=";")

The first line here is a python comment, which start with a "#" and continue for the entire line. We can put anything in the comment, it will be ignored when the program is run. This is handy way to document our code and keep track of what we are doing. 

The statement below the commend uses the "read_csv" function of the pandas library to take in a path to a csv file ("winequality-white.csv") and store it in the wine_df variable. We had to ensure that the separator variable was set to a semicolon, since that is the marker this csv uses 

## Looking at the Dataset 
Now, we want to look at an overivew of our data and make sure it was read in correctly. Look at this line: 

    #Get an overview of the data 
    print(wine_df.head())

If you run this program now in a terminal:

```bash
python3 data_exploration.py 
```

This will print the names of the columns and the first 5 or so rows of the data, giving you an excel-like view of the data. 

Sometimes it is useful to print the columns in the dataframe. You can print them as a pandas Index, or you can convert them to a python list. 

    #Print the columns - method 1
    print("Columns Index")
    print(wine_df.columns)

    #Print the columns - method 2
    print("Columns as a List")
    print(list(wine_df.columns))

It is also nice to explore some basic data statistics based on the columns, like the mean, min, max values, and the standard deviation. The describe() method gives you this information as well as information about the counts and quartiles per column. 

    #Describe the data 
    print("Describe the data")
    print(wine_df.describe())

## Indexing 
One of the most useful things we can do with pandas is index the dataframe to get different subsets of data. There are MANY ways to do this in pandas, and only a subset are shown below. 

The following command takes one column of the dataframe, when we index on the column name, and converts it to a series: 

    #Return a series with the 'quality' column of of the dataset
    quality_series = wine_df['quality'] 
    print("Quality series")
    print(quality_series)

You could also pass a list with multiple column names to get a smaller dataframe that consists only of the column names you passed in. 

Sometimes we want to convert the pandas objects back to a list of values. The following command takes the "quality" column, and converts it to a list of values located, in order, in that column. 

    #Get a list of values from a column
    quality_list = wine_df['quality'].values.tolist()
    print("Quality List")
    print(quality_list)


### Using .loc
The .loc property of the dataframe allows you to select different rows and columns, where columns are selected by label. You can also pass conditions into .loc, which we will get into later. If passing row and column indexers, the order is row, column. The .loc and .iloc properties following python slicing rules, but loc includes the start and end value in a slice, and iloc excludes the end value. 

For example: 

    #Get everything in quality 
    print("Entire quality column")
    print(wine_df.loc[:,"quality"])

By passing ":" as the row argument, you select all rows. For the column argument, we passed in the label "quality". So, we will only the quality column values for all rows. 

The next example gets the first (0-indexed) row, for only the value in the quality column. 

    #Get the first value in quality
    print("First quality value")
    print(wine_df.loc[0,"quality"])

This slicing method gets you the quality values for indexes 0-5: 

    print("First and up to 5th-indexed quality values")
    print(wine_df.loc[0:5,"quality"])

And this gets you the quality value for  everything before index 5:

    print("Everything before and up to the 5th-indexed quality values")
    print(wine_df.loc[:5,"quality"])

This gives the quality value for everything after index 4890: 

    print("Everything after the 4890th-indexed quality value")
    print(wine_df.loc[4890:,"quality"])

And this gives you both the quality and sulfate columns for row indexes 0:5: 

    print("First through 5th-indexed quality and sulphates values")
    print(wine_df.loc[0:5,["quality", "sulphates"]])

### Using .iloc 
Using iloc is very similar to using loc, except that you use numerical indexes for both the rows and columns. It still uses the order row, column. For iloc slicing, the end value is also excluded, unlike in loc. 

For instance, this gives you a dataframe subset of rows indexes 1 and 2 with column values for column indexes 1-4: 

    #Use iloc 
    print("Row indexes 1-2 and column indexes 1-4")
    print(wine_df.iloc[1:3, 1:5])

This gives you the value at row index 4 and column index 0: 

    print("4th row index, first item")
    print(wine_df.iloc[4, 0])

And this gives you all column values at row index 4:

    print("All columns, row index 4")
    print(wine_df.iloc[4, :])

### Selecting a row or rows based on a condition: 
We can also use .loc to select a subset of the data based on a condition. The following will give you all of the rows where the wine quality column has a value greater than 5: 

    #Selecting a row based on a condition 
    print("All rows where quality is above 5")
    print(wine_df.loc[wine_df["quality"] > 5])

We can also check how many rows this leaves us by getting the length ( len() ) of the dataframe index property: 

    #How many rows is this?
    print("How many rows is this?")
    print(len(wine_df.loc[wine_df["quality"] > 5].index)) 

You can also use logical and ( & ) and logical or ( | ) to combine conditions into expressions. Make sure you have parentheses around each sub-condition. 

    print("All rows where quality is above 5 and sulphates are above 0.45")
    sub_df = wine_df.loc[(wine_df["quality"] > 5) & (wine_df["sulphates"] < 0.45)]
    print(sub_df.head())
    print("How many rows is this?")
    print(len(sub_df.index))


## Handling Missing Data

Often a dataset will have missing data -- this can be a value of None, NaN (not a number) in upper or lowercase, or simply an empty cell in csv. 

We can find na (missing) data values with the .isna() property of the dataframe. This returns a dataframe where values are replaced by True or False to indicate whether that particular value at the row and column is present or NaN:


    #Find and Handle NaNs 
    #We don't have an NaN values
    print(wine_df.isna())

For a larger dataset, the .value_counts() property will give you true and false counts per column. Here, False means the value is present (not NaN) and True counts will indicate the presence of NaN values. 

    print(wine_df.isna().value_counts())

You can see we don't have any NaN values in the dataframe. That's nice! For the sake of argument, lets insert a fake NaN value and assign it to a new dataframe name so we don't mess with our original.

The following uses the python "None" value to put an NaN value in the first row in the quality column. 

    #Insert an NaN value
    print(wine_df.loc[0, 'quality'])
    new_df = wine_df
    new_df.loc[0, 'quality'] = None
    print(new_df.loc[0, 'quality'])

Now lets get rid of the NaN! The following code uses the dropna() property to drop any rows with an NaN value and assign it to a new dataframe. However, this does not reset the index of the dataframe -- meaning our dataframe would start from index 1 since we just got rid of row 0. Sometimes that can lead to weird behavior. So, lets reset the index as well. You could reassign the reset index back to the same dataframe, but we can also pass the inplace=True argument to the reset_index function so it operates on the same dataframe we call it on. A few properties have the option of using inplace=True, property. Up to you and your preference as to whether or not you want to reassign the dataframe or manipulate it in place!

    #Drop the na value 
    print("Number of rows before dropping NaN")
    print(len(new_df.index))
    cleaned_df = new_df.dropna()
    #Reset the index - in place this time 
    cleaned_df.reset_index(inplace=True)
    print("Number of rows after dropping NaN")
    print(len(cleaned_df.index))
    print(cleaned_df.loc[0, "quality"])

We can see we have one less row than we did before dropping the NaN value. So that is working! 

## Visualize
Visualizing is a huge topic and this guide only gives a small sample of what kinds of data visualization you can do on your dataset. For this tutorial, we'll use matplotlib.pyplot for the scatter visualization, and seaborns heatmap visualization. 

### Correlation
A correlation heatmap is useful to see what variables might be correlated to others. The following creates a correlation heatmap and displays it, using the seaborn heatmap and the dataframe .corr() property: 

    import matplotlib.pyplot as plt 
    import seaborn as sns 

    #Correlation
    print(wine_df.corr())
    plot = sns.heatmap(wine_df.corr()) 
    plt.show()
    plt.clf()

The plt.clf() clears the figure when you are finished, which allows you to pop up another figure if you would like. 

### Scatter Plot
For the matplotlib scatter plot, we'll create a scatter plot with two of our dataframe columns, quality and alcohol: 

    #Scatter
    plt.scatter(wine_df["quality"], wine_df["alcohol"])
    plt.show()
    plt.clf()

Output:

You can get much fancier with plot labeling and formatting. These were some very basic functionalties to get you started with pandas data exploration. 


## Final thougths
We didn't do anything worth saving in this guide, but the pd.to_csv("name_of_csv.csv") function and the plt.savefig("fig_to_save.png") are worth having in your back pocket for future work. 


I hope this helps you start becoming dangerous in python and pandas basic data manipulation! 


## Polars 
A newer python package for data manipulation, called [Polars, is also worth looking into](https://pola.rs/). It is much, much faster. Maybe slightly less used than Pandas at this point, but probably worth learning. 

