import argparse
from core import detector, fingerprint, gateway, utils

def main():
    parser = argparse.ArgumentParser(prog="omnishield", description="OmniShield 2.0 - AI Threat Defender")
    subparsers = parser.add_subparsers(dest="command")

    scan = subparsers.add_parser("scan")
    scan.add_argument("text", help="Payload à analyser")

    config = subparsers.add_parser("config")
    config.add_argument("--threat-feeds")
    config.add_argument("--compliance")

    dash = subparsers.add_parser("dashboard")
    dash.add_argument("--port", type=int, default=8080)

    args = parser.parse_args()

    if args.command == "scan":
        report = detector.scan(args.text)
        utils.pretty_print(report)
    elif args.command == "config":
        print(f"Feeds: {args.threat_feeds}, Compliance: {args.compliance}")
    elif args.command == "dashboard":
        gateway.launch_dashboard(args.port)
    else:
        parser.print_help()
