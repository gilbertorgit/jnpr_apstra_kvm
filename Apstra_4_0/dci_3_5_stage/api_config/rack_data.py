"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""
""" Rack Type Data """


def create_rack_type_dic():

    rack_type_dic = {'JNPR-SINGLE-LEAF': {'name': 'JNPR-SINGLE-LEAF',
                                          'data': f'''{{
                    "access_switches": [],
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
                                    "leaf_peer": null,
                                    "link_per_switch_count": 1,
                                    "link_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "target_switch_label": "JNPR-SINGLE-LEAF"
                                }}
                            ],
                            "logical_device": "AOS-1x10-1",
                            "loopback": "disabled",
                            "management_level": "unmanaged",
                            "port_channel_id_max": 0,
                            "port_channel_id_min": 0
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
                                    "leaf_peer": null,
                                    "link_per_switch_count": 1,
                                    "link_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "target_switch_label": "JNPR-SINGLE-LEAF"
                                }}
                            ],
                            "logical_device": "AOS-1x10-1",
                            "loopback": "disabled",
                            "management_level": "unmanaged",
                            "port_channel_id_max": 0,
                            "port_channel_id_min": 0
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
                                    "leaf_peer": null,
                                    "link_per_switch_count": 1,
                                    "link_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "target_switch_label": "JNPR-SINGLE-LEAF"
                                }}
                            ],
                            "logical_device": "AOS-1x10-1",
                            "loopback": "disabled",
                            "management_level": "unmanaged",
                            "port_channel_id_max": 0,
                            "port_channel_id_min": 0
                        }}
                    ],
                    "id": "JNPR-SINGLE-LEAF",
                    "last_modified_at": null,
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
                            "redundancy_protocol": null
                        }}
                    ],
                    "logical_devices": [
                        {{
                            "display_name": "JNPR-10x10-Leaf",
                            "href": "#/design/logical-devices/JNPR-10x10-Leaf",
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
                            "href": "#/design/logical-devices/AOS-1x10-1",
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
                    "tags": []
                    }}'''},
                     'JNPR-ESI-LEAF': {'name': 'JNPR-ESI-LEAF',
                                          'data': f'''{{
                    "access_switches": [],
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
                                    "target_switch_label": "JNPR-ESI-LEAF"
                                }}
                            ],
                            "logical_device": "AOS-2x10-1",
                            "loopback": "disabled",
                            "management_level": "unmanaged",
                            "port_channel_id_max": 0,
                            "port_channel_id_min": 0
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
                                    "target_switch_label": "JNPR-ESI-LEAF"
                                }}
                            ],
                            "logical_device": "AOS-2x10-1",
                            "loopback": "disabled",
                            "management_level": "unmanaged",
                            "port_channel_id_max": 0,
                            "port_channel_id_min": 0
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
                                    "target_switch_label": "JNPR-ESI-LEAF"
                                }}
                            ],
                            "logical_device": "AOS-2x10-1",
                            "loopback": "disabled",
                            "management_level": "unmanaged",
                            "port_channel_id_max": 0,
                            "port_channel_id_min": 0
                        }}
                    ],
                    "id": "JNPR-ESI-LEAF",
                    "last_modified_at": null,
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
                            "redundancy_protocol": "esi"
                        }}
                    ],
                    "logical_devices": [
                        {{
                            "created_at": "2021-05-28T02:41:28.490353Z",
                            "display_name": "AOS-2x10-1",
                            "href": "#/design/logical-devices/AOS-2x10-1",
                            "id": "AOS-2x10-1",
                            "last_modified_at": "2021-05-28T02:41:28.490353Z",
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
                            "created_at": "2021-06-08T16:43:33.325331Z",
                            "display_name": "JNPR-10x10-Leaf",
                            "href": "#/design/logical-devices/JNPR-10x10-Leaf",
                            "id": "JNPR-10x10-Leaf",
                            "last_modified_at": "2021-06-08T16:43:33.325331Z",
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
                    "tags": []
                    }}'''},
                     'JNPR-BORDER-LEAF': {'name': 'JNPR-BORDER-LEAF',
                                          'data': f'''{{
                    "access_switches": [],
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
                                    "leaf_peer": null,
                                    "link_per_switch_count": 1,
                                    "link_speed": {{
                                        "unit": "G",
                                        "value": 10
                                    }},
                                    "target_switch_label": "JNPR-BORDER-LEAF"
                                }}
                            ],
                            "logical_device": "AOS-1x10-1",
                            "loopback": "disabled",
                            "management_level": "unmanaged",
                            "port_channel_id_max": 0,
                            "port_channel_id_min": 0
                        }}
                    ],
                    "id": "JNPR-BORDER-LEAF",
                    "last_modified_at": null,
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
                            "redundancy_protocol": null
                        }}
                    ],
                    "logical_devices": [
                        {{
                            "display_name": "JNPR-8x10-BorderLeaf",
                            "href": "#/design/logical-devices/JNPR-8x10-BorderLeaf",
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
                            "href": "#/design/logical-devices/AOS-1x10-1",
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
                    "tags": []
                    }}'''},
                    }

    return rack_type_dic
