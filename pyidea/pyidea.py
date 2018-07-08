# -*- coding: utf-8 -*-

"""Main module."""
import click
from pathlib import Path
import peewee as pw


# Database constant
DATABASE = pw.SqliteDatabase(str(Path.home())+"/.ideas.db")


class Idea(pw.Model):
    """Main Representation of an idea."""
    text = pw.CharField()

    class Meta:
        """Meta Class for Peewee"""
        database = DATABASE


def idea_callback(ctx, param, value):
    """
    Confirm a string will be a valid idea.

    Returns:
        value: If valid, return the string unharmed.

    Note:
        If the string is invalid, a click BadParameter error
        is raised.
    """
    if isinstance(value, str) and value:
        return value
    elif value:
        raise click.BadParameter("Ideas must be strings!!!")


def create_idea(idea_str):
    """
    Given a string, returns a dictionary entry.

    Arguments:
        idea_str: A string, representing the idea the user has.

    Returns:
        idea_dict: {"text": idea_str}
    """
    return {"text": idea_str}


def save_idea(idea_dict):
    """
    Given an idea dict, save it to an sqlite database in
    the user's home directory under an application folder.
    """
    DATABASE.create_tables([Idea])
    Idea.create(**idea_dict)


def list_ideas():
    """
    Return a list of all ideas that aren't completed but
    are saved in the database.

    Returns:
        idea_list: List containing ideas and IDs
    """
    DATABASE.create_tables([Idea])
    idea_list = []
    for idea in Idea.select():
        idea_list.append("{}: {}".format(idea.id, idea.text))
    return idea_list


def complete_idea(idea_id):
    """
    Complete the idea who's id matches the id of
    idea_id, and is not completed.

    Arguments:
        idea_id: int
    Returns:
        exit_code: 0, if success.
    """
    DATABASE.create_tables([Idea])
    check = Idea.select().where(Idea.id == idea_id)
    if check.exists():
        Idea.delete().where(Idea.id == idea_id).execute()
        return 0
    else:
        raise click.BadParameter("Idea does not exist!")
