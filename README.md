# pre_ticket pre-commit plugin

**pre_ticket** is a tool written for [pre-commit](https://pre-commit.com/). This hook will automatically add the issue ticket number to your git commit message based on the current branch name.

## Installation

In order to use **pre_ticket** hook, you need to have [pre-commit installed](https://pre-commit.com/#install).

Next, add config file: `.pre-commit-config.yaml` to your project directory if you don't have it setup yet. A ready-to-use example can be found in our repository:

```yaml
repos:
-   repo: git@github.com:deployed/pre_ticket.git
    rev: v1.0.0
    hooks:
    - id:  pre_ticket
      language_version: python3.6
      stages: [commit-msg]
```

In your project dir run `$ pre-commit install` and that's it. You are good to go.

## Default settings and options

By default **pre_ticket** checks against the pattern for branch names like: `feature/123456-some_new_feature` or `chore/123456-do_something`.

The exact regex pattern is: `(feature|bug|chore)/(?P<ticket>[0-9]+)-.*`. 
Based on that the ticket number (i.e. `123456` in the above example) is picked and added to the commit message. 

You can change the regex pattern, by adding the args param to the pre-commit config file. For example:

```yaml
repos:
-   repo: git@github.com:deployed/pre_ticket.git
    rev: v1.0.0
    hooks:
    - id:  pre_ticket
      language_version: python3.6
      stages: [commit-msg]
      args: ['--regex=(feature|bug|chore)/(?P<ticket>[0-9]+)-.*']
```

By default the ticket number is added under the commit message as `Ref: #123456`. You can change this also in the config file:

```yaml
repos:
-   repo: git@github.com:deployed/pre_ticket.git
    rev: v1.0.0
    hooks:
    - id:  pre_ticket
      language_version: python3.6
      stages: [commit-msg]
      args: ['--format={ticket} - {message}']
```

Above example will put the ticket in the beginning of the commit message and separate it with a dash symbol. 

*Note*: You do not need to reinstall the pre-commit hook every time you change the config. It is always used by pre-commit on git commit actions.

# Credits

This project was based on some code primarily provided by [@Overfl0](http://github.com/overfl0) and also in many ways inspired by another pre-commit ticket plugin: [giticket](https://github.com/milin/giticket). 
