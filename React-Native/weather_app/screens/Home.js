import React,{useState, useEffect} from 'react';
import { TextInput,Button, Card } from 'react-native-paper';
import {View,Text, FlatList} from 'react-native'
import Header from './Header'


const Home = ()=>{
    const [info, setInfo] = useState({
        name:"loading !!",
        temp:"loading",
        humidity:"loading",
        desc:"loading",
        icon:"loading"
    })
    useEffect(()=>{
        getWeather()
    },[])
    const getWeather = ()=>{
        fetch(`https://api.openweathermap.org/data/2.5/weather?q=london&APPID=bd0a3b4b5e256248422c752498db3b9b&units=metric`)
        .then(data=>data.json)
        .then(results=>{
            console.log(results)
        })
    }
    return(
        <View style={{flex:1}}>
            <Header name="weather app"/>
            <Text>Home </Text>
        </View>

    )
}

export default Home