import streamlit as st
import requests

FASTAPI_URL = "http://fastcontainer:8000/track-experiment"


def main():
    st.title("MLflow Experiment Tracker")

    experiment_name = st.text_input("Enter Experiment Name", value="Experiment 01")    
    
    col1, col2= st.columns(2)
    with col1:
        param = st.text_input("Enter Parameter Name", value="Accuracy")  
    with col2:
        value = st.text_input("Enter Parameter Value", value=89)


    if st.button("Track Experiment", use_container_width=True):
        try:
            track_experiment(experiment_name, param, value)
            st.success("Experiment tracked successfully ✅")
        except:
            st.error('Failed to connect to FastAPI server', icon="🚨")
            st.write(experiment_name, param, value)

def track_experiment(experiment_name, param, value):
    payload = {
        "experiment_name": experiment_name,
        "param": param,
        "value": str(value),
    }
    response = requests.post(FASTAPI_URL, json=payload)

    if response.status_code == 200:
        st.success("Updated the Database ✅")
    else:
        st.error(f"Failed to track experiment. Server returned status code: {response.status_code}", icon="🚨")


if __name__ == "__main__":
    main()
