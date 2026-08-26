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
        <Text style = {{color:'#FDFFF5', marginLeft: 40, fontSize: 18, marginTop: 20}}>Account Name</Text>

        <TextInput placeholder="AccountName" style = {{marginLeft: 50, borderWidth: 0.5, borderColor: '#FDFFF5', marginRight: 50, height: 50, borderRadius:8, marginTop: 20}}></TextInput>
      </View>

      <View>
        <Text style = {{color:'#FDFFF5', marginLeft: 40, fontSize: 18, marginTop: 20}}>Password</Text>

        <TextInput placeholder="......." style = {{marginLeft: 50, borderWidth: 0.5, borderColor: '#FDFFF5', marginRight: 50, height: 50, borderRadius:8, marginTop: 20}}></TextInput>
      </View>

      <TouchableOpacity>
        <Text style={{ color: "white" , marginLeft: 40}}>Sign In</Text>
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
