# Guia de Instalação e Uso - LunAI

## 🚀 Começar Rápido (Recomendado para Teste)

### No Linux Mint:

```bash
# 1. Clone o repositório
git clone https://github.com/gabrielfalcao970-beep/LunAI.git
cd LunAI

# 2. Execute o script de setup
bash setup.sh

# 3. Inicie a IA
bash start.sh
```

Isso vai:
- ✅ Criar ambiente virtual
- ✅ Instalar dependências
- ✅ Iniciar LunAI com GUI

---

## 📦 Criar Executável (Opcional)

Para criar um executável standalone que não precisa de terminal:

```bash
# 1. Construir executável
bash build_linux.sh

# 2. Instalar (opcional)
bash install_linux.sh

# 3. Executar
./dist/LunAI
# ou se instalado: lunai
```

---

## 🎨 Adicionar os Avatares

1. **Crie a pasta de avatares:**
```bash
mkdir -p assets/avatars
```

2. **Coloque as 10 imagens com os nomes:**
   - `calm.png` - Calma/Relaxada
   - `neutral.png` - Neutra/Normal
   - `surprised.png` - Surpresa/Entusiasmada
   - `worried.png` - Preocupação/Dúvida
   - `sad.png` - Triste/Desapontada
   - `confused.png` - Espantada/Confusa
   - `thinking.png` - Pensativa/Concentrada
   - `happy.png` - Feliz/Alegre
   - `serene.png` - Serena/Meditativa
   - `angry.png` - Brava/Irritada

3. **Reinicie LunAI**

---

## ⚙️ Configuração

1. **Copie o arquivo de exemplo:**
```bash
cp config.example.py config.py
```

2. **Edite `config.py` com suas preferências:**
```python
# Use modo offline (padrão)
USE_OFFLINE_MODE = True

# Ou adicione suas chaves de API
OPENAI_API_KEY = "sua-chave-aqui"
GEMINI_API_KEY = "sua-chave-aqui"
USE_OFFLINE_MODE = False

# Personalize a interface
THEME = "dark"  # ou "light"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
AI_NAME = "LunAI"
PERSONALITY = "helpful"  # ou "professional", "friendly", "casual"
```

3. **Reinicie a aplicação**

---

## 🎯 Usar a IA

### Conversação Básica:
```
Você: Olá LunAI
LunAI: Oi! Como você está hoje?

Você: Estou triste
LunAI: Entendo que você está triste. Quer conversar sobre isso?

Você: Me ajuda com motivação
LunAI: Você é mais forte do que pensa! Cada dia é uma nova oportunidade...
```

### Exemplos de Comandos:
- "Olá" - Saudação
- "Estou feliz/triste/com raiva/preocupado" - Expressar sentimentos
- "Me ajuda com..." - Pedir ajuda
- "Me motiva" - Receber motivação

### Recursos:
- 💬 **Chatbot conversacional** - Conversa natural
- 😊 **Análise de sentimentos** - Detecta seu estado emocional
- 🎨 **10 avatares diferentes** - Expressões dinâmicas
- 📝 **Histórico de chats** - Salva automaticamente em `data/chat_history/`
- 📋 **Logs** - Arquivo de logs em `data/logs/`

---

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'PyQt5'"
```bash
pip install -r requirements.txt
```

### "Command 'python3' not found"
```bash
sudo apt install python3 python3-pip python3-venv
```

### Não aparece no menu de aplicações
```bash
bash create_desktop_entry.sh
```

### Desinstalar completamente
```bash
bash uninstall.sh
rm -rf ~/LunAI
rm -rf ~/.local/bin/lunai*
```

---

## 📱 Integração com APIs (Avançado)

### OpenAI GPT:
1. Obtenha chave em: https://platform.openai.com/account/api-keys
2. Edite `config.py`:
```python
OPENAI_API_KEY = "sk-..."
USE_OFFLINE_MODE = False
PREFERRED_API = "openai"
```

### Google Gemini:
1. Obtenha chave em: https://ai.google.dev/
2. Edite `config.py`:
```python
GEMINI_API_KEY = "AIza..."
USE_OFFLINE_MODE = False
PREFERRED_API = "gemini"
```

---

## 📂 Estrutura de Arquivos

```
LunAI/
├── main.py                 # Inicializador
├── start.sh               # Script para iniciar
├── build_linux.sh         # Criar executável
├── install_linux.sh       # Instalar sistema-wide
├── setup.sh               # Setup inicial
├── config.py              # Configuração (criado do exemplo)
├── requirements.txt       # Dependências
├── lunai/
│   ├── gui/              # Interface gráfica
│   ├── core/             # IA (chatbot, sentimentos)
│   ├── api/              # Integração com APIs
│   └── utils/            # Utilitários
├── assets/
│   └── avatars/          # Imagens dos avatares (você adiciona)
├── data/
│   ├── chat_history/     # Histórico de conversas
│   └── logs/             # Arquivos de log
└── README.md             # Este arquivo
```

---

## 💡 Dicas

1. **Executar em background:**
```bash
nohup bash start.sh &
```

2. **Ver logs em tempo real:**
```bash
tail -f data/logs/lunai_*.log
```

3. **Adicionar atalho ao teclado:**
   - Abra Configurações de Teclado
   - Adicione novo atalho personalizado
   - Comando: `python3 /caminho/para/LunAI/main.py`
   - Tecla: Sua escolha (ex: Ctrl+Alt+L)

4. **Atualizar para a última versão:**
```bash
git pull origin main
bash setup.sh
```

---

## 🤝 Contribuir

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para saber como contribuir!

---

## 📄 Licença

MIT License - Veja [LICENSE](LICENSE)

---

**Precisa de ajuda?** Abra uma [Issue](https://github.com/gabrielfalcao970-beep/LunAI/issues) no GitHub!

**Gostou do projeto?** Dê uma ⭐ no repositório!
