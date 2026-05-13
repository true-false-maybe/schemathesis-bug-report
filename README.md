A small example repo to create bug report for https://github.com/schemathesis/schemathesis

### How to run

Running api:

```zsh
python3 -m venv venv
source venv/bin/activate
pip install "fastapi[standard]"
fastapi dev
```

Running schemathesis:

```zsh
SCHEMATHESIS_HOOKS="./hook.py" schemathesis --config-file ./schemathesis.toml run ./oas.yaml --url http://127.0.0.1:8000 --wait-for-schema 60 --report junit
```

Bug which occurs:

```
==================================== ERRORS ====================================
___________________________________ GET /box ___________________________________
Runtime Error

[{"format":"float","maximum":180.0,"minimum":-180.0,"type":"number"},{"format":"float","maximum":90.0,"minimum":-90.0,"type":"number"},{"format":"float","maximum":180.0,"minimum":-180.0,"type":"number"},{"format":"float","maximum":90.0,"minimum":-90.0,"type":"number"}] is not of types "boolean", "object"

Failed validating "type" in schema

On instance["properties"]["box"]["items"]:
    [{"format":"float","maximum":180.0,"minimum":-180.0,"type":"number"},{"format":"float","maximum":90.0,"minimum":-90.0,"type":"number"},{"format":"float","maximum":180.0,"minimum":-180.0,"type":"number"},{"format":"float","maximum":90.0,"minimum":-90.0,"type":"number"}]

    Traceback (most recent call last):
      File "/opt/homebrew/Cellar/schemathesis/4.18.1/libexec/lib/python3.14/site-packages/schemathesis/engine/run/unit/_case.py", line 81, in run_one_case
        ctx.cache_outcome(case, exc)
        ~~~~~~~~~~~~~~~~~^^^^^^^^^^^
      File "/opt/homebrew/Cellar/schemathesis/4.18.1/libexec/lib/python3.14/site-packages/schemathesis/engine/context.py", line 125, in cache_outcome
        self.outcome_cache[hash(case)] = outcome
                           ~~~~^^^^^^
      File "/opt/homebrew/Cellar/schemathesis/4.18.1/libexec/lib/python3.14/site-packages/schemathesis/generation/case.py", line 206, in __hash__
        return hash(self.as_curl_command({SCHEMATHESIS_TEST_CASE_HEADER: "0"}))
                    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/homebrew/Cellar/schemathesis/4.18.1/libexec/lib/python3.14/site-packages/schemathesis/generation/case.py", line 304, in as_curl_command
        request_data = prepare_request(self, headers, config=self.operation.schema.config.output.sanitization)
      File "/opt/homebrew/Cellar/schemathesis/4.18.1/libexec/lib/python3.14/site-packages/schemathesis/transport/prepare.py", line 133, in prepare_request
        kwargs = REQUESTS_TRANSPORT.serialize_case(case, base_url=base_url, headers=headers)
      File "/opt/homebrew/Cellar/schemathesis/4.18.1/libexec/lib/python3.14/site-packages/schemathesis/transport/requests.py", line 124, in serialize_case
        excluded_headers = get_exclude_headers(case)
      File "/opt/homebrew/Cellar/schemathesis/4.18.1/libexec/lib/python3.14/site-packages/schemathesis/transport/prepare.py", line 44, in get_exclude_headers
        if case.meta is None:
           ^^^^^^^^^
      File "/opt/homebrew/Cellar/schemathesis/4.18.1/libexec/lib/python3.14/site-packages/schemathesis/generation/case.py", line 288, in meta
        self._revalidate_metadata()
        ~~~~~~~~~~~~~~~~~~~~~~~~~^^
      File "/opt/homebrew/Cellar/schemathesis/4.18.1/libexec/lib/python3.14/site-packages/schemathesis/generation/case.py", line 237, in _revalidate_metadata
        self.operation.schema.revalidate_case_metadata(self)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
      File "/opt/homebrew/Cellar/schemathesis/4.18.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/schemas.py", line 228, in revalidate_case_metadata
        is_valid = case._validate_component(location, value, validator_cls)
      File "/opt/homebrew/Cellar/schemathesis/4.18.1/libexec/lib/python3.14/site-packages/schemathesis/generation/case.py", line 261, in _validate_component
        return make_validator(container.schema, validator_cls).is_valid(value)
               ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/homebrew/Cellar/schemathesis/4.18.1/libexec/lib/python3.14/site-packages/schemathesis/core/jsonschema/__init__.py", line 48, in make_validator
        return validator_cls(schema, **kwargs)
    jsonschema_rs.ValidationError: [{"format":"float","maximum":180.0,"minimum":-180.0,"type":"number"},{"format":"float","maximum":90.0,"minimum":-90.0,"type":"number"},{"format":"float","maximum":180.0,"minimum":-180.0,"type":"number"},{"format":"float","maximum":90.0,"minimum":-90.0,"type":"number"}] is not of types "boolean", "object"
    Failed validating "type" in schema
    On instance["properties"]["box"]["items"]:
        [{"format":"float","maximum":180.0,"minimum":-180.0,"type":"number"},{"format":"float","maximum":90.0,"minimum":-90.0,"type":"number"},{"format":"float","maximum":180.0,"minimum":-180.0,"type":"number"},{"format":"float","maximum":90.0,"minimum":-90.0,"type":"number"}]
```

### Description:

- This seems to still happen because of `prefixItems`, but seems to be somehow related with hooks
- Schemathesis seem to not handle parsing it gracefully
