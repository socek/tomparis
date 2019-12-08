from os import path

from tomparis.chart import Chart
from tomparis.charts.postgresql.deployment import PsqlDeployment


class PostgreSQLChart(Chart):
    def prepare_settings(self):
        super().prepare_settings()
        dir_path = path.dirname(path.realpath(__file__))
        self.read_settings(path.join(dir_path, "values.yaml"))

    def prepare_chart(self):
        super().prepare_chart()
        self.add_kobject(PsqlDeployment())
