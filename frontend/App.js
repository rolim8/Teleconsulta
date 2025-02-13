import React from "react";
import { View, Text } from "react-native";
import CadastroPaciente from "./components/CadastroPaciente";

export default function App() {
  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 24, marginBottom: 20 }}>
        Cadastro de Pacientes
      </Text>
      <CadastroPaciente />
    </View>
  );
}
