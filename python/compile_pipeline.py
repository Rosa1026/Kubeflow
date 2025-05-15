from kfp import compiler
from pipeline import cluster_health_report_pipeline
import os

output_yaml_path = "pod_log_pipeline_advance.yaml"

compiler.Compiler().compile(
    pipeline_func=cluster_health_report_pipeline,
    package_path=output_yaml_path
)

print(f"Pipeline compiled successfully! YAML file saved to: {os.path.abspath(output_yaml_path)}")
