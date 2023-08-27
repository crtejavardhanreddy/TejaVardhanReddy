import { SafeAreaView, StatusBar, Text, View } from 'react-native'
import React, { Component } from 'react'
import Search from './screens/Search'

const App=()=> {
  return (
    <>
    <StatusBar barStyle="dark-content" backgroundColor="#00aaff" />
      <Search/>

    </>
  );
};

export default App;
