# Contribute

Hi there! We're thrilled that you'd like to contribute to the NHS England Data Science website. Your help is essential for keeping it great.

## Creating an issue

If you think of something worth including, improving, or you find a bug, please [raise an issue on GitHub](https://github.com/nhsengland/datascience/issues).

## Submitting a pull request

If you want to contribute to our resources I would recommend using codespaces directly in github to do this. Guidance is as follows: 
1. If your change constitutes a significant content contribution, before starting with any actual changes, you must go through a content review - follow these [instructions](#content-review)
2. In the repository [homepage](https://github.com/nhsengland/datascience), click the button on the top left which says 'main', then type the name of the branch you want to create, and press create branch
   ![image](https://github.com/user-attachments/assets/f6250b49-d5cf-4a65-8b5f-c02145daab77)
 
3. Click the green code button, then Codespaces, then the '+' symbol to create a new codespace on your branch.
    <img width="1355" alt="Screenshot 2025-03-27 at 14 13 13" src="https://github.com/user-attachments/assets/b68437a3-3f72-467e-8a42-ffb9de7fed29" />
4. This should automatically launch a codespace, which also creates a local version of the website after a minute or so, which you should be able to access in the ports section at the bottom of the codespace.
![image](https://github.com/user-attachments/assets/3192cf0a-acc3-4ca3-876a-9e348621459a)
5. Make any changes you wish to the website here and commit and push as you would in VSCode (guidance specific to project pages and blog can be found below).
6. Check your changes in the local instance to make sure they arent breaking anything and look as you want them to.
7. [Submit a pull request][pr]


If you insist on doing this locally, follow these steps:

1. [Fork][fork] or clone the repository
2. Configure and install the dependencies if you want to run the page in your machine.
3. Create a new branch: `git checkout -b my-branch-name`
4. Make your change
5. Check how your change looks on our website by hosting the website locally (follow [the steps below](#contribute-to-nhs-england-data-science-website) on how to do this)
6. Content Review (follow the [instructions](#content-review))
7. Push to your fork and [submit a pull request][pr]

Contact someone from [Marketing & Comms Function Team](https://nhsd-confluence.digital.nhs.uk/pages/viewpage.action?pageId=351578724) to review your Pull Request. You may receive some feedback and suggested changes before it can be approved and your pull request merged.

**To increase the likelihood of your pull request being accepted:**

- If you are making visual changes, include a screenshot of what the affected element looks like, both before and after.
- Follow the [style guide][style].
- Follow the [accessibility guidance](https://nhsd-confluence.digital.nhs.uk/pages/viewpage.action?pageId=902212969). The most important aspects are to include alt text for images that convey meaning, and null alt text for decorative images, colour not being the only way to convey any of the meaning in your content, descriptive heading and labels, and images aren't used as text (if you have images that convey text meaning, they should be SVGs), and any links have a descriptive text, not just "click here" or "link".
- Keep your change as focused as possible. If there are multiple changes you would like to make that are not dependent upon each other, consider submitting them as separate pull requests.
- Write [good commit messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

## Contribute to NHS England Data Science Website

The best way to check that any changes render correctly on the website is to use a codespace; you can do this from github by clicking on the green "code" button and opening a codespace, or a review using "review in code space" and then when the website has been served after about a minute go to ports and click the forwarded address. For more details on this process see the *"Submitting a pull request"* section above.
 
You can also do it locally which is more complicated and prone to error especially on a corporate device. You can see instructions for that in the *"Submitting a pull request"* section above.

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

- Add any files for new pages to the relevant folder in [`docs`](./docs/).
- Add any images you'll use in the [`docs/images`](./docs/images/) folder.
- Add your page to the appropriate place(s) in [`mkdocs.yml`](mkdocs.yml)
- Don't forget to check that the links, images, headings, and contents are all working correctly on both the website and in the GitHub repo.

The website currently uses the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/getting-started/) theme. This sets the layout, colour, font, search bar, header, footer, navigation bar and contents. You can follow the documentation to make any changes (e.g. change the [colour scheme](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)) as it is simple to use and also easy to overwrite. There is a separate stylesheet, [extra.css](./docs/stylesheets/extra.css), which is used to overwrite the colours, fonts and some of the sizing for some elements.
Here is a good [cheat sheet](https://yakworks.github.io/docmark/cheat-sheet/) for what features can be used in MkDocs and also interesting features in [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/).

### Content Review

Prior to making a pull request, ensure that, if the changes involve a change or addition of content (rather than technical or spelling changes) to the site, you have gone through a content review as outlined [here](https://nhsd-confluence.digital.nhs.uk/display/DAT/C&M:+Website+Gateway). This is to ensure that no sensitive or policy content goes into your PR, as whilst PRs aren't live on the website they are still public (as the repo is public).

### Blog / Article

Creating new articles / blog posts is easy:

- add a markdown file under the [`docs/articles/posts`](./docs/articles/posts) folder.
  - Note, you do not have to add the blog pages to the `mkdocs.yml` - it gets added to the nav bar automatically.
- add yourself to the [`docs/articles/posts/.authors.yml`], so your face and info appears next to the article.
- The markdown file should have some metadata at the start, like the below. For more info on these parameters, see the [mkdocs material blog plugin guidance](https://squidfunk.github.io/mkdocs-material/plugins/blog/). You can also copy it from another blog to make sure you've got it right.

```markdown
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

### Project Page 

- Check out the [project template](https://github.com/nhsengland/datascience/blob/main/docs/our_work/template-project.md) for how to contribute a project page to the website.


## Resources

- [Contributing to Projects](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)
- [Using Pull Requests](https://help.github.com/articles/using-pull-requests/)
- [GitHub Help](https://help.github.com)

[fork]: https://github.com/pages-themes/slate/fork
[pr]: https://github.com/pages-themes/slate/compare
[style]: http://ben.balter.com/jekyll-style-guide/
