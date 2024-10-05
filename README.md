# Campus Placement Prediction

## Overview
This project aims to predict whether a student will be placed in a company based on various academic and personal factors. By analyzing historical data, the model identifies patterns and trends that can influence campus placement decisions, providing valuable insights for students and educational institutions.

## Objective
To develop a machine learning model that predicts the likelihood of a student securing campus placement using academic performance, test scores, and other relevant features.

## Dataset
The dataset used for this project includes the following features:
- **Gender**: Male/Female
- **S.S.C. Percentage**: Secondary Education (10th Grade) percentage
- **H.S.C. Percentage**: Higher Secondary Education (12th Grade) percentage
- **Specialization**: Stream in HSC (Science/Commerce/Arts)
- **Degree Percentage**: Undergraduate academic performance
- **E-test Score**: Employability test score
- **MBA Percentage**: Post-graduation (MBA) academic performance
- **Work Experience**: Whether the student has prior work experience
- **Status**: Placement status (Placed/Not Placed)

## Approach
1. **Data Preprocessing**: The data was cleaned and preprocessed, handling missing values and encoding categorical variables.
   
2. **Exploratory Data Analysis (EDA)**: Key insights were derived from the dataset through visualization, identifying the most influential factors in campus placement.
   
3. **Model Development**: Multiple machine learning algorithms were implemented and evaluated, including:
   - **Logistic Regression**
   - **Random Forest**
   - **Support Vector Machine (SVM)**
   - **K-Nearest Neighbors (KNN)**
   
4. **Model Evaluation**: The performance of the models was compared using metrics such as accuracy, precision, recall, and F1-score.

## Results
The Logistic Regression provided the highest accuracy in predicting campus placements, outperforming other models in key metrics.

## Tools & Technologies
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **Platform**: Jupyter Notebook

## Conclusion
The project successfully demonstrated how machine learning can be applied to predict campus placement outcomes based on students' academic and personal profiles. The model offers actionable insights for students to enhance their placement potential and for institutions to guide their placement preparation strategies.

## Future Work
- Improve model accuracy by incorporating additional features such as extracurricular activities and internship experiences.
- Implement a web-based interface for easy access and prediction.
