
# Server-Side Request Forgery (SSRF) via [Parameter Name] on [Endpoint]
## SummaryA Server-Side Request Forgery (SSRF) vulnerability was identified in the `[Insert Parameter, e.g., visit_domain]` parameter of the `[Insert Path, e.g., /affiliate:link_visit]` endpoint. The application backend accepts user-supplied infrastructure strings and attempts to initiate outbound network requests without strict domain whitelisting. 
## Target Asset*   **Vulnerable URL**: `https://1win.com/[Insert-Vulnerable-Path]`
*   **Affected Parameter**: `[Insert-Parameter]`*   **Severity Tier**: High (\$1,300 Non-Blind / \$750 Blind)
## Pre-requisites*   No special authentication required / [Specify if an active researcher account was active].*   An external interaction logger (e.g., Interactsh / Burp Collaborator).
## Step-by-Step Reproduction Instructions1. Establish a live monitoring listener session using an interaction server framework (`[your-id].oast.pro`).2. Construct the target request by swapping out the parameter value with your custom server address:
   `https://1win.com/[path]?[parameter]=[your-id].oast.pro`3. Execute the single request using a manual proxy suite or curl command, verifying that tool traffic stays below 5 requests per second.4. Check the external interaction log server dashboard.
## Proof of Concept (PoC)```http
GET /[path]?[parameter]=[your-id].oast.pro HTTP/1.1
Host: 1win.com
User-Agent: Mozilla/5.0
Connection: close
```
### Captured Server Callback Log:```text
[TIMESTAMP] - Received HTTP/DNS Request from 1win Infrastructure IP: [Insert Server IP]
User-Agent String logged by backend: [Insert Backend User Agent if visible]
```
## ImpactAn attacker can utilize the 1win backend architecture as a proxy to route unauthorized traffic. Depending on infrastructure network isolation, this can allow an attacker to trace local port availability, map internal networks, or interact with unauthenticated local API directories.
## Suggested Remediation*   **Strict Whitelisting**: Restrict values supplied to internal redirection or check mechanisms to an explicit whitelist of trusted internal or partner domains.
*   **Protocol Restriction**: Disable unused protocols (such as `gopher://`, `file://`, `ftp://`) and force the parsing engine to accept only strict validation strings rather than full URLs.

------------------------------
If you are currently observing the behavior of your collaborator logs while interacting with parameters like visit_domain or lobbyUrl, let me know what types of incoming requests (DNS, HTTP, or nothing) are hitting your listener. I can help you differentiate between a client-side redirect and a true server-side callback safely.
