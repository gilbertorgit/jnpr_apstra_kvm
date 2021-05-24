"""
---------------------------------
 Author: Gilberto Rampini
 Date: 05/2021
---------------------------------
"""
##############################################
""" Rack Types Data """

data_rack_JNPR_SINGLE_LEAF = f'''{{
  "display_name": "JNPR-SINGLE-LEAF",
  "description": "JNPR-SINGLE-LEAF",
  "leafs": [
    {{
      "external_router_links": [],
      "external_router_facing": false,
      "leaf_leaf_l3_link_speed": null,
      "redundancy_protocol": null,
      "leaf_leaf_link_port_channel_id": 0,
      "leaf_leaf_l3_link_count": 0,
      "logical_device": "JNPR-10x10-Leaf",
      "leaf_leaf_link_speed": null,
      "link_per_spine_count": 1,
      "leaf_leaf_link_count": 0,
      "link_per_spine_speed": {{
        "unit": "G",
        "value": 10
      }},
      "label": "JNPR-SINGLE-LEAF",
      "leaf_leaf_l3_link_port_channel_id": 0
    }}
  ],
  "logical_devices": [
    {{
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
    }},
    {{
      "panels": [
        {{
          "panel_layout": {{
            "row_count": 1,
            "column_count": 1
          }},
          "port_indexing": {{
            "order": "T-B, L-R",
            "start_index": 1,
            "schema": "absolute"
          }},
          "port_groups": [
            {{
              "count": 1,
              "speed": {{
                "unit": "G",
                "value": 10
              }},
              "roles": [
                "leaf",
                "access"
              ]
            }}
          ]
        }}
      ],
      "display_name": "AOS-1x10-1",
      "id": "AOS-1x10-1"
    }}
  ],
  "access_switches": [],
  "id": "JNPR-SINGLE-LEAF",
  "servers": [
    {{
      "count": 1,
      "connectivity_type": "l2",
      "port_channel_id_min": 0,
      "links": [
        {{
          "link_per_switch_count": 1,
          "label": "server-1-link-1",
          "link_speed": {{
            "unit": "G",
            "value": 10
          }},
          "target_switch_label": "JNPR-SINGLE-LEAF",
          "attachment_type": "singleAttached",
          "lag_mode": null
        }}
      ],
      "ip_version": "ipv4",
      "port_channel_id_max": 0,
      "logical_device": "AOS-1x10-1",
      "label": "Server1"
    }},
    {{
      "count": 1,
      "connectivity_type": "l2",
      "port_channel_id_min": 0,
      "links": [
        {{
          "link_per_switch_count": 1,
          "label": "server-2-link-1",
          "link_speed": {{
            "unit": "G",
            "value": 10
          }},
          "target_switch_label": "JNPR-SINGLE-LEAF",
          "attachment_type": "singleAttached",
          "lag_mode": null
        }}
      ],
      "ip_version": "ipv4",
      "port_channel_id_max": 0,
      "logical_device": "AOS-1x10-1",
      "label": "Server2"
    }},
    {{
      "count": 1,
      "connectivity_type": "l2",
      "port_channel_id_min": 0,
      "links": [
        {{
          "link_per_switch_count": 1,
          "label": "server-3-link-1",
          "link_speed": {{
            "unit": "G",
            "value": 10
          }},
          "target_switch_label": "JNPR-SINGLE-LEAF",
          "attachment_type": "singleAttached",
          "lag_mode": null
        }}
      ],
      "ip_version": "ipv4",
      "port_channel_id_max": 0,
      "logical_device": "AOS-1x10-1",
      "label": "Server3"
    }}
  ]
}}'''


