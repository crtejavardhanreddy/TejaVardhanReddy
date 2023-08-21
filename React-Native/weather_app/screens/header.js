import * as React from 'react';
import { Appbar,Title } from 'react-native-paper';
import {View,Text} from 'react-native'
export default Header = () => {

  return (
    <View>   <Appbar.Header
    theme={{
      colors:{
        primary:"#00aaff"
      }
    }}
    >
    style = {{flexDirection:"row",justifyContent:"center"}}
    <Title>
      Weather App
    </Title>
    </Appbar.Header>
    
    </View>
 );
};