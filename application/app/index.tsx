import { View, Text, TextInput, TouchableOpacity } from "react-native";
import FontAwesome from '@expo/vector-icons/FontAwesome';

export default function Sign_Up() {
  return (
    <View style={{}}>
      <View style = {{alignItems: 'center', gap: '40'}}>
        <View style= {{alignItems: 'center', marginTop: 20}}>
            <FontAwesome name="lock" size={44} color="#0096C7" />
        </View>

        <Text style = {{color:'white', fontWeight: 'bold', fontSize: '34'}}>Sign In</Text>
      </View>

      <View>
        <Text style = {{color:'white'}}>Account Name</Text>

        <TextInput placeholder="AccountName"></TextInput>
      </View>

      <View>
        <Text style = {{color:'white'}}>Password</Text>

        <TextInput placeholder="......."></TextInput>
      </View>

      <TouchableOpacity>
        <Text style={{ color: "white" }}>Sign In</Text>
      </TouchableOpacity>

      <View>
        <Text style = {{color:'white'}}>Forgot Password?</Text>

        <View>
          <Text style = {{color:'white'}}>No account?</Text>

          <Text style = {{color:'white'}}>Sign Up!</Text>
        </View>
      </View>
    </View>
  );
}
