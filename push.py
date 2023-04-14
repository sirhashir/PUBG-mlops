from github import Github
import os

# Create a Github instance using the Personal Access Token
g = Github(os.environ['FULL_ACCESS'])

# Get the repository that you want to work with
repo = g.get_repo("Yuvraj-Sharma-2000/ec2")

# Create a folder inside the repository
folder_name = "I did it again"
file_name = "Katze.txt"
file_path = f"{folder_name}/{file_name}"

try:
    # Try to get the contents of the file
    file_contents = repo.get_contents(file_path)
    # Update the contents of the file
    updated_contents = "This is the updated content of the file"
    # Commit the changes to the file
    repo.update_file(file_path, "Updated content", updated_contents, file_contents.sha)
    print(f"Updated file {file_path}")
except Exception as e:
    # If the file does not exist, create it
    print(f"File {file_path} not found, creating it")
    repo.create_file(file_path, "Initial commit", "This is the content of the file")
    print(f"Created file {file_path}")