from kfp import dsl
from kfp.dsl import component, Input, Dataset

@component(base_image="python:3.9", packages_to_install=["gitpython"])
def upload_to_github(
    report_file: Input[Dataset],
    repo_url: str,
    github_token: str,
    branch: str
):

    import subprocess
    import shutil
    import os
    from datetime import datetime

    os.environ["GIT_ASKPASS"] = "echo"

    report_path = report_file.path
    print("Checking if report exists at:", report_path)
    if not os.path.exists(report_path):
        raise FileNotFoundError(f"{report_path} does not exist")

    # HTML 파일 이름 만들기
    timestamp = datetime.now().strftime("report-%Y%m%d-%H%M%S.html")
    safe_repo_url = repo_url.replace("https://", f"https://{github_token}@")
    repo_dir = "/tmp/repo"
    report_target_path = os.path.join(repo_dir, timestamp)

    # Git clone
    subprocess.run(["git", "clone", "--branch", branch, safe_repo_url, repo_dir], check=True)
    shutil.copyfile(report_path, report_target_path)

    # Git config
    subprocess.run(["git", "-C", repo_dir, "config", "user.email", "ci@example.com"], check=True)
    subprocess.run(["git", "-C", repo_dir, "config", "user.name", "CI Bot"], check=True)

    # Git commit & push
    subprocess.run(["git", "-C", repo_dir, "add", "."], check=True)
    result = subprocess.run(["git", "-C", repo_dir, "status", "--porcelain"], capture_output=True, text=True)

    if result.stdout.strip():
        subprocess.run(["git", "-C", repo_dir, "commit", "-m", f"Add {timestamp}"], check=True)
        subprocess.run(["git", "-C", repo_dir, "push"], check=True)
        print(f"Report committed and pushed to GitHub as {timestamp}.")
    else:
        print("No changes to commit. Skipping.")
