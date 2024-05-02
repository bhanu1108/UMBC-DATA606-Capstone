# 1. Title and Author

### Project Title: Predicting Used Car Prices

### Prepared for
UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang

### Author Name: Bhanusri Oleti

### Profiles and Presentations
- **GitHub Profile:** https://github.com/bhanu1108
- **Linkedin Profile:** http://linkedin.com/in/bhanu-sri-oleti-2bb328215

# 2. Background

### What is the Project about?

The purpose of this dataset is to offer a thorough understanding of the used car market's dynamics. It covers a wide range of variables that affect used car pricing and marketability, from technical details like power output and gearbox type to more arbitrary variables like seller type and unrepaired damage. Through the analysis of this dataset, one can learn about market trends for used cars, comprehend the preferences of buyers, and help sellers maximize their pricing strategies.

### Why does it matter?

For a variety of stakeholders in the automotive industry, it is essential to comprehend the variables that influence used car pricing and sales. Understanding market trends can help sellers increase the effectiveness of their pricing strategies and boost sales. Making educated purchases can be facilitated for consumers by having a solid understanding of market dynamics. Researchers and analysts looking into consumer behavior, market trends, and pricing tactics in the automotive sector may also find this dataset useful.

### What are your research questions?

1. What are the main variables affecting the cost of used cars? What impact do factors like damage, brand, mileage, and registration year have on the price?
2. What effect does the type of seller (dealer vs. private) have on used car prices and saleability?
3. Does the used car market follow any seasonal patterns? What effects do variables like last seen and month of registration have on pricing and sales activity?
4. Is it possible to forecast the average cost of a used car using regression analysis based on its specifications and industry trends?
5. What impact does unrepaired damage have on used car prices and marketability?



# 3. About Dataset

