def Check(sms_test):
  model = tensorflow.keras.models.load_model('LSTM.h5')
  tokenizer = pickle.load(open('tokenizer.pkl','rb'))
  sms_seq = tokenizer.texts_to_sequences([sms_test])

  sms_pad = pad_sequences(sms_seq, maxlen=20, padding='post')
  a=model.predict(sms_pad)
  if a > 0.7:
    return "Spam"
  else:
    return "Ham"