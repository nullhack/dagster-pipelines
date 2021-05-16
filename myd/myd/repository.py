from dagster import repository

from myd.pipelines.my_pipeline import my_pipeline
from myd.pipelines.p1 import complex_pipeline
from myd.schedules.my_hourly_schedule import my_hourly_schedule
from myd.sensors.my_sensor import my_sensor


@repository
def myd():
    """
    The repository definition for this myd Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    pipelines = [my_pipeline, complex_pipeline]
    schedules = [my_hourly_schedule]
    sensors = [my_sensor]

    return pipelines + schedules + sensors