- **Data sources:** [Used Cars Dataset on Kaggle](https://www.kaggle.com/datasets/thedevastator/uncovering-factors-that-affect-used-car-prices)
- **Data size:** 70.96 MB
- **Data shape:**  - 233531 rows, 21 columns
- **What does each row represent?**
  - Each row in the dataset represents a single advertisement for a used car. Each advertisement provides information about a specific car that is being sold, including details such as its make and model, year of registration, seller type, price, condition, and various other attributes. In summary, each row represents a unique listing of a used car for sale, with accompanying details about the vehicle and its listing.

### Data Dictionary 

**Columns:**
* dateCrawled: Date the car was crawled. (Date)
* name: Name of the car. (String)
* seller: Type of seller (private or dealer). (String)
* offerType: Type of offer (e.g. sale, repair, etc.). (String)
* price: Price of the car. (Integer)
* abtest: Test type (A or B). (String)
* vehicleType: Type of vehicle (e.g. SUV, sedan, etc.). (String)
* yearOfRegistration: Year the car was registered. (Integer)
* gearbox: Type of gearbox (manual or automatic). (String)
* powerPS: Power of the car in PS. (Integer)
* model: Model of the car. (String)
* kilometer: Kilometers the car has been driven. (Integer)
* monthOfRegistration: Month the car was registered. (Integer)
* fuelType: Type of fuel (e.g. diesel, petrol, etc.). (String)
* brand: Brand of the car. (String)
* notRepairedDamage: Whether or not the car has any damage that has not been repaired. (String)
* dateCreated: Date the car was created. (Date)
* nrOfPictures: Number of pictures of the car. (Integer)
* postalCode: Postal code of the car. (Integer)
* lastSeen: Date the car was last seen. (Date)

## Target/Label in ML Model

In a machine learning model aimed at predicting the price of used cars, the target or label variable would typically be the "price" column. This is the variable that the model will attempt to predict based on the values of other variables.

## Features/Predictors for ML Models

As for the features or predictors, several variables from the dataset could be selected:
- Year of Registration: This variable indicates how old the car is, which often correlates with its price
- Mileage: The number of kilometers the car has been driven is an important indicator of its wear and tear and hence its value.
- Brand: Some brands are associated with higher resale values than others.
- Fuel Type: Fuel Type also determines the resale value of cars. 


# 4. Exploratory Data Analysis

- There are missing value in the dataset 

**Percentage of missing values in the dataset**

![1](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos13.png)
The chart shows the distribution of missing values across several columns in the dataset. Columns like "dateCrawled" and "nrOfPictures" have a very low percentage of missing values. Other columns, like "notRepairedDamage","Vehicle Type" and "Fuel Type" appear to have a higher percentage of missing values.

- As a part of data cleaning all the null values have been dropped and 'lastSeen', 'dateCrawled', 'dateCreated', 'nrOfPictures', 'postalCode' columns have been dropped as they are not very useful for our analysis.

- Some of the names in the dataset are in german language. I have translated all of them to english language for better understanding.

- Outliers have been removed from the dataset as they can obscure patterns and relationships in the data. Removing them can make it easier to interpret the results and draw meaningful insights. Removing outliers can result in a more accurate model by reducing the influence of extreme values.

### Visualizations

**Correlation Matrix between month Of Registration, year Of Registration and price**

![2](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos1.png)
This is a correlation matrix representing the correlations between month of registration, year of registration and price. Three types of correlations are used here. We can see that there is more positive correlation between price and year of registration than price and month of registration.

**Vehicle type vs price**

![3](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos2.png)
From this bar graph we can see that Suv cars have higher prices when compared to other cars and followed by convertible cars and coupe cars. Small sedans have relatively lower prices than other cars.

**Damage repair vs price**

![4](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos3.png)
The median price of cars with not repaired damage appears to be lower than the median price of cars without not repaired damage. The box for cars with not repaired damage is entirely below the box for cars without not repaired damage. The distribution of prices for cars with not repaired damage has a wider range than the distribution of prices for cars without not repaired damage. The box for cars with not repaired damage is longer than the box for cars without not repaired damage. There appear to be more outliers for cars with not repaired damage than for cars without not repaired damage.

**kilometers vs price**

![5] (https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos4.png)
The pattern to the data points suggests that the relationship between price and mileage is not perfect. In other words, there are other factors besides mileage that can affect the price of a car. There appear to be a few data points that fall outside the main cluster of data points. These data points may be outliers, which are data points that differ significantly from the overall trend.

**Brand vs price**

![6](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos5.png)
Porsche brand cars have more resale price than all other car brands then followed by land rover, jeep, jaguar and audi etc. Daewoo brand cars have less resale price followed by rover, diahatsu, trabant etc.

**Gearbox vs price**

![7](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos6.png)
Based on this plot, it appears that cars with automatic gearboxes tend to be slightly more expensive than cars with manual gearboxes. This can potentially be due to various factors such as the popularity and demand for automatic gearboxes, or perhaps the additional features and technology that may come with cars equipped with automatic gearboxes.

**Age vs price**

![8](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos7.png)
From this bar graph, We can see that there is no standard pattern between age and price. Some cars with less age have higher prices and middle aged cars have lower prices and some cars with higher age also have higher prices. So we can say that price doesn't solely depends on price.There are other factors besides age that can affect the price of a car.

**Fueltype vs price**

![9](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos8.png)
Cars with hybrid fuel type have higher price and then followed by diesel and electric. LPG, CNG, benzin all these fueltype cars have almost same prices.

**Seller vs price**

![10](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos9.png)
Cars from private seller have more resale prices compared to cars from commercial seller type.

**Correlations between variables in the dataset**

![11](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos10.png)
This is the heatmap showing correlations between all the columns in the dataset. There appears to be strong positive correlations between "price" and "powerPS" , "Price" and "Fuel Type" and "kilometer" and "yearOfRegistration". This suggests that cars with more horsepower and cars with higher mileage  tend to be more expensive or have been driven for a longer period of time. There appears to be a strong negative correlation between "price" and "Age". This suggests that cars tend to get cheaper as they get older.

**Top 10 and bottom 10 brands ads count**

![12] (https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos11.png)
From the graph we can see that ads for the brands such as volkswagen, BMW, opel are highest in number so that these cars are the highest reselling cars. Ads for brands such as lada, trabant, rover are lowest in number suggesting that these are the least reselling cars.

**Top 10 Cars by Vehicle Type, Brand, and Model - Ads Count**

![13](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos12.png)
Here We can see that Sedan cars are the most reselling cars followed by small sedans, Estate cars, Buses etc. Volkswagen sedans are highest reselling cars folloed by Volkswagen small sedans, Opel small sedans etc.



```python

```
