import joblib

preprocessor = joblib.load("models/preprocessor.pkl")

print(type(preprocessor))
print(preprocessor)