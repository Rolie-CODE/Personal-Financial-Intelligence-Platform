import { View, Text, TextInput, TouchableOpacity } from "react-native";
import FontAwesome5 from "@expo/vector-icons/FontAwesome5";
import { SafeAreaView } from "react-native-safe-area-context";

export default function reset_password() {
  return (
    <SafeAreaView style={{ backgroundColor: "black", flex: 1 }}>
      <View style={{ alignItems: "center", gap: 25 }}>
        <View style={{ alignItems: "center", marginTop: 40 }}>
          <FontAwesome5 name="key" size={44} color="#0096C7" />
        </View>

        <Text style={{ color: "white", fontWeight: "bold", fontSize: 34 }}>
          Reset Password
        </Text>
      </View>

      <View>
        <Text
          style={{
            color: "#FDFFF5",
            marginLeft: 40,
            fontSize: 18,
            marginTop: 20,
          }}
        >
          Account Name
        </Text>

        <TextInput
          placeholder="       yourname"
          placeholderTextColor="#8A8A8A"
          autoCapitalize="none"
          style={{
            color: "#FDFFF5",
            marginLeft: 50,
            borderWidth: 0.5,
            borderColor: "#FDFFF5",
            marginRight: 50,
            height: 50,
            borderRadius: 8,
            marginTop: 20,
          }}
        ></TextInput>
      </View>

      <View>
        <Text
          style={{
            color: "#FDFFF5",
            marginLeft: 40,
            fontSize: 18,
            marginTop: 20,
          }}
        >
          Email
        </Text>

        <TextInput
          placeholder="       you@email.com"
          placeholderTextColor="#8A8A8A"
          autoCapitalize="none"
          keyboardType="email-address"
          style={{
            color: "#FDFFF5",
            marginLeft: 50,
            borderWidth: 0.5,
            borderColor: "#FDFFF5",
            marginRight: 50,
            height: 50,
            borderRadius: 8,
            marginTop: 20,
          }}
        ></TextInput>
      </View>

      <View>
        <Text
          style={{
            color: "#FDFFF5",
            marginLeft: 40,
            fontSize: 18,
            marginTop: 20,
          }}
        >
          New Password
        </Text>

        <TextInput
          placeholder="        ......."
          placeholderTextColor="#8A8A8A"
          secureTextEntry
          style={{
            color: "#FDFFF5",
            marginLeft: 50,
            borderWidth: 0.5,
            borderColor: "#FDFFF5",
            marginRight: 50,
            height: 50,
            borderRadius: 8,
            marginTop: 20,
          }}
        ></TextInput>
      </View>

      <View>
        <Text
          style={{
            color: "#FDFFF5",
            marginLeft: 40,
            fontSize: 18,
            marginTop: 20,
          }}
        >
          Confirm New Password
        </Text>

        <TextInput
          placeholder="        ......."
          placeholderTextColor="#8A8A8A"
          secureTextEntry
          style={{
            color: "#FDFFF5",
            marginLeft: 50,
            borderWidth: 0.5,
            borderColor: "#FDFFF5",
            marginRight: 50,
            height: 50,
            borderRadius: 8,
            marginTop: 20,
          }}
        ></TextInput>
      </View>

      <TouchableOpacity
        style={{
          borderWidth: 0.5,
          borderRadius: 8,
          borderColor: "#FDFFF5",
          alignItems: "center",
          marginTop: 45,
          height: 50,
          justifyContent: "center",
          marginRight: 50,
          marginLeft: 50,
          backgroundColor: "#0096C7",
        }}
      >
        <Text style={{ color: "white" }}>Reset Password</Text>
      </TouchableOpacity>

      <View style={{ marginTop: 50, alignItems: "center" }}>
        <TouchableOpacity>
          <Text style={{ color: "#0096C7" }}>Back to sign in</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}
