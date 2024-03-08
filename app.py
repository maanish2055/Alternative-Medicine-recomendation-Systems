# import streamlit as st
# import pickle
# import pandas as pd


#                                         ## To Add External CSS ##
# with open('css/style.css') as f:
#      st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)




#                                         ## Application Backend ##

#                     # To load medicine-dataframe from pickle in the form of dictionary
# medicines_dict = pickle.load(open('medicine_dict.pkl','rb'))
# medicines = pd.DataFrame(medicines_dict)

# #                     # To load similarity-vector-data from pickle in the form of dictionary
# similarity = pickle.load(open('similarity.pkl','rb'))

# def recommend(medicine):
#      medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
#      distances = similarity[medicine_index]
#      medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

#      recommended_medicines = []
#      for i in medicines_list:
#          recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
#      return recommended_medicines





#                                     # Appliaction Frontend ##

#                                    # Title of the Application
# st.title('Medicine Recommender System')

#                                         # Searchbox




# selected_medicine_name = st.selectbox(
# 'WARNING: Please consult your physician or show the proof of prescription before purchasing the recommended alternative medicine.',
#    medicines['Drug_Name'].values)



#                                    # Recommendation Program
# if st.button('Recommend Medicine'):
#      recommendations = recommend(selected_medicine_name)
#      j=1
#      for i in recommendations:
#           st.write(j,i)                      # Recommended-drug-name
#           # st.write("Click here -> "+" https://www.netmeds.com/catalogsearch/result?q="+i) # Recommnded drug purchase link from netmeds
#           # st.write("Click here -> "+" https://pharmeasy.in/search/all?name="+i) # Recommnded-drug purchase link from pharmeasy
#           j+=1



# #                                          ## Image load ##
# from PIL import Image
# image = Image.open('images/medicine-image.jpg')
# st.image(image, caption='Recommended Medicines')
































import streamlit as st
import pickle
import pandas as pd

# Load medicine dataframe from pickle
medicines_dict = pickle.load(open('medicine_dict.pkl','rb'))
medicines = pd.DataFrame(medicines_dict)

# Load similarity data from pickle
similarity = pickle.load(open('similarity.pkl','rb'))

# Function to recommend similar medicines
def recommend(medicine):
    medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_medicines = []
    for i in medicines_list:
        recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
    return recommended_medicines

# Application Frontend
def app():
    # Title of the Application
    st.title('Medicine Recommender System')

    # Searchbox with autocomplete suggestions
    entered_medicine = st.text_input("Enter the medicine name")

    # Generate list of medicine names for autocomplete
    medicine_list = medicines['Drug_Name'].values.tolist()

    # Check if entered medicine is in the dataset
    if entered_medicine:
        filtered_medicines = [medicine for medicine in medicine_list if entered_medicine.lower() in medicine.lower()]
        if filtered_medicines:
            selected_medicine_name = st.selectbox(
                'Select the medicine name',
                [entered_medicine] + filtered_medicines
            )
        else:
            st.error("Medicine not found. Please enter a valid medicine name.")
            selected_medicine_name = None
    else:
        selected_medicine_name = None

    # Recommendation Program
    if selected_medicine_name is not None and st.button('Recommend Medicine'):
        recommendations = recommend(selected_medicine_name)
        if recommendations:
            st.subheader("Recommended Medicines:")
            for i, recommendation in enumerate(recommendations, 1):
                st.write(f"{i}. {recommendation}")
        else:
            st.write("No recommendations found for the selected medicine.")



if __name__ == '__main__':
  
    app()
from PIL import Image
image = Image.open('images/medicine-image.jpg')
st.image(image, caption='Recommended Medicines')
