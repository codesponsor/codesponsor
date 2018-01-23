# Contributing to Code Sponsor

Contributions to Code Sponsor could come in different forms. Some contribute code
changes, others contribute docs, others help answer questions from users, help
keep the infrastructure running.

We welcome all contributions from folks who are willing to work in good faith
with the community. No contribution is too small and all contributions are
valued.

* [Code of Conduct](#code-of-conduct)
* [Issues](#issues)
* [Discussions And General Help](#discussions-and-general-help)
* [Pull Requests](#pull-requests)
  * [Step 1: Fork](#step-1-fork)
  * [Step 2: Branch](#step-2-branch)
  * [Step 3: Code](#step-3-code)
  * [Step 4: Commit](#step-4-commit)
  * [Step 5: Rebase](#step-5-rebase)

## Code of Conduct
Contributions to Code Sponsor are governed by the [Contributor Covenant version 1.4](https://www.contributor-covenant.org/version/1/4/code-of-conduct.html).
All contributors and participants agree to abide by its terms. To report
violations, shoot out an email to team@codesponsor.io

The Code of Conduct is designed and intended, above all else, to help establish
a culture within the project that allows anyone and everyone who wants to
contribute to feel safe doing so.

Open, diverse, and inclusive communities live and die on the basis of trust.
Contributors can disagree with one another so long as they are done in good
faith and everyone is working towards a common goal.

## Issues
Issues in `codesponsor/codesponsor` are the primary means by which bug reports and
general discussions are made. An contributor is allowed to create an issue,
discuss and provide a fix if needed.

## Discussions And General Help
As Code Sponsor is still at its early stages, drop by
[slack.codesponsor.io](https://slack.codesponsor.io) and say hi to know what's next / to get
your answers cleared up.

## Pull Requests
Pull Requests are the way in which concrete changes are made to the code and
documentation.

## Prerequisites

You must install [pre-commit](https://pre-commit.com/#install) in order to enable our
precommit hooks and `pre-commit install` from your `codesponsor/codesponsor` root directory.

### Step 1: Fork

Fork the project [on GitHub](https://github.com/codesponsor/codesponsor) and clone your
fork locally.

```text
$ git clone git@github.com:username/codesponsor.git
$ cd codesponsor
$ git remote add upstream https://github.com/codesponsor/codesponsor.git
$ git fetch upstream
```

### Step 2: Branch

It's always better to create local branches to work on a specific issue. Makes
life easier for you if you are the kind who enjoys multiple things parallely.
These should also be created directly off of the `master` branch.

```text
$ git checkout -b my-branch -t upstream/master
```

### Step 3: Code

As of now, we don't have any sort of design style / lint to validate things.
So we ask you to ensure all these are met before you shoot out a PR.
- Avoid trailing whitespace & un-necessary white lines
- Indentation is as follows
  - 1 tab = 2 spaces for `.html` files
  - 1 tab = 4 spaces for everything else
  - __Linters will be added to make this easier.__

### Step 4: Commit

1. List all your changes as a list if needed else simply give a brief
  description on what the changes
2. All lines at 100 columns.
3. If your PR fixed an issue, Use the `Fixes:` prefix and the full issue URL.
  For other references use `Refs:`.

   _Example:_
   - `Fixes: https://github.com/codesponsor/codesponsor/issues/23`
   - `Refs: https://github.com/codesponsor/codesponsor/issues/91`

4. _Sample commit A_
   ```txt
   if you can write down the changes explaining it in a paragraph which each
   line wrapped within 100 lines.

   Fixes: https://github.com/codesponsor/codesponsor/issues/87
   Refs: https://github.com/codesponsor/codesponsor/issues/91
   ```

   _Sample commit B_
   ```txt
   - list out your changes as points if there are many changes
   - if needed you can also send it across as
   - all wrapped within 100 lines

   Fixes: https://github.com/codesponsor/codesponsor/issues/87
   Refs: https://github.com/codesponsor/codesponsor/issues/91
   ```
5. [Squashing](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) and
   [Merging](https://git-scm.com/docs/git-merge) your commits to make our
   history neater is always welcomed.

### Step 5: Rebase

Ensure you neat description on what your PR is for, so that it's
easier for folks to understand the gist of it without before jumping to the
the code / doc.

As a best practice, once you have committed your changes, it is a good idea
to use `git rebase` (not `git merge`) to ensure your changes are placed at the
top. Plus merge conflicts can be resolved

```text
$ git fetch upstream
$ git rebase upstream/master
```
