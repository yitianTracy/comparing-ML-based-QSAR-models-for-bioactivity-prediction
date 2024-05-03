# Comparing ML-based QSAR models for bioactivity prediction
- Group 15 Machine Learning Project 

To reproduce the project result, you should follow the steps as below:
1. Run the "Data.ipynb" file to extract data from ChemBL database, the extracted data is also provided under the "data" folder called "CHEMBI_active.csv".
2. Run the "FP_conversion_PCA.ipynb" file to convert the data into 2048-digit fingerprint. PCA is also included in this file to reduce the fingerprint dimensionality. The PCA-reduced data is also provided under the the "data" folder called "outlier_cleaned.csv".
3. Run the "Linear_Regression.ipynb" for construction of our ridge regression model and its results display.
4. Run the "kNN.ipynb" for knn model and its result visualization.
5. Run the "Random_Forest.ipynb" to do grid serach in cross validation of random forest model, and the prediction of the random forest regression model with best parameters.
6. Run the "draw_models_evaluation.py" to generate the figure that comparing the model perfomances from 4 evaluation metrics.

The "Result" folder stores the figures we made for each model, which are also included in the poster and final essay.
