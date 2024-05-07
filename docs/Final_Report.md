# 1. Title and Author

### Project Title: Predicting Used Car Prices

### Prepared for
UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang

### Author Name: Bhanusri Oleti

### Profiles and Presentations
- **GitHub Profile:** https://github.com/bhanu1108
- **Linkedin Profile:** http://linkedin.com/in/bhanu-sri-oleti-2bb328215
- **Presentation file:** https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/Final_ppt.pptx
- **Youtube Link:**

# 2. Background

### What is the Project about?

The purpose of this project is to offer a thorough understanding of the used car market dynamics. The dataset covers a wide range of variables that affect used car pricing and marketability, from technical details like power output and gearbox type to more arbitrary variables like fuel type and mileage. Through the analysis of this dataset, one can learn about market trends for used cars, comprehend the preferences of buyers, and help sellers maximize their pricing strategies.

### Why does it matter?

For a variety of stakeholders in the automotive industry, it is essential to comprehend the variables that influence used car pricing and sales. Understanding market trends can help sellers increase the effectiveness of their pricing strategies and boost sales. Making educated purchases can be facilitated for consumers by having a solid understanding of market dynamics. Researchers and analysts looking into consumer behavior, market trends, and pricing tactics in the automotive sector may also find this dataset useful.

### What are your research questions?

1. What are the main variables affecting the cost of used cars? What impact do factors like powerPS, brand, mileage, and registration year have on the price?
2. What effect does the type of gearbox have on used car prices and saleability?
3. Does the used car market follow any seasonal patterns? 
4. Is it possible to forecast the average cost of a used car using regression analysis based on its specifications and industry trends?
5. What impact does fuel type have on used car prices and marketability?



# 3. About Dataset

