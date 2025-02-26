import utilities
import time
import datetime
import json
import os


def run_app():
  # get_daily_details(["https://reddit.com/r/ethfinance/comments/kos3ok/"])
  # print(get_recent_daily())
  # dailies = [{'date': '2025-02-25', 'title': 'Daily General Discussion - February 25, 2025', 'link': 'https://reddit.com/r/ethereum/comments/1ixp2ge/', 'comments': '4'}, {'date': '2025-02-24', 'title': 'Daily General Discussion - February 24, 2025', 'link': 'https://reddit.com/r/ethereum/comments/1iww3r0/', 'comments': '422'}, {'date': '2025-02-23', 'title': 'Daily General Discussion - February 23, 2025', 'link': 'https://reddit.com/r/ethereum/comments/1iw4ccq/', 'comments': '239'}, {'date': '2025-02-22', 'title': 'Daily General Discussion - February 22, 2025', 'link': 'https://reddit.com/r/ethereum/comments/1ivczmq/', 'comments': '323'}, {'date': '2025-02-21', 'title': 'Daily General Discussion - February 21, 2025', 'link': 'https://reddit.com/r/ethereum/comments/1iukyyr/', 'comments': '581'}]
  dailies = get_recent_daily()
  if len(dailies) > 0:
    update_dailies(dailies)




def get_recent_daily():
  daily_list = []
  daily_yml = ""
  weeklies_list = []
  weeklies_yml = ""
  delay = 60
  url = utilities.REDDIT_PROXY
  source = utilities.fetch(url=url, data_type="json", retry_delay=delay)
  print(f"status: {source['status']}")
  if source['status'] != 200:
    return
  entries = source['data']['data']['children']
  # print(entries)
  # print(len(entries))
  # print("-----------")
  for entry in entries:
    epoch = entry['data']['created_utc']
    date = datetime.datetime.utcfromtimestamp(epoch).strftime('%Y-%m-%d')
    title = entry['data']['title']
    link = f"https://reddit.com/r/ethereum/comments/{entry['data']['id']}/"
    comments = entry['data']['num_comments']
    entry_yml = f"- date: {date}\n  title: {title}\n  link: {link}\n  comments: {comments}\n"
    entry_dict = {"date":date, "title":title, "link":link, "comments":comments}
    if "daily_general_discussion" in entry['data']['permalink']:
      daily_list.append(entry_dict)
      daily_yml += entry_yml
    if "weekly_discussion_thread" in entry['data']['permalink']:
      weeklies_list.append(entry_dict)
      weeklies_yml += entry_yml
  # print(daily_yml)
  # print("-----------")
  # print(weeklies_yml)
  # print("-----------")
  print(daily_list)
  # daily_list = sorted(daily_list, key=lambda x: x['date'], reverse=True)
  return daily_list[:5]




# def get_recent_daily():
#   entries_list = []
#   entries_yml = ""
#   weeklies_list = []
#   delay = 60
#   url = "https://old.reddit.com/user/EthereumDailyThread/submitted/"
#   source = utilities.fetch(url=url, data_type="text", retry_delay=delay)
#   print(f"status: {source['status']}")
#   if source['status'] != 200:
#     return
#   entries = source['data'].split('thing id')
#   entries.pop(0)
#   # print(entries)
#   # print("-----------")
#   for entry in entries:
#     date = entry.split('datetime="')[1].split('T')[0]
#     title = entry.split('tabindex="1"')[1].split('<')[0].split('>')[1]
#     link = entry.split('data-url="')[1].split('"')[0].split('daily')[0]
#     link = f"https://reddit.com{link}"
#     comments = entry.split('data-event-action="comments"')[1].split(' comments</')[0].split('>')[1]
#     entry_yml = f"- date: {date}\n  title: {title}\n  link: {link}\n  comments: {comments}\n"
#     entries_yml += entry_yml
#     entry_dict = {"date":date, "title":title, "link":link, "comments":comments}
#     if "daily" in entry_dict['title'].lower():
#       entries_list.append(entry_dict)
#     if "weekly" in entry_dict['link'].lower():
#       weeklies_list.append(entry_dict)
#   print(entries_yml)
#   # print("-----------")
#   # print(entries_list)
#   # entries_list = sorted(entries_list, key=lambda x: x['date'], reverse=True)
#   return entries_list[:5]




def update_dailies(new_dailies):
  # load old dailies list
  repo_root = os.path.abspath(__file__ + '/../../')
  dailies_path = repo_root + '/_data/dailies.json'
  with open(dailies_path, 'r') as dailies_file:
    dailies = json.load(dailies_file)
  print(f"dailies count: {len(dailies)}")
  print(dailies[:5])

  # merge new and old daily data
  for new_daily in new_dailies:
    included = False
    for daily in dailies:
      if daily['link'] == new_daily['link']:
        included = True
        daily['comments'] = new_daily['comments']
    if included == False:
      dailies.append(new_daily)

  # sort list by date, recent first
  dailies = sorted(dailies, key=lambda x: x['date'], reverse=True)
  print(f"updated dailies count: {len(dailies)}")
  print(dailies[:5])

  # save file
  with open(dailies_path, "w") as dailies_file:
    json.dump(dailies, dailies_file)




def get_daily_details(url_list):
  entries_list = []
  entries_yml = ""
  delay = 60
  for url in url_list:
    url = url.replace('https://reddit.com', 'https://old.reddit.com')
    # url = url.replace('https://reddit.com', 'https://np.reddit.com')
    source = utilities.fetch(url=url, data_type="text", retry_delay=delay)
    print(f"status: {source['status']}")
    if source['status'] != 200:
      return
    date = source['data'].split('<time datetime="')[1].split('</time>')[0].split('T')[0]
    title = source['data'].split('<title>')[1].split('</title>')[0].split(' : ')[0]
    link = url.split('reddit.com')[1]
    link = f"https://reddit.com{link}"
    comments = source['data'].split('data-event-action="comments"')[1].split(' comments</')[0].split('>')[1]
    entry_yml = f"- date: {date}\n  title: {title}\n  link: {link}\n  comments: {comments}\n"
    entries_yml += entry_yml
    entry_dict = {"date":date, "title":title, "link":link, "comments":comments}
    entries_list.append(entry_dict)
    print(entries_yml)
    print("-----------")
    print(entries_list)
    time.sleep(delay)


run_app()
print(f"Error count: {utilities.error_count}")

