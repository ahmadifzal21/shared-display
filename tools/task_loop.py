import json
import subprocess
import sys
from typing import Sequence, Union

Command = Union[str, Sequence[str]]

def sh(cmd: Command):
    if isinstance(cmd, (list, tuple)):
        cmd = " ".join(str(part) for part in cmd)
    return subprocess.run(cmd, capture_output=True, text=True, shell=True)

def list_tasks_json():
    result = sh(["task-master", "list", "--format", "json"])
    if result.returncode != 0:
        print("Error listing tasks:", result.stderr.strip())
        sys.exit(1)

    raw_output = result.stdout or "{}"
    try:
        payload = json.loads(raw_output)
    except json.JSONDecodeError as exc:
        print("Error parsing JSON from task-master list:", exc)
        print("Raw output:", raw_output.strip())
        sys.exit(1)

    if isinstance(payload, dict):
        tasks = payload.get("tasks")
        if tasks is None:
            return []
        if isinstance(tasks, list):
            return tasks
        print("Unexpected JSON structure: 'tasks' is not a list.")
        sys.exit(1)

    if isinstance(payload, list):
        return payload

    print("Unexpected JSON structure received from task-master.")
    sys.exit(1)

def first_pending(tasks):
    pending = [task for task in tasks if task.get("status") == "pending"]
    if not pending:
        return None

    def sort_key(task):
        identifier = task.get("id")
        try:
            return int(identifier)
        except (TypeError, ValueError):
            return identifier or ""

    return sorted(pending, key=sort_key)[0]

def set_status(task_id, status):
    result = sh(["task-master", "set-status", "--id", str(task_id), "--status", status])
    if result.returncode != 0:
        print("Error updating status:", result.stderr.strip())

def main():
    while True:
        tasks = list_tasks_json()
        next_task = first_pending(tasks)
        if not next_task:
            print("No pending tasks right now.")
            break

        print(f'Next Task: [{next_task.get("id")}] {next_task.get("title", "")}')

        details = next_task.get("acceptance") or next_task.get("details")
        if details:
            print("\nDetails:\n" + details.strip() + "\n")

        answer = input("Mark IN-PROGRESS and let Codex/me do work now? (Y/N/Q): ").strip().upper()
        if answer == "Q":
            break
        if answer != "Y":
            continue

        set_status(next_task.get("id"), "in-progress")
        print("\n--> Do the work now (Codex edits, run shell). Press ENTER when done.")
        input()

        done = input("Mark DONE? (Y/N): ").strip().upper()
        if done == "Y":
            set_status(next_task.get("id"), "done")
            print("Marked DONE.")

if __name__ == "__main__":
    main()