- **Data source:** [Used Cars Dataset](https://www.kaggle.com/datasets/thedevastator/uncovering-factors-that-affect-used-car-prices)
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

There are missing value in the dataset 

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

![5](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos4.png)

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

![12](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos11.png)

From the graph we can see that ads for the brands such as volkswagen, BMW, opel are highest in number so that these cars are the highest reselling cars. Ads for brands such as lada, trabant, rover are lowest in number suggesting that these are the least reselling cars.

**Top 10 Cars by Vehicle Type, Brand, and Model - Ads Count**

![13](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos12.png)

Here We can see that Sedan cars are the most reselling cars followed by small sedans, Estate cars, Buses etc. Volkswagen sedans are highest reselling cars folloed by Volkswagen small sedans, Opel small sedans etc.

# 5. Model Training

The primary objective of model training is to develop a predictive algorithm that accurately estimates the price of used cars based on their attributes. Through the utilization of machine learning methods, my aim is to discover patterns within the dataset, enabling the development of a model that can make dependable predictions. 
- The machine learning algorithms used for this predictions are Linear Regression, Random Forest and Gradient Booster.

### 1. Data Preprocessing

**Encoding Categorical Variables:**
The categorical variables 'brand' and 'fuelType' are encoded using the LabelEncoder from the sklearn.preprocessing module. This step assigns numerical labels to each unique category in the categorical variables. The 'brand' variable is encoded using fit_transform method of LabelEncoder, which fits the encoder to the 'brand' column and transforms it into numerical labels.
The mapping of original categories to numerical labels is stored in the brands dictionary for future reference.

**Mapping Ordinal Variable:**
The 'gearbox' variable, which represents the type of gearbox (manual or automatic), is mapped to numerical values using a predefined dictionary gearbox where 'manual' is mapped to 0 and 'automatic' is mapped to 1.
Similarly, the 'fuelType' variable is mapped using a predefined dictionary fuel where 'benzin', 'diesel', and 'lpg' are mapped to 0, 1, and 2 respectively.

**Feature Selection:**
The selected features for training the model are assigned to the variable X, which includes 'yearOfRegistration', 'powerPS', 'kilometer', 'monthOfRegistration', and the encoded 'brand'.
'yearOfRegistration', 'powerPS', 'kilometer', and 'monthOfRegistration' represent numerical features.
'brand' represents the encoded categorical feature.

**Target Variable Selection:**
The target variable 'price' is assigned to the variable y, representing the prices of the used cars.

**Printing Preprocessed Data:**
Finally, the preprocessed feature matrix X and the target variable y are printed to verify the data before training the model.

### 2. Model Building

**Data Splitting:**
The dataset is split into training and testing sets using the train_test_split function from sklearn.model_selection. The features X and the target variable y are split into X_train, X_test, y_train, and y_test, with a test size of 20% and a specified random state for reproducibility. 

**Model Training:**
Machine Learning models are built by using sklearn module and models are trained on the training data (X_train, y_train) using the fit method, which learns the relationships between the features and the target variable.

### 3. Model Evaluation

**Prediction:**
The trained model is used to make predictions on the test data X_test using the predict method. The predicted values are stored in y_pred.

**Evaluation Metrics:**
Three evaluation metrics are computed to assess the performance of the model:
- Mean Absolute Error (MAE): It measures the average absolute difference between the predicted and actual values.
- Mean Squared Error (MSE): It measures the average squared difference between the predicted and actual values.
- R-squared Score (R2): It indicates the proportion of the variance in the target variable that is explained by the model. It ranges from 0 to 1, where a higher value indicates a better fit.

## Results

**Linear Regression:**
- Mean Absolute Error: 2235.57
- Mean Squared Error: 11301011.58
- R-squared: 0.63

**Random Forest:**
- Mean Absolute Error: 1092.74
- Mean Squared Error: 4079283.74
- R-squared: 0.87

**Gradient Booster:**
- Mean Absolute Error: 1266.07
- Mean Squared Error: 4842543.72
- R-squared: 0.84

From the evaluation metrics, we can say that Random Forest has the lowest Mean Absolute Error (MAE) and Mean Squared Error (MSE), indicating better accuracy in predicting the target variable compared to the other models.

Random Forest also has the highest R-squared value, suggesting that it explains a larger portion of the variance in the dependent variable compared to the other models.

Therefore, based on the provided metrics, the Random Forest model appears to be the best among the three for this particular prediction tasks. It offers the lowest errors and the highest R-squared value, indicating better performance in terms of accuracy and explanatory power.

So We can choose Random Forest Regression algorithm for the price prediction of used cars.

# 6. Application of the Trained Models

Creating a web application with Flask to forecast used car prices using a Random Forest Regression model follows several steps. 
- Initially, it involves setting up routes in Flask to manage incoming requests and render HTML templates. 
- Within the prediction page route, a form is designed for users to input car details. 
- Upon form submission, Flask processes the data, feeding it into the trained Random Forest Regression model to predict the car's price. 
- The predicted price is then presented to the user on a results page. It's crucial to preprocess the input data consistently with the model's training preprocessing to ensure compatibility. 
- Finally, deploying the Flask app on a web server enables remote access, extending the predictive functionality to a broader audience. Flask simplifies the integration of machine learning models into web apps, facilitating their efficient deployment and usage in practical scenarios.

![14](https://github.com/bhanu1108/UMBC-DATA606-Capstone/blob/main/docs/autos14.png)

# 7. Conclusion

In conclusion, this project demonstrates the effective fusion of machine learning with web development using Flask, with a focus on predicting used car prices based on crucial features like registration year, gearbox type, power output, mileage, registration month, fuel type, and brand. Upon assessing the predictive performance of Linear Regression, Random Forest, and Gradient Boosting models, it's clear that Random Forest stands out for its superior accuracy. Utilizing a Random Forest Regression model, the application delivers precise price predictions, empowering users to make well-informed decisions within the ever-changing used car market.

## Limitations

- **Market Dynamics:** Factors outside the model's scope, such as economic shifts and regulatory alterations, can impact the used car market, thereby influencing the accuracy of model predictions.
- **Model Complexity:** Although Random Forest and Gradient Boosting models achieve superior predictive accuracy, they entail greater computational complexity and resource demands compared to simpler models like Linear Regression. Implementing and managing such intricate models in production settings can present logistical challenges.
- **Scalability:** As the dataset expands, the training and inference durations for advanced models like Random Forest and Gradient Boosting could become impractical. It's essential to account for scalability concerns to guarantee the viability of deploying these models in real-world scenarios.
- **Limited Scope:** The dataset might not encompass all relevant factors affecting used car prices. Variables like vehicle condition, maintenance records, and local market trends could exert substantial influence on prices yet may not be represented in the dataset.
- **Feature Selection:** The effectiveness of the model depends on the inclusion of pertinent features. Omitting crucial features or incorporating irrelevant ones can affect the accuracy of predictions.

## Lessons Learned

- **Data Quality is Primary:** The effectiveness of predictive modeling relies significantly on the quality of the data utilized. Allocating adequate resources to activities like data cleansing, preprocessing, and validation is imperative to guarantee the data's accuracy and dependability. This is essential for creating models that are trustworthy and capable of generating precise predictions.
- **Model Evaluation is Essential:** Thoroughly assessing model performance using suitable metrics is essential to gauge predictive accuracy and the ability to generalize. This evaluation offers valuable insights into the model's strengths, weaknesses, and areas that require enhancement.
- **Continuous Model Refinement:** Model development involves an ongoing iterative process. Iteratively refining and optimizing models through feedback, incorporation of new data, and adaptation to evolving requirements enhances their efficacy and applicability over time.
- **Learning from Failures:** Failures are an intrinsic aspect of the modeling journey. Embracing these setbacks as chances for learning, iterating on errors, and consistently striving for enhancement fosters progress and innovation in predictive modeling pursuits.

## Future Scope

- **Integration of Additional Data Sources:**  Incorporating the dataset with supplementary sources like vehicle history reports, market trends, and consumer sentiment can bolster the predictive capability of the models. Utilizing real-time data streams and advanced data integration methods enables a deeper understanding of pricing dynamics, enhancing the overall predictive insights.
- **Advanced Feature Engineering:** Delving into sophisticated feature engineering methods, such as text mining to extract insights from unstructured data (like vehicle descriptions and user reviews) and image processing for analyzing vehicle images, can enrich the dataset and enhance model precision.
- **Deployment in E-Commerce Platforms:** Integrating predictive pricing models into e-commerce platforms and online marketplaces enables sellers to make well-informed pricing decisions promptly. Delivering pricing recommendations and insights directly within the selling interface simplifies the pricing procedure and improves user satisfaction.
- **User Integration with Blockchain Technology:** Utilizing blockchain technology to establish transparent and immutable records of vehicle history, ownership, and transactions has the potential to boost trust and transparency within the used car market.

# References

-Hao, J., & Ho, T. K. (2019). Machine Learning Made Easy: A Review of Scikit-learn Package in Python Programming Language. Educational and Psychological Measurement, 44(3). https://doi.org/10.3102/1076998619832248

-Zhu, Y. (2023). Prediction of the price of used cars based on machine learning algorithms. Applied and Computational Engineering, 6(1), 785-791. https://doi.org/10.54254/2755-2721/6/20230917

-Hunt-Walker, N. (2018, April). An introduction to the Flask Python web app framework. Opensource.com. https://opensource.com/article/18/4/flask




```python

```
