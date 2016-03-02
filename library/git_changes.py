#!/usr/bin/python

import subprocess

def main():
    types = ['major', 'minor', 'patch']
    module = AnsibleModule(
        argument_spec = dict(
            repo_path=dict(required=True),
            exclude_pattern=dict(default=False, required=False),
        ),
        supports_check_mode=False
    )

    repo_path = module.params['repo_path']
    exclude_pattern = module.params['exclude_pattern']

    try:
        if not repo_path:
            raise Exception('Repository path not provided', repo_path)
        
        new = []
        deleted = []
        updated = []
        changes = os.popen("cd "+repo_path+" && git fetch origin --no-tags --prune 2>&1 >/dev/null | grep '\s\->\sorigin\/'").read().splitlines()
        for change in changes:
            search_branch = re.search("->\sorigin\/(.*)$", change)
            if search_branch:
                branch = search_branch.group(1)
            else:    
                continue
                
            if exclude_pattern and re.search(exclude_pattern, branch) is not None: 
                continue                
                                
            if re.search("\[new\sbranch\]", change) is not None:
                branch_diff = os.popen("cd "+repo_path+" && git diff --name-status origin/master origin/"+branch).read().splitlines()
                if branch_diff:
                    new.append(branch)
            elif re.search("\[deleted\]", change) is not None:   
                deleted.append(branch)
            else:
                updated.append(branch)  
    except Exception as error:
        module.fail_json(msg=error.args[0])

    module.exit_json(changed=False, new=new, updated=updated, deleted=deleted)

from ansible.module_utils.basic import *
from ansible.module_utils.known_hosts import *

if __name__ == '__main__':
    main()
