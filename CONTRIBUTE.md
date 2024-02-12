# Contribute

Hi there! We're thrilled that you'd like to contribute to the NHS England Data Science website. Your help is essential for keeping it great.

## Creating an issue

If you think of something worth including, improving, or want to contribute, please [raise an issue on GitHub](https://github.com/nhsengland/datascience/issues).

## Submitting a pull request

If you want to contribute to our resources:

1. [Fork][fork] or clone the repository
2. Configure and install the dependencies if you want to run the page in your machine, otherwise none.
3. Create a new branch: `git checkout -b my-branch-name`
4. Make your change
5. Check how your change looks on our website by hosting the website locally (follow [the steps below](#contribute-to-nhs-england-data-science-website) on how to do this)
6. Push to your fork and [submit a pull request][pr]

Your pull request will then be reviewed. You may receive some feedback and suggested changes before it can be approved and your pull request merged.

To increase the likelihood of your pull request being accepted:

- If you are making visual changes, include a screenshot of what the affected element looks like, both before and after.
- Follow the [style guide][style].
- Keep your change as focussed as possible. If there are multiple changes you would like to make that are not dependent upon each other, consider submitting them as separate pull requests.
- Write [good commit messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

## Contribute to NHS England Data Science Website

### Installing MkDocs

Run the commands (or follow the MkDocs documentation to locally pip install MkDocs):

```bash
    pip install -r requirements.txt
```

### Hosting

To host the website locally to view the live changes, run the command:

```bash
    mkdocs serve
```

### Editing the contents

To add a new file to the repository and website:

* Add any files for new pages to the relevant folder in [`docs`](./docs/).
* Add any images you'll use in the [`docs/images`](./docs/images/) folder.
* Because this website uses the `awesome-pages` mkdocs addon, we don't need to update the 'nav' in mkdocs.yml - it will happen automatically when the website is built.
* Don't forget to check that the links, images, headings, and contents are all working correctly on both the website and in the GitHub repo.

The website currently uses the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/getting-started/) theme. This sets the layout, colour, font, search bar, header, footer, navigation bar and contents. You can follow the documentation to make any changes (e.g. change the [colour scheme](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)) as it is simple to use and also easy to overwrite. There is a separate stylesheet, [extra.css](./docs/stylesheets/extra.css), which is used to overwrite the colours, fonts and some of the sizing for some elements.
Here is a good [cheat sheet](https://yakworks.github.io/docmark/cheat-sheet/) for what features can be used in MkDocs and also interesting features in [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/).

#### Blog / Article

Creating new articles / blog posts is easy:
* add a markdown file under the [`docs/articles/posts`](./docs/articles/posts) folder.
    * Note, you do not have to add the blog pages to the `mkdocs.yml` - it gets added to the nav bar automatically.
* add yourself to the [`docs/articles/posts/.authors.yml`], so your face and info appears next to the article.
* The markdown file should have some metadata at the start, like the below. For more info on these parameters, see the [mkdocs material blog plugin guidance](https://squidfunk.github.io/mkdocs-material/plugins/blog/).

```
---
title: Why we’re getting our data teams to RAP
authors: [SamHollings]
date: 2023-01-05
categories:
    - RAP
    - Python
links:
    - https://digital.nhs.uk/blog/data-points-blog/2023/why-were-getting-our-data-teams-to-rap
slug: rap-in-NHSE
description: >
    Reproducible analytical pipelines (RAP) help ensure all published statistics meet the highest standards of transparency and reproducibility. Sam Hollings and Alistair Bullward share their insights on adopting RAP and give advice to those starting out.
---
```

## Resources

- [Contributing to Projects](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)
- [Using Pull Requests](https://help.github.com/articles/using-pull-requests/)
- [GitHub Help](https://help.github.com)

[fork]: https://github.com/pages-themes/slate/fork
[pr]: https://github.com/pages-themes/slate/compare
[style]: http://ben.balter.com/jekyll-style-guide/
