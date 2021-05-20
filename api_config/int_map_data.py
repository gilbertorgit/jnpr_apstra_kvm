
########################################################
########################################################

""" -------------- Interface Maps """

data_JNPR_vQFX_7_10_Spine = f'''{{
  "logical_device_id": "JNPR-7x10-Spine",
  "device_profile_id": "Juniper_vQFX",
  "id": "JNPR_vQFX-7x10-Spine",
  "label": "JNPR_vQFX-7x10-Spine",
  "interfaces": [
    {{
      "name": "xe-0/0/0",
      "roles": [
        "superspine",
        "leaf"
      ],
      "mapping": [
        1,
        1,
        1,
        1,
        1
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 1,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/1",
      "roles": [
        "superspine",
        "leaf"
      ],
      "mapping": [
        2,
        1,
        1,
        1,
        2
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 2,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/2",
      "roles": [
        "superspine",
        "leaf"
      ],
      "mapping": [
        3,
        1,
        1,
        1,
        3
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 3,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/3",
      "roles": [
        "superspine",
        "leaf"
      ],
      "mapping": [
        4,
        1,
        1,
        1,
        4
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 4,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/4",
      "roles": [
        "superspine",
        "leaf"
      ],
      "mapping": [
        5,
        1,
        1,
        1,
        5
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 5,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/5",
      "roles": [
        "external_router"
      ],
      "mapping": [
        6,
        1,
        1,
        1,
        6
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 6,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/6",
      "roles": [
        "external_router"
      ],
      "mapping": [
        7,
        1,
        1,
        1,
        7
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 7,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/7",
      "roles": [
        "unused"
      ],
      "mapping": [
        8,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 8,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/8",
      "roles": [
        "unused"
      ],
      "mapping": [
        9,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 9,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/9",
      "roles": [
        "unused"
      ],
      "mapping": [
        10,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 10,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/10",
      "roles": [
        "unused"
      ],
      "mapping": [
        11,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 11,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/11",
      "roles": [
        "unused"
      ],
      "mapping": [
        12,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 12,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }}
  ]
}}'''


data_JNPR_vQFX_7_10_SuperSpine = f'''{{
  "logical_device_id": "JNPR-7x10-SuperSpine",
  "device_profile_id": "Juniper_vQFX",
  "id": "JNPR_vQFX-7x10-SuperSpine",
  "label": "JNPR_vQFX-7x10-SuperSpine",
  "interfaces": [
    {{
      "name": "xe-0/0/0",
      "roles": [
        "spine"
      ],
      "mapping": [
        1,
        1,
        1,
        1,
        1
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 1,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/1",
      "roles": [
        "spine"
      ],
      "mapping": [
        2,
        1,
        1,
        1,
        2
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 2,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/2",
      "roles": [
        "spine"
      ],
      "mapping": [
        3,
        1,
        1,
        1,
        3
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 3,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/3",
      "roles": [
        "spine"
      ],
      "mapping": [
        4,
        1,
        1,
        1,
        4
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 4,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/4",
      "roles": [
        "spine"
      ],
      "mapping": [
        5,
        1,
        1,
        1,
        5
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 5,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/5",
      "roles": [
        "external_router"
      ],
      "mapping": [
        6,
        1,
        1,
        1,
        6
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 6,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/6",
      "roles": [
        "external_router"
      ],
      "mapping": [
        7,
        1,
        1,
        1,
        7
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 7,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/7",
      "roles": [
        "unused"
      ],
      "mapping": [
        8,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 8,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/8",
      "roles": [
        "unused"
      ],
      "mapping": [
        9,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 9,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/9",
      "roles": [
        "unused"
      ],
      "mapping": [
        10,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 10,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/10",
      "roles": [
        "unused"
      ],
      "mapping": [
        11,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 11,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/11",
      "roles": [
        "unused"
      ],
      "mapping": [
        12,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 12,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }}
  ]
}}'''


