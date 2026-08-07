import networkx as nx

# 1. Initialize a directed network graph object
network_map = nx.DiGraph()

# 2. Add structural nodes representing the application architecture
network_map.add_nodes_from([
    ("v_public", {"label": "Internet Traffic Source"}),
    ("v_gateway", {"label": "Reverse Proxy (Nginx)"}),
    ("v_user_api", {"label": "Public User Endpoint (/api/v1/)"}),
    ("v_admin_api", {"label": "Protected Admin API (/api/internal/)"}),
    ("v_database", {"label": "Core Financial Database"})
])

# 3. Define the intended corporate network routing paths (Edges)
network_map.add_edges_from([
    ("v_public", "v_gateway"),
    ("v_gateway", "v_user_api"),
    ("v_user_api", "v_database")
])

# 4. Inject an anomaly path discovered via manual path normalization auditing
# This represents the Nginx path-traversal bypass route we mapped mathematically
print("[*] Simulating edge injection via path-traversal anomaly...")
network_map.add_edge("v_gateway", "v_admin_api") # The broken path
network_map.add_edge("v_admin_api", "v_database")

# 5. Graph Theory Analysis: Proving Path Reachability
# Mathematically test if an unauthenticated user can hit the admin API or DB
unauth_source = "v_public"
protected_target = "v_admin_api"

is_reachable = nx.has_path(network_map, unauth_source, protected_target)

if is_reachable:
    print(f"\n[!] TOPOLOGICAL ISOLATION BREACH DETECTED!")
    
    # Calculate the exact shortest pathway vector the data flows through
    vulnerable_pathway = nx.shortest_path(network_map, unauth_source, protected_target)
    path_visualization = " -> ".join(vulnerable_pathway)
    
    print(f"    Exposed Path Map: {path_visualization}")
    print("    Action Required: Re-configure backend proxy route parsers to enforce isolation constraints.")
else:
    print("\n[+] Verification successful: Core network graph layers are strictly isolated.")
