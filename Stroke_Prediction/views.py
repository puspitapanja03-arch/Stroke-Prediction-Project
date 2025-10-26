from django.http import HttpRequest
from django.shortcuts import render
import pickle
from django.conf import settings
import os

model_path = os.path.join(settings.BASE_DIR,"rfc_model.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)

def home(request):
    message = None
    if request.method == 'POST':
        try: 
            gender= float(request.POST['gender'])
            age = int(request.POST['age'])
            hypertension = int(request.POST['hypertension'])
            heart_disease = int(request.POST['heart_disease'])
            ever_married=float(request.POST['ever_married'])
            work_type = float(request.POST['work_type'])
            Residence_type=float(request.POST['Residence_type'])
            avg_glucose_level=float(request.POST['avg_glucose_level'])
            bmi	=float(request.POST['bmi'])
            smoking_status=float(request.POST['smoking_status'])

            data = [[gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]]
            model_pred = model.predict(data)
            model_pred = int(model_pred[0])
            if model_pred == 1:
                message = "⚠️ High risk of stroke detected. Please consult a doctor."
            else:
                message = "✅ Low risk of stroke. Stay healthy!"
        except Exception as e:
            print("Error:", e)
            message = "Invalid input! Please check your entries and try again."
    context = {
     "result" : message
        }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")
def services(request):
    return render(request, "services.html")
