"""The order of the conditions is very important. More specific cases should come before more general ones; otherwise, the general condition may match first and prevent the specific condition from ever being reached."""

def response(hey_bob):

    """A yelling question is both a question and a yell, so it must be checked before the separate checks for questions or yelling."""
    
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        return "Fine. Be that way!"

    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"

    if hey_bob.isupper():
        return "Whoa, chill out!"

    if hey_bob.endswith("?"):
        return "Sure."

    return "Whatever."