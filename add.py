import os
import base64
from github import Github, InputGitAuthor

def save_object():
    file_path = "artifacts/proprocessor.pkl"
    obj = "README.md"
    try:
        # Initialize the GitHub API client
        g = Github(os.environ["$${{secrets.FULL_ACCESS}}"])
        
        # Get the repository and branch information
        repo = g.get_repo("Yuvraj-Sharma-2000/ec2")
        branch = repo.get_branch("main")
        
        # Get the contents of the file as bytes
        with open(file_path, "rb") as file_obj:
            file_contents = file_obj.read()
        
        # Encode the file contents as base64
        file_contents_base64 = base64.b64encode(file_contents).decode("utf-8")
        
        # Create a new file object with the updated contents
        file_name = os.path.basename(file_path)
        file_path_in_repo = os.path.join("path", "to", "directory", file_name) # Change this to the desired path in the repo
        file_obj_in_repo = repo.get_contents(file_path_in_repo, ref=branch)
        new_file_obj = repo.update_file(
            path=file_obj_in_repo.path,
            message="Update file", # Change this to a meaningful commit message
            content=file_contents_base64,
            sha=file_obj_in_repo.sha,
            branch=branch.name,
            committer=InputGitAuthor(
                "GitHub Actions",
                "actions@github.com"
            )
        )
        
        # Print the URL of the updated file
        print(f"File updated: {new_file_obj.html_url}")
    
    except Exception as e:
        raise CustomException(e, sys)
