import { View, Text, StatusBar, SafeAreaView } from 'react-native'
import React from 'react'
import Search from './screens/Search'
import { SafeAreaProvider } from 'react-native-safe-area-context';
import  Header  from './screens/header';

export default function App() {
  return (
    <SafeAreaProvider>
    <SafeAreaView>
      <StatusBar barStyle="dark-content" backgroundColor="#00aaff"/>
      <Text>Hello Text</Text>
      <Header/>
    </SafeAreaView>
    </SafeAreaProvider>
  )
}