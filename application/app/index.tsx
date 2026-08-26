import {View, Text, TextInput, TouchableOpacity} from 'react-native'


export default function Sign_Up(){
    return (
        <View>
            <View>
                <Text>
                    Lock
                </Text>

                <Text>
                    Sign In 
                </Text>
            </View>

            <View>
                <Text>
                    Account Name
                </Text>

                <TextInput
                placeholder='AccountName'>
                </TextInput>
            </View>

            <View>
                <Text>
                    Password
                </Text>

                <TextInput
                placeholder='.......'>
                </TextInput>
            </View>

            <TouchableOpacity>
                <Text style={{color: 'white'}}>
                    Sign In
                </Text>
            </TouchableOpacity>

            <View>
                <Text>
                    Forgot Password?
                </Text>

                <View>
                    <Text>
                        No account?
                    </Text>

                    <Text>
                        Sign Up!
                    </Text>
                </View>
            </View>
        </View>
    )
}