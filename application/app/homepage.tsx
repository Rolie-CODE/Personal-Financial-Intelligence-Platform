import { withLayoutContext } from "expo-router";
import { View, Text, TextInput, TouchableOpacity } from "react-native";
import { Link } from "expo-router";


export default function home(){
    return(

        <View style  = {{backgroundColor: 'black'}}>
            <Link href = '/create_account'> Go to create account page </Link>
            <Text style = {{color: 'white'}} >
                Hello this is the homescreen
            </Text>
        </View>
    )
}