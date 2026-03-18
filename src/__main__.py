"""CLI for ai-content-watermark."""
import sys, json, argparse
from .core import AiContentWatermark

def main():
    parser = argparse.ArgumentParser(description="Invisible watermarking for AI-generated content — detect and verify provenance")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = AiContentWatermark()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.detect(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"ai-content-watermark v0.1.0 — Invisible watermarking for AI-generated content — detect and verify provenance")

if __name__ == "__main__":
    main()
