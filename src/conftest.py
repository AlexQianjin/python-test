import pytest
import re
import json
import requests
from py.xml import html
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

def get_str_from_html(html):
    p = re.compile('<.+>(\d+.+)<.+>')
    m = p.match(html)
    g = m.group(1)
    
    return g

def send_test_summary_to_teams(summary):
    message = {
        '@type': 'MessageCard',
        '@context': 'http://schema.org/extensions',
        'themeColor': '0076D7',
        'summary': 'Enterprise Learning Automation',
        'sections': [
            {
                'activityTitle': f'**Enterprise Learning Automation** | Test plan run completed at {datetime.now()}',
                'activitySubtitle': summary[0],
                'markdown': True,
                'facts': [
                    {
                        'name': summary[1]
                    },
                    {
                        'name': summary[2]
                    },
                    {
                        'name': summary[3]
                    },
                    {
                        'name': summary[4]
                    },
                    {
                        'name': summary[5]
                    },
                    {
                        'name': summary[6]
                    }
                ]
            }
        ]
    }

    json_str = json.dumps(message)
    TEAMS_WEBHOOK_URL=os.getenv('TEAMS_WEBHOOK_URL')
    print(TEAMS_WEBHOOK_URL)
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Content-Length': str(len(json_str))}   
    r = requests.post(TEAMS_WEBHOOK_URL, data=json_str, headers=headers)
    print(r.text)
    print(r.status_code)
    print(r.request.body)

def pytest_html_report_title(report):
    report.title = 'ACTC Automation Test Result'

def pytest_html_results_summary(prefix, summary, postfix):
    summary_result = []
    summary_result.append(get_str_from_html(str(summary[0])))
    summary_result.append(get_str_from_html(str(summary[3])))
    summary_result.append(get_str_from_html(str(summary[6])))
    summary_result.append(get_str_from_html(str(summary[9])))
    summary_result.append(get_str_from_html(str(summary[12])))
    summary_result.append(get_str_from_html(str(summary[15])))
    summary_result.append(get_str_from_html(str(summary[18])))

    send_test_summary_to_teams(summary_result)
