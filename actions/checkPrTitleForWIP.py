"""
Github Action: comment on PRs that have WIP.
"""

import json
import os

import github

def main():
    """Triggers on PR edit/open/reopen."""

    gh = github.Github(os.getenv('GITHUB_TOKEN'))
    event = json.load(open(os.getenv('GITHUB_EVENT_PATH')))
    if 'WIP' in event['pull_request']['title']:
        repo = gh.get_repo(event['repository']['full_name'])
        issue = repo.get_issue(event['pull_request']['number'])
        comment = ('Hi @' + event['pull_request']['user']['login'] + ' '
                   'We typically do not want WIP PRs since each push will '
                   'make the Travis queue unnecessarily long. If you need '
                   'to run automated tests, please see our guides:'
                   'please see our guides: '
                   'https://github.com/oppia/oppia/wiki/'
                   'Setup-your-own-CircleCI-instance '
                   'https://github.com/oppia/oppia/wiki/'
                   'Setup-your-own-Travis-instance '
                   'Thanks!')
        issue.create_comment(comment)

if __name__ == '__main__':
    main()
