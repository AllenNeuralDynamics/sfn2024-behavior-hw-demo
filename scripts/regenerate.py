import inspect
from pathlib import Path

import sfn2024_behavior_hw_demo.rig
from aind_behavior_services.utils import (
    convert_pydantic_to_bonsai,
    pascal_to_snake_case,
    snake_to_pascal_case,
)

SCHEMA_ROOT = Path("./src/DataSchemas/")
EXTENSIONS_ROOT = Path("./src/Extensions/")
NAMESPACE_PREFIX = "AindVrForagingDataSchema"


def main():
    models = [
        sfn2024_behavior_hw_demo.rig.Rig,
    ]

    for model in models:
        module_name = inspect.getmodule(model).__name__
        module_name = module_name.split(".")[-1]
        schema_name = f"{pascal_to_snake_case(model.__name__)}"
        namespace = f"{NAMESPACE_PREFIX}.{snake_to_pascal_case(module_name)}"

        print((schema_name, namespace))
        convert_pydantic_to_bonsai(
            {schema_name: model}, schema_path=SCHEMA_ROOT, output_path=EXTENSIONS_ROOT, namespace=namespace
        )


if __name__ == "__main__":
    main()
