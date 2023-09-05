import argparse
from database import DatabaseConnection
from req import BoredAPIWrapper
from serializer import Serializer
from models import BORED_ACTIVITY_MODEL


def main():
    parser = argparse.ArgumentParser(
        description="Random Activity Generator",
    )
    parser.add_argument(
        "command", choices=["new", "list"],
        help="Choose a command"
    )
    parser.add_argument("--type")
    parser.add_argument("--participants", type=int)
    parser.add_argument("--price_min", type=float)
    parser.add_argument("--price_max", type=float)
    parser.add_argument("--accessibility_min", type=float)
    parser.add_argument("--accessibility_max", type=float)
    args = parser.parse_args()

    db = DatabaseConnection()

    if args.command == "new":
        activity_params = {
            "type": args.type,
            "participants": args.participants,
            "minprice": args.price_min,
            "maxprice": args.price_max,
            "minaccessibility": args.accessibility_min,
            "maxaccessibility": args.accessibility_max,
        }

        api = BoredAPIWrapper()
        activity = api.get_random_activity(activity_params)
        activity = Serializer(activity, BORED_ACTIVITY_MODEL)
        activity.save(db)
        print("Activity saved!")

    elif args.command == "list":
        latest_activities = db.get_latest_activities()
        for activity in latest_activities:
            print(activity)


if __name__ == "__main__":
    main()
