"""
---------------------------------
 Author: Gilberto Rampini
 Date: 05/2021
---------------------------------
"""

data_JNPR_3_STAGE_TEMPLATE = f'''{{
  "external_routing_policy": {{
    "export_policy": {{
      "all_routes": true,
      "spine_leaf_links": true,
      "l3edge_server_links": true,
      "l2edge_subnets": true,
      "loopbacks": true
    }},
    "extra_export_routes": [],
    "extra_import_routes": [],
    "import_policy": "all",
    "aggregate_prefixes": []
  }},
  "display_name": "JNPR-3-STAGE-TEMPLATE",
  "virtual_network_policy": {{
    "overlay_control_protocol": "evpn"
  }},
  "fabric_addressing_policy": {{
    "spine_leaf_links": "ipv4",
    "spine_superspine_links": "ipv4"
  }},
  "spine": {{
    "count": 2,
    "external_link_speed": null,
    "link_per_superspine_count": 0,
    "link_per_superspine_speed": null,
    "external_links_per_node": 0,
    "external_facing_node_count": 0,
    "logical_device": {{
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
    }},
    "external_link_count": 0
  }},
  "rack_type_counts": [
    {{
      "rack_type_id": "JNPR-BORDER-LEAF",
      "count": 1
    }},
    {{
      "rack_type_id": "JNPR-ESI-LEAF",
      "count": 1
    }},
    {{
      "rack_type_id": "JNPR-SINGLE-LEAF",
      "count": 1
    }}
  ],
  "dhcp_service_intent": {{
    "active": true
  }},
  "rack_types": [
    {{
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
    }},
    {{
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
    }},
    {{
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
    }}
  ],
  "asn_allocation_policy": {{
    "spine_asn_scheme": "distinct"
  }},
  "type": "rack_based",
  "id": "JNPR-3-STAGE-TEMPLATE"
}}'''


data_JNPR_5_STAGE_BASE = f'''{{
  "external_routing_policy": {{
    "export_policy": {{
      "all_routes": true,
      "spine_leaf_links": true,
      "l3edge_server_links": true,
      "l2edge_subnets": true,
      "loopbacks": true
    }},
    "extra_export_routes": [],
    "extra_import_routes": [],
    "import_policy": "all",
    "aggregate_prefixes": []
  }},
  "display_name": "JNPR-5-STAGE-BASE",
  "virtual_network_policy": {{
    "overlay_control_protocol": "evpn"
  }},
  "fabric_addressing_policy": {{
    "spine_leaf_links": "ipv4",
    "spine_superspine_links": "ipv4"
  }},
  "spine": {{
    "count": 1,
    "external_link_speed": null,
    "link_per_superspine_count": 1,
    "link_per_superspine_speed": {{
      "unit": "G",
      "value": 10
    }},
    "external_links_per_node": 0,
    "external_facing_node_count": 0,
    "logical_device": {{
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
    }},
    "external_link_count": 0
  }},
  "rack_type_counts": [
    {{
      "rack_type_id": "JNPR-BORDER-LEAF",
      "count": 1
    }},
    {{
      "rack_type_id": "JNPR-SINGLE-LEAF",
      "count": 1
    }}
  ],
  "dhcp_service_intent": {{
    "active": true
  }},
  "rack_types": [
    {{
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
    }},
    {{
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
    }}
  ],
  "asn_allocation_policy": {{
    "spine_asn_scheme": "single"
  }},
  "type": "rack_based",
  "id": "JNPR-5-STAGE-BASE"
}}'''


data_JNPR_5_STAGE_TEMPLATE = f'''{{
  "display_name": "JNPR-5-STAGE-TEMPLATE",
  "rack_based_templates": [
    {{
      "external_routing_policy": {{
        "export_policy": {{
          "all_routes": true,
          "spine_leaf_links": true,
          "l3edge_server_links": true,
          "l2edge_subnets": true,
          "loopbacks": true
        }},
        "extra_export_routes": [],
        "extra_import_routes": [],
        "import_policy": "all",
        "aggregate_prefixes": []
      }},
      "display_name": "JNPR-5-STAGE-BASE",
      "virtual_network_policy": {{
        "overlay_control_protocol": "evpn"
      }},
      "fabric_addressing_policy": {{
        "spine_leaf_links": "ipv4",
        "spine_superspine_links": "ipv4"
      }},
      "spine": {{
        "count": 1,
        "external_link_speed": null,
        "link_per_superspine_count": 1,
        "link_per_superspine_speed": {{
          "unit": "G",
          "value": 10
        }},
        "external_links_per_node": 0,
        "external_facing_node_count": 0,
        "logical_device": {{
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
        }},
        "external_link_count": 0
      }},
      "rack_type_counts": [
        {{
          "rack_type_id": "JNPR-BORDER-LEAF",
          "count": 1
        }},
        {{
          "rack_type_id": "JNPR-SINGLE-LEAF",
          "count": 1
        }}
      ],
      "dhcp_service_intent": {{
        "active": true
      }},
      "rack_types": [
        {{
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
        }},
        {{
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
        }}
      ],
      "asn_allocation_policy": {{
        "spine_asn_scheme": "single"
      }},
      "id": "JNPR-5-STAGE-BASE"
    }}
  ],
  "fabric_addressing_policy": {{
    "spine_leaf_links": "ipv4",
    "spine_superspine_links": "ipv4"
  }},
  "superspine": {{
    "plane_count": 1,
    "external_link_speed": null,
    "external_link_count": 0,
    "logical_device": {{
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
    }},
    "superspine_per_plane": 1
  }},
  "rack_based_template_counts": [
    {{
      "rack_based_template_id": "JNPR-5-STAGE-BASE",
      "count": 2
    }}
  ],
  "type": "pod_based",
  "id": "JNPR-5-STAGE-TEMPLATE"
}}'''