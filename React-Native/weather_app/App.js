import { SafeAreaView, StatusBar, Text, View } from 'react-native'
import React, { Component } from 'react'
import Search from './screens/Search'

export default class App extends Component {
  render() {
    return (
      <SafeAreaView>
        <StatusBar barStyle="dark-content" backgroundColor="#00aaff"/>
        <Text>Weather App</Text>
        <Search/>
      </SafeAreaView>
    )
  }
}