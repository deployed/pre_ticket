import io
import re

import six

from .commands import call_command


def get_current_branch():
    return call_command(["git", "rev-parse", "--abbrev-ref", "HEAD"])


def retrieve_ticket(branch, regex):
    matches = re.match(regex, branch)
    if matches:
        ticket_number = matches.group("ticket")
        return ticket_number


def is_ticket_in_message(contents, ticket):
    for line in contents.splitlines():
        stripped = line.strip().lower()

        if stripped == "" or stripped.startswith("#"):
            continue

        if ticket in stripped:
            return True


def add_ticket_number(filename, regex, format_template):
    branch = get_current_branch()
    ticket_number = retrieve_ticket(branch, regex)

    if ticket_number:
        with io.open(filename, "r+") as fd:
            contents = fd.read()

            if (
                is_ticket_in_message(contents, ticket_number)
                or not contents[:contents.find("\n")]
            ):
                return

            ticket_msg = format_template.format(message=contents, ticket=ticket_number)
            fd.seek(0)
            fd.write(six.text_type(ticket_msg))
            fd.truncate()
