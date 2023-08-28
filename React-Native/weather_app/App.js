import { SafeAreaView, StatusBar, Text, View } from 'react-native'
import React, { Component } from 'react'
import Search from './screens/Search'
import Home from './screens/Home'
const App=()=> {
  return (
    <>
    <StatusBar barStyle="dark-content" backgroundColor="#00aaff" />
      <Search/>
        <Home/>
    </>
  );
};

export default App;
