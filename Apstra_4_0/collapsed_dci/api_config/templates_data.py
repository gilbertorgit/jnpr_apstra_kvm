"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""


def create_templates_dic():

    templates_dic = {'JNPR-3-STAGE-TEMPLATE': {'name': 'JNPR-3-STAGE-TEMPLATE',
                                               'data': f'''{{
                    "asn_allocation_policy": {{
                        "spine_asn_scheme": "distinct"
                    }},
                    "dhcp_service_intent": {{
                        "active": true
                    }},
                    "display_name": "JNPR-3-STAGE-TEMPLATE",
                    "external_routing_policy": {{
                        "export_policy": {{
                            "all_routes": true,
                            "l2edge_subnets": true,
                            "l3edge_server_links": true,
                            "loopbacks": true,
                            "spine_leaf_links": true,
                            "static_routes": false
                        }},
                        "import_policy": "all"
                    }},
                    "fabric_addressing_policy": {{
                        "spine_leaf_links": "ipv4"
                    }},
                    "rack_type_counts": [
                        {{
                            "count": 1,
                            "rack_type_id": "JNPR-BORDER-LEAF"
                        }},
                        {{
                            "count": 1,
                            "rack_type_id": "JNPR-ESI-LEAF"
                        }},
                        {{
                            "count": 1,
                            "rack_type_id": "JNPR-SINGLE-LEAF"
                        }}
                    ],
                    "rack_types": [
                        {{
                            "access_switches": [],
                            "created_at": "2021-06-08T17:10:37.917211Z",
                            "description": "",
                            "display_name": "JNPR-BORDER-LEAF",
                            "fabric_connectivity_design": "l3clos",
                            "generic_systems": [
                                {{
                                    "asn_domain": "disabled",
                                    "count": 1,
                                    "label": "external-router-link-1",
                                    "links": [
                                        {{
                                            "attachment_type": "singleAttached",
                                            "label": "external-router -link-1",
                                            "lag_mode": null,
                                            "link_per_switch_count": 1,
                                            "link_speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }},
                                            "tags": [],
                                            "target_switch_label": "JNPR-BORDER-LEAF"
                                        }}
                                    ],
                                    "logical_device": "AOS-1x10-1",
                                    "loopback": "disabled",
                                    "management_level": "unmanaged",
                                    "port_channel_id_max": 0,
                                    "port_channel_id_min": 0,
                                    "tags": []
                                }}
                            ],
                            "id": "JNPR-BORDER-LEAF",
                            "last_modified_at": "2021-06-08T17:10:37.917211Z",
                            "leafs": [
                                {{
                                    "label": "JNPR-BORDER-LEAF",
                                    "leaf_leaf_l3_link_count": 0,
                                    "leaf_leaf_l3_link_port_channel_id": 0,
                                    "leaf_leaf_l3_link_speed": null,
                                    "leaf_leaf_link_count": 0,
                                    "leaf_leaf_link_port_channel_id": 0,
                                    "leaf_leaf_link_speed": null,
                                    "link_per_spine_count": 1,
                                    "link_per_spine_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "logical_device": "JNPR-8x10-BorderLeaf",
                                    "redundancy_protocol": null,
                                    "tags": []
                                }}
                            ],
                            "logical_devices": [
                                {{
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
                                            }}
                                        }}
                                    ]
                                }},
                                {{
                                    "display_name": "AOS-1x10-1",
                                    "id": "AOS-1x10-1",
                                    "panels": [
                                        {{
                                            "panel_layout": {{
                                                "column_count": 1,
                                                "row_count": 1
                                            }},
                                            "port_groups": [
                                                {{
                                                    "count": 1,
                                                    "roles": [
                                                        "leaf",
                                                        "access"
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
                                            }}
                                        }}
                                    ]
                                }}
                            ],
                            "servers": [],
                            "tags": []
                        }},
                        {{
                            "access_switches": [],
                            "created_at": "2021-06-08T17:25:52.992340Z",
                            "description": "JNPR-ESI-LEAF",
                            "display_name": "JNPR-ESI-LEAF",
                            "fabric_connectivity_design": "l3clos",
                            "generic_systems": [
                                {{
                                    "asn_domain": "disabled",
                                    "count": 1,
                                    "label": "Server1",
                                    "links": [
                                        {{
                                            "attachment_type": "dualAttached",
                                            "label": "server-1-dual-link",
                                            "lag_mode": "lacp_active",
                                            "link_per_switch_count": 1,
                                            "link_speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }},
                                            "tags": [],
                                            "target_switch_label": "JNPR-ESI-LEAF"
                                        }}
                                    ],
                                    "logical_device": "AOS-2x10-1",
                                    "loopback": "disabled",
                                    "management_level": "unmanaged",
                                    "port_channel_id_max": 0,
                                    "port_channel_id_min": 0,
                                    "tags": []
                                }},
                                {{
                                    "asn_domain": "disabled",
                                    "count": 1,
                                    "label": "Server2",
                                    "links": [
                                        {{
                                            "attachment_type": "singleAttached",
                                            "label": "server-2-link-1",
                                            "lag_mode": null,
                                            "leaf_peer": "first",
                                            "link_per_switch_count": 1,
                                            "link_speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }},
                                            "tags": [],
                                            "target_switch_label": "JNPR-ESI-LEAF"
                                        }}
                                    ],
                                    "logical_device": "AOS-2x10-1",
                                    "loopback": "disabled",
                                    "management_level": "unmanaged",
                                    "port_channel_id_max": 0,
                                    "port_channel_id_min": 0,
                                    "tags": []
                                }},
                                {{
                                    "asn_domain": "disabled",
                                    "count": 1,
                                    "label": "Server3",
                                    "links": [
                                        {{
                                            "attachment_type": "singleAttached",
                                            "label": "server-3-link-1",
                                            "lag_mode": null,
                                            "leaf_peer": "second",
                                            "link_per_switch_count": 1,
                                            "link_speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }},
                                            "tags": [],
                                            "target_switch_label": "JNPR-ESI-LEAF"
                                        }}
                                    ],
                                    "logical_device": "AOS-2x10-1",
                                    "loopback": "disabled",
                                    "management_level": "unmanaged",
                                    "port_channel_id_max": 0,
                                    "port_channel_id_min": 0,
                                    "tags": []
                                }}
                            ],
                            "id": "JNPR-ESI-LEAF",
                            "last_modified_at": "2021-06-08T17:25:52.992340Z",
                            "leafs": [
                                {{
                                    "label": "JNPR-ESI-LEAF",
                                    "leaf_leaf_l3_link_count": 0,
                                    "leaf_leaf_l3_link_port_channel_id": 0,
                                    "leaf_leaf_l3_link_speed": null,
                                    "leaf_leaf_link_count": 0,
                                    "leaf_leaf_link_port_channel_id": 0,
                                    "leaf_leaf_link_speed": null,
                                    "link_per_spine_count": 1,
                                    "link_per_spine_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "logical_device": "JNPR-10x10-Leaf",
                                    "redundancy_protocol": "esi",
                                    "tags": []
                                }}
                            ],
                            "logical_devices": [
                                {{
                                    "display_name": "AOS-2x10-1",
                                    "id": "AOS-2x10-1",
                                    "panels": [
                                        {{
                                            "panel_layout": {{
                                                "column_count": 2,
                                                "row_count": 1
                                            }},
                                            "port_groups": [
                                                {{
                                                    "count": 2,
                                                    "roles": [
                                                        "leaf",
                                                        "access"
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
                                            }}
                                        }}
                                    ]
                                }},
                                {{
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
                                            }}
                                        }}
                                    ]
                                }}
                            ],
                            "servers": [],
                            "tags": []
                        }},
                        {{
                            "access_switches": [],
                            "created_at": "2021-06-08T17:18:24.747115Z",
                            "description": "JNPR-SINGLE-LEAF",
                            "display_name": "JNPR-SINGLE-LEAF",
                            "fabric_connectivity_design": "l3clos",
                            "generic_systems": [
                                {{
                                    "asn_domain": "disabled",
                                    "count": 1,
                                    "label": "Server1",
                                    "links": [
                                        {{
                                            "attachment_type": "singleAttached",
                                            "label": "server-1-link-1",
                                            "lag_mode": null,
                                            "link_per_switch_count": 1,
                                            "link_speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }},
                                            "tags": [],
                                            "target_switch_label": "JNPR-SINGLE-LEAF"
                                        }}
                                    ],
                                    "logical_device": "AOS-1x10-1",
                                    "loopback": "disabled",
                                    "management_level": "unmanaged",
                                    "port_channel_id_max": 0,
                                    "port_channel_id_min": 0,
                                    "tags": []
                                }},
                                {{
                                    "asn_domain": "disabled",
                                    "count": 1,
                                    "label": "Server2",
                                    "links": [
                                        {{
                                            "attachment_type": "singleAttached",
                                            "label": "server-2-link-1",
                                            "lag_mode": null,
                                            "link_per_switch_count": 1,
                                            "link_speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }},
                                            "tags": [],
                                            "target_switch_label": "JNPR-SINGLE-LEAF"
                                        }}
                                    ],
                                    "logical_device": "AOS-1x10-1",
                                    "loopback": "disabled",
                                    "management_level": "unmanaged",
                                    "port_channel_id_max": 0,
                                    "port_channel_id_min": 0,
                                    "tags": []
                                }},
                                {{
                                    "asn_domain": "disabled",
                                    "count": 1,
                                    "label": "Server3",
                                    "links": [
                                        {{
                                            "attachment_type": "singleAttached",
                                            "label": "server-3-link-1",
                                            "lag_mode": null,
                                            "link_per_switch_count": 1,
                                            "link_speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }},
                                            "tags": [],
                                            "target_switch_label": "JNPR-SINGLE-LEAF"
                                        }}
                                    ],
                                    "logical_device": "AOS-1x10-1",
                                    "loopback": "disabled",
                                    "management_level": "unmanaged",
                                    "port_channel_id_max": 0,
                                    "port_channel_id_min": 0,
                                    "tags": []
                                }}
                            ],
                            "id": "JNPR-SINGLE-LEAF",
                            "last_modified_at": "2021-06-08T17:18:24.747115Z",
                            "leafs": [
                                {{
                                    "label": "JNPR-SINGLE-LEAF",
                                    "leaf_leaf_l3_link_count": 0,
                                    "leaf_leaf_l3_link_port_channel_id": 0,
                                    "leaf_leaf_l3_link_speed": null,
                                    "leaf_leaf_link_count": 0,
                                    "leaf_leaf_link_port_channel_id": 0,
                                    "leaf_leaf_link_speed": null,
                                    "link_per_spine_count": 1,
                                    "link_per_spine_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "logical_device": "JNPR-10x10-Leaf",
                                    "redundancy_protocol": null,
                                    "tags": []
                                }}
                            ],
                            "logical_devices": [
                                {{
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
                                            }}
                                        }}
                                    ]
                                }},
                                {{
                                    "display_name": "AOS-1x10-1",
                                    "id": "AOS-1x10-1",
                                    "panels": [
                                        {{
                                            "panel_layout": {{
                                                "column_count": 1,
                                                "row_count": 1
                                            }},
                                            "port_groups": [
                                                {{
                                                    "count": 1,
                                                    "roles": [
                                                        "leaf",
                                                        "access"
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
                                            }}
                                        }}
                                    ]
                                }}
                            ],
                            "servers": [],
                            "tags": []
                        }}
                    ],
                    "spine": {{
                        "count": 2,
                        "link_per_superspine_count": 0,
                        "link_per_superspine_speed": null,
                        "logical_device": {{
                            "created_at": "2021-06-08T16:43:33.101278Z",
                            "display_name": "JNPR-7x10-Spine",
                            "id": "JNPR-7x10-Spine",
                            "last_modified_at": "2021-06-08T16:43:33.101278Z",
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
                                    }}
                                }}
                            ],
                            "ui": {{
                                "capabilities-summary": {{
                                    "{{:speed {{:unit \\"G\\", :value 10}}}}": 7
                                }},
                                "ld-summary": {{
                                    "created_at": "2021-06-08T16:43:33.101278Z",
                                    "display_name": "JNPR-7x10-Spine",
                                    "href": "#/design/logical-devices/JNPR-7x10-Spine",
                                    "id": "JNPR-7x10-Spine",
                                    "last_modified_at": "2021-06-08T16:43:33.101278Z",
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
                                            }}
                                        }}
                                    ]
                                }},
                                "num-panels": 1,
                                "num-ports": 7,
                                "ports": [
                                    {{
                                        "count": 2,
                                        "roles": [
                                            "generic"
                                        ],
                                        "speed": {{
                                            "unit": "G",
                                            "value": 10
                                        }}
                                    }},
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
                                    }}
                                ],
                                "ports-summary": {{
                                    "{{:speed {{:unit \\"G\\", :value 10}}, :roles [\\"generic\\"]}}": 2,
                                    "{{:speed {{:unit \\"G\\", :value 10}}, :roles [\\"superspine\\" \\"leaf\\"]}}": 5
                                }}
                            }}
                        }},
                        "tags": []
                    }},
                    "type": "rack_based",
                    "id": "JNPR-3-STAGE-TEMPLATE",
                    "virtual_network_policy": {{
                        "overlay_control_protocol": "evpn"
                    }}
                    }}'''},
                     'JNPR-5-STAGE-BASE': {'name': 'JNPR-5-STAGE-BASE',
                                               'data': f'''{{
                    "asn_allocation_policy": {{
                        "spine_asn_scheme": "single"
                    }},
                    "dhcp_service_intent": {{
                        "active": true
                    }},
                    "display_name": "JNPR-5-STAGE-BASE",
                    "external_routing_policy": {{
                        "export_policy": {{
                            "all_routes": true,
                            "l2edge_subnets": true,
                            "l3edge_server_links": true,
                            "loopbacks": true,
                            "spine_leaf_links": true,
                            "static_routes": false
                        }},
                        "import_policy": "all"
                    }},
                    "fabric_addressing_policy": {{
                        "spine_leaf_links": "ipv4"
                    }},
                    "rack_type_counts": [
                        {{
                            "count": 1,
                            "rack_type_id": "JNPR-BORDER-LEAF"
                        }},
                        {{
                            "count": 1,
                            "rack_type_id": "JNPR-SINGLE-LEAF"
                        }}
                    ],
                    "rack_types": [
                        {{
                            "access_switches": [],
                            "created_at": "2021-06-08T17:10:37.917211Z",
                            "description": "",
                            "display_name": "JNPR-BORDER-LEAF",
                            "fabric_connectivity_design": "l3clos",
                            "generic_systems": [
                                {{
                                    "asn_domain": "disabled",
                                    "count": 1,
                                    "label": "external-router-link-1",
                                    "links": [
                                        {{
                                            "attachment_type": "singleAttached",
                                            "label": "external-router -link-1",
                                            "lag_mode": null,
                                            "link_per_switch_count": 1,
                                            "link_speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }},
                                            "tags": [],
                                            "target_switch_label": "JNPR-BORDER-LEAF"
                                        }}
                                    ],
                                    "logical_device": "AOS-1x10-1",
                                    "loopback": "disabled",
                                    "management_level": "unmanaged",
                                    "port_channel_id_max": 0,
                                    "port_channel_id_min": 0,
                                    "tags": []
                                }}
                            ],
                            "id": "JNPR-BORDER-LEAF",
                            "last_modified_at": "2021-06-08T17:10:37.917211Z",
                            "leafs": [
                                {{
                                    "label": "JNPR-BORDER-LEAF",
                                    "leaf_leaf_l3_link_count": 0,
                                    "leaf_leaf_l3_link_port_channel_id": 0,
                                    "leaf_leaf_l3_link_speed": null,
                                    "leaf_leaf_link_count": 0,
                                    "leaf_leaf_link_port_channel_id": 0,
                                    "leaf_leaf_link_speed": null,
                                    "link_per_spine_count": 1,
                                    "link_per_spine_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "logical_device": "JNPR-8x10-BorderLeaf",
                                    "redundancy_protocol": null,
                                    "tags": []
                                }}
                            ],
                            "logical_devices": [
                                {{
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
                                            }}
                                        }}
                                    ]
                                }},
                                {{
                                    "display_name": "AOS-1x10-1",
                                    "id": "AOS-1x10-1",
                                    "panels": [
                                        {{
                                            "panel_layout": {{
                                                "column_count": 1,
                                                "row_count": 1
                                            }},
                                            "port_groups": [
                                                {{
                                                    "count": 1,
                                                    "roles": [
                                                        "leaf",
                                                        "access"
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
                                            }}
                                        }}
                                    ]
                                }}
                            ],
                            "servers": [],
                            "tags": []
                        }},
                        {{
                            "access_switches": [],
                            "created_at": "2021-06-08T17:18:24.747115Z",
                            "description": "JNPR-SINGLE-LEAF",
                            "display_name": "JNPR-SINGLE-LEAF",
                            "fabric_connectivity_design": "l3clos",
                            "generic_systems": [
                                {{
                                    "asn_domain": "disabled",
                                    "count": 1,
                                    "label": "Server1",
                                    "links": [
                                        {{
                                            "attachment_type": "singleAttached",
                                            "label": "server-1-link-1",
                                            "lag_mode": null,
                                            "link_per_switch_count": 1,
                                            "link_speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }},
                                            "tags": [],
                                            "target_switch_label": "JNPR-SINGLE-LEAF"
                                        }}
                                    ],
                                    "logical_device": "AOS-1x10-1",
                                    "loopback": "disabled",
                                    "management_level": "unmanaged",
                                    "port_channel_id_max": 0,
                                    "port_channel_id_min": 0,
                                    "tags": []
                                }},
                                {{
                                    "asn_domain": "disabled",
                                    "count": 1,
                                    "label": "Server2",
                                    "links": [
                                        {{
                                            "attachment_type": "singleAttached",
                                            "label": "server-2-link-1",
                                            "lag_mode": null,
                                            "link_per_switch_count": 1,
                                            "link_speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }},
                                            "tags": [],
                                            "target_switch_label": "JNPR-SINGLE-LEAF"
                                        }}
                                    ],
                                    "logical_device": "AOS-1x10-1",
                                    "loopback": "disabled",
                                    "management_level": "unmanaged",
                                    "port_channel_id_max": 0,
                                    "port_channel_id_min": 0,
                                    "tags": []
                                }},
                                {{
                                    "asn_domain": "disabled",
                                    "count": 1,
                                    "label": "Server3",
                                    "links": [
                                        {{
                                            "attachment_type": "singleAttached",
                                            "label": "server-3-link-1",
                                            "lag_mode": null,
                                            "link_per_switch_count": 1,
                                            "link_speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }},
                                            "tags": [],
                                            "target_switch_label": "JNPR-SINGLE-LEAF"
                                        }}
                                    ],
                                    "logical_device": "AOS-1x10-1",
                                    "loopback": "disabled",
                                    "management_level": "unmanaged",
                                    "port_channel_id_max": 0,
                                    "port_channel_id_min": 0,
                                    "tags": []
                                }}
                            ],
                            "id": "JNPR-SINGLE-LEAF",
                            "last_modified_at": "2021-06-08T17:18:24.747115Z",
                            "leafs": [
                                {{
                                    "label": "JNPR-SINGLE-LEAF",
                                    "leaf_leaf_l3_link_count": 0,
                                    "leaf_leaf_l3_link_port_channel_id": 0,
                                    "leaf_leaf_l3_link_speed": null,
                                    "leaf_leaf_link_count": 0,
                                    "leaf_leaf_link_port_channel_id": 0,
                                    "leaf_leaf_link_speed": null,
                                    "link_per_spine_count": 1,
                                    "link_per_spine_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "logical_device": "JNPR-10x10-Leaf",
                                    "redundancy_protocol": null,
                                    "tags": []
                                }}
                            ],
                            "logical_devices": [
                                {{
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
                                            }}
                                        }}
                                    ]
                                }},
                                {{
                                    "display_name": "AOS-1x10-1",
                                    "id": "AOS-1x10-1",
                                    "panels": [
                                        {{
                                            "panel_layout": {{
                                                "column_count": 1,
                                                "row_count": 1
                                            }},
                                            "port_groups": [
                                                {{
                                                    "count": 1,
                                                    "roles": [
                                                        "leaf",
                                                        "access"
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
                                            }}
                                        }}
                                    ]
                                }}
                            ],
                            "servers": [],
                            "tags": []
                        }}
                    ],
                    "spine": {{
                        "count": 1,
                        "link_per_superspine_count": 1,
                        "link_per_superspine_speed": {{
                            "unit": "G",
                            "value": 10
                        }},
                        "logical_device": {{
                            "created_at": "2021-06-08T16:43:33.101278Z",
                            "display_name": "JNPR-7x10-Spine",
                            "id": "JNPR-7x10-Spine",
                            "last_modified_at": "2021-06-08T16:43:33.101278Z",
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
                                    }}
                                }}
                            ],
                            "ui": {{
                                "capabilities-summary": {{
                                    "{{:speed {{:unit \\"G\\", :value 10}}}}": 7
                                }},
                                "ld-summary": {{
                                    "created_at": "2021-06-08T16:43:33.101278Z",
                                    "display_name": "JNPR-7x10-Spine",
                                    "href": "#/design/logical-devices/JNPR-7x10-Spine",
                                    "id": "JNPR-7x10-Spine",
                                    "last_modified_at": "2021-06-08T16:43:33.101278Z",
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
                                            }}
                                        }}
                                    ]
                                }},
                                "num-panels": 1,
                                "num-ports": 7,
                                "ports": [
                                    {{
                                        "count": 2,
                                        "roles": [
                                            "generic"
                                        ],
                                        "speed": {{
                                            "unit": "G",
                                            "value": 10
                                        }}
                                    }},
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
                                    }}
                                ],
                                "ports-summary": {{
                                    "{{:speed {{:unit \\"G\\", :value 10}}, :roles [\\"generic\\"]}}": 2,
                                    "{{:speed {{:unit \\"G\\", :value 10}}, :roles [\\"superspine\\" \\"leaf\\"]}}": 5
                                }}
                            }}
                        }},
                        "tags": []
                    }},
                    "type": "rack_based",
                    "id": "JNPR-5-STAGE-BASE",
                    "virtual_network_policy": {{
                        "overlay_control_protocol": "evpn"
                    }}
                    }}'''},
                     'JNPR-5-STAGE-TEMPLATE': {'name': 'JNPR-5-STAGE-TEMPLATE',
                                               'data': f'''{{
                    "display_name": "JNPR-5-STAGE-TEMPLATE",
                    "fabric_addressing_policy": {{
                        "spine_superspine_links": "ipv4"
                    }},
                    "rack_based_template_counts": [
                        {{
                            "count": 2,
                            "rack_based_template_id": "a056e972-b0e6-48d4-a1f2-0e299e1b163e"
                        }}
                    ],
                    "rack_based_templates": [
                        {{
                            "asn_allocation_policy": {{
                                "spine_asn_scheme": "single"
                            }},
                            "capability": "pod",
                            "created_at": "2021-06-08T21:09:49.491833Z",
                            "dhcp_service_intent": {{
                                "active": true
                            }},
                            "display_name": "JNPR-5-STAGE-BASE",
                            "external_routing_policy": {{
                                "aggregate_prefixes": [],
                                "expect_default_ipv4_route": true,
                                "expect_default_ipv6_route": true,
                                "export_policy": {{
                                    "l2edge_subnets": true,
                                    "l3edge_server_links": true,
                                    "loopbacks": true,
                                    "spine_leaf_links": true,
                                    "static_routes": false
                                }},
                                "extra_export_routes": [],
                                "extra_import_routes": [],
                                "import_policy": "all",
                                "label": "Default_immutable"
                            }},
                            "fabric_addressing_policy": {{
                                "spine_leaf_links": "ipv4",
                                "spine_superspine_links": "ipv4"
                            }},
                            "id": "a056e972-b0e6-48d4-a1f2-0e299e1b163e",
                            "last_modified_at": "2021-06-08T21:09:49.491833Z",
                            "rack_type_counts": [
                                {{
                                    "count": 1,
                                    "rack_type_id": "JNPR-BORDER-LEAF"
                                }},
                                {{
                                    "count": 1,
                                    "rack_type_id": "JNPR-SINGLE-LEAF"
                                }}
                            ],
                            "rack_types": [
                                {{
                                    "access_switches": [],
                                    "created_at": "1970-01-01T00:00:00.000000Z",
                                    "description": "",
                                    "display_name": "JNPR-BORDER-LEAF",
                                    "fabric_connectivity_design": "l3clos",
                                    "generic_systems": [
                                        {{
                                            "asn_domain": "disabled",
                                            "count": 1,
                                            "label": "external-router-link-1",
                                            "links": [
                                                {{
                                                    "attachment_type": "singleAttached",
                                                    "label": "external-router -link-1",
                                                    "lag_mode": null,
                                                    "link_per_switch_count": 1,
                                                    "link_speed": {{
                                                        "unit": "G",
                                                        "value": 10
                                                    }},
                                                    "tags": [],
                                                    "target_switch_label": "JNPR-BORDER-LEAF"
                                                }}
                                            ],
                                            "logical_device": "AOS-1x10-1",
                                            "loopback": "disabled",
                                            "management_level": "unmanaged",
                                            "port_channel_id_max": 0,
                                            "port_channel_id_min": 0,
                                            "tags": []
                                        }}
                                    ],
                                    "id": "JNPR-BORDER-LEAF",
                                    "last_modified_at": "2021-06-08T17:10:37.917211Z",
                                    "leafs": [
                                        {{
                                            "label": "JNPR-BORDER-LEAF",
                                            "leaf_leaf_l3_link_count": 0,
                                            "leaf_leaf_l3_link_port_channel_id": 0,
                                            "leaf_leaf_l3_link_speed": null,
                                            "leaf_leaf_link_count": 0,
                                            "leaf_leaf_link_port_channel_id": 0,
                                            "leaf_leaf_link_speed": null,
                                            "link_per_spine_count": 1,
                                            "link_per_spine_speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }},
                                            "logical_device": "JNPR-8x10-BorderLeaf",
                                            "mlag_vlan_id": 0,
                                            "redundancy_protocol": null,
                                            "tags": []
                                        }}
                                    ],
                                    "logical_devices": [
                                        {{
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
                                                    }}
                                                }}
                                            ]
                                        }},
                                        {{
                                            "display_name": "AOS-1x10-1",
                                            "id": "AOS-1x10-1",
                                            "panels": [
                                                {{
                                                    "panel_layout": {{
                                                        "column_count": 1,
                                                        "row_count": 1
                                                    }},
                                                    "port_groups": [
                                                        {{
                                                            "count": 1,
                                                            "roles": [
                                                                "leaf",
                                                                "access"
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
                                                    }}
                                                }}
                                            ]
                                        }}
                                    ],
                                    "servers": [],
                                    "tags": []
                                }},
                                {{
                                    "access_switches": [],
                                    "created_at": "1970-01-01T00:00:00.000000Z",
                                    "description": "JNPR-SINGLE-LEAF",
                                    "display_name": "JNPR-SINGLE-LEAF",
                                    "fabric_connectivity_design": "l3clos",
                                    "generic_systems": [
                                        {{
                                            "asn_domain": "disabled",
                                            "count": 1,
                                            "label": "Server1",
                                            "links": [
                                                {{
                                                    "attachment_type": "singleAttached",
                                                    "label": "server-1-link-1",
                                                    "lag_mode": null,
                                                    "link_per_switch_count": 1,
                                                    "link_speed": {{
                                                        "unit": "G",
                                                        "value": 10
                                                    }},
                                                    "tags": [],
                                                    "target_switch_label": "JNPR-SINGLE-LEAF"
                                                }}
                                            ],
                                            "logical_device": "AOS-1x10-1",
                                            "loopback": "disabled",
                                            "management_level": "unmanaged",
                                            "port_channel_id_max": 0,
                                            "port_channel_id_min": 0,
                                            "tags": []
                                        }},
                                        {{
                                            "asn_domain": "disabled",
                                            "count": 1,
                                            "label": "Server2",
                                            "links": [
                                                {{
                                                    "attachment_type": "singleAttached",
                                                    "label": "server-2-link-1",
                                                    "lag_mode": null,
                                                    "link_per_switch_count": 1,
                                                    "link_speed": {{
                                                        "unit": "G",
                                                        "value": 10
                                                    }},
                                                    "tags": [],
                                                    "target_switch_label": "JNPR-SINGLE-LEAF"
                                                }}
                                            ],
                                            "logical_device": "AOS-1x10-1",
                                            "loopback": "disabled",
                                            "management_level": "unmanaged",
                                            "port_channel_id_max": 0,
                                            "port_channel_id_min": 0,
                                            "tags": []
                                        }},
                                        {{
                                            "asn_domain": "disabled",
                                            "count": 1,
                                            "label": "Server3",
                                            "links": [
                                                {{
                                                    "attachment_type": "singleAttached",
                                                    "label": "server-3-link-1",
                                                    "lag_mode": null,
                                                    "link_per_switch_count": 1,
                                                    "link_speed": {{
                                                        "unit": "G",
                                                        "value": 10
                                                    }},
                                                    "tags": [],
                                                    "target_switch_label": "JNPR-SINGLE-LEAF"
                                                }}
                                            ],
                                            "logical_device": "AOS-1x10-1",
                                            "loopback": "disabled",
                                            "management_level": "unmanaged",
                                            "port_channel_id_max": 0,
                                            "port_channel_id_min": 0,
                                            "tags": []
                                        }}
                                    ],
                                    "id": "JNPR-SINGLE-LEAF",
                                    "last_modified_at": "2021-06-08T17:18:24.747115Z",
                                    "leafs": [
                                        {{
                                            "label": "JNPR-SINGLE-LEAF",
                                            "leaf_leaf_l3_link_count": 0,
                                            "leaf_leaf_l3_link_port_channel_id": 0,
                                            "leaf_leaf_l3_link_speed": null,
                                            "leaf_leaf_link_count": 0,
                                            "leaf_leaf_link_port_channel_id": 0,
                                            "leaf_leaf_link_speed": null,
                                            "link_per_spine_count": 1,
                                            "link_per_spine_speed": {{
                                                "unit": "G",
                                                "value": 10
                                            }},
                                            "logical_device": "JNPR-10x10-Leaf",
                                            "mlag_vlan_id": 0,
                                            "redundancy_protocol": null,
                                            "tags": []
                                        }}
                                    ],
                                    "logical_devices": [
                                        {{
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
                                                    }}
                                                }}
                                            ]
                                        }},
                                        {{
                                            "display_name": "AOS-1x10-1",
                                            "id": "AOS-1x10-1",
                                            "panels": [
                                                {{
                                                    "panel_layout": {{
                                                        "column_count": 1,
                                                        "row_count": 1
                                                    }},
                                                    "port_groups": [
                                                        {{
                                                            "count": 1,
                                                            "roles": [
                                                                "leaf",
                                                                "access"
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
                                                    }}
                                                }}
                                            ]
                                        }}
                                    ],
                                    "servers": [],
                                    "tags": []
                                }}
                            ],
                            "spine": {{
                                "count": 1,
                                "link_per_superspine_count": 1,
                                "link_per_superspine_speed": {{
                                    "unit": "G",
                                    "value": 10
                                }},
                                "logical_device": {{
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
                                            }}
                                        }}
                                    ]
                                }},
                                "tags": []
                            }},
                            "type": "rack_based",
                            "virtual_network_policy": {{
                                "overlay_control_protocol": "evpn"
                            }}
                        }}
                    ],
                    "superspine": {{
                        "logical_device": {{
                            "created_at": "2021-06-08T16:43:33.182131Z",
                            "display_name": "JNPR-7x10-SuperSpine",
                            "id": "JNPR-7x10-SuperSpine",
                            "last_modified_at": "2021-06-08T16:43:33.182131Z",
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
                                    }}
                                }}
                            ],
                            "ui": {{
                                "capabilities-summary": {{
                                    "{{:speed {{:unit \\"G\\", :value 10}}}}": 7
                                }},
                                "ld-summary": {{
                                    "created_at": "2021-06-08T16:43:33.182131Z",
                                    "display_name": "JNPR-7x10-SuperSpine",
                                    "href": "#/design/logical-devices/JNPR-7x10-SuperSpine",
                                    "id": "JNPR-7x10-SuperSpine",
                                    "last_modified_at": "2021-06-08T16:43:33.182131Z",
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
                                            }}
                                        }}
                                    ]
                                }},
                                "num-panels": 1,
                                "num-ports": 7,
                                "ports": [
                                    {{
                                        "count": 2,
                                        "roles": [
                                            "generic"
                                        ],
                                        "speed": {{
                                            "unit": "G",
                                            "value": 10
                                        }}
                                    }},
                                    {{
                                        "count": 5,
                                        "roles": [
                                            "spine"
                                        ],
                                        "speed": {{
                                            "unit": "G",
                                            "value": 10
                                        }}
                                    }}
                                ],
                                "ports-summary": {{
                                    "{{:speed {{:unit \\"G\\", :value 10}}, :roles [\\"generic\\"]}}": 2,
                                    "{{:speed {{:unit \\"G\\", :value 10}}, :roles [\\"spine\\"]}}": 5
                                }}
                            }}
                        }},
                        "plane_count": 1,
                        "superspine_per_plane": 1,
                        "tags": []
                    }},
                    "type": "pod_based",
                    "id": "JNPR-5-STAGE-TEMPLATE"
                    }}'''},
                    }

    return templates_dic







