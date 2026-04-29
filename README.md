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
schemathesis --config-file ./schemathesis.toml run ./oas.yaml --url http://127.0.0.1:8000 --wait-for-schema 60 --report junit
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
      File "/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/engine/run/unit/_executor.py", line 129, in run_test
        test_function(
        ~~~~~~~~~~~~~^
            ctx=ctx,
            ^^^^^^^^
        ...<6 lines>...
            continue_on_failure=continue_on_failure,
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        )
        ^
      File "/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/generation/hypothesis/builder.py", line 280, in test_func
        def test_wrapper(*args: Any, **kwargs: Any) -> Any:
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/hypothesis/core.py", line 2264, in wrapped_test
        raise the_error_hypothesis_found
      File "/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/_hypothesis.py", line 144, in openapi_cases
        query_ = generate_parameter(
            ParameterLocation.QUERY,
        ...<8 lines>...
            mix_examples=mix_examples,
        )
      File "/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/_hypothesis.py", line 700, in generate_parameter
        value, metadata = get_parameters_value(
                          ~~~~~~~~~~~~~~~~~~~~^
            explicit,
            ^^^^^^^^^
        ...<8 lines>...
            mix_examples=mix_examples,
            ^^^^^^^^^^^^^^^^^^^^^^^^^^
        )
        ^
      File "/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/_hypothesis.py", line 619, in get_parameters_value
        strategy = get_parameters_strategy(
            operation,
        ...<4 lines>...
            mix_examples=mix_examples,
        )
      File "/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/_hypothesis.py", line 755, in get_parameters_strategy
        return container.get_strategy(
               ~~~~~~~~~~~~~~~~~~~~~~^
            operation,
            ^^^^^^^^^^
        ...<4 lines>...
            mix_examples=mix_examples,
            ^^^^^^^^^^^^^^^^^^^^^^^^^^
        )
        ^
      File "/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/adapter/parameters.py", line 1118, in get_strategy
        strategy = strategy_factory(
            schema_obj,
        ...<5 lines>...
            self.name_to_uri,
        )
      File "/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/_hypothesis.py", line 857, in make_negative_strategy
        return negative_schema(
            schema,
        ...<6 lines>...
            name_to_uri=name_to_uri,
        )
      File "/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/negative/__init__.py", line 149, in negative_schema
        validator = get_validator(cache_key)
      File "/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/negative/__init__.py", line 105, in get_validator
        return cache_key.validator_cls(
               ~~~~~~~~~~~~~~~~~~~~~~~^
            cache_key.schema,
            ^^^^^^^^^^^^^^^^^
        ...<2 lines>...
            pattern_options=FANCY_REGEX_OPTIONS,
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        )
        ^
    jsonschema_rs.ValidationError: [{"format":"float","maximum":180.0,"minimum":-180.0,"type":"number"},{"format":"float","maximum":90.0,"minimum":-90.0,"type":"number"},{"format":"float","maximum":180.0,"minimum":-180.0,"type":"number"},{"format":"float","maximum":90.0,"minimum":-90.0,"type":"number"}] is not of types "boolean", "object"
    Failed validating "type" in schema
    On instance["properties"]["box"]["items"]:
        [{"format":"float","maximum":180.0,"minimum":-180.0,"type":"number"},{"format":"float","maximum":90.0,"minimum":-90.0,"type":"number"},{"format":"float","maximum":180.0,"minimum":-180.0,"type":"number"},{"format":"float","maximum":90.0,"minimum":-90.0,"type":"number"}]
    while generating 'case' from one_of(openapi_cases(operation=APIOperation(path='/box',
     method='get',
     definition=,
     schema=,
     responses=OpenApiResponses(_inner={'200': OpenApiResponse(status_code='200',
        definition={'description': 'OK',
         'content': {'application/json': {'schema': {'type': 'string'}}}},
        resolver=<schemathesis.specs.openapi.references.ReferenceResolver object at 0x10d1a8980>,
        scope='file:///Users/user/Projects/schemathesis-bug-report/oas.yaml',
        adapter=<module 'schemathesis.specs.openapi.adapter.v3_1' from '/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/adapter/v3_1.py'>),
       '422': OpenApiResponse(status_code='422',
        definition={'description': 'Error',
         'content': {'application/json': {'schema': {'type': 'object'}}}},
        resolver=<schemathesis.specs.openapi.references.ReferenceResolver object at 0x10d1a8980>,
        scope='file:///Users/user/Projects/schemathesis-bug-report/oas.yaml',
        adapter=<module 'schemathesis.specs.openapi.adapter.v3_1' from '/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/adapter/v3_1.py'>)},
      resolver=<schemathesis.specs.openapi.references.ReferenceResolver object at 0x10d1a8980>,
      scope='file:///Users/user/Projects/schemathesis-bug-report/oas.yaml',
      adapter=<module 'schemathesis.specs.openapi.adapter.v3_1' from '/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/adapter/v3_1.py'>),
     security=OpenApiSecurityParameters(_parameters=[]),
     label='GET /box',
     app=None,
     base_url='http://127.0.0.1:8000',
     path_parameters=,
     headers=,
     cookies=,
     query=,
     body=,
     filter_case_tracker=None)), openapi_cases(operation=APIOperation(path='/box',
     method='get',
     definition=,
     schema=,
     responses=OpenApiResponses(_inner={'200': OpenApiResponse(status_code='200',
        definition={'description': 'OK',
         'content': {'application/json': {'schema': {'type': 'string'}}}},
        resolver=<schemathesis.specs.openapi.references.ReferenceResolver object at 0x10d1a8980>,
        scope='file:///Users/user/Projects/schemathesis-bug-report/oas.yaml',
        adapter=<module 'schemathesis.specs.openapi.adapter.v3_1' from '/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/adapter/v3_1.py'>),
       '422': OpenApiResponse(status_code='422',
        definition={'description': 'Error',
         'content': {'application/json': {'schema': {'type': 'object'}}}},
        resolver=<schemathesis.specs.openapi.references.ReferenceResolver object at 0x10d1a8980>,
        scope='file:///Users/user/Projects/schemathesis-bug-report/oas.yaml',
        adapter=<module 'schemathesis.specs.openapi.adapter.v3_1' from '/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/adapter/v3_1.py'>)},
      resolver=<schemathesis.specs.openapi.references.ReferenceResolver object at 0x10d1a8980>,
      scope='file:///Users/user/Projects/schemathesis-bug-report/oas.yaml',
      adapter=<module 'schemathesis.specs.openapi.adapter.v3_1' from '/opt/homebrew/Cellar/schemathesis/4.16.1/libexec/lib/python3.14/site-packages/schemathesis/specs/openapi/adapter/v3_1.py'>),
     security=OpenApiSecurityParameters(_parameters=[]),
     label='GET /box',
     app=None,
     base_url='http://127.0.0.1:8000',
     path_parameters=,
     headers=,
     cookies=,
     query=,
     body=,
     filter_case_tracker=None), generation_mode=<GenerationMode.NEGATIVE: 'negative'>))
```

### Description:

- This seems to happen because of `prefixItems`
- Schemathesis seem to not handle parsing it gracefully
