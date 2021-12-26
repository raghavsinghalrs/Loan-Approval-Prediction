import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/a/Desktop/New folder/ML Projects/project/trained_model.sav','rb'))

def loan_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 0):
        return 'Loan is not approved'
    else:
        return 'Loan is approved' 


def main():

    st.title("Loan Status Prediction Web Application")
    st.header('built by Raghav Singhal')

    Gender = st.text_input("Enter the Gender? for male-> 0, for female->1")
    Married = st.text_input("Enter the Marital Status? for No->0, for Yes->1")
    Dependents = st.text_input("Enter Number of Dependends? for eg: 0->0.0, for 1->1.0 so on..")
    Education = st.text_input("Enter the education status? for graudated people->0, for not-graduated->1")
    Self_Employed = st.text_input("Self employment status? For no-> 0, for Yes->1")
    ApplicantIncome = st.text_input("Enter the Applicant's Income")
    CoapplicantIncome = st.text_input("Enter the Coapplicant's Income")
    LoanAmount = st.text_input("Enter the loan Amount in thousand")
    Credit_History = st.text_input("Enter the credit history? 0.0 or 1.0")
    Property_Area = st.text_input("Enter the type of property's area? for rural-> 0, for semi-urban->1 and for Urban->1")

    Status = ''    

    if st.button('Loan Status Result'):
        Status = loan_prediction([Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Credit_History, Property_Area])

    st.success(Status)



if __name__ == '__main__':
    main()

