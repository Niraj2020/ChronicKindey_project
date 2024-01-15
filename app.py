from flask import Flask, request, render_template
from src.Kidney.pipeline.Prediction_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

# Define the home route

@app.route("/",methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    
    else:
        data=CustomData (   
            age=(request.form.get("age")),
            blood_pressure=(request.form.get("blood_pressure")),
            specific_gravity=(request.form.get("specific_gravity")),
            albumin=(request.form.get("albumin")),
            sugar=(request.form.get("sugar")),
            red_blood_cells=(request.form.get("red_blood_cells")),
            pus_cell = (request.form.get("pus_cell")),
            pus_cell_clumps = (request.form.get("pus_cell_clumps")),
            bacteria = (request.form.get("bacteria")),
            blood_glucose_random = (request.form.get("blood_glucose_random")),
            blood_urea = (request.form.get("blood_urea")),
            serum_creatinine = (request.form.get("serum_creatinine")),
            sodium = (request.form.get("sodium")),
            potassium = (request.form.get("potassium")),
            haemoglobin = (request.form.get("haemoglobin")),
            packed_cell_volume = int(request.form.get("packed_cell_volume")),
            white_blood_cell_count = int(request.form.get("white_blood_cell_count")),
            red_blood_cell_count = int(request.form.get("red_blood_cell_count")),
            hypertension = int(request.form.get("hypertension")),
            diabetes_mellitus = int(request.form.get("diabetes_mellitus")),
            coronary_artery_disease = int(request.form.get("coronary_artery_disease")),
            appetite = int(request.form.get("appetite")),
            peda_edema	 = int(request.form.get("peda_edema")),
            aanemia = int(request.form.get("aanemia")))
            
            
            
            
            
        # this is my final data
        final_data=data.get_data_as_dataframe()
        
        predict_pipeline=PredictPipeline()
        
        pred=predict_pipeline.predict(final_data)
        
        result=round(pred[0],2)
        #if pred[0]==1:
                #result ='Person is not Healthy as suffering with Kidney Disease'
                
        #else:
               # result='Person is Healthy, Do not have Kidney Disease'
        
        return render_template("result.html",final_result=result)

#execution begin
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)           