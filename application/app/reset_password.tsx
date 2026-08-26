import { View, Text, TextInput, TouchableOpacity } from "react-native";
import FontAwesome5 from '@expo/vector-icons/FontAwesome5';

export default function reset_password(){

    return(

        <View>
            <View>
                <FontAwesome5 name="key" size={24} color="black" />

                <Text>
                    Reset Password
                </Text>
            </View>

            <View>
                <Text>
                    Confirm your account and email, then set a new password
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
                <TextInput placeholder="........">

                </TextInput>
            </View>

            <View>
                <Text>
                    New Password
                </Text>
                <TextInput placeholder="..........">

                </TextInput>
            </View>

            <View>
                <Text>
                    Confirm New Password
                </Text>
                <TextInput placeholder="..........">

                </TextInput>
            </View>

            <TouchableOpacity>
                <Text>
                    Reset Password
                </Text>
            </TouchableOpacity>

            <Text>
                Back to sign in
            </Text>
        </View>

    )

}