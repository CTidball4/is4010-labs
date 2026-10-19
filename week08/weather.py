import argparse
import os
import sys
from pathlib import Path

try:
    from favorites import FavoritesManager
    from weather_api import WeatherAPI, format_current_weather, format_forecast
except ImportError:
    from week08.favorites import FavoritesManager
    from week08.weather_api import (
        WeatherAPI,
        format_current_weather,
        format_forecast,
    )

FAVORITES_FILE = Path(__file__).parent / "favorites.json"


def load_api_key():
    key = os.environ.get("WEATHER_API_KEY")
    if key:
        return key
    try:
        import config
        key = getattr(config, "WEATHER_API_KEY", None)
        if key and key != "YOUR_API_KEY_HERE":
            return key
        return None
    except ImportError:
        return None


def build_parser():
    parser = argparse.ArgumentParser(description="Weather command-line app")
    sub = parser.add_subparsers(dest="command", required=True)

    current = sub.add_parser("current", help="Show current weather")
    current.add_argument("location")

    forecast = sub.add_parser("forecast", help="Show forecast")
    forecast.add_argument("location")
    forecast.add_argument("--days", type=int, default=3)

    fav = sub.add_parser("favorites", help="Manage favorites")
    fav_sub = fav.add_subparsers(dest="favorites_command", required=True)

    add = fav_sub.add_parser("add", help="Add a favorite")
    add.add_argument("name")
    add.add_argument("location")

    fav_sub.add_parser("list", help="List favorites")

    remove = fav_sub.add_parser("remove", help="Remove a favorite")
    remove.add_argument("name")

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    favorites = FavoritesManager(str(FAVORITES_FILE))

    if args.command == "favorites":
        if args.favorites_command == "add":
            if favorites.add(args.name, args.location):
                print(f"Added favorite: {args.name} -> {args.location}")
                return 0
            print(f"Favorite '{args.name}' already exists.", file=sys.stderr)
            return 1
        if args.favorites_command == "list":
            for name, location in favorites.list_all().items():
                print(f"{name}: {location}")
            return 0
        if args.favorites_command == "remove":
            if favorites.remove(args.name):
                print(f"Removed favorite: {args.name}")
                return 0
            print(f"Favorite '{args.name}' not found.", file=sys.stderr)
            return 1

    api_key = load_api_key()
    if not api_key:
        print(
            "Error: no API key found. Set WEATHER_API_KEY or edit config.py.",
            file=sys.stderr,
        )
        return 1

    # A favorite name can replace a location
    location = favorites.get_location(args.location) or args.location
    api = WeatherAPI(api_key)

    if args.command == "current":
        data = api.get_current_weather(location)
        if data is None:
            print("Error: could not get current weather.", file=sys.stderr)
            return 1
        print(format_current_weather(data))
        return 0

    if args.command == "forecast":
        try:
            data = api.get_forecast(location, args.days)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
        if data is None:
            print("Error: could not get forecast.", file=sys.stderr)
            return 1
        print(format_forecast(data))
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())