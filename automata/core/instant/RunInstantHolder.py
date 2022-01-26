from datetime import datetime, timezone


class RunInstantHolder:
    run_instant = None

    @staticmethod
    def initialize(run_instant=None):
        if run_instant is not None:
            RunInstantHolder.run_instant = run_instant
        else:
            RunInstantHolder.run_instant = datetime.now(timezone.utc)

    @staticmethod
    def numeric_run_instance():
        return RunInstantHolder.run_instant.timestamp() if type(RunInstantHolder.run_instant) is datetime else RunInstantHolder.run_instant
