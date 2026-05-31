# GitHub Repository Analyzer

## Transforming Repository Exploration into Architectural Insight

GitHub Repository Analyzer is an AI-powered web application that helps developers quickly understand unfamiliar codebases. By combining the GitHub REST API with Google Gemini, the platform transforms a repository's file structure into a concise architectural analysis, enabling faster onboarding, technical evaluation, and project discovery.

**Live Application**  
[https://app-repo-analyzer-soz26zh69hjme2xeufypeb.streamlit.app/](https://app-repo-analyzer-soz26zh69hjme2xeufypeb.streamlit.app/)

---

## Overview

Modern software projects often contain hundreds or thousands of files distributed across complex directory structures. Understanding a new codebase typically requires significant time spent navigating folders, reading documentation, and inspecting configuration files.

GitHub Repository Analyzer streamlines this process by automatically extracting repository metadata and generating a structured architectural overview. Instead of manually exploring a project, users can simply provide a public GitHub repository URL and receive meaningful insights within seconds.

This project demonstrates how AI can be integrated into developer workflows to improve software discovery, technical understanding, and engineering productivity.

---

## Problem Statement

When evaluating an unfamiliar repository, developers commonly need to answer questions such as:

- What technologies are being used?
- How is the project structured?
- Which architectural patterns are present?
- Are engineering best practices being followed?
- What improvements could strengthen the codebase?

While GitHub provides access to repository contents, obtaining these insights still requires manual effort.

GitHub Repository Analyzer addresses this challenge by combining automated repository inspection with AI-powered interpretation to generate a clear, actionable architectural report.

---

## Solution

The application retrieves repository structure data directly from GitHub using the GitHub REST API and analyzes it through Google Gemini.

The generated report provides:

- Technology stack identification
- Architectural structure analysis
- Engineering quality observations
- Development workflow indicators
- Recommendations for improvement

This enables developers to understand a project's high-level design without cloning the repository or manually reviewing every file.

---

## Key Features

### Repository Structure Analysis

Extracts and maps the file hierarchy of public GitHub repositories using GitHub's Tree API.

### Technology Stack Detection

Identifies programming languages, frameworks, libraries, and development tools used throughout the project.

### Architectural Breakdown

Provides a high-level explanation of project organization and architectural patterns when identifiable.

### Engineering Standards Review

Evaluates the presence of common software engineering practices, including:

- Testing infrastructure
- Continuous Integration workflows
- Containerization support
- Documentation quality
- Configuration management

### AI-Powered Architectural Insights

Leverages Google Gemini to transform repository metadata into a structured and human-readable analysis.

---

## User Journey

### 1. Submit Repository URL

The user enters a public GitHub repository URL.

### 2. Repository Inspection

The application retrieves the repository structure through the GitHub REST API.

### 3. AI Analysis

Repository metadata is processed and analyzed using Google Gemini.

### 4. Insight Generation

The system produces a comprehensive architectural report describing technologies, structure, and engineering practices.

---

## System Architecture

```text
User
  ↓
Streamlit Interface
  ↓
Repository URL Validation
  ↓
GitHub REST API
  ↓
Repository Tree Extraction
  ↓
Google Gemini
  ↓
Architectural Analysis Report
```

### Repository Extraction Layer

The application retrieves repository contents directly through GitHub's Tree API without requiring local cloning.

### Analysis Layer

Extracted metadata is transformed into structured prompts and processed by Google Gemini.

### Presentation Layer

Results are displayed through Streamlit, providing a simple and accessible user experience.

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Programming Language | Python |
| Repository Data Source | GitHub REST API |
| AI Engine | Google Gemini |
| Deployment Platform | Streamlit Community Cloud |
| Configuration Management | Environment Variables & Streamlit Secrets |

---

## Core Capabilities

Given a public GitHub repository, the application automatically generates:

- Technology stack overview
- Architectural structure summary
- Repository organization insights
- Engineering quality observations
- Development workflow indicators
- Improvement recommendations

---

## Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/GitHub-Repo-Analyzer.git
cd GitHub-Repo-Analyzer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

### 6. Launch the Application

```bash
streamlit run app.py
```

---

## Deployment

This application is deployed using **Streamlit Community Cloud**.

For cloud deployment, store the Gemini API key securely through **App Settings → Secrets**:

```toml
GEMINI_API_KEY="your_api_key_here"
```

---

## Security Considerations

- API keys are managed through environment variables and deployment secrets.
- Sensitive credentials are never hardcoded into source files.
- The `.env` file should be excluded from version control.

Recommended `.gitignore` entry:

```gitignore
.env
```

---

## Future Enhancements

Potential future developments include:

- Repository dependency visualization
- Multi-repository comparison
- Commit history analysis
- Pull request and issue insights
- Exportable architecture reports
- Private repository support through OAuth authentication

---

## Learning Outcomes

This project explores the intersection of software engineering, AI-assisted development, and developer experience design. Key areas of learning include:

- REST API integration
- AI-powered codebase analysis
- Prompt engineering
- Secure configuration management
- Cloud deployment workflows
- Product-oriented developer tooling

---

## Author

Developed as part of a continuous exploration of AI-powered developer tools, software architecture analysis, and human-centered engineering experiences.

---

## License

This project is available for educational, learning, and portfolio purposes. Add an open-source license if you intend to distribute or accept contributions.
