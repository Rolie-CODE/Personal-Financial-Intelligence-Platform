import { View, Text, TextInput, TouchableOpacity } from "react-native";
import MaterialCommunityIcons from '@expo/vector-icons/MaterialCommunityIcons';



export default function create_account() {

    return (

        <View>
            <View>
                <MaterialCommunityIcons name="account" size={24} color="black" />
                <Text>
                    Create Account
                </Text>
            </View>

            <View>
                <Text>
                    Account Name
                </Text>
                <TextInput placeholder="yourname">

                </TextInput>
            </View>

            <View>
                <Text>
                    Email
                </Text>
                <TextInput placeholder="you@email.com">

                </TextInput>
            </View>

            <View>
                <Text>
                    Password
                </Text>
                <TextInput placeholder="......">

                </TextInput>
            </View>

            <View>
                <Text>
                    Confirm Password
                </Text>
                <TextInput placeholder=".......">

                </TextInput>
            </View>

            <TouchableOpacity>
                <Text>
                    Sign Up
                </Text>
            </TouchableOpacity>

            <View style = {{}}>
                <Text>
                    Already have an account?
                </Text>

                <Text>
                    Sign In
                </Text>
            </View>
        </View>

    )
}