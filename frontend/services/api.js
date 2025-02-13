import axios from "axios";

const API_URL = "http://localhost:5000"; // Substitua pelo endereço do seu backend

export const cadastrarPaciente = async (paciente) => {
  const response = await axios.post(`${API_URL}/pacientes`, paciente);
  return response.data;
};
