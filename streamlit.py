import streamlit as st
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img,img_to_array

import numpy as np
from keras.models import load_model

model = load_model('C://Users//sudhir//Desktop//project birds//model.h5',compile=False)
lab = {0: 'ALEXANDRINE PARAKEET', 1: 'BALD EAGLE', 2: 'CROW', 3: 'DARJEELING WOODPECKER' ,4: 'EMPEROR PENGUIN', 5: 'GOLDEN PIPIT' ,6: 'HIMALAYAN MONAL', 7:'INDIAN PITTA', 8:'KIWI', 9: 'MYNA',10:'NICOBAR PIGEON',11:'OVENBIRD',12:'PINK ROBIN',13:'ROYAL FLYCATCHER',14:'STRIPPED SWALLOW',15:'TURKEY VULTURE',16:'YELLOW HEADED BLACKBIRD'}
def processed_img(img_path):

    img=load_img(img_path,target_size=(224,224,3))
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    answer=model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int
    res = lab[y]
    print(res)
    return res

def run():
    img1 = Image.open('C://Users//sudhir//Desktop//project birds//logo1.png')
    img1 = img1.resize((350,350))
    st.image(img1,use_column_width=False)
    st.title("Birds Species Classification")
    st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>* Data is based "270 Bird Species also see 70 Sports Dataset"</h4>''',
                unsafe_allow_html=True)

    img_file = st.file_uploader("Choose an Image of Bird", type=["jpg", "png"])
    if img_file is not None:
        st.image(img_file,use_column_width=False)
        save_image_path = 'C://Users//sudhir//Desktop//project birds//uploads'+img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        if st.button("Predict"):
            result = processed_img(save_image_path)
            st.success("Predicted Bird is: "+result)
run()