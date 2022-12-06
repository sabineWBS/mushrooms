import streamlit as st
import pandas as pd
# from files_to_update.students import students
from src.pd_functions import *

# path to results
RESULTS_PATH = 'data/results.csv'

# introduce participant name
text_input_container = st.empty()
text_input_container.text_input(
    "Introduce participant name: ",
    key="text_input"
)
if st.session_state.text_input != "":
    # if st.session_state.text_input in students:
    text_input_container.empty()
    st.info('Participant name ' + st.session_state.text_input)

    # upload results file
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None and st.session_state.text_input != "":
        try:
            # prepare test file
            test = get_ready_test(RESULTS_PATH, uploaded_file)

            # get participant accuracy and prepare data for leaderboard
            participant_results = get_metrics(RESULTS_PATH, test)

            st.success('Dataframe uploaded successfully!')
            # print participant results
            st.title('Participant results')
            st.dataframe(participant_results)

            # update all submissions
            try:
                update_submissions(participant_results)
                # plot_submissions(st.session_state.text_input)
            except:
                participant_results.to_pickle(
                    'files_to_update/submissions.pkl')

        except:
            st.error(
                'The file has a wrong format, please, review it and load it again.')

    # else:
    #     st.error("Please, introduce the your correct student name.")

try:
    show_leaderboard()
except:
    st.write("There are no submissions yet.")
