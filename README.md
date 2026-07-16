# 🌙 LunAI - Seu Assistente Pessoal de IA

**LunAI** é um assistente inteligente pessoal que roda localmente no seu computador. Ela é uma IA de auto-ajuda que conversa com você, entende seus sentimentos e oferece suporte no dia a dia.

## ✨ Características

- 🤖 **Chatbot Conversacional**: Conversa natural e inteligente
- 💬 **Análise de Sentimentos**: Entende seu estado emocional
- 🎨 **10 Avatares Diferentes**: Expressões que refletem as emoções da IA
- 🖥️ **GUI Sobreposta**: Widget que funciona sobre outros apps (como Steam)
- 🧠 **Memória Conversacional**: Lembra de conversas anteriores
- 💾 **Histórico de Chats**: Salva todas as conversas
- 🔌 **Integração com APIs**: Suporte para GPT, Gemini e outras
- 🌙 **Tema Personalizado**: Interface moderna e responsiva

## 🚀 Instalação Rápida

### Requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)
- Linux Mint (ou qualquer Linux/Windows/macOS)

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/gabrielfalcao970-beep/LunAI.git
cd LunAI
```

2. Execute o setup:
```bash
bash setup.sh
```

3. Inicie a IA:
```bash
bash start.sh
```

## 📁 Estrutura do Projeto

```
LunAI/
├── main.py                 # Arquivo principal
├── requirements.txt        # Dependências
├── config.example.py       # Configuração de exemplo
├── config.py              # Configuração (local)
├── start.sh               # Script para iniciar rápido
├── build_linux.sh         # Criar executável
├── install_linux.sh       # Instalar sistema-wide
├── setup.sh               # Setup inicial
├── lunai/
│   ├── __init__.py
│   ├── gui/               # Interface gráfica
│   │   ├── __init__.py
│   │   ├── window.py      # Janela principal
│   │   └── styles.py      # Estilos CSS
│   ├── core/              # Núcleo da IA
│   │   ├── __init__.py
│   │   ├── chatbot.py     # Lógica do chatbot
│   │   ├── sentiment.py   # Análise de sentimentos
│   │   └── memory.py      # Memória conversacional
│   ├── api/               # Integrações com APIs
│   │   ├── __init__.py
│   │   ├── openai_api.py  # OpenAI/GPT
│   │   └── gemini_api.py  # Google Gemini
│   └── utils/             # Utilitários
│       ├── __init__.py
│       ├── logger.py      # Sistema de logs
│       └── config.py      # Gerenciador de config
├── assets/
│   └── avatars/           # Imagens dos avatares (10 imagens)
│       ├── calm.png
│       ├── neutral.png
│       ├── surprised.png
│       ├── worried.png
│       ├── sad.png
│       ├── confused.png
│       ├── thinking.png
│       ├── happy.png
│       ├── serene.png
│       └── angry.png
├── data/
│   ├── chat_history/      # Histórico de chats
│   └── logs/              # Arquivos de log
└── README.md             # Este arquivo
```

## 🎯 Uso

### Iniciar a IA
```bash
bash start.sh
```

A interface gráfica abrirá como um widget sobreposto. Você pode:
- 💬 Digitar mensagens na caixa de texto
- 📌 Fixar/desafixar a janela
- 🔄 Fechar e reabrir quando quiser
- 🎨 Ver o avatar mudar de expressão baseado no contexto

### Exemplos de Conversa

```
Você: Olá LunAI
LunAI: Oi! Como você está hoje?

Você: Estou triste
LunAI: Entendo... Quer conversar sobre isso? Estou aqui para ouvir.

Você: Me ajuda com motivação
LunAI: Claro! Lembre-se de que cada dia é uma nova oportunidade...
```

## ⚙️ Configuração

### Copiar configuração
```bash
cp config.example.py config.py
```

### Editar config.py
```python
# Modo offline (padrão - sem API)
USE_OFFLINE_MODE = True

# Ou adicione sua chave de API
OPENAI_API_KEY = "sua-chave-aqui"
GEMINI_API_KEY = "sua-chave-aqui"
USE_OFFLINE_MODE = False

# Personalizar interface
THEME = "dark"  # ou "light"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
AI_NAME = "LunAI"
```

## 📊 Análise de Sentimentos

A LunAI analisa automaticamente suas mensagens e:
- 😊 Detecta alegria, entusiasmo
- 😢 Reconhece tristeza, desapontamento
- 😠 Identifica raiva, frustração
- 😨 Percebe medo, preocupação
- 😕 Nota confusão, dúvida

E ajusta sua resposta e avatar de acordo!

## 💾 Histórico de Chats

Todas as conversas são salvas em `data/chat_history/` com timestamp. Você pode:
- Revisar conversas antigas
- Exportar em formato TXT ou JSON
- Limpar histórico quando quiser

## 🔌 APIs Suportadas

- **OpenAI GPT** - Para respostas mais inteligentes
- **Google Gemini** - Alternativa de IA
- **Expansível** - Fácil adicionar novas APIs

## 🖥️ Modo Offline

A LunAI funciona completamente offline com NLP básico! Basta:

```python
# config.py
USE_OFFLINE_MODE = True
```

## 📝 Logs

Os logs são salvos em `data/logs/`. Para ver em tempo real:

```bash
tail -f data/logs/lunai_*.log
```

## 🛠️ Criar Executável (Linux)

```bash
# Construir
bash build_linux.sh

# Instalar
bash install_linux.sh

# Executar
lunai
```

## 🤝 Contribuindo

Quer melhorar a LunAI? Siga o guia de contribuição em [CONTRIBUTING.md](CONTRIBUTING.md)

## 📄 Licença

MIT License - Veja [LICENSE](LICENSE) para detalhes

## 👨‍💻 Autor

Criado por Gabriel Falcão | [@gabrielfalcao970-beep](https://github.com/gabrielfalcao970-beep)

## 💬 Suporte

Tem dúvidas? Abra uma [Issue](https://github.com/gabrielfalcao970-beep/LunAI/issues) ou entre em contato!

---

**Made with ❤️ by Gabriel Falcão**
