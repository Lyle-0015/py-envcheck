"""Validate required environment variables. Standard library only."""


def missing(required, env):
    return [k for k in required if not env.get(k)]


def require(required, env):
    m = missing(required, env)
    if m:
        raise KeyError("missing required env: " + ", ".join(m))
