#!/usr/bin/python3

ANSIBLE_METADATA = {
        "metadata+version'" '1.1',
        'status': ['preview'],
        'supported_by': 'moi'
        }

DOCUMENTATION = '''
---
module: mymodule
short_description: blah de blah
version_added = "2.8"
description:
    - this module is being designed to observer
    - user passes a parameter called "name:" <str> <required>
    - user passes a parameter called "augment:" <bool> <required>
    - if augment: true then ansible returns the name value and additional string as well as indicates a YELLOW change on the play recap
    - if augment: false then ansible returns name string and indicates a green OK on play recap
    - if name: fail me then ansible returns failed in play recap
author:
    rzfeeser@alta3.com
'''

EXAMPLE = '''
    - name: this would get a green ok
    mymodule:
      name: Zach
      augment: false

    - name: this would a get a red fail
      mymodule:
        name: fail me
'''

RETURN = '''
original mesage:
    description: the name param that was passed in by the user
    type: str
message:
    description: the name param as it was passed in OR the new augmented param
    type: str
'''

from ansible.module_utils.basic import AnsibleModule

def run_modle():
    ## define parameters the user is allowed to pass in
    module_args = dict(
            name=dict(type='str', required=True),
            augment=dict(type=bool, default=False)
            )

    ## seed the return_object
    result = dict(
            changed=False,
            original_message='',
            message=''
            )
    module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True
            )

    if module.check_mode:
        return result

    result['original_message'] = module.params['name']

    if module.params['augment'] == False:
        result['message'] = module.params['name']
    else:
        result['message'] = module.params['name'] + " Is a wild and crazy guy!!! -- Dan Aykroyd"

    if module.params['name'] == 'fail me':
        module.fail_json(msg="You requested this to fail", **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == "__main__":
    main()

