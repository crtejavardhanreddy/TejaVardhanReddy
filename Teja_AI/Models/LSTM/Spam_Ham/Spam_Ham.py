# importing the Required libraries
import pandas as pd
import tensorflow
import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding

# Reading the CSV Data
df = pd.read_csv('Spam.csv',header=0,encoding='latin1')
df = df[['Label','Message']]

df['target'] = df['Label'].map( {'spam':1, 'ham':0 })

# Splitting into training and testing part
df_train = df.sample(frac=.8, random_state=11)
df_test = df.drop(df_train.index)

y_train = df_train['target'].values
y_test = df_test['target'].values
X_train = df_train['Message'].values
X_test = df_test['Message'].values

# Tokenizing the data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
pickle.dump(tokenizer,open('tokenizer.pkl','wb'))
word_dict = tokenizer.index_word
X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

# Padding the sequence
X_train_pad = pad_sequences(X_train_seq, maxlen=20, padding='post')
X_test_pad = pad_sequences(X_test_seq, maxlen=20, padding='post')

# Model building
Padding_length = 20
anz_woerter = 7982

lstm_model = Sequential()
lstm_model.add(Embedding(input_dim=anz_woerter+1, output_dim=20, input_length=Padding_length))
lstm_model.add(LSTM(400))
lstm_model.add(Dense(1, activation='sigmoid'))

# Model Compiling
lstm_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
lstm_model.summary()

# Model Saving
lstm_model.save("LSTM.h5")

# Training and validating the model
history = lstm_model.fit(X_train_pad, y_train, epochs=10, batch_size=64,
                        validation_data=(X_test_pad, y_test))