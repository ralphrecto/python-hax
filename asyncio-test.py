import asyncio

class Runner:
  def __init__(self):
    self.data_generators = {}

  async def _datagen(self, k):
    await asyncio.sleep(1)
    i = 0
    data = f"testkey: {k}"
    while True:
      i += 1
      yield f"access #{i}: {data}"

  def get_data_generator(self, k):
    if k not in self.data_generators:
      self.data_generators[k] = self._datagen(k)

    return self.data_generators[k]

  async def get_data(self, k):
    async for datum in self.get_data_generator(k):
      return datum

  async def process(self, k):
    print(await self.get_data(k))

async def main():
  runner = Runner()
  key = "id"
  proc1 = runner.process(key)
  proc2 = runner.process(key)
  proc3 = runner.process(key)

  await asyncio.gather(proc1, proc2, proc3)

asyncio.run(main())
