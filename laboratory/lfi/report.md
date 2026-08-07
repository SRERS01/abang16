# Local File Inclusion (LFI) via Unsanitized Input in [Parameter Name]

## Summary
A Local File Inclusion (LFI) vulnerability was identified within the `[Insert Parameter, e.g., path / lang]` parameter of the `[Insert Endpoint Path]` endpoint. The application uses user-controlled data to locate and render structural components from the server's local file system without sufficient validation. An attacker can use directory traversal characters to read internal application files, matching 1win's **Critical** severity tier ($1,200 bounty).

## Vulnerable Asset
*   **Target Endpoint URL**: `https://1win.com/[Insert-Path]`
*   **Affected Parameter Layer**: `[Insert-Parameter]`
*   **Severity Tier**: Critical (CVSS 8.6)

## Pre-requisites
*   No special privileges required / [Specify if an active researcher test session was required].
*   Testing traffic restricted strictly under the 5 requests-per-second boundary.

## Step-by-Step Reproduction Instructions
1. Navigate to the target page with an active interception proxy: `https://1win.com/[path]?[parameter]=[valid_value]`
2. Modify the target query parameter to include a safe, relative directory breakout path string: `[Your Safe Non-Destructive Payload]`
3. Transmit the standalone request to the server host.
4. Observe the response content block to confirm if the backend reads from an unvalidated directory.

## Proof of Concept (PoC)
```http
GET /[path]?[parameter]=[Safe-Breakout-Payload] HTTP/1.1
Host: 1win.com
Connection: close
```
*Note: The response successfully bypassed folder boundaries and returned the raw layout elements of the local infrastructure file template rather than a standard localized error message.*

## Impact
An unauthorized operator exploiting this vulnerability can read internal application configurations, source files, or localized scripts stored on the server file system. This subverts application isolation layers and can result in the exposure of internal environment structures.

## Suggested Remediation
*   **Indirect Mapping Whitelists**: Implement a strict, closed whitelist for any parameter that dictates local page content selection. Map input keys (e.g., `lang=1`, `lang=2`) to static file paths server-side rather than accepting raw filename inputs.
*   **Path Sanitization**: Use built-in filesystem sanitization functions (such as Java's `Paths.get().normalize()` or PHP's `basename()`) to ensure input parameters strip out all directory traversal sequences (`..` or `/`) before processing occurs.
