# Title :Job Acceptance Prediction System





## Introduction



&nbsp;Recruitment and placement teams handle large volumes of candidate data related to academic performance, technical skills, interview outcomes, and job market conditions. However, not all candidates who receive job offers accept them.This project aims to analyze candidate placement data and develop a machine learning–based Job Acceptance Prediction System that predicts whether a candidate will accept or reject a job offer.



#### Problem Statement



* Predict whether a candidate will accept or reject a job offer
* Identify key factors influencing job acceptance decisions
* Provide actionable insights to improve recruitment strategies





#### Data Understanding



* Dataset shape and size inspection
* Data type validation
* Sample record analysis
* Missing value distribution
* Target variable distribution

Placement distribution showed class imbalance with more rejected candidates than accepted candidates.





#### Data Cleaning \& Preprocessing



###### **Missing Value Handling**



* Numerical features filled using median values
* Categorical features filled using mode



###### **Data Consistency**



* Corrected inconsistent categorical labels
* Standardized text formatting



###### **Feature Encoding**



* Label Encoding for binary categorical variables
* One-Hot Encoding for multi-category features



###### **Feature Scaling**

* StandardScaler applied to numerical features to normalize data



###### **Logical Validation**

* Ensured realistic ranges for experience, scores, and salary





#### Exploratory Data Analysis (EDA)

EDA was performed to understand patterns and relationships:



* Interview score vs placement outcome
* Skills match percentage impact
* Company tier vs acceptance rate
* Experience vs placement probability
* Competition level impact
* Correlation analysis among numeric features





#### Feature Engineering



New features were created to improve model performance:



* Experience Category (Fresher / Junior / Senior)
* Academic Performance Bands
* Interview Average Score
* Skills Match Level
* Placement Probability Score



#### Data Storage(MYSQL)



* Table creation with appropriate data types
* Efficient querying for reporting
* Scalability for future integration



#### Machine Learning Modeling



Target variable

* Placed → 1 (Accepted)
* Not Placed → 0 (Rejected)



Model tested

* Logistic Regression
* Random Forest Classifier



Final Model Performance

* Accuracy: 88.25%
* Precision: 86%
* Recall: 73%
* F1-Score: 79%



#### Feature Importance Analysis- HR DECISION MAKING



* Skills Match Percentage
* Interview Scores
* Expected Salary
* Relevant Experience
* Company Tier
* Technical Score



#### Streamlit Dashboard - visualize analytics and predictions.



###### Dashboard Features



* Placement distribution charts
* Company tier analysis
* Interview performance visualization
* Skills impact analysis
* Real-time analytics insights



#### Business Insights



* Candidates with higher interview scores have significantly higher acceptance rates
* Skills match percentage is a strong predictor of placement success
* Higher expected salary mismatch increases dropout probability
* Experience level positively influences acceptance probability



#### Conclusion



The Job Acceptance Prediction System successfully predicts candidate job acceptance with high accuracy and provides actionable insights for HR teams. The integration of machine learning with analytics dashboards enables organizations to optimize recruitment strategies and reduce hiring inefficiencies.





































