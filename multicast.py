import asyncio

import hoshino
from hoshino.service import sucmd
from hoshino.typing import CommandSession, CQHttpError


@sucmd('multicast', aliases=('mc', '群播'))
async def multicast(session: CommandSession):
    msg = session.current_arg
    x = msg.split(' ', 1)
    if x[0] and x[1]:
        try:
            # await session.send(f'{x[0]}：{x[1]}')
            await session.bot.send_group_msg(group_id=int(x[0]), message=x[1])
            hoshino.logger.info(f'群{x[0]} 投递群播成功')
        except Exception as e:
            hoshino.logger.error(f'群{x[0]} 投递群播失败：{repr(e)}')
            try:
                await session.send(f'群{x[0]} 投递群播失败：{repr(e)}')
            except Exception as e:
                hoshino.logger.critical(f'向群播发起者进行错误回报时发生错误：{repr(e)}')
        # await session.send(f'群播完成！')
    else:
        await session.send(f'群播指令不完整！')
