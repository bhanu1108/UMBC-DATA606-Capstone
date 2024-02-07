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

# Target/Label in ML Model

In a machine learning model aimed at predicting the price of used cars, the target or label variable would typically be the "price" column. This is the variable that the model will attempt to predict based on the values of other variables.

# Features/Predictors for ML Models

As for the features or predictors, several variables from the dataset could be selected:
- Year of Registration: This variable indicates how old the car is, which often correlates with its price
- Mileage: The number of kilometers the car has been driven is an important indicator of its wear and tear and hence its value.
- Brand: Some brands are associated with higher resale values than others.
- Seller Type: Whether the seller is a private individual or a dealer can influence pricing.
- Not Repaired Damage: The presence of unrepaired damage can significantly impact the value of a used car.
