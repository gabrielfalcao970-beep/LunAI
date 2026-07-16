# LunAI Configuration File
# Copie este arquivo para config.py e configure com suas credenciais

# ============== API Configuration ==============

# OpenAI GPT Configuration
OPENAI_API_KEY = "sua-chave-openai-aqui"
OPENAI_MODEL = "gpt-3.5-turbo"  # ou "gpt-4" se tiver acesso

# Google Gemini Configuration
GEMINI_API_KEY = "sua-chave-gemini-aqui"

# ============== AI Behavior ==============

# Use modo offline (sem APIs externas)
USE_OFFLINE_MODE = True

# API preferida quando disponível
PREFERRED_API = "openai"  # "openai", "gemini" ou "offline"

# Temperatura da IA (0.0 a 2.0 - quanto maior, mais criativa)
TEMPERATURE = 0.7

# Máximo de tokens por resposta
MAX_TOKENS = 500

# ============== GUI Configuration ==============

# Tema padrão
THEME = "dark"  # "dark" ou "light"

# Tamanho da janela
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600

# Manter janela sempre visível
ALWAYS_ON_TOP = True

# Iniciar minimizado
START_MINIMIZED = False

# ============== Personalization ==============

# Nome da IA
AI_NAME = "LunAI"

# Personalidade da IA (afeta tom das respostas)
PERSONALITY = "helpful"  # "helpful", "professional", "friendly", "casual"

# ============== Data & Storage ==============

# Caminho para salvar histórico de chats
CHAT_HISTORY_PATH = "data/chat_history/"

# Caminho para logs
LOGS_PATH = "data/logs/"

# Salvar histórico automaticamente
AUTO_SAVE_HISTORY = True

# Limite de histórico salvo (em MB)
HISTORY_SIZE_LIMIT = 100

# ============== Sentiment Analysis ==============

# Ativar análise de sentimentos
ENABLE_SENTIMENT_ANALYSIS = True

# Threshold para detectar sentimentos (0.0 a 1.0)
SENTIMENT_THRESHOLD = 0.5

# ============== Logging ==============

# Nível de log ("DEBUG", "INFO", "WARNING", "ERROR")
LOG_LEVEL = "INFO"

# Salvar logs em arquivo
SAVE_LOGS_TO_FILE = True

# Máximo de linhas no console
MAX_CONSOLE_LINES = 100

# ============== Memory ==============

# Número de mensagens anteriores a lembrar
CONVERSATION_MEMORY = 10

# Ativar aprendizado contínuo
CONTINUOUS_LEARNING = False

# ============== Advanced ==============

# Debug mode
DEBUG = False

# Check for updates
CHECK_FOR_UPDATES = True
