import asyncio

import hoshino
from hoshino.service import sucmd
from hoshino.typing import CommandSession, CQHttpError


@sucmd('unicast', aliases=('uc', '单播'))
async def unicast(session: CommandSession):
    msg = session.current_arg
    x = msg.split(' ', 1)
    if x[0] and x[1]:
        try:
            await session.bot.send_private_msg(user_id=int(x[0]), message=x[1])
            hoshino.logger.info(f'向{g} 投递单播成功')
        except Exception as e:
            hoshino.logger.error(f'向{g} 投递单播失败：{repr(e)}')
            try:
                await session.send(f'向{g} 投递单播失败：{repr(e)}')
            except Exception as e:
                hoshino.logger.critical(f'向单播发起者进行错误回报时发生错误：{repr(e)}')
    # await session.send(f'单播完成！')
    else:
        await session.send(f'单播指令不完整！')
