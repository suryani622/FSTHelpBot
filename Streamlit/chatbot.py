import streamlit as st
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import random
import time
from PIL import Image

def app():
    
    with open("style.css") as f:
     st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)   
    
    col3, col4 = st.columns(2)

    with col3:
        image = Image.open('bot kiyowo.png') #di bagian sini, bisa tambahkan foto/ilustrasi chatbot
        st.image(image, use_column_width=True)

    with col4:
        
        st.write('''
        # 
        ##### Selamat Datang!
        ''')

        paragraph4 = 'Temui FSTHelpBot yang siap membantu Anda dengan informasi terkait prosedur layanan administrasi akademik yang tersedia melalui halaman Seminar-FST. FSTHelpBot dapat memberikan panduan dan jawaban yang Anda butuhkan. Silahkan tulis pertanyaan Anda lalu tekan Enter'

        st.markdown(f'<div style="text-align: justify;">{paragraph4}</div>', unsafe_allow_html=True)
        st.write("")
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Load encoder decoder models
    encoder_model = load_model('encoder_model.h5')
    decoder_model = load_model('decoder_model.h5')

    encoder_model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001),loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    decoder_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


    # Load tokenizer from tokenizer.pkl
    with open('tokenizer.pkl', 'rb') as file:
        tokenizer = pickle.load(file)

    # Max length ques and ans
    maxlen_questions = 100
    maxlen_answers = 100

    def str_to_tokens(sentences):
        words = sentences.lower().split()
        token_list = [tokenizer.word_index.get(word, 0) for word in words]
        return pad_sequences([token_list], maxlen=maxlen_questions, padding='post')

    def chatbot_inference(input_text):
        sampled_word = None
        states_values = encoder_model.predict(str_to_tokens(input_text))
        empty_target_seq = np.zeros((1, 1))
        empty_target_seq[0, 0] = tokenizer.word_index['start']
        stop_condition = False
        decoded_translation = ''

        while not stop_condition:
            sampled_word = None
            dec_outputs, h, c = decoder_model.predict([empty_target_seq] + states_values)
            sampled_word_index = np.argmax(dec_outputs[0, -1, :])

            for word, index in tokenizer.word_index.items():
                if sampled_word_index == index:
                    if word != 'end':
                        decoded_translation += f'{word} '
                    sampled_word = word

            if sampled_word == 'end' or len(decoded_translation.split()) > maxlen_answers:
                stop_condition = True

            empty_target_seq = np.zeros((1, 1))
            empty_target_seq[0, 0] = sampled_word_index
            states_values = [h, c]

        return decoded_translation

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    #Tampilkan chat input
    st.markdown('<div class="chat-input-container">', unsafe_allow_html=True)

    if prompt := st.chat_input("You: "):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("User"):
            st.markdown(prompt)
        with st.chat_message("Bot"):
            message_placeholder = st.empty()
            
            response = chatbot_inference(prompt)
            full_response = ""

            # Simulate stream of response with milliseconds delay
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)

                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    st.markdown('</div>', unsafe_allow_html=True)
