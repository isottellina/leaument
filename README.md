# Léaument

Léaument is a converter from Gregorian date to Republican date. It uses the [French Republican calendar](https://en.wikipedia.org/wiki/French_Republican_calendar), uses Romme's proposed system (with a leap year every 4 years, except for years that are multiples of 100, except for years that are multiples of 400). It considers the first leap year was on An IV (year 4). For this reason, it might not be historically accurate to the first years of the Revolutionary era, which did not use this exact system.

It's in French, as I thought no non-French-speaking person would want to use it. Might do translations later.

The code sucks, might clean it up later. I wanted to do it quickly for the new year.

## Usage

You can simply run it locally with Poetry using:
```shell
poetry install
poetry run uvicorn leaument.main:app
```

## License 

This work is released under the terms of the GPLv3. Derived works must disclose their source and use the same license or a stronger one, include the copyright notice and document their changes. If you ever do anything using this, let me know!
