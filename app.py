import streamlit as st
import requests
import pickle
import numpy as np
from PIL import Image

book_list = pickle.load(open('pivot.pkl','rb'))
book_list = book_list.index
similarity_score = pickle.load(open('similarity.pkl','rb'))
whole_book = pickle.load(open('whole_book_data.pkl','rb'))
top50 = pickle.load(open('top50.pkl','rb'))
top50_img = top50['Image-URL-M'].reset_index()
top50_img = top50_img['Image-URL-M']
top50_tit = top50['Book-Title'].reset_index()
top50_tit = top50_tit['Book-Title']
top50_auth = top50['Book-Author'].reset_index()
top50_auth = top50_auth['Book-Author']

image = Image.open('myimage.jpg')

st.title('Book Shelf')

st.sidebar.write('Built By -')
st.sidebar.title('Rishabh Vyas')
st.sidebar.image(image,caption='Machine Learning Engineer',width=160)
st.sidebar.write('E-mail - rishabhvyas472@gmail.com')

tab1,tab2= st.tabs(['Book Recommender','Top Books'])

 
def recomend(book_name):
    index_num = np.where(book_list == book_name)[0][0]
    similarity = similarity_score[index_num]
    sorted_score = sorted(list(enumerate(similarity)),key = lambda x:x[1],reverse=True)[1:7]
    
    
    title =[]
    author = []
    images =[]

    for i in sorted_score:
        title.append(book_list[i[0]])
        author.append(list(whole_book[whole_book['Book-Title']==book_list[i[0]]].drop_duplicates('Book-Title')['Book-Author'].values))
        images.append(list(whole_book[whole_book['Book-Title']==book_list[i[0]]].drop_duplicates('Book-Title')['Image-URL-M'].values))
            
        
    return title,author,images



with tab1:
    st.header('Book Recommender')

select_books = st.selectbox(
    'Selecte the book from the list or type name',
    book_list,index=0)

if st.button('Recommend'):
    st.header('These are the 5 books you would love to read')
    tit,auth,img = recomend(select_books)

    col1,col2,col3,col4,col5,col6 = st.columns(6,gap="small")

    with col1:
        st.image(img[0][0])
        st.write(tit[0])
        st.caption('Author:'+auth[0][0])

    with col2:
        st.image(img[1][0])
        st.write(tit[1])
        st.caption('Author:'+auth[1][0])

    with col3:
        st.image(img[2][0])
        st.write(tit[2])
        st.caption('Author:'+auth[2][0])

    with col4:
        st.image(img[3][0])
        st.write(tit[3])
        st.caption('Author:'+auth[3][0])

    with col5:
        st.image(img[4][0])
        st.write(tit[4])
        st.caption('Author:'+auth[4][0])
        
    with col6:
        st.image(img[5][0])
        st.write(tit[5])
        st.caption('Author:'+auth[5][0])

