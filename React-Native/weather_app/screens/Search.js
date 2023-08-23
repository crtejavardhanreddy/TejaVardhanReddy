import React,{useState} from 'react';
import { TextInput,Button } from 'react-native-paper';
import {View,Text} from 'react-native'
import Header from './header'

export default Search = () => {
  const [city,setCity] = useState('')
  return (
    <View style={{flex:1}}>
      <Header name= "Search Screen" />
      <TextInput 
        label = "city name"
        theme = {{colors:{primary:"#00aaff"}}}
        value = {city}
        onChangeText = {(text)=>setCity(text)}
      />
      <Button 
      icon="content-save" 
      mode="contained"
      theme = {{colors:{primary:"#00aaff"}}}
      style = {{margin:20}}
      onPress={() => console.log('Pressed')}>
        Press me
      </Button>
    </View>
  );
}

// export default Header;