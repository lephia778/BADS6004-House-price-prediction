# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 22:11:41 2019

@author: admin
"""

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

if __name__ == "__main__":
    # Create Session
    spark = SparkSession.builder.appName('PredictionHousePrice').master("local").enableHiveSupport().getOrCreate()
    spark.sparkContext.setLogLevel('WARN')
    
    # Load Data
    
    df = spark.sql("SELECT * FROM house_sales")
    
    # Machine learning
    # Vector Assembler
    vectorAssembler = VectorAssembler(inputCols = df.schema.names[1:-1], outputCol = 'features')
    assem_df = vectorAssembler.transform(df)
    assem_df = assem_df.select(['features', 'price'])
    
        
    # Train Test split
    train, test = assem_df.randomSplit([0.7, 0.3], seed=0)
        
    # Linear Regression
    lr = LinearRegression(featuresCol = 'features', labelCol='price')
    lr_model = lr.fit(train)
    
    # Coefficient
    print('------------------------------')
    print('Linear Regression Coefficients')
    print('------------------------------')
    for i, coeff in enumerate(lr_model.coefficients):
        print(df.columns[i+1], coeff)
        
    print("Intercept: " + str(lr_model.intercept))
    
    # Prediction
    predictions = lr_model.transform(test)
    
    # Evaluate
    evaluation_summary = lr_model.evaluate(test)
    print('------------------------------')
    print('Accuracy')
    print('RMSE: ',evaluation_summary.rootMeanSquaredError)
    print('R^2: ',round(evaluation_summary.r2,2))
    print('------------------------------')
    