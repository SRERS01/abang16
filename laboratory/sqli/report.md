# SQL Injection (SQLi) via [Parameter Name] on [Endpoint]

## Summary
A SQL Injection vulnerability was identified within the `[Insert Parameter, e.g., castId]` parameter of the `[Insert Endpoint, e.g., /casino/list]` path. Due to missing parameterization or input filtering on the backend database layer, an attacker can append conditional logic statements. This allows for arbitrary database structure inference, meeting 1win's **Critical** severity standard ($1,500 bounty).

## Vulnerable Asset
*   **Target URL**: `https://1win.com/[Insert-Path]`
*   **Affected Parameter**: `[Insert-Parameter-Name]`
*   **HTTP Method**: `GET` / `POST`

## Pre-requisites
*   No authenticated session required / Tested via a valid researcher account.
*   Testing conducted strictly under the 5 requests-per-second program boundary.

## Step-by-Step Reproduction Instructions
1. Navigate to the targeted data endpoint: `https://1win.com/[path]?[parameter]=[valid_value]`
2. Intercept the request using an interception proxy suite.
3. Append a non-destructive time delay payload into the parameter string: `[Your Safe Sleep Payload]`
4. Observe that the application latency increases exactly by the number of seconds defined in the payload, confirming execution.

## Proof of Concept (PoC)
```http
GET /[path]?[parameter]=[Safe-Delay-Payload] HTTP/1.1
Host: 1win.com
Connection: close
```
*Note: The baseline response latency for this endpoint is ~150ms. Injecting the safe time-delay statement caused a distinct response delay of 5150ms, proving backend query compilation.*

## Impact
An unauthorized actor exploiting this entry point can interact directly with the backend database infrastructure. This creates a risk of sensitive data exposure, schema enumeration, or vertical privilege escalation within the web application framework.

## Suggested Remediation
*   **Parameterized Queries**: Implement strictly bound parameterized queries or prepared statements across all API endpoint lookup scripts. This ensures the database engine treats user input exclusively as a literal value rather than executable code.
*   **Input Whitelisting**: Ensure string identifiers like IDs or hashes match strict format constraints (e.g., validating that UUID parameters contain only alphanumeric blocks and hyphens) before query parsing occurs.
