#!/usr/bin/env python


def main():
    module = AnsibleModule(
        argument_spec = dict(
            data = dict(required=True, type='dict'),
        )
    )

    data = module.params['data']

    data['phones'].insert(3, 'unknown')

    module.exit_json(changed=True, data=data)


from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
