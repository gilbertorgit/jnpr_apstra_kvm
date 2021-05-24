"""
---------------------------------
 Author: Gilberto Rampini
 Date: 05/2021
---------------------------------
"""
# Design Data

data_JNPR_7_10_Spine = f'''{{
  "panels": [
    {{
      "panel_layout": {{
        "row_count": 1,
        "column_count": 7
      }},
      "port_indexing": {{
        "order": "T-B, L-R",
        "start_index": 1,
        "schema": "absolute"
      }},
      "port_groups": [
        {{
          "count": 5,
          "speed": {{
            "unit": "G",
            "value": 10
          }},
          "roles": [
            "superspine",
            "leaf"
          ]
        }},
        {{
          "count": 2,
          "speed": {{
            "unit": "G",
            "value": 10
          }},
          "roles": [
            "external_router"
          ]
        }}
      ]
    }}
  ],
  "display_name": "JNPR-7x10-Spine",
  "id": "JNPR-7x10-Spine"
}}'''

data_JNPR_7_10_SuperSpine = f'''{{
  "panels": [
    {{
      "panel_layout": {{
        "row_count": 1,
        "column_count": 7
      }},
      "port_indexing": {{
        "order": "T-B, L-R",
        "start_index": 1,
        "schema": "absolute"
      }},
      "port_groups": [
        {{
          "count": 5,
          "speed": {{
            "unit": "G",
            "value": 10
          }},
          "roles": [
            "spine"
          ]
        }},
        {{
          "count": 2,
          "speed": {{
            "unit": "G",
            "value": 10
          }},
          "roles": [
            "external_router"
          ]
        }}
      ]
    }}
  ],
  "display_name": "JNPR-7x10-SuperSpine",
  "id": "JNPR-7x10-SuperSpine"
}}'''

data_JNPR_8_10_BorderLeaf = f'''{{
  "panels": [
    {{
      "panel_layout": {{
        "row_count": 1,
        "column_count": 8
      }},
      "port_indexing": {{
        "order": "T-B, L-R",
        "start_index": 1,
        "schema": "absolute"
      }},
      "port_groups": [
        {{
          "count": 4,
          "speed": {{
            "unit": "G",
            "value": 10
          }},
          "roles": [
            "spine"
          ]
        }},
        {{
          "count": 2,
          "speed": {{
            "unit": "G",
            "value": 10
          }},
          "roles": [
            "peer"
          ]
        }},
        {{
          "count": 2,
          "speed": {{
            "unit": "G",
            "value": 10
          }},
          "roles": [
            "external_router"
          ]
        }}
      ]
    }}
  ],
  "display_name": "JNPR-8x10-BorderLeaf",
  "id": "JNPR-8x10-BorderLeaf"
}}'''

data_JNPR_10_10_Leaf = f'''{{
  "panels": [
    {{
      "panel_layout": {{
        "row_count": 1,
        "column_count": 10
      }},
      "port_indexing": {{
        "order": "T-B, L-R",
        "start_index": 1,
        "schema": "absolute"
      }},
      "port_groups": [
        {{
          "count": 2,
          "speed": {{
            "unit": "G",
            "value": 10
          }},
          "roles": [
            "spine"
          ]
        }},
        {{
          "count": 2,
          "speed": {{
            "unit": "G",
            "value": 10
          }},
          "roles": [
            "peer"
          ]
        }},
        {{
          "count": 4,
          "speed": {{
            "unit": "G",
            "value": 10
          }},
          "roles": [
            "l2_server",
            "access",
            "l3_server"
          ]
        }},
        {{
          "count": 2,
          "speed": {{
            "unit": "G",
            "value": 10
          }},
          "roles": [
            "external_router"
          ]
        }}
      ]
    }}
  ],
  "display_name": "JNPR-10x10-Leaf",
  "id": "JNPR-10x10-Leaf"
}}'''
