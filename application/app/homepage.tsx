import { withLayoutContext } from "expo-router";
import { View, Text, TextInput, TouchableOpacity } from "react-native";


export default function home(){
    return(
        <View style  = {{backgroundColor: 'black'}}>
            <Text style = {{color: 'white'}} >
                Hello this is the homescreen
            </Text>
        </View>
    )
}