import sys
sys.dont_write_bytecode = True

import requests
import os
import time
import json
import base64
import yaml
import xmltodict
import pprint
from datetime import datetime, timezone
from dotenv import load_dotenv


current_time = round(time.time()) # seconds
date = datetime.now(timezone.utc).strftime('%Y-%m-%d') # yyyy-mm-dd
print(f"Epoch: {current_time}")
print(f"Date: {date}")

pp = pprint.PrettyPrinter(indent=4)
# use_test_data = True
use_test_data = False
save_file = True
# save_file = False
# print_logs = True
print_logs = False
pretty_print = False
exit_on_fetch_error = False
exit_on_save_error = False
exit_on_report_error = False
submit_error = True
error_count = 0


load_dotenv()
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")
REDDIT_PROXY = os.environ.get("REDDIT_PROXY")



def fetch(url, method="GET", payload={}, headers={}, retries=2, delay=0, retry_delay=0.5, context="", data_type="json"):
  print(f"Fetch: {url}")
  response = {"status": 0, "attempts": 0, "data": None}
  try: 
    while response["attempts"] <= retries and (response["status"] != 200 or response["data"] == None):
      if (response["attempts"] == 0):
        time.sleep(delay)
      elif (response["attempts"] > 0):
        print(f"Retrying fetch: {url}")
        time.sleep(retry_delay)
      response["attempts"] = response["attempts"] + 1
      r = requests.request(method, url, headers=headers, data=payload)
      if data_type == "json":
        response = {"status": r.status_code, "attempts": response["attempts"], "data": r.json()}
      elif data_type == "xml":
        response = {"status": r.status_code, "attempts": response["attempts"], "data": xml2json(r.text)}
      elif data_type == "yaml" or data_type == "yml":
        response = {"status": r.status_code, "attempts": response["attempts"], "data": yaml.safe_load(r.content.decode("utf-8"))}
      elif data_type == "text":
        response = {"status": r.status_code, "attempts": response["attempts"], "data": r.text}
      else:
        response = {"status": r.status_code, "attempts": response["attempts"], "data": r.text}
  except:
    error = f"Fetch failed: {url}"
    report_error(error, context)
    if exit_on_fetch_error:
      raise SystemExit(error)
    else:
      print(error)
  finally:
    context = f"Fetch response for {url}"
    log(data=response, context=context)
    return response


def save_to_file(rel_path, data, context="", data_type="json"):
  # log(data, context=f"Saving file: {context}")
  log("", context=f"Saving file: {rel_path}")
  # rel_path is relative to project root folder
  # add preceeding "/" to path if not already included
  if not rel_path.startswith("/"):
    rel_path = "/" + rel_path
  abs_path = os.path.abspath(__file__ + "/../../") + rel_path
  # skip file save if using test data
  if use_test_data or not save_file:
    print(f"Save aborted: file save turned off")
    return
  else:
    try:
      # write to file
      with open(abs_path, 'w') as f:
        if data_type == "json":
          json.dump(data, f, indent=None, separators=(',', ':'), ensure_ascii=False)
        else:
          f.write(data)
      f.close()
      print(f"{rel_path} data has been updated")
    except:
      # file is empty or malformed data
      error = f"ERROR: {rel_path} save error"
      report_error(error, context)
      if exit_on_save_error:
        raise SystemExit(error)
      else:
        print(error)


def read_file(rel_path, file_type="json", context=""):
  log(f"Reading file: {rel_path}", context)
  # rel_path is relative to project root folder
  # add preceeding "/" to path if not already included
  if not rel_path.startswith("/"):
    rel_path = "/" + rel_path
  abs_path = os.path.abspath(__file__ + "/../../") + rel_path
  try:
    with open(abs_path, 'r') as f:
      if file_type == "json":
        response = json.load(f)
      elif file_type == "yaml":
        response = yaml.safe_load(f)
      elif file_type == "text":
        response = f.read()
      f.close()
      return response
  except:
    error = f"File read error: {abs_path}"
    report_error(error, context)
    if exit_on_fetch_error:
      raise SystemExit(error)
    else:
      print(error)


def xml2json(xml):
  return xmltodict.parse(xml)


def report_error(error, context=""):
  global error_count
  error_count += 1
  if context == "":
      msg = f"{error}"
  else:
    msg = f"{context}: {error}"
  print(msg)
  if use_test_data and not submit_error:
    return
  else:
    data = {"content": msg}
    attempts = 0
    status = 0
    try:
      while (attempts < 3) and (status < 200 or status >= 300):
        attempts += 1
        r = requests.post(DISCORD_WEBHOOK, json=data)
        status = r.status_code
    except Exception as error:
      error_count += 1
      if exit_on_report_error:
        raise SystemExit(error)
      else:
        print(error)


def print_file(rel_path, file_type="json", context=""):
  # rel_path is relative to project root folder
  data = read_file(rel_path, file_type, context)
  log(data)


def print_path(rel_path):
  # rel_path is relative to project root folder
  abs_path = os.path.abspath(__file__ + "/../../") + rel_path
  print(abs_path)


def log(data, context=None):
  if print_logs:
    if context:
      print(f"{context}:")
    if pretty_print:
      pp.pprint(data)
    else:
      print(data)


def pprint(data):
  pp.pprint(data)


def sendDiscordMsg(msg):
  print(msg)
  # if use_test_data:
  #   print(msg)
  # else:
  #   data = {"content": msg}
  #   attempts = 0
  #   status = 0
  #   try:
  #     while (attempts < 3) and (status < 200 or status >= 300):
  #       attempts += 1
  #       r = requests.post(DISCORD_WEBHOOK, json=data)
  #       status = r.status_code
  #   except Exception as error:
  #     report_error(error, f"sendDiscordMsg: {msg}")
  #     if exit_on_report_error:
  #       raise SystemExit(error)
  #     else:
  #       print(error)




