# Remote Code Execution via Unsanitized Parameter in Registration Endpoint

## Summary
A Remote Code Execution (RCE) vulnerability was identified within the registration parameter logic. The application fails to properly sanitize or validate user input supplied via the `code` parameter before passing it to an internal backend function. By appending command injection sequences, an attacker can execute arbitrary system commands in the context of the web application user, leading to complete server compromise.

## Vulnerable Asset
*   **URL**: `https://1win.com/register`
*   **Parameter**: `code`
*   **Severity**: Critical (CVSS 9.8)

## Requirements & Pre-requisites
*   No authentication required (Unauthenticated entry point).
*   A proxy tool (e.g., Burp Suite) to monitor responses.

## Step-by-Step Reproduction Instructions
1. Navigate to the registration page containing the parameter: `https://1win.com/register?code=[PAYLOAD]`
2. Insert a benign, non-destructive command injection payload designed to verify code execution (e.g., a time-based delay or a basic system query like `whoami`).
3. Intercept the request and analyze the response headers and body.
4. Note that the command executes on the underlying operating system and returns the output or alters response latency accordingly.

## Proof of Concept (PoC)
*(Note: Replace this placeholder with your safe, non-destructive replication syntax, such as a curl command demonstrating a benign sleep delay)*

```bash
curl -i -s "https://1win.com[SAFE_PAYLOAD_HERE]"
```

## Impact
Exploitation of this vulnerability allows unauthenticated attackers to achieve arbitrary code execution on the hosting infrastructure. This grants full access to the application’s environment variables, local file system, database credentials, and source code, creating a risk of lateral network movement.

## Remediation
*   **Input Whitelisting**: Implement strict alphanumeric validation on the backend for the `code` parameter. Reject any input containing metacharacters (e.g., `;`, `|`, `&`, `` ` ``, `$`).
*   **Avoid Shell Execution**: Ensure that referral codes are strictly handled as data strings within database queries or application logic, rather than being passed to system command wrappers or dynamic evaluation code.
