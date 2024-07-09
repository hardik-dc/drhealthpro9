import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import numpy as np

class MrHealthPro:
    def __init__(self):
        # Load data
        self.diseases_df = pd.read_csv('diseases.csv')
        self.precautions_df = pd.read_csv('precautions.csv')
        
        # Prepare the vectorizer and model
        self.vectorizer = TfidfVectorizer()
        self.model = NearestNeighbors(n_neighbors=2)
        
        # Fit the model
        self._fit_model()
    
    def _fit_model(self):
        symptoms = self.diseases_df['symptoms']
        tfidf_matrix = self.vectorizer.fit_transform(symptoms)
        self.model.fit(tfidf_matrix)
    
    def predict(self, input_symptoms):
        input_tfidf = self.vectorizer.transform([input_symptoms])
        distances, indices = self.model.kneighbors(input_tfidf)
        
        if len(indices[0]) == 0:
            return []  # No predictions found
        
        predicted_diseases = self.diseases_df.iloc[indices[0]]['disease'].values
        
        predicted_precautions = []
        for disease in predicted_diseases:
            precautions = self.precautions_df[self.precautions_df['disease'] == disease]['precaution'].values
            if len(precautions) > 0:
                predicted_precautions.append(precautions[0])
            else:
                predicted_precautions.append("No specific precautions found.")
        
        return list(zip(predicted_diseases, predicted_precautions))
