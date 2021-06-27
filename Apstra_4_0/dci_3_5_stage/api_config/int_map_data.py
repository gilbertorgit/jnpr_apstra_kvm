"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""
""" -------------- Interface Maps """


def create_interface_map_dic():

    interface_map_data_dic = {'JNPR_vQFX-7x10-Spine': {'name': 'JNPR_vQFX-7x10-Spine',
                                                       'data': f'''{{
                            "device_profile_id": "Juniper_vQFX",
                            "label": "JNPR_vQFX-7x10-Spine",
                            "id": "JNPR_vQFX-7x10-Spine",
                            "logical_device_id": "JNPR-7x10-Spine",
                            "interfaces": [
                                {{
                                    "mapping": [
                                        1,
                                        1,
                                        1,
                                        1,
                                        1
                                    ],
                                    "name": "xe-0/0/0",
                                    "position": 1,
                                    "roles": [
                                        "superspine",
                                        "leaf"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        2,
                                        1,
                                        1,
                                        1,
                                        2
                                    ],
                                    "name": "xe-0/0/1",
                                    "position": 2,
                                    "roles": [
                                        "superspine",
                                        "leaf"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        3,
                                        1,
                                        1,
                                        1,
                                        3
                                    ],
                                    "name": "xe-0/0/2",
                                    "position": 3,
                                    "roles": [
                                        "superspine",
                                        "leaf"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        4,
                                        1,
                                        1,
                                        1,
                                        4
                                    ],
                                    "name": "xe-0/0/3",
                                    "position": 4,
                                    "roles": [
                                        "superspine",
                                        "leaf"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        5,
                                        1,
                                        1,
                                        1,
                                        5
                                    ],
                                    "name": "xe-0/0/4",
                                    "position": 5,
                                    "roles": [
                                        "superspine",
                                        "leaf"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        6,
                                        1,
                                        1,
                                        1,
                                        6
                                    ],
                                    "name": "xe-0/0/5",
                                    "position": 6,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        7,
                                        1,
                                        1,
                                        1,
                                        7
                                    ],
                                    "name": "xe-0/0/6",
                                    "position": 7,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        8,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/7",
                                    "position": 8,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        9,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/8",
                                    "position": 9,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        10,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/9",
                                    "position": 10,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        11,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/10",
                                    "position": 11,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        12,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/11",
                                    "position": 12,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }}
                            ]
                            }}'''},
                              'JNPR_vQFX_7x10-SuperSpine': {'name': 'JNPR_vQFX_7x10-SuperSpine',
                                                       'data': f'''{{
                            "device_profile_id": "Juniper_vQFX",
                            "label": "JNPR_vQFX_7x10-SuperSpine",
                            "id": "JNPR_vQFX_7x10-SuperSpine",
                            "logical_device_id": "JNPR-7x10-SuperSpine",
                            "interfaces": [
                                {{
                                    "mapping": [
                                        1,
                                        1,
                                        1,
                                        1,
                                        1
                                    ],
                                    "name": "xe-0/0/0",
                                    "position": 1,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        2,
                                        1,
                                        1,
                                        1,
                                        2
                                    ],
                                    "name": "xe-0/0/1",
                                    "position": 2,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        3,
                                        1,
                                        1,
                                        1,
                                        3
                                    ],
                                    "name": "xe-0/0/2",
                                    "position": 3,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        4,
                                        1,
                                        1,
                                        1,
                                        4
                                    ],
                                    "name": "xe-0/0/3",
                                    "position": 4,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        5,
                                        1,
                                        1,
                                        1,
                                        5
                                    ],
                                    "name": "xe-0/0/4",
                                    "position": 5,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        6,
                                        1,
                                        1,
                                        1,
                                        6
                                    ],
                                    "name": "xe-0/0/5",
                                    "position": 6,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        7,
                                        1,
                                        1,
                                        1,
                                        7
                                    ],
                                    "name": "xe-0/0/6",
                                    "position": 7,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        8,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/7",
                                    "position": 8,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        9,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/8",
                                    "position": 9,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        10,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/9",
                                    "position": 10,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        11,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/10",
                                    "position": 11,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        12,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/11",
                                    "position": 12,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }}
                            ]
                            }}'''},
                              'JNPR_vQFX-8x10-BorderLeaf': {'name': 'JNPR_vQFX-8x10-BorderLeaf',
                                                            'data': f'''{{
                            "device_profile_id": "Juniper_vQFX",
                            "label": "JNPR_vQFX-8x10-BorderLeaf",
                            "id": "JNPR_vQFX-8x10-BorderLeaf",
                            "logical_device_id": "JNPR-8x10-BorderLeaf",
                            "interfaces": [
                                {{
                                    "mapping": [
                                        1,
                                        1,
                                        1,
                                        1,
                                        1
                                    ],
                                    "name": "xe-0/0/0",
                                    "position": 1,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        2,
                                        1,
                                        1,
                                        1,
                                        2
                                    ],
                                    "name": "xe-0/0/1",
                                    "position": 2,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        3,
                                        1,
                                        1,
                                        1,
                                        3
                                    ],
                                    "name": "xe-0/0/2",
                                    "position": 3,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        4,
                                        1,
                                        1,
                                        1,
                                        4
                                    ],
                                    "name": "xe-0/0/3",
                                    "position": 4,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        5,
                                        1,
                                        1,
                                        1,
                                        5
                                    ],
                                    "name": "xe-0/0/4",
                                    "position": 5,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        6,
                                        1,
                                        1,
                                        1,
                                        6
                                    ],
                                    "name": "xe-0/0/5",
                                    "position": 6,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        7,
                                        1,
                                        1,
                                        1,
                                        7
                                    ],
                                    "name": "xe-0/0/6",
                                    "position": 7,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        8,
                                        1,
                                        1,
                                        1,
                                        8
                                    ],
                                    "name": "xe-0/0/7",
                                    "position": 8,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        9,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/8",
                                    "position": 9,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        10,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/9",
                                    "position": 10,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        11,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/10",
                                    "position": 11,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        12,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/11",
                                    "position": 12,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }}
                            ]
                            }}'''},
                              'JNPR_vQFX-10x10-Leaf': {'name': 'JNPR_vQFX-10x10-Leaf',
                                                            'data': f'''{{
                            "device_profile_id": "Juniper_vQFX",
                            "label": "JNPR_vQFX-10x10-Leaf",
                            "id": "JNPR_vQFX-10x10-Leaf",
                            "logical_device_id": "JNPR-10x10-Leaf",
                            "interfaces": [
                                {{
                                    "mapping": [
                                        1,
                                        1,
                                        1,
                                        1,
                                        1
                                    ],
                                    "name": "xe-0/0/0",
                                    "position": 1,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        2,
                                        1,
                                        1,
                                        1,
                                        2
                                    ],
                                    "name": "xe-0/0/1",
                                    "position": 2,
                                    "roles": [
                                        "spine"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        3,
                                        1,
                                        1,
                                        1,
                                        3
                                    ],
                                    "name": "xe-0/0/2",
                                    "position": 3,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        4,
                                        1,
                                        1,
                                        1,
                                        4
                                    ],
                                    "name": "xe-0/0/3",
                                    "position": 4,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        5,
                                        1,
                                        1,
                                        1,
                                        5
                                    ],
                                    "name": "xe-0/0/4",
                                    "position": 5,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        6,
                                        1,
                                        1,
                                        1,
                                        6
                                    ],
                                    "name": "xe-0/0/5",
                                    "position": 6,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        7,
                                        1,
                                        1,
                                        1,
                                        7
                                    ],
                                    "name": "xe-0/0/6",
                                    "position": 7,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        8,
                                        1,
                                        1,
                                        1,
                                        8
                                    ],
                                    "name": "xe-0/0/7",
                                    "position": 8,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        9,
                                        1,
                                        1,
                                        1,
                                        9
                                    ],
                                    "name": "xe-0/0/8",
                                    "position": 9,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        10,
                                        1,
                                        1,
                                        1,
                                        10
                                    ],
                                    "name": "xe-0/0/9",
                                    "position": 10,
                                    "roles": [
                                        "generic"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        11,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/10",
                                    "position": 11,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }},
                                {{
                                    "mapping": [
                                        12,
                                        1,
                                        1,
                                        null,
                                        null
                                    ],
                                    "name": "xe-0/0/11",
                                    "position": 12,
                                    "roles": [
                                        "unused"
                                    ],
                                    "setting": {{
                                        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
                                    }},
                                    "speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "state": "active"
                                }}
                            ]
                            }}'''},
                            }

    return interface_map_data_dic











