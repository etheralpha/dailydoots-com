# dailydoots-com

This is the source code for <https://dailydoots.com>.

## Local Development

1. Clone the repo (or fork the repo to your account)
1. Install dependencies: `bundle install`
1. Create a feature branch off of the `main` branch
1. Start the local server: `bundle exec jekyll serve`
1. Go to <http://localhost:4400/> to view changes

To build the site use `bundle exec jekyll build`.

Resources:

- [Jekyll Docs](https://jekyllrb.com/docs/)
- [Liquid Syntax](https://shopify.github.io/liquid/basics/introduction/)



## Integrate Data

To use this data, simply query one of the following endpoints:

- Dailies - https://dailydoots.com/dailies.json (updates 30min after midnight UTC+0)
- Doots - https://dailydoots.com/doots.json (updates once a week Fridays 2pm EST)
- Profiles - https://dailydoots.com/profiles.json (updated as needed)

Please do not abuse these endpoints. Checking once or twice a day would be sufficient given the update frequency.



## Contributing

Most of the content resides in data files withing `_data`. If you'd like to update your user profile edit/add an entry in `_data/profiles.yml` or send a DM to u/hanniabu on Reddit.


**Weekly Update**

1. Update the leaderboard by uploading the RES file from u/jtnichol to [this tool](https://dailydoots.com/tools/), copying the resulting JSON output, and saving it to `_data/doots.json` replacing the existing contents.
1. Update podcast guest list in `_data/guests.yml`, remove or comment out old items if necessary
1. Update announcement list in `_data/announcements.yml`, remove or comment out old items if necessary
1. Update events list in `_data/events.yml`, remove or comment out old items if necessary
1. Update the weekly roundup:
    1. Create a `.md` file under `weekly/historical` named after the weekly roundup date in `yyyy-mm-dd.md` format
    1. Copying the contents template (`weekly/_template`) into this new file
    1. Update the metadata at the top
        - If there is no podcast then just enter the `date` and `weekly_link` and leave the rest empty
        - `weekly_link` should have no subdomain specific, so `reddit.com` instead of `old.reddit.com` or `www.reddit.com`
        - `date` follows `yyyy-mm-dd` format
        - `episode` is just the podcast episode number, do not include a `#`
    1. Copy over the weekly doots
        1. For each item copy the item text and paste into the `<summary> {{paste here}} </summary>` tags
        1. Copy the comment links into the `[View on Reddit →]( {{paste here}} )` field
        1. View the comment under `old.reddit.com` using the RES extention to copy the comment "source" (markdown) and paste the in the area below "View on Reddit" and before the closing `</details>` tag
        1. Bare links (non hyperlinked) need to be wrapped in `< {{link}} >` to properly be converted to a hyperlink
        1. You'll need to copy the templated `<details> ... </details>` sections for each of the weekly doots, there's a separate template for single and double doots (double doots means it references 2 comments)
        1. Do a find/replace to replace all instances of `old.reddit.com` or `www.reddit.com` with `reddit.com`



## Miscellaneous Info

- [r/ethfinance initiation thread](https://reddit.com/r/ethtrader/comments/cs84ar/6_of_10_moderators_are_leaving_ethtrader_a/)
- r/ethfinance creation on 2019-01-22 by u/dcinvestor
- Sub stats
    - https://subredditstats.com/r/ethfinance
    - https://subredditstats.com/r/ethereum
- [PushShift Archive](https://api.pushshift.io/reddit/search/comment?author=ethfinance)

