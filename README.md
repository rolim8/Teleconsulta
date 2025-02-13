# Teleconsulta App

Bem-vindo ao repositório do projeto **Teleconsulta App**! 

Este sistema foi desenvolvido para melhorar o monitoramento clínico de infecções ginecológicas em mulheres reclusas no regime fechado, oferecendo funcionalidades como prontuário eletrônico, telemedicina, monitoramento de sintomas e gestão de medicamentos.

## 📌 Índice
- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## 📖 Visão Geral
O **Teleconsulta App** é um sistema de telemedicina desenvolvido para instituições penitenciárias femininas. Ele permite que profissionais de saúde realizem consultas remotas, monitorem sintomas e gerenciem medicamentos de forma eficiente e segura. O sistema é acessível via dispositivos móveis e desktops, garantindo praticidade e conformidade com a **Lei Geral de Proteção de Dados (LGPD)**.

## 🚀 Funcionalidades
- **Prontuário Eletrônico**: Cadastro e gerenciamento de pacientes.
- **Telemedicina**: Consultas remotas via chat e vídeo.
- **Monitoramento de Sintomas**: Registro diário de sintomas e alertas automáticos.
- **Gestão de Medicamentos**: Controle de medicamentos e alertas para horários de medicação.
- **Relatórios Epidemiológicos**: Geração de relatórios para análise de dados clínicos.

## 🛠 Tecnologias Utilizadas
### Frontend:
- React Native (para aplicativos móveis multiplataforma).
- JavaScript ou TypeScript (para desenvolvimento da interface do usuário).

### Backend:
- Python com Flask (para desenvolvimento da API).
- PostgreSQL (banco de dados relacional).

### Inteligência Artificial:
- TensorFlow ou PyTorch (para modelos de IA).
- spaCy (para processamento de linguagem natural).

### Outras Ferramentas:
- Docker (para conteinerização).
- Git (para controle de versão).
- GitHub Actions (para CI/CD).

## ▶ Como Executar o Projeto
### ✅ Pré-requisitos:
- Python 3.8+ instalado.
- PostgreSQL instalado e configurado.
- Node.js e npm instalados (para o frontend).
- Git instalado.

### 🏃 Passos para Execução:

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/teleconsulta-ia-avatar.git
cd teleconsulta-ia-avatar
```

2. **Configuração do Backend:**
   - Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
   - Instale as dependências:
   ```bash
   pip install -r backend/requirements.txt
   ```
   - Configure o banco de dados:
     - Crie um banco de dados chamado `teleconsulta` no PostgreSQL.
     - Atualize o arquivo `backend/config.py` com as credenciais do banco de dados.
   - Execute o servidor:
   ```bash
   python backend/app.py
   ```

3. **Configuração do Frontend:**
   - Instale as dependências:
   ```bash
   cd frontend
   npm install
   ```
   - Execute o aplicativo:
   ```bash
   npx react-native run-android  # ou npx react-native run-ios
   ```

4. **Acesse o sistema:**
   - O backend estará disponível em: `http://localhost:5000`
   - O frontend estará disponível no emulador ou dispositivo móvel.

## 📂 Estrutura do Projeto
```
teleconsulta-ia-avatar/
│
├── backend/             # Código do backend (Flask)
│   ├── app.py          # Ponto de entrada do backend
│   ├── models.py       # Modelos do banco de dados
│   ├── requirements.txt # Dependências do Python
│   └── config.py       # Configurações do banco de dados
│
├── frontend/            # Código do frontend (React Native)
│   ├── App.js          # Ponto de entrada do frontend
│   ├── components/     # Componentes React Native
│   └── services/       # Serviços de API
│
├── docs/                # Documentação do projeto
│   └── SRS.md          # Especificação de Requisitos de Software
│
└── README.md            # Este arquivo
```

## 🤝 Contribuição
Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um **fork** do repositório.
2. Crie uma **branch** para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça **commit** das suas alterações:
   ```bash
   git commit -m "Adicionando nova funcionalidade"
   ```
4. Envie as alterações para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um **Pull Request** no GitHub.

## 📜 Licença
Este projeto está licenciado sob a **MIT License**. Consulte o arquivo `LICENSE` para mais detalhes.

## 📧 Contato
- **Nome**: Orlando L R Filho
- **Email**: [rolimorlando@gmail.com]
- **GitHub**: [rolim8](https://github.com/rolim8)
