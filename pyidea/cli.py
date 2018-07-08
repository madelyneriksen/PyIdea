# -*- coding: utf-8 -*-

"""Console script for pyidea."""
import click
from pyidea.pyidea import create_idea, save_idea, list_ideas
from pyidea.pyidea import complete_idea
from pyidea.pyidea import idea_callback


@click.command()
@click.option("--show", "-s", is_flag=True, help="List all saved ideas.")
@click.option("--complete", "-c", default=0,
              help="Complete/delete an idea by ID.")
@click.option("--new", "-n", default="", callback=idea_callback,
              help="Save a new idea.", required=False)
def main(show, complete, new):
    """
    PyIdea stores ideas for safe keeping in a simple way. Ideas are
    stored in the user's home folder.

    Create a new idea like this:\n
    $ pyidea --new "My Awesome Idea"
    """
    exit_code = 0
    # New Ideas
    if new:
        idea_object = create_idea(new)
        exit_code = 0
        save_idea(idea_object)
        click.echo("Idea saved!")
    # Showing Ideas
    if show:
        ideas = list_ideas()
        if ideas:
            click.echo("Here are your active ideas:")
            for idea in ideas:
                click.echo(idea)
                exit_code = 0
        else:
            click.echo("You have no active ideas!")
    # Complete Ideas
    if complete:
        exit_code = complete_idea(complete)
        if exit_code == 0:
            click.echo("Completed idea %s!" % complete)
    return exit_code


if __name__ == "__main__":
    main()  # pragma: no cover
