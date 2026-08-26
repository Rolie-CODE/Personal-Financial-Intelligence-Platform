import { useState } from "react";
import {
  Alert,
  View,
  Text,
  TextInput,
  TouchableOpacity,
  SafeAreaView,
} from "react-native";
import { router } from "expo-router";
import FontAwesome from "@expo/vector-icons/FontAwesome";

export default function Sign_Up() {
  const [accountName, setAccountName] = useState("");
  const [password, setPassword] = useState("");
  const [isSigningIn, setIsSigningIn] = useState(false);

  const handleSignIn = async () => {
    if (!accountName.trim() || !password) {
      Alert.alert(
        "Sign in failed",
        "Please enter your account name and password.",
      );
      return;
    }

    setIsSigningIn(true);

    try {
      const params = new URLSearchParams({
        account_name: accountName.trim(),
        password,
      });

      const response = await fetch(
        `https://finanace-api.onrender.com/signin?${params.toString()}`,
        {
          method: "POST",
        },
      );

      if (!response.ok) {
        let message = "Please check your account name and password.";

        try {
          const data = await response.json();
          if (typeof data?.detail === "string") {
            message = data.detail;
          } else if (Array.isArray(data?.detail) && data.detail[0]?.msg) {
            message = data.detail[0].msg;
          }
        } catch {
          // Keep the default message when the API does not return JSON.
        }

        Alert.alert("Sign in failed", message);
        return;
      }

      router.push("/homepage");
    } catch {
      Alert.alert(
        "Sign in failed",
        "Unable to connect to the sign in service. Please try again.",
      );
    } finally {
      setIsSigningIn(false);
    }
  };

  return (
    <SafeAreaView style={{ backgroundColor: "black", flex: 1 }}>
      <View style={{ alignItems: "center", gap: 40 }}>
        <View style={{ alignItems: "center", marginTop: 40 }}>
          <FontAwesome name="lock" size={44} color="#0096C7" />
        </View>

        <Text style={{ color: "white", fontWeight: "bold", fontSize: 34 }}>
          Sign In
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
          placeholder="       AccountName"
          placeholderTextColor="#8A8A8A"
          value={accountName}
          onChangeText={setAccountName}
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
          Password
        </Text>

        <TextInput
          placeholder="        ......."
          placeholderTextColor="#8A8A8A"
          value={password}
          onChangeText={setPassword}
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
        disabled={isSigningIn}
        onPress={handleSignIn}
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
          backgroundColor: isSigningIn ? "#5AAFCB" : "#0096C7",
        }}
      >
        <Text style={{ color: "white" }}>
          {isSigningIn ? "Signing In..." : "Sign In"}
        </Text>
      </TouchableOpacity>

      <View style={{ marginTop: 50, alignItems: "center" }}>
        <TouchableOpacity>
          <Text style={{ color: "#FDFFF5" }}>Forgot Password?</Text>
        </TouchableOpacity>

        <View
          style={{
            display: "flex",
            flexDirection: "row",
            gap: 10,
            marginTop: 20,
          }}
        >
          <Text style={{ color: "white" }}>No account?</Text>

          <TouchableOpacity>
            <Text style={{ color: "#0096C7" }}>Sign Up!</Text>
          </TouchableOpacity>
        </View>
      </View>
    </SafeAreaView>
  );
}