with tab2:
    st.header('Top 50 Books')

    col1, col2, col3, col4, col5 = st.columns(5, gap="small")

    with col1:
        st.image(top50_img[0])
        st.write(top50_tit[0])
        st.caption('Author:' + top50_auth[0])

    with col2:
        st.image(top50_img[1])
        st.write(top50_tit[1])
        st.caption('Author:' + top50_auth[1])

    with col3:
        st.image(top50_img[2])
        st.write(top50_tit[2])
        st.caption('Author:' + top50_auth[2])

    with col4:
        st.image(top50_img[3])
        st.write(top50_tit[3])
        st.caption('Author:' + top50_auth[3])

    with col5:
        st.image(top50_img[4])
        st.write(top50_tit[4])
        st.caption('Author:' + top50_auth[4])

    col6, col7, col8, col9, col10 = st.columns(5, gap="small")

    with col6:
        st.image(top50_img[5])
        st.write(top50_tit[5])
        st.caption('Author:' + top50_auth[5])

    with col7:
        st.image(top50_img[6])
        st.write(top50_tit[6])
        st.caption('Author:' + top50_auth[6])

    with col8:
        st.image(top50_img[7])
        st.write(top50_tit[7])
        st.caption('Author:' + top50_auth[7])

    with col9:
        st.image(top50_img[8])
        st.write(top50_tit[8])
        st.caption('Author:' + top50_auth[8])

    with col10:
        st.image(top50_img[9])
        st.write(top50_tit[9])
        st.caption('Author:' + top50_auth[9])

    # ------------------Second row--------------------#

    col11, col12, col13, col14, col15 = st.columns(5, gap="small")

    with col11:
        st.image(top50_img[10])
        st.write(top50_tit[10])
        st.caption('Author:' + top50_auth[10])

    with col12:
        st.image(top50_img[11])
        st.write(top50_tit[11])
        st.caption('Author:' + top50_auth[11])

    with col13:
        st.image(top50_img[12])
        st.write(top50_tit[12])
        st.caption('Author:' + top50_auth[12])

    with col14:
        st.image(top50_img[13])
        st.write(top50_tit[13])
        st.caption('Author:' + top50_auth[13])

    with col15:
        st.image(top50_img[14])
        st.write(top50_tit[14])
        st.caption('Author:' + top50_auth[14])

    col16, col17, col18, col19, col20 = st.columns(5, gap="small")

    with col16:
        st.image(top50_img[15])
        st.write(top50_tit[15])
        st.caption('Author:' + top50_auth[15])

    with col17:
        st.image(top50_img[16])
        st.write(top50_tit[16])
        st.caption('Author:' + top50_auth[16])

    with col18:
        st.image(top50_img[17])
        st.write(top50_tit[17])
        st.caption('Author:' + top50_auth[17])

    with col19:
        st.image(top50_img[18])
        st.write(top50_tit[18])
        st.caption('Author:' + top50_auth[18])

    with col20:
        st.image(top50_img[19])
        st.write(top50_tit[19])
        st.caption('Author:' + top50_auth[19])

        # -----------Third row---------------#

    col21, col22, col23, col24, col25 = st.columns(5, gap="small")

    with col21:
        st.image(top50_img[20])
        st.write(top50_tit[20])
        st.caption('Author:' + top50_auth[20])

    with col22:
        st.image(top50_img[21])
        st.write(top50_tit[21])
        st.caption('Author:' + top50_auth[21])

    with col23:
        st.image(top50_img[22])
        st.write(top50_tit[22])
        st.caption('Author:' + top50_auth[22])

    with col24:
        st.image(top50_img[23])
        st.write(top50_tit[23])
        st.caption('Author:' + top50_auth[23])

    with col25:
        st.image(top50_img[24])
        st.write(top50_tit[24])
        st.caption('Author:' + top50_auth[24])

    col26, col27, col28, col29, col30 = st.columns(5, gap="small")

    with col26:
        st.image(top50_img[25])
        st.write(top50_tit[25])
        st.caption('Author:' + top50_auth[25])

    with col27:
        st.image(top50_img[26])
        st.write(top50_tit[26])
        st.caption('Author:' + top50_auth[26])

    with col28:
        st.image(top50_img[27])
        st.write(top50_tit[27])
        st.caption('Author:' + top50_auth[27])

    with col29:
        st.image(top50_img[28])
        st.write(top50_tit[28])
        st.caption('Author:' + top50_auth[28])

    with col30:
        st.image(top50_img[29])
        st.write(top50_tit[29])
        st.caption('Author:' + top50_auth[29])

        # ---------Fourth Row------------#

    col31, col32, col33, col34, col35 = st.columns(5, gap="small")

    with col31:
        st.image(top50_img[30])
        st.write(top50_tit[30])
        st.caption('Author:' + top50_auth[30])

    with col32:
        st.image(top50_img[31])
        st.write(top50_tit[31])
        st.caption('Author:' + top50_auth[31])

    with col33:
        st.image(top50_img[32])
        st.write(top50_tit[32])
        st.caption('Author:' + top50_auth[32])

    with col34:
        st.image(top50_img[33])
        st.write(top50_tit[33])
        st.caption('Author:' + top50_auth[33])

    with col35:
        st.image(top50_img[34])
        st.write(top50_tit[34])
        st.caption('Author:' + top50_auth[34])

    col36, col37, col38, col39, col40 = st.columns(5, gap="small")

    with col36:
        st.image(top50_img[35])
        st.write(top50_tit[35])
        st.caption('Author:' + top50_auth[35])

    with col37:
        st.image(top50_img[36])
        st.write(top50_tit[36])
        st.caption('Author:' + top50_auth[36])

    with col38:
        st.image(top50_img[37])
        st.write(top50_tit[37])
        st.caption('Author:' + top50_auth[37])

    with col39:
        st.image(top50_img[38])
        st.write(top50_tit[38])
        st.caption('Author:' + top50_auth[38])

    with col40:
        st.image(top50_img[39])
        st.write(top50_tit[39])
        st.caption('Author:' + top50_auth[39])

        # -------------Fifth Row-----------#

    col41, col42, col43, col44, col45 = st.columns(5, gap="small")

    with col41:
        st.image(top50_img[40])
        st.write(top50_tit[40])
        st.caption('Author:' + top50_auth[40])

    with col42:
        st.image(top50_img[41])
        st.write(top50_tit[41])
        st.caption('Author:' + top50_auth[41])

    with col43:
        st.image(top50_img[42])
        st.write(top50_tit[42])
        st.caption('Author:' + top50_auth[42])

    with col44:
        st.image(top50_img[43])
        st.write(top50_tit[43])
        st.caption('Author:' + top50_auth[43])

    with col45:
        st.image(top50_img[44])
        st.write(top50_tit[44])
        st.caption('Author:' + top50_auth[44])

    col46, col47, col48, col49, col50 = st.columns(5, gap="small")

    with col46:
        st.image(top50_img[45])
        st.write(top50_tit[45])
        st.caption('Author:' + top50_auth[45])

    with col47:
        st.image(top50_img[46])
        st.write(top50_tit[46])
        st.caption('Author:' + top50_auth[46])

    with col48:
        st.image(top50_img[47])
        st.write(top50_tit[47])
        st.caption('Author:' + top50_auth[47])

    with col49:
        st.image(top50_img[48])
        st.write(top50_tit[48])
        st.caption('Author:' + top50_auth[48])

    with col50:
        st.image(top50_img[49])
        st.write(top50_tit[49])
        st.caption('Author:' + top50_auth[49])

            