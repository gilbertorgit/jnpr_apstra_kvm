"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""
# Design Data

data_JNPR_7_10_Spine = f'''{{
    "display_name": "JNPR-7x10-Spine",
    "id": "JNPR-7x10-Spine",
    "panels": [
        {{
            "panel_layout": {{
                "column_count": 7,
                "row_count": 1
            }},
            "port_groups": [
                {{
                    "count": 5,
                    "roles": [
                        "superspine",
                        "leaf"
                    ],
                    "speed": {{
                        "unit": "G",
                        "value": 10
                    }}
                }},
                {{
                    "count": 2,
                    "roles": [
                        "generic"
                    ],
                    "speed": {{
                        "unit": "G",
                        "value": 10
                    }}
                }}
            ],
            "port_indexing": {{
                "order": "T-B, L-R",
                "schema": "absolute",
                "start_index": 1
            }},
            "selected-port-count": 2
        }}
    ]
}}'''

data_JNPR_7_10_SuperSpine = f'''{{
    "display_name": "JNPR-7x10-SuperSpine",
    "id": "JNPR-7x10-SuperSpine",
    "panels": [
        {{
            "panel_layout": {{
                "column_count": 7,
                "row_count": 1
            }},
            "port_groups": [
                {{
                    "count": 5,
                    "roles": [
                        "spine"
                    ],
                    "speed": {{
                        "unit": "G",
                        "value": 10
                    }}
                }},
                {{
                    "count": 2,
                    "roles": [
                        "generic"
                    ],
                    "speed": {{
                        "unit": "G",
                        "value": 10
                    }}
                }}
            ],
            "port_indexing": {{
                "order": "T-B, L-R",
                "schema": "absolute",
                "start_index": 1
            }},
            "selected-port-count": 2
        }}
    ]
}}'''

data_JNPR_8_10_BorderLeaf = f'''{{
    "display_name": "JNPR-8x10-BorderLeaf",
    "id": "JNPR-8x10-BorderLeaf",
    "panels": [
        {{
            "panel_layout": {{
                "column_count": 8,
                "row_count": 1
            }},
            "port_groups": [
                {{
                    "count": 4,
                    "roles": [
                        "spine"
                    ],
                    "speed": {{
                        "unit": "G",
                        "value": 10
                    }}
                }},
                {{
                    "count": 4,
                    "roles": [
                        "generic"
                    ],
                    "speed": {{
                        "unit": "G",
                        "value": 10
                    }}
                }}
            ],
            "port_indexing": {{
                "order": "T-B, L-R",
                "schema": "absolute",
                "start_index": 1
            }},
            "selected-port-count": 4
        }}
    ]
}}'''

data_JNPR_10_10_Leaf = f'''{{
    "display_name": "JNPR-10x10-Leaf",
    "id": "JNPR-10x10-Leaf",
    "panels": [
        {{
            "panel_layout": {{
                "column_count": 10,
                "row_count": 1
            }},
            "port_groups": [
                {{
                    "count": 2,
                    "roles": [
                        "spine"
                    ],
                    "speed": {{
                        "unit": "G",
                        "value": 10
                    }}
                }},
                {{
                    "count": 8,
                    "roles": [
                        "generic"
                    ],
                    "speed": {{
                        "unit": "G",
                        "value": 10
                    }}
                }}
            ],
            "port_indexing": {{
                "order": "T-B, L-R",
                "schema": "absolute",
                "start_index": 1
            }},
            "selected-port-count": 8
        }}
    ]
}}'''
