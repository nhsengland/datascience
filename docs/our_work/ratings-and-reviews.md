---
title: "NHS.UK: Automatic Moderation of Ratings & Reviews"
summary: "Using NLP to reduce the average moderation time on the NHS.UK website from days to seconds "
origin: ""
tags: ["NLP", "AI", "ML", "NHS.UK"]
---

The NHS.UK website receives around a hundred thousand reviews every year. These reviews need moderating -- there's [a set of NHS policies which need to be applied to these](https://www.nhs.uk/our-policies/comments-policy/#:~:text=Users%20should%20only%20post%20one,service%20will%20not%20be%20published.) before they can be published.

This project automates much of that work. We use machine learning models - some built by us, some open-source - to make decisions about the different rules which need to be enforced. Users now receive instant feedback on when a review violates a rule, allowing them to edit and re-submit their review without delay. This reduces the average moderation time from days to seconds, makes for more reliable and consistent moderation, and creates a much more scalable service.

Taking a ground truth from expert moderators, our models perform comparably to the people who used to do the moderation[^1] manually. If a user disagrees with a decision our AI makes, there's still a human-in-the-loop who can make a final moderation decision.

[^1]: Prior to this project, the moderation work was done manually by a third-party company, hired on a fixed-term contract.

![Flow of reviews in automoderation](../images/ratings_reviews/reviews_uk_website_query_diagram_flowchart.excalidraw.png)

The flow follows four stages:

1. The review text is submitted to the website.
2. The Flask app contains the logic of the rules which are to be applied. Some of these rules are applied directly, on the Flask app compute.

3. More complicated rules (such as detecting safeguarding concerns) are applied by models which are deployed independently of the Flask app. Here the Flask app sends queries to each of these, they evaluate the text, and send a response.

4. The Flask app now has an answer for each of the rules which are to be applied, and can send a final response to the NHS.UK website.

If there's anything amiss, the website will produce a response informing the user (the person leaving the review) which rule has been broken. This ranges from asking the reviewer to remove something (such as a name) from a review, to directing them to resources specific to the content of their review. For most cases, the user has the opportunity to edit and re-submit their review.
[The reviews policy is here.](https://www.nhs.uk/our-policies/comments-policy/)

## Results

- Reduced moderation time from days to seconds.
- Gives users opportunity to edit reviews when rules are broken, which increases the proportion of reviews which will get published.
- Service is much more scaleable now - no longer constrained by moderation capacity.
- All models match or out-perform the way the work was done before.
- First AI product to gain clinical approval within NHS.UK.

## Outputs

| Output                             | Link                                                                 |
| ---------------------------------- | -------------------------------------------------------------------- |
| Published Repo for Flask app       | [Github Repo](https://github.com/nhsengland/nhsuk.moderation-api)  (will be published soon) |
| Published Repo for our models       | Coming soon   |
<!-- | Published repo for creating models | [Github Repo](PUT LINK HERE) | -->

[comment]: <> (The below header stops the title from being rendered (as mkdocs adds it to the page from the "title" attribute) - this way we can add it in the main.html, along with the summary.)
#