data_rack_JNPR_ESI_LEAF = f'''{{
  "display_name": "JNPR-ESI-LEAF",
  "description": "JNPR-ESI-LEAF",
  "leafs": [
    {{
      "external_router_links": [],
      "external_router_facing": false,
      "leaf_leaf_l3_link_speed": null,
      "redundancy_protocol": "esi",
      "leaf_leaf_link_port_channel_id": 0,
      "leaf_leaf_l3_link_count": 0,
      "logical_device": "JNPR-10x10-Leaf",
      "leaf_leaf_link_speed": null,
      "link_per_spine_count": 1,
      "leaf_leaf_link_count": 0,
      "link_per_spine_speed": {{
        "unit": "G",
        "value": 10
      }},
      "label": "JNPR-ESI-LEAF",
      "leaf_leaf_l3_link_port_channel_id": 0
    }}
  ],
  "logical_devices": [
    {{
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
    }},
    {{
      "panels": [
        {{
          "panel_layout": {{
            "row_count": 1,
            "column_count": 2
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
                "leaf",
                "access"
              ]
            }}
          ]
        }}
      ],
      "display_name": "AOS-2x10-1",
      "id": "AOS-2x10-1"
    }},
    {{
      "panels": [
        {{
          "panel_layout": {{
            "row_count": 1,
            "column_count": 1
          }},
          "port_indexing": {{
            "order": "T-B, L-R",
            "start_index": 1,
            "schema": "absolute"
          }},
          "port_groups": [
            {{
              "count": 1,
              "speed": {{
                "unit": "G",
                "value": 10
              }},
              "roles": [
                "leaf",
                "access"
              ]
            }}
          ]
        }}
      ],
      "display_name": "AOS-1x10-1",
      "id": "AOS-1x10-1"
    }}
  ],
  "access_switches": [],
  "id": "JNPR-ESI-LEAF",
  "servers": [
    {{
      "count": 1,
      "connectivity_type": "l2",
      "port_channel_id_min": 0,
      "links": [
        {{
          "link_per_switch_count": 1,
          "label": "server-1-dual-link",
          "link_speed": {{
            "unit": "G",
            "value": 10
          }},
          "target_switch_label": "JNPR-ESI-LEAF",
          "attachment_type": "dualAttached",
          "lag_mode": "lacp_active"
        }}
      ],
      "ip_version": "ipv4",
      "port_channel_id_max": 0,
      "logical_device": "AOS-2x10-1",
      "label": "Server1"
    }},
    {{
      "count": 1,
      "connectivity_type": "l2",
      "port_channel_id_min": 0,
      "links": [
        {{
          "link_per_switch_count": 1,
          "leaf_peer": "first",
          "label": "server-2-link-1",
          "link_speed": {{
            "unit": "G",
            "value": 10
          }},
          "target_switch_label": "JNPR-ESI-LEAF",
          "attachment_type": "singleAttached",
          "lag_mode": null
        }}
      ],
      "ip_version": "ipv4",
      "port_channel_id_max": 0,
      "logical_device": "AOS-1x10-1",
      "label": "Server2"
    }},
    {{
      "count": 1,
      "connectivity_type": "l2",
      "port_channel_id_min": 0,
      "links": [
        {{
          "link_per_switch_count": 1,
          "leaf_peer": "second",
          "label": "server-3-link-1",
          "link_speed": {{
            "unit": "G",
            "value": 10
          }},
          "target_switch_label": "JNPR-ESI-LEAF",
          "attachment_type": "singleAttached",
          "lag_mode": null
        }}
      ],
      "ip_version": "ipv4",
      "port_channel_id_max": 0,
      "logical_device": "AOS-1x10-1",
      "label": "Server3"
    }}
  ]
}}'''

data_rack_JNPR_BORDER_LEAF = f'''{{
  "display_name": "JNPR-BORDER-LEAF",
  "description": "JNPR-BORDER-LEAF",
  "leafs": [
    {{
      "external_router_links": [
        {{
          "count": 1,
          "speed": {{
            "unit": "G",
            "value": 10
          }}
        }}
      ],
      "external_router_facing": true,
      "leaf_leaf_l3_link_speed": null,
      "redundancy_protocol": null,
      "leaf_leaf_link_port_channel_id": 0,
      "leaf_leaf_l3_link_count": 0,
      "logical_device": "JNPR-8x10-BorderLeaf",
      "leaf_leaf_link_speed": null,
      "link_per_spine_count": 1,
      "leaf_leaf_link_count": 0,
      "link_per_spine_speed": {{
        "unit": "G",
        "value": 10
      }},
      "label": "JNPR-BORDER-LEAF",
      "leaf_leaf_l3_link_port_channel_id": 0
    }}
  ],
  "logical_devices": [
    {{
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
    }}
  ],
  "access_switches": [],
  "id": "JNPR-BORDER-LEAF",
  "servers": []
}}'''