# COVID-19-Regression-Model-India
 A polynomial regression model to predict the number of infections, recoveries and deaths on a particular day in the future. Currently predicion is based on the Indian dataset. Can be altered according to your prefered dataset. Steps for altering dataset will be present in the README file.

## Steps to run
1. ### Install the following Python libraries
    1. NumPy
    ```
    pip install numpy
    ```
    2. MatPlotLib
    ```
    pip install matplotlib
    ```
    3. Pandas
    ```
    pip install pandas
    ```
    4. Sci-Kit Learn
    ```
    pip install sklearn
    ```
2. ### Run Covid19.py
    ### **NOTE**
    
    Please enter a whole number when prompted to enter a Day i.e. 1,2,3...n.
    
    Do not enter the date. Please refer the dataset to understand better.

## Steps to alter the dataset
1. Download the latest dataset (case_time_series.csv) from the following link. You can replace this dataset with your own. Remeber to edit the python script and the dataframe values in the script accordingly.

    https://api.covid19india.org/csv/latest/case_time_series.csv

2. If you are using the updated version of the same dataset then, 
    * Create another column at the end called 'Day No'.
    * Using Excel, fill in this column with values from 1 to latest day number. Since Excel has a QuickAnalyze feature, it can fill this entire column with just one click.
3. Save and you're ready to go.

## License
### **© Aryan Felix**