import os
import sys
import pandas as pd
from src.Kidney.logger import logging
from src.Kidney.utils.utils import load_object
from src.Kidney.exception import customexception

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path=os.path.join("Artifacts","preprocessor.pkl")
            model_path=os.path.join("Artifacts","model.pkl")
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            scaled_data=preprocessor.transform(features)
            pred=model.predict(scaled_data)
            return pred

        except Exception as e:
            raise customexception(e,sys)
    
class CustomData:
    def __init__(self,
                 age:int,
                 blood_pressure:int,
                 specific_gravity:int,
                 albumin:int,
                 sugar:int,
                 red_blood_cells:int,
                 pus_cell:int,
                 pus_cell_clumps:int,
                 bacteria:int,
                 blood_glucose_random:float,
                 blood_urea:int,
                 serum_creatinine:int,
                 sodium:int,
                 potassium:int,
                 haemoglobin:int,
                 packed_cell_volume:int,
                 white_blood_cell_count:int,
                 red_blood_cell_count:int,
                 hypertension:int,
                 diabetes_mellitus:int,
                 coronary_artery_disease:int,
                 appetite:int,
                 peda_edema:int,
                 aanemia:int
                 ):
        
        self.age = age
        self.blood_pressure = blood_pressure
        self.specific_gravity = specific_gravity
        self.albumin = albumin
        self.sugar = sugar
        self.red_blood_cells = red_blood_cells
        self.pus_cell = pus_cell
        self.pus_cell_clumps = pus_cell_clumps
        self.bacteria = bacteria
        self.blood_glucose_random = blood_glucose_random
        self.blood_urea = blood_urea
        self.serum_creatinine = serum_creatinine
        self.sodium=sodium
        self.potassium = potassium
        self.haemoglobin = haemoglobin
        self.packed_cell_volume = packed_cell_volume
        self.white_blood_cell_count = white_blood_cell_count
        self.red_blood_cell_count = red_blood_cell_count
        self.hypertension = hypertension
        self.diabetes_mellitus = diabetes_mellitus
        self.coronary_artery_disease = coronary_artery_disease
        self.appetite = appetite
        self.peda_edema = peda_edema
        self.aanemia = aanemia


            
                
    def get_data_as_dataframe(self):
            try:
                custom_data_input_dict = {
                    'age':[self.age],
                    'blood_pressure':[self.blood_pressure],
                    'specific_gravity':[self.specific_gravity],
                    'albumin':[self.albumin],
                    'sugar':[self.sugar],
                    'red_blood_cells':[self.red_blood_cells],
                    'pus_cell':[self.pus_cell],
                    'pus_cell_clumps':[self.pus_cell_clumps],
                    'bacteria':[self.bacteria],
                    'blood_glucose_random':[self.blood_glucose_random],
                    'blood_urea':[self.blood_urea],
                    'serum_creatinine':[self.serum_creatinine],
                    'sodium':[self.sodium],
                    'potassium':[self.potassium],
                    'haemoglobin':[self.haemoglobin],
                    'packed_cell_volume':[self.packed_cell_volume],
                    'white_blood_cell_count':[self.white_blood_cell_count],
                    'red_blood_cell_count':[self.red_blood_cell_count],
                    'hypertension':[self.hypertension],
                    'diabetes_mellitus':[self.diabetes_mellitus],
                    'coronary_artery_disease':[self.coronary_artery_disease],
                    'appetite':[self.appetite],
                    'peda_edema':[self.peda_edema],
                    'aanemia':[self.aanemia]

                }
                df = pd.DataFrame(custom_data_input_dict)
                print(df)
                logging.info('Dataframe Gathered')
                return df
            except Exception as e:
                logging.info('Exception Occured in prediction pipeline')
                raise customexception(e,sys)