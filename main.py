import argparse
from llm_agent import generate_linkedin_post
from automation import open_linkedin_and_paste
from utils import extract_first_url, safe_preview

def parse_command(cmd: str):
    url = extract_first_url(cmd)
    return url or cmd

def cli_entry():
    parser = argparse.ArgumentParser(description="LinkedIn Ollama Agent")
    parser.add_argument("--cmd", type=str, required=True)
    parser.add_argument("--tone", type=str, default="professional")
    parser.add_argument("--prompt", type=str, default="")
    args = parser.parse_args()

    cert_link = parse_command(args.cmd)
    print("Input used (preview):", safe_preview(cert_link))

    print("\nGenerating LinkedIn post using Ollama...")
    post = generate_linkedin_post(args.cmd, tone=args.tone)

    if isinstance(post, (list, tuple)):
        post = " ".join(map(str, post))

    post = str(post)

    print("\n--- GENERATED POST PREVIEW ---\n")
    print(post)
    print("\n-------------------------------\n")

    confirm = input("Proceed to open Chrome and paste this on LinkedIn? (yes/no): ").strip().lower()
    if confirm not in ("y", "yes"):
        print("Aborted.")
        return

    open_linkedin_and_paste(post)

if __name__ == "__main__":
    cli_entry()
