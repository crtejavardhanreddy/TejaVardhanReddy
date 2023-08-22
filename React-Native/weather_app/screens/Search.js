import * as React from 'react';
import { Appbar,Title } from 'react-native-paper';
import {View,Text} from 'react-native'
import Header from './header'

export default Search = () => {

  return (
    <View
    style={{flex:1}}>
      <Header/>
      <Text>Search Screen</Text>
    </View>
  );
}

// export default Header;