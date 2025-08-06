# Code Ocean MCP Agent Chat

A minimalist Streamlit chat interface for interacting with Code Ocean through an AI agent powered by Claude and MCP (Model Context Protocol).

## 🚀 Features

- **Chat Interface**: Clean Streamlit-based chat UI for natural conversations
- **Code Ocean Integration**: Direct access to Code Ocean's computational platform via MCP
- **AI Agent**: Claude-powered assistant specialized in Code Ocean operations
- **Session Management**: Persistent conversation history with session clearing
- **Tool Integration**: Search, run, and manage capsules, data assets, and computations

## 📋 Prerequisites

- Python 3.11 or higher
- Code Ocean account with API access
- Anthropic API key

## 🛠️ Installation

### 1. Install uv (Python package manager)

```bash
pip install uv
```

### 2. Sync dependencies

```bash
uv sync
```

## ⚙️ Environment Variables

```bash
# Anthropic API Key for Claude
ANTRHROPIC_API_KEY=your_anthropic_api_key_here

# Code Ocean Configuration
CODEOCEAN_DOMAIN=your_codeocean_domain
CODEOCEAN_TOKEN=your_codeocean_token
```

### Getting Your API Keys:

1. **Anthropic API Key**: 
   - Visit [console.anthropic.com](https://console.anthropic.com)
   - Create an account and generate an API key

2. **Code Ocean Credentials**:
   - Log into your Code Ocean account
   - Navigate to Account Settings → API
   - Generate a new API token
   - Use your Code Ocean domain (e.g., `mycompany.codeocean.com`)

## 📁 Project Structure

```
├── code/
│   ├── agent.py           # Main agent configuration and setup
│   ├── model.py           # Anthropic Claude model configuration
│   ├── mcps.py           # Code Ocean MCP client setup
│   └── streamlit_app.py  # Streamlit chat interface
├── scratch/              # Session storage directory
├── pyproject.toml        # Project dependencies
├── uv.lock              # Dependency lock file
└── README.md            # This file
```

## 📚 File Descriptions

### `code/agent.py`
- **Purpose**: Core agent setup and configuration
- **Key Functions**:
  - `get_agent()`: Creates a new agent instance with fresh session
- **Features**: 
  - Session management with file-based storage
  - Sliding window conversation memory (10 messages)
  - Integration with Code Ocean tools and Claude model

### `code/model.py`
- **Purpose**: Anthropic Claude model configuration
- **Configuration**: 
  - Model: `claude-sonnet-4-20250514`
  - Max tokens: 4096
  - API key from environment variables

### `code/mcps.py`
- **Purpose**: Code Ocean MCP (Model Context Protocol) client setup
- **Features**:
  - Connects to Code Ocean MCP server
  - Provides tools for capsule and data asset management
  - Requires `uvx` and `codeocean-mcp-server`

### `code/streamlit_app.py`
- **Purpose**: Web-based chat interface
- **Features**:
  - Clean chat UI with message history
  - Welcome instructions for new users
  - Clear chat functionality
  - Real-time agent responses with loading indicators

## 🚀 Usage

### 1. Start the Streamlit App

```bash
cd code
streamlit run streamlit_app.py
```

### 2. Access the Interface

Open your browser to `http://localhost:8501` (or the URL shown in terminal)

### 3. Chat with Aqua

The AI assistant can help you:
- 🔍 Search for capsules and data assets
- ▶️ Run computational workflows
- 📊 Manage and create data assets
- 📁 Download and analyze results

### 4. Example Commands

Try asking Aqua:
- "List my recent capsules"
- "Search for data assets related to machine learning"
- "Run capsule XYZ with my dataset"
- "Show me the results from computation ABC"

### Adding New Dependencies

```bash
uv add package-name
```

### Updating Dependencies

```bash
uv sync --upgrade
```

## 🐛 Troubleshooting

### Common Issues:

1. **MCP Connection Error**: Ensure `uvx` is installed and `codeocean-mcp-server` is available
2. **API Key Issues**: Verify environment variables are set correctly
3. **Import Errors**: Run `uv sync` to ensure all dependencies are installed

### Debug Mode:

Check terminal output when running the Streamlit app for detailed error messages.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

[Add your license information here]

## 📞 Support

For issues related to:
- Code Ocean integration: Check Code Ocean documentation
- MCP protocol: Visit [MCP GitHub repository](https://github.com/modelcontextprotocol)
- Streamlit: See [Streamlit documentation](https://docs.streamlit.io)

---

Built with ❤️ using Streamlit, Claude, and Code Ocean MCP