data_JNPR_vQFX_8_10_BorderLeaf = f'''{{
  "logical_device_id": "JNPR-8x10-BorderLeaf",
  "device_profile_id": "Juniper_vQFX",
  "id": "JNPR_vQFX_8x10-BorderLeaf",
  "label": "JNPR_vQFX_8x10-BorderLeaf",
  "interfaces": [
    {{
      "name": "xe-0/0/0",
      "roles": [
        "spine"
      ],
      "mapping": [
        1,
        1,
        1,
        1,
        1
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 1,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/1",
      "roles": [
        "spine"
      ],
      "mapping": [
        2,
        1,
        1,
        1,
        2
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 2,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/2",
      "roles": [
        "spine"
      ],
      "mapping": [
        3,
        1,
        1,
        1,
        3
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 3,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/3",
      "roles": [
        "spine"
      ],
      "mapping": [
        4,
        1,
        1,
        1,
        4
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 4,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/4",
      "roles": [
        "peer"
      ],
      "mapping": [
        5,
        1,
        1,
        1,
        5
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 5,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/5",
      "roles": [
        "peer"
      ],
      "mapping": [
        6,
        1,
        1,
        1,
        6
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 6,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/6",
      "roles": [
        "external_router"
      ],
      "mapping": [
        7,
        1,
        1,
        1,
        7
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 7,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/7",
      "roles": [
        "external_router"
      ],
      "mapping": [
        8,
        1,
        1,
        1,
        8
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 8,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/8",
      "roles": [
        "unused"
      ],
      "mapping": [
        9,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 9,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/9",
      "roles": [
        "unused"
      ],
      "mapping": [
        10,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 10,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/10",
      "roles": [
        "unused"
      ],
      "mapping": [
        11,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 11,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/11",
      "roles": [
        "unused"
      ],
      "mapping": [
        12,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 12,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }}
  ]
}}'''

data_JNPR_vQFX_10_10_Leaf = f'''{{
  "logical_device_id": "JNPR-10x10-Leaf",
  "device_profile_id": "Juniper_vQFX",
  "id": "JNPR_vQFX_10x10-Leaf",
  "label": "JNPR_vQFX_10x10-Leaf",
  "interfaces": [
    {{
      "name": "xe-0/0/0",
      "roles": [
        "spine"
      ],
      "mapping": [
        1,
        1,
        1,
        1,
        1
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 1,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/1",
      "roles": [
        "spine"
      ],
      "mapping": [
        2,
        1,
        1,
        1,
        2
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 2,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/2",
      "roles": [
        "peer"
      ],
      "mapping": [
        3,
        1,
        1,
        1,
        3
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 3,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/3",
      "roles": [
        "peer"
      ],
      "mapping": [
        4,
        1,
        1,
        1,
        4
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 4,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/4",
      "roles": [
        "l2_server",
        "access",
        "l3_server"
      ],
      "mapping": [
        5,
        1,
        1,
        1,
        5
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 5,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/5",
      "roles": [
        "l2_server",
        "access",
        "l3_server"
      ],
      "mapping": [
        6,
        1,
        1,
        1,
        6
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 6,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/6",
      "roles": [
        "l2_server",
        "access",
        "l3_server"
      ],
      "mapping": [
        7,
        1,
        1,
        1,
        7
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 7,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/7",
      "roles": [
        "l2_server",
        "access",
        "l3_server"
      ],
      "mapping": [
        8,
        1,
        1,
        1,
        8
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 8,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/8",
      "roles": [
        "external_router"
      ],
      "mapping": [
        9,
        1,
        1,
        1,
        9
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 9,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/9",
      "roles": [
        "external_router"
      ],
      "mapping": [
        10,
        1,
        1,
        1,
        10
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 10,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/10",
      "roles": [
        "unused"
      ],
      "mapping": [
        11,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 11,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }},
    {{
      "name": "xe-0/0/11",
      "roles": [
        "unused"
      ],
      "mapping": [
        12,
        1,
        1,
        null,
        null
      ],
      "state": "active",
      "setting": {{
        "param": "{{\\"interface\\": {{\\"speed\\": \\"\\"}}, \\"global\\": {{\\"speed\\": \\"\\"}}}}"
      }},
      "position": 12,
      "speed": {{
        "unit": "G",
        "value": 10
      }}
    }}
  ]
}}'''