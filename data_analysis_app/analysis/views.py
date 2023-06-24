import pandas as pd
from django.shortcuts import render
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# 
def analyze_data(request):
    if request.method == 'POST' and request.FILES['file']:
        # Open file selection dialog
        Tk().withdraw()
        file = request.FILES['file']
        df = pd.read_csv(file)

        # Perform data analysis and generate insights
        insights = {}

        # Number of rows and columns
        insights['Rows'] = df.shape[0]
        insights['Columns'] = df.shape[1]

        # Data types of columns
        insights['Data Types'] = df.dtypes.to_dict()

        # Summary statistics for numeric columns
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        insights['Summary Statistics'] = df[numeric_cols].describe().to_dict()

        # Unique values for categorical columns
        categorical_cols = df.select_dtypes(include=['object']).columns
        insights['Unique Values'] = {col: df[col].unique().tolist() for col in categorical_cols}

        # Correlation matrix for numeric columns
        correlation_matrix = df[numeric_cols].corr().to_dict()
        insights['Correlation Matrix'] = correlation_matrix

        # Perform additional analytics and generate recommendations based on the insights

        # Example recommendation: Identify missing values
        missing_values = df.isnull().sum().sum()
        if missing_values > 0:
            recommendations = "There are missing values in the dataset. Consider handling them appropriately."
        else:
            recommendations = "No missing values found in the dataset."

        context = {
            'insights': insights,
            'recommendations': recommendations
        }

        return render(request, 'analysis.html', context)

    return render(request, 'upload.html')
