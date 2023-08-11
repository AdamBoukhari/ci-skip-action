def read_commits(file_path):
    with open(file_path, 'r') as file:
        messages = file.read().strip().split('\n')
    return messages

#dokomademo
if __name__ == "__main__":
    commit_file_path = "/app/commit_messages.txt"
    commits = read_commits(commit_file_path)
    is_even = len(commits) % 2 == 0
    print(commits)
    with open("/app/result.txt", "w") as file:
        file.write("execute" if is_even else "skip")
         