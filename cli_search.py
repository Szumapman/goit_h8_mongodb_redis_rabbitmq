import difflib
import sys
from datetime import datetime

from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter

from models import Author, Quote, Tag
import connect


def authors_view_adapter(authors: list):
    return [f"{author.name} - born: {author.born_date.strftime('%B %d, %Y')}, {author.born_location}\n{author.description}" for author in authors]


def quotes_view_adapter(quotes: list):
    return [f"{quote.author.name}: {quote.quote}\ntags: {', '.join([tag.name for tag in quote.tags])}" for quote in quotes]


def db_query(type_objects, arguments: list):
    answers = []
    if type_objects == Author:
        for arg in arguments:
            answers += type_objects.objects(name__istartswith=arg)
        if answers:
            return authors_view_adapter(answers)
    elif type_objects == Quote:
        for arg in arguments:
            answers += type_objects.objects(tags__name__icontains=arg)
            if answers:
                return quotes_view_adapter(answers)
    return []


def exit_program():
    print("See you soon!")
    sys.exit(0)


COMMANDS = {
    "name": Author,
    "tag": Quote,
    "tags": Quote,
    "exit": exit_program,
}


def user_command_input():
    commands_completer = FuzzyWordCompleter(list(COMMANDS.keys()))
    user_input = prompt(">>> ", completer=commands_completer)
    if user_input:
        return parse_command(user_input)
    return "", []


def parse_command(command: str) -> (str, list):
    tokens = command.split(":")
    command = tokens[0].strip().lower()
    args = []
    if len(tokens) > 1:
        arguments = tokens[1].split(",")
        for arg in arguments:
            args.append(arg.strip())
    return command, args


def execute_command(command: str, arguments: list):
    if command not in COMMANDS:
        matches = difflib.get_close_matches(command, list(COMMANDS.keys()))
        info = f"\nmaybe you meant: {' or '.join(matches)}" if matches else ""
        return [f'Command "{command}" is not recognized' + info]
    cmd = COMMANDS[command]
    if cmd == exit_program:
        exit_program()
    return db_query(cmd, arguments)


def main():
    while True:
        command, arguments = user_command_input()
        answers = execute_command(command, arguments)
        if answers:
            for answer in answers:
                print(answer)
        else:
            print("No results found")


if __name__ == "__main__":
    main()
