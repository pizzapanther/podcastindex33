import typer

from typing import Optional

import podcastindex33 as pci


def main(
  api_key: Optional[str] = None,
  api_secret: Optional[str] = None,
):
  print('narf')


def run ():
  typer.run(main)

if __name__ == "__main__":
  run()
