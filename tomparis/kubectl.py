from asyncio import create_subprocess_shell
from asyncio.subprocess import PIPE

from tomparis.chart import Chart


class KubeCtl:
    async def _exec(self, command, stdin=None):
        command = f"kubectl {command}"
        proc = await create_subprocess_shell(command, stdout=PIPE, stdin=PIPE)
        return await proc.communicate(stdin)

    async def cluster_info(self):
        stdout, stderr = await self._exec("cluster-info")
        print(stdout.decode())

    async def apply(self, chart: Chart):
        return await self._exec("apply -f -", chart.stream())
