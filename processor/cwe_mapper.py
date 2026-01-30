def infer_cwe(summary):
    if not summary:
        return "UNKNOWN"

    s = summary.lower()

    if "xss" in s or "cross-site scripting" in s:
        return "CWE-79"
    if "sql injection" in s:
        return "CWE-89"
    if "csrf" in s or "cross-site request forgery" in s:
        return "CWE-352"
    if "authentication bypass" in s:
        return "CWE-287"
    if "information exposure" in s or "information disclosure" in s:
        return "CWE-200"
    if "rce" in s or "remote code execution" in s:
        return "CWE-94"

    return "UNKNOWN"
