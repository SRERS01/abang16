# Cross-Site Scripting (XSS) via [Parameter Name] on [Endpoint Path]

## Summary
A Reflected Cross-Site Scripting (XSS) vulnerability was identified in the `[Insert Parameter, e.g., search]` parameter of the `[Insert Path, e.g., /casino]` endpoint. The application reflects user-supplied query strings directly into the DOM structure without proper output encoding, allowing for client-side script execution within the user's session context.

## Vulnerable Asset
*   **Target Page**: `https://1win.com/[Insert-Path]`
*   **Affected Parameter**: `[Insert-Parameter-Name]`
*   **Severity Tier**: Medium (\$150 bounty)

## Requirements & Pre-requisites
*   No authenticated session required / [Specify if an active test session was required].
*   Standard modern web browser testing context.

## Step-by-Step Reproduction Instructions
1. Open a web browser and navigate to the targeted platform path containing your safe proof payload:
   `https://1win.com/[path]?[parameter]=%3Cimg%20src%3Dx%20onerror%3Dconsole.log(document.domain)%3E`
2. Open the browser Developer Tools interface (F12) and switch to the **Console** panel.
3. Observe that the payload successfully bypasses encoding, triggers the fallback event, and logs the execution context data directly to the console.

## Proof of Concept (PoC)
```html
<!-- Example of the resulting unsanitized DOM reflection structure observed -->
<div class="search-results-header">
    Results for: <img src=x onerror=console.log(document.domain)>
</div>
```
*(Please find attached `console_log_capture.png` documenting the verified application execution output).*

## Impact
An attacker could craft a malicious link containing an execution string and distribute it via social engineering channels. If a user clicks the link, the script executes within their active browser session, potentially allowing unauthorized actions to be performed on behalf of the user or altering the visual presentation of the target application interface.

## Suggested Remediation
*   **Context-Aware Output Encoding**: Implement strict context-aware output encoding across all frontend rendering templates. Ensure that query tokens reflected into HTML contexts undergo full HTML-entity encoding before display.
*   **Secure Framework Sinks**: Avoid the use of flexible inner layout modifiers (such as `innerHTML` or `v-html` in framework elements) when displaying raw query strings. Use safe alternative properties like `textContent` or `innerText` to ensure browser rendering engines treat the input strictly as text.
