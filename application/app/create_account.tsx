import { useState } from "react";
import { Alert, View, Text, TextInput, TouchableOpacity } from "react-native";
import MaterialCommunityIcons from "@expo/vector-icons/MaterialCommunityIcons";
import { router } from "expo-router";
import { SafeAreaView } from "react-native-safe-area-context";

export default function CreateAccount() {
    const [accountName, setAccountName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");

    const handleSignUp = () => {
        if (!accountName.trim() || !email.trim() || !password || !confirmPassword) {
            Alert.alert("Sign up failed", "Please complete all fields.");
            return;
        }

        if (password !== confirmPassword) {
            Alert.alert("Sign up failed", "Passwords do not match.");
            return;
        }

        Alert.alert("Account created", "Your account is ready.", [
            { text: "Sign In", onPress: () => router.replace("/") },
        ]);
    };

    return (
        <SafeAreaView style={{ backgroundColor: "black", flex: 1 }}>
            <View style={{ alignItems: "center", gap: 40 }}>
                <View style={{ alignItems: "center", marginTop: 40 }}>
                    <MaterialCommunityIcons name="account" size={44} color="#0096C7" />
                </View>

                <Text style={{ color: "white", fontWeight: "bold", fontSize: 34 }}>
                    Create Account
                </Text>
            </View>

            <View>
                <Text style={{ color: "#FDFFF5", marginLeft: 40, fontSize: 18, marginTop: 20 }}>
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
                />
            </View>

            <View>
                <Text style={{ color: "#FDFFF5", marginLeft: 40, fontSize: 18, marginTop: 20 }}>
                    Email
                </Text>
                <TextInput
                    placeholder="       you@email.com"
                    placeholderTextColor="#8A8A8A"
                    value={email}
                    onChangeText={setEmail}
                    keyboardType="email-address"
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
                />
            </View>

            <View>
                <Text style={{ color: "#FDFFF5", marginLeft: 40, fontSize: 18, marginTop: 20 }}>
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
                />
            </View>

            <View>
                <Text style={{ color: "#FDFFF5", marginLeft: 40, fontSize: 18, marginTop: 20 }}>
                    Confirm Password
                </Text>
                <TextInput
                    placeholder="        ......."
                    placeholderTextColor="#8A8A8A"
                    value={confirmPassword}
                    onChangeText={setConfirmPassword}
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
                />
            </View>

            <TouchableOpacity
                onPress={handleSignUp}
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
                <Text style={{ color: "white" }}>Sign Up</Text>
            </TouchableOpacity>

            <View style={{ marginTop: 50, alignItems: "center" }}>
                <View style={{ display: "flex", flexDirection: "row", gap: 10, marginTop: 20 }}>
                    <Text style={{ color: "white" }}>Already have an account?</Text>
                    <TouchableOpacity onPress={() => router.replace("/")}>
                        <Text style={{ color: "#0096C7" }}>Sign In</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </SafeAreaView>
    );
}

// optimize this