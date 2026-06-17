# GitBot - Groq-Powered GitHub Assistant

An intelligent chatbot powered by Groq LLM and Model Context Protocol (MCP) that can manage and edit your GitHub repositories through natural language conversations.

## Features

✅ **GitHub Operations via LLM**
- List and explore repositories
- Create/update files
- Commit and push code
- Create branches and pull requests
- Manage issues and discussions

✅ **Natural Language Interface**
- Chat-based interaction
- Groq LLM reasoning
- Automatic tool selection and execution

✅ **Secure Credential Management**
- Environment-based authentication
- Never exposes tokens in code

## Requirements

### System Requirements
- **Python 3.8+**
- **Node.js** (for GitHub MCP server)
- **npm** (for MCP dependencies)
- **Git** (for version control)

### Python Dependencies
See `requirements.txt`:
- `groq` - Groq API client
- `mcp` - Model Context Protocol
- `python-dotenv` - Environment variable management
- `aiohttp` - Async HTTP client

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Nithisrizoya/test-mcp.git
cd test-mcp
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Node.js Dependencies (for MCP)
```bash
npm install -g @modelcontextprotocol/server-github
```

### 4. Set Up Environment Variables

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```
GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_personal_access_token
GROQ_MODEL=llama-3.1-8b-instant
```

**How to get credentials:**
- **Groq API Key**: https://console.groq.com
- **GitHub Token**: https://github.com/settings/tokens (create with `repo`, `gist` scopes)

## Usage

Run the chatbot:
```bash
python main.py
```

### Example Interactions

```
You: List my repositories
GitBot: *[System Activity: Executing GitHub tool 'list_user_repositories'...]*
GitBot: Here are your repositories: [list shown]

You: Create a new file called test.txt in my repository
GitBot: *[System Activity: Executing GitHub tool 'create_file'...]*
GitBot: File created successfully!

You: Commit and push the changes
GitBot: *[System Activity: Executing GitHub tool 'commit_and_push'...]*
GitBot: Changes committed and pushed!
```

## How It Works

```
User Input → Groq LLM → Tool Selection → GitHub MCP Server → GitHub API
     ↓           ↓              ↓                  ↓              ↓
  Chat      Reasoning      Decision        Execution      Result
```

## Architecture

- **Groq LLM** — Understands user requests and decides which tools to use
- **GitHub MCP** — Provides GitHub operations (create files, commit, push, etc.)
- **GITHUB_TOKEN** — Authenticates with GitHub API

## Security Best Practices

⚠️ **IMPORTANT:**
- Never commit `.env` file (it''s in `.gitignore`)
- Use `.env.example` as a template for others
- Regenerate tokens if accidentally exposed
- Keep `GROQ_API_KEY` and `GITHUB_TOKEN` confidential

## Troubleshooting

**Error: "GROQ_API_KEY is not set"**
→ Check your `.env` file and ensure `GROQ_API_KEY` is set

**Error: "GITHUB_TOKEN is not set"**
→ Check your `.env` file and ensure `GITHUB_TOKEN` is set

**Error: "MCP server connection failed"**
→ Ensure Node.js and `@modelcontextprotocol/server-github` are installed
```bash
npm install -g @modelcontextprotocol/server-github
```

**Error: "Tool execution failed"**
→ Check GitHub token permissions (needs `repo` scope)

## Available GitHub Tools

The chatbot can use these GitHub operations:
- `list_user_repositories` - List your repos
- `get_repository` - Get repo details
- `create_file` - Create new files
- `update_file` - Update existing files
- `delete_file` - Delete files
- `create_branch` - Create branches
- `create_pull_request` - Create PRs
- `create_issue` - Create issues

## Example Use Cases

1. **Auto-generate code files** - Ask the chatbot to create Python scripts
2. **Automated commits** - Request the chatbot to commit and push changes
3. **Repository management** - List, organize, and manage your repos
4. **Issue tracking** - Create and manage GitHub issues

## License

Open Source

## Author

Nithisri Raja

## Contributing

Feel free to fork, modify, and contribute!
