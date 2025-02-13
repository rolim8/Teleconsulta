import React, { useState } from "react";
import { View, TextInput, Button, Alert } from "react-native";
import { cadastrarPaciente } from "../services/api";

export default function CadastroPaciente() {
  const [nome, setNome] = useState("");
  const [dataNascimento, setDataNascimento] = useState("");
  const [historicoMedico, setHistoricoMedico] = useState("");

  const handleCadastro = async () => {
    try {
      await cadastrarPaciente({
        nome,
        data_nascimento: dataNascimento,
        historico_medico: historicoMedico,
      });
      Alert.alert("Sucesso", "Paciente cadastrado com sucesso!");
    } catch (error) {
      Alert.alert("Erro", "Não foi possível cadastrar o paciente.");
    }
  };

  return (
    <View>
      <TextInput
        placeholder="Nome"
        value={nome}
        onChangeText={setNome}
        style={{ marginBottom: 10, padding: 10, borderWidth: 1 }}
      />
      <TextInput
        placeholder="Data de Nascimento"
        value={dataNascimento}
        onChangeText={setDataNascimento}
        style={{ marginBottom: 10, padding: 10, borderWidth: 1 }}
      />
      <TextInput
        placeholder="Histórico Médico"
        value={historicoMedico}
        onChangeText={setHistoricoMedico}
        style={{ marginBottom: 10, padding: 10, borderWidth: 1 }}
        multiline
      />
      <Button title="Cadastrar" onPress={handleCadastro} />
    </View>
  );
}
