import streamlit as st
import pickle
lin_model=pickle.load(open('lin_model.pkl','rb'))
log_model=pickle.load(open('log_model.pkl','rb'))
svc_model=pickle.load(open('svc_model.pkl','rb'))
def classify(num):
  if num<=0.5:
    return 'Setosa'
  elif num<1.5:
    return 'Versicolar'
  else:  
    return 'Virginica'
def main():
  st.title("species classifier")
  activities=['Linear Regression','Logistic Regression','SVM']
  option=st.sidebar.selectionbox('which model would you like to choose',activities)
  st.subheader(option)
  st.spinner("hello")
  sl=st.slider('Select Sepal Length',0.0,10.0)
  sw=st.slider('Select Sepal Width',0.0,10.0)
  pl=st.slider('Select Petal Length',0.0,10.0)
  pw=st.slider('Select Petal Width',0.0,10.0)
  inputs=[[sl,sw,pl,pw]]
  if st.button('Classify'):
    if option=='Linear Regression':
      st.success(classify((lin_model.predict(inputs))))
    elif option=='Logistic Regression':
      st.success(classify((log_model.predict(inputs))))
    else:
      st.success(classify((svc_model.predict(inputs))))
  if __name__=='__main__':
    main()
