import os
import re
import requests
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Initialize environment variables
load_dotenv()

# Configure the Gemini API client
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def parse_github_url(url: str) -> tuple[str | None, str | None]:
    """Extracts the repository owner and name from a standard GitHub URL."""
    pattern = r"github\.com/([^/]+)/([^/]+)"
    match = re.search(pattern, url)
    if match:
        owner = match.group(1)
        repo = match.group(2).replace(".git", "")
        return owner, repo
    return None, None

def fetch_repository_structure(owner: str, repo: str) -> tuple[list | None, str | None]:
    """
    Interfaces with the GitHub REST API to fetch the repository's default branch 
    and subsequently retrieves the recursive file tree.
    """
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    # 1. Fetch repository metadata to determine the default branch
    repo_url = f"https://api.github.com/repos/{owner}/{repo}"
    repo_response = requests.get(repo_url, headers=headers)
    
    if repo_response.status_code != 200:
        return None, "Failed to locate repository. Ensure it is public and the URL is correct."
        
    repo_data = repo_response.json()
    default_branch = repo_data.get("default_branch", "main")
    
    # 2. Fetch the recursive file tree based on the default branch
    tree_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{default_branch}?recursive=1"
    tree_response = requests.get(tree_url, headers=headers)
    
    if tree_response.status_code != 200:
        return None, "Failed to retrieve the repository file structure."
        
    tree_data = tree_response.json()
    
    # Filter out directories to reduce token load, keeping only file paths
    file_paths = [item["path"] for item in tree_data.get("tree", []) if item["type"] == "blob"]
    
    # Truncate if the repository is excessively large to respect LLM token limits
    if len(file_paths) > 800:
        file_paths = file_paths[:800]
        file_paths.append("... [Truncated for size limits]")
        
    return file_paths, None

def generate_architectural_report(file_structure: list) -> str:
    """Passes the repository structure to the LLM to generate a static analysis report."""
    try:
        # Dynamically select an available text-generation model to prevent 404 deprecation errors
        available_models = [
            m.name for m in genai.list_models() 
            if 'generateContent' in m.supported_generation_methods
        ]
        
        if not available_models:
            return "System Error: The provided API key lacks access to text-generation models."
            
        # Prioritize modern models (flash or pro) if available, otherwise use the default
        chosen_model = available_models[0]
        for model_name in available_models:
            if "flash" in model_name or "pro" in model_name:
                chosen_model = model_name
                break
                
        model = genai.GenerativeModel(chosen_model)
        
        prompt = f"""
        You are a Senior Software Engineer conducting a static analysis of a codebase. 
        Below is the file and directory structure of a GitHub repository:
        
        {file_structure}
        
        Based solely on these file paths and names, provide a comprehensive technical breakdown formatted in Markdown:
        
        1. **Tech Stack Detection**: Identify the primary programming languages, frameworks, and build tools.
        2. **Project Architecture**: Explain the likely purpose of the application and how the directories are structured (e.g., MVC pattern, microservices, frontend/backend split).
        3. **Suggested Improvements**: Identify missing industry standards (e.g., lack of Dockerfiles, missing CI/CD workflows, absent testing directories, or poor documentation practices).
        
        Maintain a professional, objective, and analytical tone. Do not use conversational filler.
        """
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"Error during AI analysis: {str(e)}"

# --- UI Generation ---

def main():
    st.set_page_config(page_title="GitHub Repository Analyzer", layout="centered")
    
    st.title("GitHub Repository Analyzer")
    st.write("Provide a public GitHub repository link to generate an automated architectural breakdown.")
    
    # Input field
    repo_url = st.text_input("Repository URL:", placeholder="https://github.com/owner/repository")
    
    if st.button("Initialize Analysis"):
        if not GEMINI_API_KEY:
            st.error("Configuration Error: GEMINI_API_KEY is not set in the environment.")
            return
            
        if not repo_url:
            st.warning("Input required. Please provide a repository URL.")
            return
            
        owner, repo = parse_github_url(repo_url)
        
        if owner and repo:
            with st.spinner("Retrieving repository topology via GitHub API..."):
                file_structure, error = fetch_repository_structure(owner, repo)
            
            if error:
                st.error(error)
            elif file_structure:
                with st.spinner("Compiling static analysis report via LLM..."):
                    report = generate_architectural_report(file_structure)
                    
                st.success("Analysis complete.")
                st.markdown("---")
                st.markdown(report)
        else:
            st.warning("Invalid URL format. Please provide a standard GitHub repository link.")

if __name__ == "__main__":
    main()