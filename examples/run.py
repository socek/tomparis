from asyncio import run

from examples.second_chart import MySecondChart
from tomparis.chart import Chart
from tomparis.charts.postgresql.chart import PostgreSQLChart
from tomparis.kubectl import KubeCtl


class MyChart(Chart):
    def prepare_requirements(self):
        super().prepare_requirements()
        self.add_chart(MySecondChart("mysecond"))
        self.add_chart(PostgreSQLChart("psql"))

    def prepare_settings(self):
        super().prepare_settings()
        self.read_settings("values.yaml")

        self.update_subchart("mysecond", self.settings["mysecond"])


async def caller():
    chart = MyChart("mychart")
    ctl = KubeCtl()
    await ctl.cluster_info()
    print("------")
    stdout, stderr = await ctl.apply(chart)
    print(stdout.decode())
    print("---")
    print(stderr)


run(caller())
